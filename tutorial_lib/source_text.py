"""Source-text rules for student-authored active lessons."""

import re
import tutorial_lib.model


NUMERIC_ENTITY = re.compile(r"&#(?:[0-9]+|[xX][0-9A-Fa-f]+);")


def source_diagnostics(document: tutorial_lib.model.Document) -> list[tutorial_lib.model.Diagnostic]:
	"""Return ASCII-source diagnostics without changing an author's text."""
	diagnostics = []
	for line_number, line in enumerate(document.source.splitlines(), start=1):
		location = tutorial_lib.model.SourceSpan(str(document.path), line_number, line_number)
		for match in NUMERIC_ENTITY.finditer(line):
			diagnostics.append(tutorial_lib.model.Diagnostic(
				"error", "source-numeric-entity", location,
				f"Numeric character reference {match[0]} is not allowed in student source",
				"Use ASCII punctuation or a readable named entity such as &alpha;"))
		for column, character in enumerate(line, start=1):
			if ord(character) <= 127:
				continue
			diagnostics.append(tutorial_lib.model.Diagnostic(
				"error", "source-non-ascii", location,
				f"Non-ASCII character U+{ord(character):04X} at column {column}",
				"Use ordinary keyboard punctuation or a readable named entity"))
	return diagnostics
