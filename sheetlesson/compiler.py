"""Compile parsed Markdown into one source-located tutorial/workbook model."""

import re
import json
import math
import pathlib
import urllib.parse
import sheetlesson.model as model
import sheetlesson.parser
import sheetlesson.references as references

NUMBER = re.compile(r"[+-]?(?:[0-9]+(?:\.[0-9]*)?|\.[0-9]+)(?:[eE][+-]?[0-9]+)?\Z")
STRUCTURE = re.compile(r"(Part|Step|Substep)(?: ([0-9]+(?:\.[0-9]+)?))?:\s*(.+)\Z")
ASSIGNMENT = re.compile(r"(Label|Enter|Replace)\s+(.+):\Z")


def span(document: model.Document, token: object) -> model.SourceSpan:
	location = token.map if token.map is not None else [0, 1]
	return model.SourceSpan(str(document.path), location[0] + 1, location[1])


def diagnostic(document: model.Document, category: str, location: model.SourceSpan,
	message: str, correction: str, severity: str = "error", **details) -> None:
	document.diagnostics.append(model.Diagnostic(
		severity, category, location, message, correction, **details,
	))


def scalar_text(raw: str) -> str:
	children = sheetlesson.parser.markdown_parser().parseInline(raw)[0].children
	if len(children) == 1 and children[0].type == "code_inline":
		return children[0].content
	if any(child.type not in ("text", "html_inline", "softbreak") for child in children):
		raise ValueError("Only plain text or one complete code span is allowed")
	pieces = []
	for child in children:
		if child.type == "html_inline":
			if re.fullmatch(r"<br\s*/?>", child.content, re.IGNORECASE) is None:
				raise ValueError("Only br markup is allowed in workbook scalars")
			pieces.append("\n")
		else:
			pieces.append(child.content)
	return "".join(pieces).strip()


def parse_scalar(raw: str) -> model.Scalar:
	# Table structural escapes are already removed; JSON escapes belong to JSON,
	# not Markdown. Code spans still follow the normal Markdown literal rules.
	text = raw.strip() if raw.strip().startswith('"') else scalar_text(raw)
	return _scalar_value(text)


def _scalar_value(text: str) -> model.Scalar:
	if not text:
		return model.Scalar("blank", None)
	if text.startswith('"'):
		try:
			value = json.loads(text)
		except json.JSONDecodeError as error:
			raise ValueError("Malformed JSON quoted string") from error
		if not isinstance(value, str):
			raise ValueError("Quoted cell value must be a JSON string")
		return model.Scalar("text", value)
	if text.startswith("="):
		if "\n" in text or not text[1:].strip():
			raise ValueError("A formula must contain one logical nonempty line")
		return model.Scalar("formula", text)
	if text in ("TRUE", "FALSE"):
		return model.Scalar("boolean", text == "TRUE")
	if NUMBER.fullmatch(text):
		value = float(text)
		if not math.isfinite(value):
			raise ValueError("Numeric values must be finite")
		if not any(item in text.lower() for item in (".", "e")):
			value = int(text)
		return model.Scalar("number", value)
	return model.Scalar("text", text)


def _table(document: model.Document, index: int, sheet: model.Worksheet,
	anchor: str) -> None:
	token = document.tokens[index]
	location = span(document, token)
	address = references.parse_reference(anchor, sheet.name)
	if address is None or ":" in anchor or "!" in anchor:
		diagnostic(document, "table-anchor", location, f"Invalid table anchor {anchor}",
			"Use one unqualified A1 cell")
		return
	lines = document.source.splitlines()[token.map[0]:token.map[1]]
	rows = [sheetlesson.parser.split_table_row(line) for offset, line in enumerate(lines)
		if offset != 1]
	width = len(rows[0])
	if any(len(row) != width for row in rows):
		diagnostic(document, "ragged-table", location, "Table rows have different cell counts",
			"Give every authored row the same number of cells")
		return
	end_row = address.start_row + len(rows) - 1
	end_column = address.start_column + width - 1
	if end_row > 1048576 or end_column > 16384:
		diagnostic(document, "table-bounds", location, "Table exceeds XLSX coordinates",
			"Move or shorten the table")
		return
	region = model.TableRegion(address.start_row, address.start_column, end_row, end_column,
		location)
	for previous in sheet.regions:
		row = max(previous.start_row, region.start_row)
		column = max(previous.start_column, region.start_column)
		if row <= min(previous.end_row, end_row) and column <= min(previous.end_column, end_column):
			diagnostic(document, "table-overlap", location, "Workbook table rectangles overlap",
				"Move the anchored table", worksheet=sheet.name,
				address=f"{references.column_letters(column)}{row}", related=previous.span)
			return
	sheet.regions.append(region)
	for row_offset, row in enumerate(rows):
		physical = token.map[0] + row_offset + (1 if row_offset == 0 else 2)
		cell_span = model.SourceSpan(str(document.path), physical, physical)
		for column_offset, raw in enumerate(row):
			try:
				scalar = parse_scalar(raw)
			except ValueError as error:
				diagnostic(document, "cell-scalar", cell_span, str(error),
					"Use a supported plain scalar or JSON quoted string")
				continue
			row_number = address.start_row + row_offset
			column_number = address.start_column + column_offset
			sheet.cells[(row_number, column_number)] = model.CellSeed(
				row_number, column_number, scalar, cell_span,
			)


def _mapping(document: model.Document, sheet: model.Worksheet, payload: str,
	location: model.SourceSpan) -> None:
	url = urllib.parse.urlparse(payload)
	match = re.fullmatch(r"/spreadsheets/d/([A-Za-z0-9_-]+)/(?:edit)?", url.path)
	parameters = urllib.parse.parse_qs(url.fragment)
	if url.scheme != "https" or url.netloc != "docs.google.com" or match is None:
		diagnostic(document, "google-mapping", location, "Malformed Google Sheets URL",
			"Supply an https docs.google.com spreadsheet edit URL")
		return
	gids = parameters.get("gid", [])
	if gids and (len(gids) != 1 or not gids[0].isdigit()):
		diagnostic(document, "google-mapping", location, "Google tab gid must be numeric",
			"Copy the worksheet URL with its numeric gid")
		return
	if sheet.google is not None:
		diagnostic(document, "google-mapping", location, "Duplicate worksheet mapping",
			"Keep one Google URL per worksheet")
		return
	sheet.google = model.GoogleMapping(payload, match[1], gids[0] if gids else None)
	if not gids:
		diagnostic(document, "google-tab-missing", location, "URL has no tab gid",
			"Include the worksheet gid to enable cell links", "warning")


def _opening(inline: object) -> tuple[str | None, str]:
	children = inline.children
	# markdown-it emits an empty text token before an opening emphasis delimiter.
	start = 0
	while start < len(children) and children[start].type == "text" and not children[start].content:
		start += 1
	if start >= len(children) or children[start].type != "strong_open":
		return None, inline.content
	end = start + 1
	while end < len(children) and children[end].type != "strong_close":
		end += 1
	if end == len(children):
		return None, inline.content
	opening = "".join(child.content for child in children[start + 1:end])
	# Source extraction preserves code span delimiters needed by scalar validation.
	match = re.match(r"\s*(?:\*\*|__).*?(?:\*\*|__)\s*", inline.content)
	payload = inline.content[match.end():] if match is not None else ""
	return opening, payload


def compile_document(path: str | pathlib.Path) -> model.Document:
	path = pathlib.Path(path).resolve()
	return compile_source(path.read_text(encoding="utf-8"), path)


def compile_source(source: str, path: str | pathlib.Path = "tutorial.md") -> model.Document:
	document = sheetlesson.parser.parse_source(source, path)
	_compile_structure(document)
	import sheetlesson.validation as validation
	validation.validate_document(document)
	return document


def _compile_structure(document: model.Document) -> None:
	section = "introduction"
	seen_sections = []
	sheet = None
	anchor = None
	part = None
	step = None
	part_number = 0
	step_number = 0
	substep_number = 0
	part_has_step = False
	part_span = None
	scope = None
	list_stack = []
	item_stack = []
	alternative_counter = 0
	previous_heading_level = 1
	skip_until = -1
	title_count = 0
	for index, token in enumerate(document.tokens):
		location = span(document, token)
		if section != "Workbook":
			document.content_token_indices.append(index)
		if index <= skip_until:
			continue
		if token.type == "heading_open":
			inline = document.tokens[index + 1]
			text = inline.content
			level = int(token.tag[1:])
			if level == 1:
				title_count += 1
				document.title = text
				if index != 0:
					diagnostic(document, "document-structure", location,
						"Document title must be first", "Place one H1 title first")
			elif level == 2:
				if section == "Workbook" and anchor is not None:
					diagnostic(document, "table-anchor", location, "At heading has no following table",
						"Place one table after each At heading")
				seen_sections.append(text)
				section = text
				previous_heading_level = 2
				if text not in ("Workbook", "Tutorial"):
					diagnostic(document, "document-structure", location,
						f"Unknown H2 section {text}", "Use Workbook then Tutorial")
				# Structural section headings are omitted from student content.
				for omitted in range(index, index + 3):
					if omitted in document.content_token_indices:
						document.content_token_indices.remove(omitted)
				skip_until = index + 2
				continue
			elif section == "Workbook":
				if level == 3 and text.startswith("Sheet:"):
					if anchor is not None:
						diagnostic(document, "table-anchor", location, "At heading has no following table",
							"Place a table before declaring another worksheet")
					name = text[6:].strip()
					if (not name or len(name) > 31 or re.search(r"[:\\/?*\[\]]", name)
						or name.startswith("'") or name.endswith("'")):
						diagnostic(document, "worksheet-name", location, "Invalid worksheet name",
							"Use a valid XLSX worksheet name of at most 31 characters")
					if any(existing.name.casefold() == name.casefold()
						for existing in document.worksheets):
						diagnostic(document, "worksheet-name", location, "Duplicate worksheet name",
							"Use names unique ignoring case")
					sheet = model.Worksheet(name, location)
					document.worksheets.append(sheet)
					anchor = None
				elif level == 4 and text.startswith("At:"):
					if anchor is not None:
						diagnostic(document, "table-anchor", location, "Unused preceding At heading",
							"Place a table after each At heading")
					anchor = text[3:].strip()
				else:
					diagnostic(document, "workbook-content", location, "Unexpected Workbook heading",
						"Use Sheet or At declarations")
				skip_until = index + 2
				continue
			elif section == "Tutorial":
				match = STRUCTURE.fullmatch(text)
				if match is None and re.match(r"(?i)(part|step|substep)\b", text):
					diagnostic(document, "heading-syntax", location, "Near-miss structural heading",
						"Use Part:, Step:, or Substep: with matching capitalization")
				if level > previous_heading_level + 1:
					diagnostic(document, "heading-hierarchy", location, "Heading skips a level",
						"Use the next heading level")
				previous_heading_level = level
				kind, number, title = "informational", None, text
				if match is not None:
					kind, explicit, title = match.groups()
					if kind != "Substep" and explicit is not None and "." in explicit:
						diagnostic(document, "heading-number", location, "Part and Step numbers must be integers",
							f"Use {kind}: {title}")
						explicit = None
					if level != {"Part": 3, "Step": 4, "Substep": 5}[kind]:
						diagnostic(document, "heading-hierarchy", location, "Structural heading at wrong level",
							"Use H3 Part, H4 Step, and H5 Substep")
					if kind == "Part":
						if part is not None and not part_has_step:
							diagnostic(document, "empty-part", part_span, "Part has no Step",
								"Add at least one Step with instructions")
						expected = int(explicit) if part_number == 0 and explicit else part_number + 1
						part_number = expected
						part, step, scope = title, None, None
						part_span, part_has_step, step_number = location, False, 0
						number = str(expected)
					elif kind == "Step":
						if part is None:
							diagnostic(document, "heading-hierarchy", location, "Step outside Part",
								"Add a Part heading before this Step")
						if scope is None:
							if len(document.worksheets) == 1:
								scope = document.worksheets[0].name
							else:
								diagnostic(document, "worksheet-scope", location, "Part has no worksheet scope",
									"Add a Worksheet declaration before its first Step")
						expected = int(explicit) if not part_has_step and explicit else step_number + 1
						step_number, substep_number = expected, 0
						part_has_step, step = True, title
						number = str(expected)
					else:
						if step is None:
							diagnostic(document, "heading-hierarchy", location, "Substep outside Step",
								"Add a containing Step")
						suffix = explicit.split(".")[-1] if explicit else None
						substep_number = int(suffix) if substep_number == 0 and suffix else substep_number + 1
						number = f"{step_number}.{substep_number}"
					if explicit is not None and explicit != number:
						diagnostic(document, "heading-number", location, "Contradictory explicit heading number",
							f"Use {kind} {number}: {title}")
					if kind == "Part" and part_number < 1 or kind == "Substep" and substep_number < 1:
						diagnostic(document, "heading-number", location, "Number must start at 1 or greater",
							"Use a positive part or substep number")
				display = f"{kind} {number}: {title}" if number else title
				if kind == "Substep":
					display = f"{number}: {title}"
				slug = re.sub(r"[^\w\s-]", "", text.lower())
				slug = re.sub(r"\s+", "-", slug.strip())
				heading = model.Heading(level, title, display, slug, location, index, kind.lower(), number)
				document.headings.append(heading)
				token.meta["heading"] = heading
			continue
		if section == "Workbook":
			if token.type == "table_open":
				if sheet is None:
					diagnostic(document, "worksheet-missing", location, "Table has no worksheet",
						"Declare a Sheet before the table")
				elif sheet.regions and anchor is None:
					diagnostic(document, "table-anchor", location, "Additional table has no At heading",
						"Add an At cell heading")
				else:
					_table(document, index, sheet, anchor if anchor is not None else "A1")
				anchor = None
				end = index + 1
				while document.tokens[end].type != "table_close":
					end += 1
				skip_until = end
			elif token.type == "inline":
				opening, payload = _opening(token)
				if (opening == "Google Sheets:" and sheet is not None
					and index >= 2 and document.tokens[index - 2].type == "list_item_open"
					and token.level == 3):
					if sheet.regions:
						diagnostic(document, "google-mapping", location, "Mapping occurs after first table",
							"Move metadata before the first table")
					_mapping(document, sheet, payload, location)
				else:
					diagnostic(document, "workbook-content", location, "Unrecognized Workbook content",
						"Move prose into Tutorial or use supported metadata")
			elif token.type in ("fence", "code_block", "html_block", "hr"):
				diagnostic(document, "workbook-content", location, "Unrecognized Workbook block",
					"Use worksheet declarations and rectangular tables")
			continue
		if section != "Tutorial":
			continue
		if token.type in ("bullet_list_open", "ordered_list_open"):
			list_stack.append({"group": None, "branches": 0})
		elif token.type in ("bullet_list_close", "ordered_list_close"):
			list_stack.pop()
		elif token.type == "list_item_open":
			item_stack.append({"opening": False, "alternative": None, "end": token.map[1]})
		elif token.type == "list_item_close":
			item_stack.pop()
		elif token.type == "inline" and item_stack and not item_stack[-1]["opening"]:
			item_stack[-1]["opening"] = True
			opening, payload = _opening(token)
			if opening is None:
				diagnostic(document, "list-opening", location, "List item has no bold opening",
					"Add a descriptive opening strong span", "warning")
			if opening is not None and opening.startswith("Alternative:"):
				if not opening[len("Alternative:"):].strip() or payload.strip():
					diagnostic(document, "alternative-syntax", location,
						"Alternative needs its title inside the opening strong span",
						"Use **Alternative: Description** followed by nested instructions")
				if any(item["alternative"] is not None for item in item_stack[:-1]):
					diagnostic(document, "nested-alternative", location, "Nested alternatives are unsupported",
						"Keep alternatives as sibling choice items")
				if list_stack[-1]["group"] is None:
					alternative_counter += 1
					list_stack[-1]["group"] = alternative_counter
				list_stack[-1]["branches"] += 1
				item_stack[-1]["alternative"] = (
					list_stack[-1]["group"], list_stack[-1]["branches"],
				)
				token.meta["alternative"] = item_stack[-1]["alternative"]
				token.meta["alternative_end"] = item_stack[-1]["end"]
				continue
			if list_stack:
				list_stack[-1]["group"] = None
				list_stack[-1]["branches"] = 0
			if opening == "Worksheet:":
				if part is None or step is not None or scope is not None:
					diagnostic(document, "worksheet-scope", location, "Worksheet declaration is out of place",
						"Place one declaration after Part and before its first Step")
				scope = payload.strip()
				if not any(item.name == scope for item in document.worksheets):
					diagnostic(document, "unknown-sheet", location, f"Unknown worksheet {scope}",
						"Name a declared worksheet")
				action = model.Action("worksheet", location, index, payload, worksheet=scope)
				document.actions.append(action)
				token.meta["action"] = action
				continue
			assignment = ASSIGNMENT.fullmatch(opening) if opening is not None else None
			kind = assignment[1].lower() if assignment else None
			if opening in ("Select:", "Choose:"):
				kind = opening[:-1].lower()
			if kind is None:
				if opening is not None and re.match(r"(Label|Enter|Replace|Select|Choose)\b", opening):
					diagnostic(document, "action-syntax", location, "Malformed recognized action",
						"Use a complete action opening including its colon")
				continue
			if step is None:
				diagnostic(document, "action-scope", location, "Action has no containing Step",
					"Move this action beneath a Step")
			action = model.Action(kind, location, index, payload, worksheet=scope)
			alternatives = [item["alternative"] for item in item_stack if item["alternative"] is not None]
			if alternatives:
				action.alternative_group, action.alternative_branch = alternatives[-1]
			if kind == "choose":
				try:
					path = scalar_text(payload)
				except ValueError as error:
					diagnostic(document, "menu-path", location, str(error),
						"Use a plain menu path or one complete code span")
					continue
				action.menu = [part.strip() for part in re.split(r">|\u2192", path)]
				if any(not segment for segment in action.menu):
					diagnostic(document, "menu-path", location, "Empty menu path segment",
						"Supply a name between each menu separator")
			else:
				try:
					target_text = assignment[2] if assignment else scalar_text(payload)
				except ValueError as error:
					diagnostic(document, "action-target", location, str(error),
						"Use a plain A1 reference or one complete code span")
					continue
				action.target = references.parse_reference(target_text, scope if scope else "")
				if action.target is None or kind != "select" and ":" in target_text:
					diagnostic(document, "action-target", location, "Invalid action target",
						"Use one A1 cell for assignments or a valid range for Select")
				if kind != "select":
					_scalar_action(document, action, index, item_stack[-1]["end"])
			document.actions.append(action)
			token.meta["action"] = action
	if title_count != 1 or seen_sections != ["Workbook", "Tutorial"]:
		diagnostic(document, "document-structure", model.SourceSpan(str(document.path), 1, 1),
			"Require one title followed by Workbook and Tutorial", "Use the required H1/H2 structure")
	if not document.worksheets:
		diagnostic(document, "worksheet-missing", model.SourceSpan(str(document.path), 1, 1),
			"Workbook has no worksheets", "Declare at least one Sheet")
	if part is None or not part_has_step:
		diagnostic(document, "empty-part", part_span if part_span else model.SourceSpan(str(document.path), 1, 1),
			"Tutorial needs a Part containing a Step", "Add authored tutorial instructions")
	section_indices = {document.tokens[index + 1].content: index
		for index, token in enumerate(document.tokens) if token.type == "heading_open"
		and token.tag == "h2"}
	if "Workbook" in section_indices and "Tutorial" in section_indices:
		document.content_token_indices = list(range(section_indices["Workbook"]))
		document.content_token_indices.extend(range(section_indices["Tutorial"] + 3,
			len(document.tokens)))


def _scalar_action(document: model.Document, action: model.Action, index: int,
	item_end: int) -> None:
	raw = action.payload
	fences = []
	for following in document.tokens[index + 1:]:
		if following.map is not None and following.map[0] >= item_end:
			break
		if following.type == "fence" and following.level == document.tokens[index].level - 1:
			fences.append(following)
	if fences:
		if (action.kind == "label" or raw.strip() or len(fences) != 1
			or fences[0].info.strip() != "sheets"):
			diagnostic(document, "action-scalar", action.span, "Competing or unsupported formula block",
				"Use literal text for Label; use one sheets formula block for Enter or Replace")
			return
		formula = fences[0].content.rstrip("\n")
		if (not formula.startswith("=") or not formula[1:].strip()
			or "\n" in formula):
			diagnostic(document, "action-scalar", action.span, "Formula block must contain one formula line",
				"Use one logical line starting with equals")
			return
		action.scalar = _scalar_value(formula)
		return
	try:
		if action.kind == "label":
			action.scalar = model.Scalar("text", scalar_text(raw))
		else:
			action.scalar = parse_scalar(raw)
			if action.scalar.kind == "blank":
				raise ValueError("Assignment payload is empty")
			if action.scalar.kind == "formula" and not fences:
				children = document.tokens[index].children
				if sum(child.type == "code_inline" for child in children) != 1:
					raise ValueError("Instruction formulas require one code span")
	except ValueError as error:
		diagnostic(document, "action-scalar", action.span, str(error),
			"Use one scalar; put explanations in a separate paragraph")
