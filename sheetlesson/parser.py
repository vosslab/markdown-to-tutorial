"""Markdown adapter retaining physical rows before GFM table normalization."""

import pathlib
import markdown_it
import sheetlesson.model


def markdown_parser() -> markdown_it.MarkdownIt:
	parser = markdown_it.MarkdownIt("commonmark", {"html": True})
	parser.enable("table")
	return parser


def parse_source(source: str, path: str | pathlib.Path) -> sheetlesson.model.Document:
	document = sheetlesson.model.Document(pathlib.Path(path), source)
	document.tokens = markdown_parser().parse(source)
	return document


def split_table_row(line: str) -> list[str]:
	"""Split GFM geometry: an escaped pipe is literal even inside code spans."""
	line = line.strip()
	if line.startswith("|"):
		line = line[1:]
	if line.endswith("|"):
		backslashes = len(line[:-1]) - len(line[:-1].rstrip("\\"))
		if backslashes % 2 == 0:
			line = line[:-1]
	parts = [""]
	for character in line:
		backslashes = len(parts[-1]) - len(parts[-1].rstrip("\\"))
		if character == "|" and backslashes % 2 == 0:
			parts.append("")
		elif character == "|":
			parts[-1] = parts[-1][:-1] + "|"
		else:
			parts[-1] += character
	return [part.strip() for part in parts]
