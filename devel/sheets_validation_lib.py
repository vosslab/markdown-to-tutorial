"""Prepare tutorial execution cases and inspect actual Google Sheets results."""

import math
import time
import random

import tutorial_lib.model
import tutorial_lib.references


#============================================
def extended_value(scalar: tutorial_lib.model.Scalar) -> dict:
	"""Preserve scalar types, including formula and literal equals-prefixed text."""
	keys = {"formula": "formulaValue", "text": "stringValue", "number": "numberValue",
		"boolean": "boolValue"}
	if scalar.kind == "blank":
		return {}
	result = {keys[scalar.kind]: scalar.value}
	return result


#============================================
def cell_write(sheet: str, row: int, column: int,
	scalar: tutorial_lib.model.Scalar, line: int) -> dict:
	address = f"{tutorial_lib.references.column_letters(column)}{row}"
	result = {"sheet": sheet, "row": row, "column": column, "address": address,
		"value": extended_value(scalar), "line": line}
	return result


#============================================
def prepare_cases(document: tutorial_lib.model.Document) -> list[dict]:
	"""Cover each alternative once, changing one group from the baseline at a time."""
	if document.has_errors:
		raise ValueError(f"Cannot execute invalid tutorial: {document.path}")
	groups = {}
	for action in document.actions:
		if action.alternative_group is not None:
			groups.setdefault(action.alternative_group, set()).add(action.alternative_branch)
	baseline = {group: min(branches) for group, branches in groups.items()}
	selections = [("baseline", baseline)]
	for group, branches in sorted(groups.items()):
		for branch in sorted(branches):
			if branch != baseline[group]:
				selections.append((f"group-{group}-branch-{branch}", baseline | {group: branch}))
	seeds = []
	for sheet in document.worksheets:
		for seed in sheet.cells.values():
			seeds.append(cell_write(sheet.name, seed.row, seed.column,
				seed.scalar, seed.span.start_line))
	cases = []
	for name, selected in selections:
		writes = []
		for action in document.actions:
			if action.alternative_group is not None:
				if selected[action.alternative_group] != action.alternative_branch:
					continue
			executable = action.generated_actions if action.kind == "fill" else [action]
			for entry in executable:
				if entry.scalar is None or entry.target is None:
					continue
				write = cell_write(entry.target.sheet, entry.target.start_row,
					entry.target.start_column, entry.scalar, action.span.start_line)
				write["action"] = entry.kind
				writes.append(write)
		cases.append({"tutorial": str(document.path), "scenario": name,
			"branches": selected, "sheets": [sheet.name for sheet in document.worksheets],
			"seeds": seeds, "writes": writes})
	return cases


#============================================
def update_request(write: dict, sheet_ids: dict) -> dict:
	result = {"updateCells": {"start": {"sheetId": sheet_ids[write["sheet"]],
		"rowIndex": write["row"] - 1, "columnIndex": write["column"] - 1},
		"rows": [{"values": [{"userEnteredValue": write["value"]}]}],
		"fields": "userEnteredValue"}}
	return result


#============================================
def a1_range(write: dict) -> str:
	quoted = write["sheet"].replace("'", "''")
	result = f"'{quoted}'!{write['address']}"
	return result


#============================================
def execute_request(request: object) -> dict:
	"""Pace requests and use the client's bounded retry policy."""
	time.sleep(1.05 + random.random())
	result = request.execute(num_retries=3)
	return result


#============================================
def read_cells(service: object, spreadsheet_id: str, ranges: list[str]) -> dict:
	response = execute_request(service.spreadsheets().get(
		spreadsheetId=spreadsheet_id, ranges=ranges, includeGridData=True,
		fields="sheets(properties(title),data(startRow,startColumn,rowData(values("
		"userEnteredValue,effectiveValue,formattedValue))))"))
	cells = {}
	for sheet in response.get("sheets", []):
		for grid in sheet.get("data", []):
			for row_offset, row in enumerate(grid.get("rowData", [])):
				for column_offset, cell in enumerate(row.get("values", [])):
					row_number = grid.get("startRow", 0) + row_offset + 1
					column = grid.get("startColumn", 0) + column_offset + 1
					address = tutorial_lib.references.column_letters(column) + str(row_number)
					cells[sheet["properties"]["title"] + "!" + address] = cell
	return cells


#============================================
def compare_expectations(cells: dict, expectations: dict) -> list[dict]:
	results = []
	for address, expectation in expectations.items():
		expected = expectation["value"]
		cell = cells.get(address, {})
		effective = cell.get("effectiveValue", {})
		actual = None
		has_actual_value = False
		for key in ("numberValue", "stringValue", "boolValue"):
			if key in effective:
				actual = effective[key]
				has_actual_value = True
		matches = has_actual_value and type(actual) is type(expected) and actual == expected
		if type(expected) in (int, float) and type(actual) in (int, float):
			matches = math.isclose(actual, expected,
				rel_tol=expectation.get("relative_tolerance", 1e-7),
				abs_tol=expectation.get("absolute_tolerance", 1e-9))
		results.append({"address": address, "expected": expected, "actual": actual,
			"status": "passed" if matches and "errorValue" not in effective else "failed"})
	return results


#============================================
def run_case(service: object, case: dict, expected: dict,
	record_created: object) -> dict:
	"""Create a private test workbook; never consult authored Google mapping IDs."""
	sheet_ids = {name: index for index, name in enumerate(case["sheets"])}
	# Include distant targets instead of relying on the default 1000-by-26 grid.
	dimensions = {name: [1000, 26] for name in sheet_ids}
	for write in case["seeds"] + case["writes"]:
		size = dimensions[write["sheet"]]
		size[0], size[1] = max(size[0], write["row"]), max(size[1], write["column"])
	created = execute_request(service.spreadsheets().create(body={
		"properties": {"title": "TUTORIAL VALIDATION - " + case["scenario"] + " - "
			+ case["tutorial"].split("/")[-1], "locale": "en_US"},
		"sheets": [{"properties": {"sheetId": sheet_ids[name], "title": name,
			"gridProperties": {"rowCount": dimensions[name][0],
				"columnCount": dimensions[name][1]}}} for name in case["sheets"]]},
		fields="spreadsheetId,spreadsheetUrl"))
	# Persist ownership before any subsequent operation can fail.
	record_created(created)
	spreadsheet_id = created["spreadsheetId"]
	if case["seeds"]:
		execute_request(service.spreadsheets().batchUpdate(spreadsheetId=spreadsheet_id,
			body={"requests": [update_request(write, sheet_ids) for write in case["seeds"]]}))
	checkpoints = []
	for write in case["writes"]:
		execute_request(service.spreadsheets().batchUpdate(spreadsheetId=spreadsheet_id,
			body={"requests": [update_request(write, sheet_ids)]}))
		if "formulaValue" in write["value"]:
			cells = read_cells(service, spreadsheet_id, [a1_range(write)])
			checkpoints.append({"line": write["line"], "address": write["sheet"] + "!"
				+ write["address"], "cells": cells})
	# Read the whole populated sheets, including spill results and error values.
	cells = read_cells(service, spreadsheet_id,
		["'" + name.replace("'", "''") + "'" for name in case["sheets"]])
	errors = [{"address": address, "error": cell["effectiveValue"]["errorValue"]}
		for address, cell in cells.items() if "errorValue" in cell.get("effectiveValue", {})]
	for checkpoint in checkpoints:
		checkpoint_cell = checkpoint["cells"].get(checkpoint["address"], {})
		if not checkpoint_cell.get("effectiveValue"):
			errors.append({"address": checkpoint["address"], "line": checkpoint["line"],
				"error": {"type": "MISSING_RESULT", "message": "Formula cell not returned"}})
		for address, cell in checkpoint["cells"].items():
			if "errorValue" in cell.get("effectiveValue", {}):
				errors.append({"address": address, "line": checkpoint["line"],
					"error": cell["effectiveValue"]["errorValue"]})
	# A missing computed value is unavailable evidence, never a clean formula result.
	final_writes = {write["sheet"] + "!" + write["address"]: write
		for write in case["seeds"] + case["writes"]}
	for address, write in final_writes.items():
		if "formulaValue" in write["value"]:
			cell = cells.get(address, {})
			if not cell.get("effectiveValue"):
				errors.append({"address": address,
					"error": {"type": "MISSING_RESULT", "message": "No calculated value returned"}})
	comparisons = compare_expectations(cells, expected)
	oracle_status = "not_provided"
	if comparisons:
		oracle_status = "passed" if all(x["status"] == "passed" for x in comparisons) else "failed"
	result = {"tutorial": case["tutorial"], "scenario": case["scenario"], **created,
		"sheets_status": "failed" if errors else "passed", "errors": errors,
		"oracle_status": oracle_status, "comparisons": comparisons,
		"checkpoints": checkpoints, "cells": cells}
	return result
