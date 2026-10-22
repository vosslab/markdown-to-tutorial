"""Protect native formula fidelity and document navigation in DOCX output."""

import pathlib
import base64
import zipfile

import markdown_it
import defusedxml.ElementTree
import docx

import tutorial_lib.model
import tutorial_lib.compiler
import tutorial_lib.docx_renderer
import tutorial_lib.docx_styles


NAMESPACES = {
	"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main",
	"r": "http://schemas.openxmlformats.org/package/2006/relationships",
}


#============================================
def test_standard_styles_and_direct_fonts() -> None:
	"""Paragraph fonts stay editable through styles while role fonts remain explicit."""
	source = "# Title\n\n### Overview\n\n#### Detail\n\n##### Evidence\n\n###### Deep\n\n"
	source += "Body [link](https://example.org) and `=SUM(A1:B1)`\n\n"
	source += "> Quoted evidence\n\n```sheets\n=SUM(A1:B1)\n```\n\n"
	source += "| Note | Formula |\n| --- | --- |\n| [Compact](https://example.org) | `=SUM(A1:B1)` |\n"
	document = tutorial_lib.model.Document(pathlib.Path("styles.md"), source)
	document.tokens = markdown_it.MarkdownIt("commonmark").enable("table").parse(source)
	document.content_token_indices = list(range(len(document.tokens)))
	output = docx.Document()
	tutorial_lib.docx_styles.configure(output)
	tutorial_lib.docx_renderer.render_tokens(output, document)
	standard = {"Normal", "Title", "Subtitle", "Heading 1", "Heading 2", "Heading 3"}
	for name in standard:
		style = output.styles[name]
		assert style.font.name == "PT Sans"
		fonts = style._element.rPr.rFonts
		assert not any("Theme" in key or "theme" in key for key in fonts.attrib)
	assert [p.style.name for p in output.paragraphs[:5]] == [
		"Title", "Heading 1", "Heading 2", "Heading 3", "Heading 3",
	]
	assert all(p.style.name in standard for p in output.paragraphs)
	assert all(run.font.name is None for p in output.paragraphs[:5] for run in p.runs)
	assert output.paragraphs[5].runs[0].font.name is None
	assert output.sections[0].footer.paragraphs[0].style.name == "Normal"
	table_link = output.tables[0].cell(1, 0)._tc.find(".//w:hyperlink/w:r", NAMESPACES)
	assert table_link.find("w:rPr/w:rFonts", NAMESPACES).get(
		docx.oxml.ns.qn("w:ascii")) == "PT Sans Narrow"
	assert output.tables[0].cell(1, 1).paragraphs[0].runs[0].font.name == "Roboto Mono"
	formula = output.paragraphs[-1]
	assert formula.runs[0].font.name == "Roboto Mono"
	assert formula._p.find("w:pPr/w:shd", NAMESPACES) is not None
	assert formula._p.find("w:pPr/w:pBdr", NAMESPACES) is not None
	assert output.paragraphs[-2].paragraph_format.left_indent is not None
	runs = output._element.findall(".//w:r", NAMESPACES)
	assert not any(run.find("w:rPr/w:rStyle", NAMESPACES) is not None for run in runs)
	link = output._element.find(".//w:hyperlink/w:r", NAMESPACES)
	assert link.find("w:rPr/w:u", NAMESPACES) is not None
	assert link.find("w:rPr/w:rFonts", NAMESPACES) is None


#============================================
def test_editable_formula_links_and_independent_lists(tmp_path: pathlib.Path) -> None:
	"""Formula copy text and links must survive without rasterizing tutorial content."""
	formula = '=IF(B2>0,"A B",SUM($C$2:C8))'
	source = "# Native tutorial\n\n### Part: First\n\n#### Step: Calculate\n\n"
	source += "3. **Enter D2:** `" + formula + "`\n"
	source += "   - **See:** [calculate](#step-calculate), `B2`, H<sub>2</sub>O<br>next\n\n"
	source += "   - Another child can move independently.\n\n"
	source += "```sheets\n" + formula + "\n```\n\n"
	source += "7. **Choose:** Format > Number\n"
	document = tutorial_lib.model.Document(tmp_path / "input.md", source, title="Native tutorial")
	document.tokens = markdown_it.MarkdownIt("commonmark", {"html": True}).parse(source)
	document.content_token_indices = list(range(len(document.tokens)))
	span = tutorial_lib.model.SourceSpan(str(document.path), 1, 1)
	reference = tutorial_lib.model.CellReference("Data", 2, 2, 2, 2, "B2")
	worksheet = tutorial_lib.model.Worksheet("Data", span)
	worksheet.google = tutorial_lib.model.GoogleMapping("source", "workbook123", "99")
	document.worksheets.append(worksheet)
	for index, token in enumerate(document.tokens):
		if token.type == "heading_open" and token.tag == "h4":
			heading = tutorial_lib.model.Heading(4, "Calculate", "Step 1: Calculate",
				"step-calculate", span, index, kind="step", number="1")
			token.meta["heading"] = heading
		if token.children:
			for child in token.children:
				if child.type == "code_inline" and child.content == "B2":
					child.meta["reference"] = reference
	output = tmp_path / "native.docx"
	tutorial_lib.docx_renderer.write_document(document, output)
	with zipfile.ZipFile(output) as archive:
		document_xml = defusedxml.ElementTree.fromstring(archive.read("word/document.xml"))
		numbering = defusedxml.ElementTree.fromstring(archive.read("word/numbering.xml"))
		footer_xml = defusedxml.ElementTree.fromstring(archive.read("word/footer1.xml"))
		relations = archive.read("word/_rels/document.xml.rels").decode("utf-8")
	texts = [node.text for node in document_xml.findall(".//w:t", NAMESPACES)]
	assert texts.count(formula) == 2
	assert "Step 1: Calculate" in "".join(texts)
	assert "workbook123/edit#gid=99&amp;range=B2" in relations
	assert document_xml.find(".//w:hyperlink[@w:anchor]", NAMESPACES) is not None
	assert document_xml.find(".//w:bookmarkStart", NAMESPACES) is not None
	page_field = footer_xml.find(".//w:fldSimple[@w:instr='PAGE']", NAMESPACES)
	assert page_field is not None
	assert document_xml.find(".//w:vertAlign[@w:val='subscript']", NAMESPACES) is not None
	starts = numbering.findall(".//w:start", NAMESPACES)
	assert {"3", "7"}.issubset({node.get("{" + NAMESPACES["w"] + "}val") for node in starts})
	assert document_xml.find(".//w:numPr", NAMESPACES) is not None
	cell_run = next(run for run in document_xml.findall(".//w:r", NAMESPACES)
		if run.find("w:t", NAMESPACES) is not None
		and run.find("w:t", NAMESPACES).text == "B2")
	assert cell_run.find("w:rPr/w:b", NAMESPACES) is not None
	assert cell_run.find("w:rPr/w:rFonts", NAMESPACES).get(
		docx.oxml.ns.qn("w:ascii")) == "Roboto Mono"
	paragraphs = {
		"".join(node.text or "" for node in paragraph.findall(".//w:t", NAMESPACES)): paragraph
		for paragraph in document_xml.findall(".//w:body/w:p", NAMESPACES)
	}
	parent = paragraphs["Enter D2: " + formula]
	child = paragraphs["See: calculate, B2, H2Onext"]
	heading = paragraphs["Step 1: Calculate"]
	assert heading.find(".//w:rFonts", NAMESPACES) is None
	assert parent.find("w:pPr/w:keepNext", NAMESPACES) is not None
	assert child.find("w:pPr/w:keepNext", NAMESPACES) is None
	assert paragraphs["Choose: Format > Number"].find("w:pPr/w:keepNext", NAMESPACES) is None


#============================================
def test_result_labels_stay_with_adjacent_entries(tmp_path: pathlib.Path) -> None:
	"""Keep adjacent result pairs without joining chains or crossing block boundaries."""
	source = "# Results\n\n## Workbook\n\n### Sheet: Data\n\n"
	source += "| x | y |\n| --- | --- |\n| 1 | 2 |\n\n"
	source += "## Tutorial\n\n### Part: Analysis\n\n#### Step: Calculate\n\n"
	source += "- **Label C1:** Summary\n"
	source += "- **Label C2:** Slope\n"
	source += "- **Enter D2:** `=SUM(A2:B2)`\n"
	source += "- **Label C3:** Intercept\n\n"
	source += "Explain what this result means.\n\n"
	source += "- **Enter D3:** `=SUM(A2:B2)`\n"
	source += "- **Label C4:** Earlier label\n"
	source += "- **Label C5:** Interpretation\n"
	source += "- **Instruction:** In cell `D5`, write what this result means.\n\n"
	source += "- **Label C6:** Before heading\n\n"
	source += "#### Step: Interpret\n\n"
	source += "- **Instruction:** In cell `D6`, explain the result.\n\n"
	source += "- **Label C7:** Before prose\n\n"
	source += "Consider the evidence.\n\n"
	source += "- **Instruction:** In cell `D7`, explain the evidence.\n\n"
	source += "- Parent\n  - **Label C8:** Nested label\n"
	source += "- **Instruction:** In cell `D8`, explain the nested result.\n\n"
	source += "- **Label C9:** Before table\n\n"
	source += "| Note |\n| --- |\n| Evidence |\n\n"
	source += "- **Instruction:** In cell `D9`, explain the table.\n\n"
	source += "- **Label C10:** Before plain instruction\n"
	source += "- Instruction: In cell `D10`, explain the result.\n"
	source += "- **Label C11:** Before later bold label\n"
	source += "- Read this **Instruction:** carefully.\n"
	document = tutorial_lib.compiler.compile_source(source, tmp_path / "results.md")
	assert not document.has_errors
	output = tmp_path / "results.docx"
	tutorial_lib.docx_renderer.write_document(document, output)
	with zipfile.ZipFile(output) as archive:
		document_xml = defusedxml.ElementTree.fromstring(archive.read("word/document.xml"))
	kept = [
		"".join(node.text or "" for node in paragraph.findall(".//w:t", NAMESPACES))
		for paragraph in document_xml.findall(".//w:body/w:p", NAMESPACES)
		if paragraph.find("w:pPr/w:keepNext", NAMESPACES) is not None
	]
	assert "Label C2: Slope" in kept
	assert "Label C1: Summary" not in kept
	assert "Label C3: Intercept" not in kept
	assert "Enter D2: =SUM(A2:B2)" not in kept
	assert "Label C5: Interpretation" in kept
	assert "Instruction: In cell D5, write what this result means." not in kept
	assert not set(kept).intersection({
		"Label C4: Earlier label", "Label C6: Before heading", "Label C7: Before prose",
		"Label C8: Nested label", "Label C9: Before table",
		"Label C10: Before plain instruction", "Label C11: Before later bold label",
	})


#============================================
def test_native_tables_images_and_menu_segments(tmp_path: pathlib.Path) -> None:
	"""Tables and images retain editable content, embedded data and authored order."""
	png = "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAwMCAO+aS1sAAAAASUVORK5CYII="
	(tmp_path / "pixel.png").write_bytes(base64.b64decode(png))
	source = "Before [linked before ![Local alt](pixel.png) linked after](https://example.org) after\n\n"
	source += "| Group | Value |\n| --- | --- |\n| native | 12 |\n\n"
	source += "![Data alt](data:image/png;base64," + png + ")\n\n"
	source += "- **Choose:** Format > Number > Percent\n"
	document = tutorial_lib.model.Document(tmp_path / "images.md", source)
	parser = markdown_it.MarkdownIt("commonmark").enable("table")
	document.tokens = parser.parse(source)
	document.content_token_indices = list(range(len(document.tokens)))
	span = tutorial_lib.model.SourceSpan(str(document.path), 1, 1)
	for index, token in enumerate(document.tokens):
		if token.type == "inline" and token.content.startswith("**Choose:"):
			token.meta["action"] = tutorial_lib.model.Action(
				"choose", span, index, "Format > Number > Percent",
				menu=["Format", "Number", "Percent"],
			)
	output = tmp_path / "images.docx"
	tutorial_lib.docx_renderer.write_document(document, output)
	with zipfile.ZipFile(output) as archive:
		document_xml = defusedxml.ElementTree.fromstring(archive.read("word/document.xml"))
		relations = archive.read("word/_rels/document.xml.rels").decode("utf-8")
		assert any(name.startswith("word/media/") for name in archive.namelist())
	texts = "".join(node.text or "" for node in document_xml.findall(".//w:t", NAMESPACES))
	assert "Before linked before  linked after after" in texts
	link = document_xml.find(".//w:hyperlink", NAMESPACES)
	linked_content = []
	for run in link.findall("w:r", NAMESPACES):
		if run.find("w:drawing", NAMESPACES) is not None:
			linked_content.append("image")
		else:
			linked_content.append("".join(node.text or "" for node in run.findall("w:t", NAMESPACES)))
	assert linked_content == ["linked before ", "image", " linked after"]
	assert 'Target="https://example.org"' in relations
	assert "native12" in texts
	assert "Format > Number > Percent" in texts
	menu_run = next(run for run in document_xml.findall(".//w:r", NAMESPACES)
		if "Format >" in "".join(run.itertext()))
	assert menu_run.find("w:rPr/w:b", NAMESPACES) is not None
	assert menu_run.find("w:rPr/w:rFonts", NAMESPACES).get(
		docx.oxml.ns.qn("w:ascii")) == "Roboto Mono"
	assert len(document_xml.findall(".//w:tbl", NAMESPACES)) == 1
	rows = document_xml.findall(".//w:tbl/w:tr", NAMESPACES)
	assert all(row.find("w:trPr/w:cantSplit", NAMESPACES) is not None for row in rows)
	assert rows[0].find("w:trPr/w:tblHeader", NAMESPACES) is not None
	assert rows[1].find("w:trPr/w:tblHeader", NAMESPACES) is None
	assert document_xml.find(".//w:tbl/w:tr/w:tc/w:p/w:pPr/w:keepNext", NAMESPACES) is None
	assert len(document_xml.findall(".//w:drawing", NAMESPACES)) == 2
