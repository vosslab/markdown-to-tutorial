"""Static spreadsheet reference recognition using lexical formula tokens."""

import re
import openpyxl.formula.tokenizer
import sheetlesson.model

CELL = re.compile(r"\$?([A-Za-z]{1,3})\$?([1-9][0-9]*)\Z")
REFERENCE = re.compile(r"(?:(?:'((?:[^']|'')+)'|([^'!]+))!)?([^!]+)\Z")


def column_number(letters: str) -> int:
	value = 0
	for letter in letters.upper():
		value = value * 26 + ord(letter) - 64
	return value


def column_letters(column: int) -> str:
	letters = ""
	while column:
		column, remainder = divmod(column - 1, 26)
		letters = chr(65 + remainder) + letters
	return letters


def parse_reference(text: str, default_sheet: str) -> sheetlesson.model.CellReference | None:
	match = REFERENCE.fullmatch(text.strip())
	if match is None:
		return None
	quoted, plain, address = match.groups()
	sheet = quoted.replace("''", "'") if quoted is not None else plain
	if sheet is None:
		sheet = default_sheet
	coordinates = address.split(":")
	if len(coordinates) not in (1, 2):
		return None
	cells = [CELL.fullmatch(value) for value in coordinates]
	if any(cell is None for cell in cells):
		return None
	first = cells[0]
	last = cells[-1]
	start_column = column_number(first[1])
	end_column = column_number(last[1])
	start_row, end_row = int(first[2]), int(last[2])
	if not (1 <= start_column <= end_column <= 16384):
		return None
	if not (1 <= start_row <= end_row <= 1048576):
		return None
	return sheetlesson.model.CellReference(
		sheet, start_row, start_column, end_row, end_column, address,
	)


def formula_references(formula: str, sheet: str) -> tuple[list, list[str], list[str]]:
	"""Tokenize strings/functions separately; never scan quoted formula text as references."""
	try:
		tokens = openpyxl.formula.tokenizer.Tokenizer(formula).items
	except (openpyxl.formula.tokenizer.TokenizerError, IndexError):
		return [], ["Formula syntax could not be tokenized"], []
	references = []
	limitations = []
	invalid_addresses = []
	common = {
		"SUM", "AVERAGE", "COUNT", "COUNTA", "STDEV", "STDEV.S", "STDEV.P", "VAR",
		"VAR.S", "VAR.P", "SQRT", "ABS", "MIN", "MAX", "ROUND", "IF", "AND", "OR",
		"NOT", "T.TEST", "TTEST", "F.TEST", "FTEST", "Z.TEST", "ZTEST", "T.DIST",
		"T.DIST.2T", "T.DIST.RT", "T.INV", "T.INV.2T", "NORM.DIST", "NORM.S.DIST",
		"NORM.INV", "NORM.S.INV", "F.DIST", "F.DIST.RT", "F.INV", "F.INV.RT",
		"CHISQ.TEST", "CHISQ.DIST", "CHISQ.DIST.RT", "CHISQ.INV", "CHISQ.INV.RT",
		"COUNTIF", "COUNTIFS", "SUMIF", "SUMIFS", "MEDIAN", "MODE", "POWER", "EXP",
		"LN", "LOG", "LOG10", "CORREL", "SLOPE", "INTERCEPT", "STEYX", "RSQ",
	}
	for token in tokens:
		if token.type == "OPERAND" and token.subtype == "RANGE":
			reference = parse_reference(token.value, sheet)
			match = REFERENCE.fullmatch(token.value)
			# A recognizable static A1 reference that fails coordinate validation is
			# an authored error, rather than an unsupported formula feature.
			coordinates = match[3].split(":") if match is not None else []
			static_address = (len(coordinates) in (1, 2)
				and not any(character in token.value for character in "[]")
				and not (match[2] is not None and ":" in match[2])
				and all(re.fullmatch(r"\$?[A-Za-z]+\$?[0-9]+", item)
					for item in coordinates))
			if reference is None and static_address:
				invalid_addresses.append(token.value)
			elif (reference is None or "[" in token.value or "]" in token.value
				or ":" in reference.sheet):
				limitations.append(f"Unsupported reference syntax: {token.value}")
			else:
				references.append(reference)
		elif token.type == "FUNC" and token.subtype == "OPEN":
			function = token.value[:-1].upper()
			if function not in common:
				limitations.append(f"Function compatibility unchecked: {function}")
		elif token.type in ("ARRAY",) or token.value in ("@", "#"):
			limitations.append("Array or spill syntax is not validated")
	return references, list(dict.fromkeys(limitations)), list(dict.fromkeys(invalid_addresses))
