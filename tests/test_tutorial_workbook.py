"""Protect workbook seed integrity and fail-closed one-time import behavior."""

import pathlib
import zipfile

import pytest
import openpyxl

import sheetlesson.model
import sheetlesson.compiler
import sheetlesson.workbook


#============================================
def test_seed_types_and_student_targets_roundtrip(tmp_path: pathlib.Path) -> None:
	"""Student actions cannot leak answers or coerce literal and empty text seeds."""
	model = sheetlesson.model
	span = model.SourceSpan("source.md", 1, 1)
	sheet = model.Worksheet("Data", span)
	values = [model.Scalar("text", "=literal"), model.Scalar("text", ""),
		model.Scalar("blank", None), model.Scalar("number", 1.2345678901234567),
		model.Scalar("boolean", False), model.Scalar("formula", '=IF(A1="x",2,3)')]
	for column, scalar in enumerate(values, 1):
		sheet.cells[(4, column)] = model.CellSeed(4, column, scalar, span)
	sheet.entry_cells = {(4, 1), (4, 3), (100, 8)}
	document = model.Document(pathlib.Path("source.md"), "", worksheets=[sheet])
	document.actions = [model.Action("Enter", span, 0, "secret answer")]
	path = tmp_path / "student.xlsx"
	sheetlesson.workbook.write_workbook(document, path)
	sheetlesson.workbook.verify_workbook(document, path)
	book = openpyxl.load_workbook(path, data_only=False)
	assert book["Data"]["A4"].data_type == "s"
	assert book["Data"]["H100"].value is None
	assert book["Data"]["C4"].fill.fill_type == "solid"
	assert book["Data"]["A4"].fill.fill_type is None
	with zipfile.ZipFile(path) as archive:
		assert b"secret answer" not in b"".join(archive.read(n) for n in archive.namelist())
	book.close()


#============================================
def test_import_preserves_sparse_addresses_and_literal_types(tmp_path: pathlib.Path) -> None:
	"""Sparse sheet imports remain bounded and quote ambiguous text and formulas faithfully."""
	book = openpyxl.Workbook()
	sheet = book.active
	sheet.title = "Data"
	sheet["C8"] = "001"
	sheet["D8"] = ""
	sheet["D8"].data_type = "s"
	sheet["E8"] = "literal &amp; <br> `ticks` \\| and\nnewline"
	sheet["F1000000"] = '=IF(C8="a|b",1,0)'
	book.create_sheet("Empty")
	path = tmp_path / "sparse.xlsx"
	book.save(path)
	book.close()
	draft = sheetlesson.workbook.import_workbook(path)
	assert "#### At: C8" in draft
	assert "#### At: F1000000" in draft
	assert '` "001" `' in draft and '` "" `' in draft
	assert r'=IF(C8="a\|b",1,0)' in draft
	assert "### Sheet: Empty\n\n|  |\n| --- |" in draft
	assert len(draft) < 1500
	# Finish the intentionally incomplete scaffold to exercise the shared scalar parser.
	source = draft.replace("Write the tutorial instructions here.",
		"### Part: Review\n\n- **Worksheet:** Data\n\n"
		"#### Step: Inspect\n\n- **Compare:** Inspect the imported cells.")
	document = sheetlesson.compiler.compile_source(source)
	assert not document.has_errors
	rebuilt = tmp_path / "rebuilt.xlsx"
	sheetlesson.workbook.write_workbook(document, rebuilt)
	sheetlesson.workbook.verify_workbook(document, rebuilt)
	book = openpyxl.load_workbook(rebuilt, data_only=False)
	assert book["Data"]["E8"].value == "literal &amp; <br> `ticks` \\| and\nnewline"
	assert book["Data"]["F1000000"].value == '=IF(C8="a|b",1,0)'
	book.close()


#============================================
@pytest.mark.parametrize("feature", ["merge", "date", "error", "epoch", "iteration"])
def test_import_blocks_semantic_loss(tmp_path: pathlib.Path, feature: str) -> None:
	"""A draft must not silently discard workbook and cell semantics."""
	book = openpyxl.Workbook()
	sheet = book.active
	if feature == "merge":
		sheet.merge_cells("A1:B1")
	elif feature == "date":
		sheet["A1"] = 45000
		sheet["A1"].number_format = "yyyy-mm-dd"
	elif feature == "epoch":
		book.epoch = openpyxl.utils.datetime.CALENDAR_MAC_1904
		sheet["A1"] = "=DATE(2026,1,1)"
		sheet["B1"] = 44561
	elif feature == "iteration":
		book.calculation = openpyxl.workbook.properties.CalcProperties(
			iterate=True, iterateCount=1000, iterateDelta=0.0001)
		sheet["A1"] = "=(A1+1)/2"
	else:
		sheet["A1"] = "#DIV/0!"
	path = tmp_path / "unsupported.xlsx"
	book.save(path)
	book.close()
	message = "import blocked"
	if feature == "epoch":
		message = "1904 date epoch"
	elif feature == "iteration":
		message = "iterative calculation"
	with pytest.raises(ValueError, match=message):
		sheetlesson.workbook.import_workbook(path)
