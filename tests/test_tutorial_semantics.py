"""Durable author-facing semantic contracts independent of rendering internals."""

import json
import tutorial_lib.compiler


def compile_tutorial(instructions: str, workbook: str = "") -> object:
	if not workbook:
		workbook = "### Sheet: Data\n\n| A | B |\n| --- | --- |\n| 1 | 2 |"
	source = "# Example\n\n## Workbook\n\n" + workbook
	source += "\n\n## Tutorial\n\n### Part 3: Analysis\n\n#### Step: Calculate\n\n"
	source += instructions
	return tutorial_lib.compiler.compile_source(source)


def test_scalar_fidelity_and_student_destinations() -> None:
	workbook = '### Sheet: Data\n\n| "001" | `"=text"` | `=IF(A2="x\\|y",1,0)` |\n'
	workbook += '| --- | --- | --- |\n| 0 | FALSE | |'
	document = compile_tutorial('- **Enter D2:** `=SUM(A2:B2)`', workbook)
	assert not document.has_errors
	sheet = document.worksheets[0]
	assert sheet.cells[(1, 1)].scalar.value == "001"
	assert sheet.cells[(1, 2)].scalar.kind == "text"
	assert sheet.cells[(1, 3)].scalar.value == '=IF(A2="x|y",1,0)'
	assert (2, 4) in sheet.entry_cells and (2, 4) not in sheet.cells
	assert sheet.cells[(2, 1)].scalar.value == 0
	assert sheet.cells[(2, 2)].scalar.value is False
	# Ordinary JSON escaping survives table syntax and optional code spans.
	for value in ('a\\b', 'say "hi"', 'x|y', 'line\nnext', '*literal*'):
		encoded = json.dumps(value).replace("|", "\\|")
		workbook = f'### Sheet: Data\n\n| {encoded} | `{encoded}` |\n| --- | --- |'
		document = compile_tutorial('- **Enter C2:** ' + json.dumps(value), workbook)
		assert not document.has_errors
		assert [cell.scalar.value for cell in document.worksheets[0].cells.values()] == [value, value]
		assert document.actions[0].scalar.value == value
	literal = compile_tutorial('- **Label C2:** `a\\b`')
	assert literal.actions[0].scalar.value == 'a\\b'


def test_invalid_tables_report_physical_and_related_locations() -> None:
	workbook = '### Sheet: Data\n\n| A | B |\n| --- | --- |\n| 1 | 2 |\n'
	workbook += '\n#### At: B2\n\n| | |\n| --- | --- |'
	document = compile_tutorial('- **Explain:** Observe.', workbook)
	overlap = next(item for item in document.diagnostics if item.category == "table-overlap")
	assert overlap.address == "B2" and overlap.related.start_line == 7
	ragged = compile_tutorial('- **Explain:** Observe.', workbook.replace('| 1 | 2 |', '| 1 |'))
	assert any(item.category == "ragged-table" for item in ragged.diagnostics)


def test_alternatives_preserve_possible_states_and_numbering() -> None:
	instructions = '- **Alternative: First**\n  - **Enter D2:** `=SUM(A2:B2)`\n'
	instructions += '- **Alternative: Second**\n  - **Enter D2:** `=AVERAGE(A2:B2)`\n'
	instructions += '\n#### Step: Continue\n\n##### Substep: Review\n\n'
	instructions += '- **Replace D2:** `=MAX(A2:B2)`\n'
	document = compile_tutorial(instructions)
	assert not document.has_errors
	assert [heading.number for heading in document.headings] == ["3", "1", "2", "2.1"]
	conditional = compile_tutorial(instructions.replace(
		'  - **Enter D2:** `=AVERAGE(A2:B2)`', '  - **Explain:** No entry.'))
	assert any(item.category == "replacement-unavailable" for item in conditional.diagnostics)


def test_static_formula_tokens_skip_strings_and_report_partial_coverage() -> None:
	instructions = '- **Enter D2:** `=IF(A2="Missing!Z99",SUM($A$2:B$2),0)`\n'
	instructions += '- **Enter D3:** `=SUM(A:A)+INDIRECT("Z99")`\n'
	document = compile_tutorial(instructions)
	assert not document.has_errors
	assert document.formula_checks[0].status == "verified"
	assert [ref.address for ref in document.formula_checks[0].references] == ["A2", "$A$2:B$2"]
	assert document.formula_checks[1].status == "unchecked"
	wrong_sheet = compile_tutorial('- **Enter D2:** `=SUM(Absent!A2:B2)`')
	assert any(item.category == "unknown-sheet" for item in wrong_sheet.diagnostics)
	for address in ('XFE1', 'A1048577', 'A0', 'B2:A1'):
		invalid = compile_tutorial(f'- **Enter D2:** `={address}+1`')
		assert any(item.category == "invalid-address" and item.severity == "error"
			for item in invalid.diagnostics)
		assert invalid.formula_checks[0].status != "verified"
	for formula in ('=SUM(A1))', '=A1)'):
		malformed = compile_tutorial(f'- **Enter D2:** `{formula}`')
		assert malformed.has_errors
		assert malformed.formula_checks[0].status != "verified"
		diagnostic = next(item for item in malformed.diagnostics if item.category == "formula-syntax")
		assert diagnostic.span.start_line > 1
		assert "Correct the formula syntax" in diagnostic.correction


def test_literal_scalar_reference_text_is_not_classified_as_workbook_reference() -> None:
	for action in ('Label', 'Enter'):
		document = compile_tutorial(f'- **{action} C2:** `Absent!A1`')
		assert not any(item.category == "unknown-sheet" for item in document.diagnostics)
	assert any(item.category == "unknown-sheet" for item in compile_tutorial(
		'- **Explain:** Refer to `Absent!A1`.').diagnostics)
	assert any(item.category == "unknown-sheet" for item in compile_tutorial(
		'- **Select:** `Absent!A1`').diagnostics)


def test_action_payload_contracts_produce_source_diagnostics() -> None:
	cases = [
		('- **Choose:** **Insert** > Chart', 'menu-path'),
		('- **Select:** **A1**', 'action-target'),
		('- **Label C2:**\n\n  ```sheets\n  =A2\n  ```', 'action-scalar'),
		('- **Enter C2:**\n\n  ```sheets\n  =\n  ```', 'action-scalar'),
		('- **Enter C2:** `=   `', 'action-scalar'),
	]
	for instructions, category in cases:
		document = compile_tutorial(instructions)
		assert document.has_errors
		assert any(item.category == category and item.span.start_line > 1
			for item in document.diagnostics)
	valid = compile_tutorial('- **Enter C2:**\n\n  ```sheets\n  =A2\n  ```')
	assert not valid.has_errors
	assert valid.actions[0].scalar.value == '=A2'


def test_label_only_list_items_need_substantive_content() -> None:
	empty_leaf = compile_tutorial('- **Guide:** **For Sample Means:**')
	diagnostics = [item for item in empty_leaf.diagnostics
		if item.category == "incomplete-instruction"]
	assert len(diagnostics) == 1
	assert diagnostics[0].severity == "error"
	assert diagnostics[0].span.start_line == 17

	valid = compile_tutorial('- **Guide:** **Setup Another Table:**\n'
		'  - **Enter C2:** `=A2`')
	assert not any(item.category == "incomplete-instruction" for item in valid.diagnostics)
	assert not valid.has_errors

	for instructions in (
		'- **Guide:**\n\n  Continue in prose.',
		'- **Guide:** **For Sample Means:**\n  Continue in the same paragraph.',
		'- **Enter C2:** `=A2`',
	):
		document = compile_tutorial(instructions)
		assert not any(item.category == "incomplete-instruction" for item in document.diagnostics)

	empty_child = compile_tutorial('- **Guide:**\n  - **Setup Another Table:**')
	assert any(item.category == "incomplete-instruction" and item.span.start_line == 18
		for item in empty_child.diagnostics)

	nonempty_fence = compile_tutorial('- **Guide:** **For Sample Means:**\n\n'
		'  ```text\n  Notes for this step.\n  ```')
	assert not any(item.category == "incomplete-instruction"
		for item in nonempty_fence.diagnostics)
	empty_fence = compile_tutorial('- **Guide:** **For Sample Means:**\n\n'
		'  ```text\n  ```')
	assert any(item.category == "incomplete-instruction" for item in empty_fence.diagnostics)

	outside_tutorial = ('# Example\n\n- **Introduction:** **Overview:**\n\n'
		'## Workbook\n\n- **Worksheet:** **Instructions:**\n\n'
		'### Sheet: Data\n\n| A | B |\n| --- | --- |\n| 1 | 2 |\n\n'
		'## Tutorial\n\n### Part 3: Analysis\n\n#### Step: Calculate\n\n'
		'- **Enter C2:** `=A2`')
	document = tutorial_lib.compiler.compile_source(outside_tutorial)
	assert not any(item.category == "incomplete-instruction" for item in document.diagnostics)
	inside_tutorial = outside_tutorial.replace(
		'- **Enter C2:** `=A2`', '- **Guide:** **For Sample Means:**')
	# The same label-only shape is diagnosed when it appears in the Tutorial region.
	document = tutorial_lib.compiler.compile_source(inside_tutorial)
	assert any(item.category == "incomplete-instruction" for item in document.diagnostics)


def test_unsupported_footnotes_exempt_literal_code() -> None:
	literal = compile_tutorial('- **Explain:** Type `[^1]` literally.')
	assert not literal.has_errors
	footnote = compile_tutorial('- **Explain:** This needs a footnote[^1].')
	assert any(item.category == "unsupported-content" for item in footnote.diagnostics)
