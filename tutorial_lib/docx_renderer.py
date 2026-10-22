"""Native DOCX export of the compiled tutorial, excluding workbook declarations."""

import pathlib
import copy
import re

import docx
import docx.oxml
import docx.oxml.ns
import docx.shared

import tutorial_lib.model
import tutorial_lib.docx_inline
import tutorial_lib.docx_styles
import tutorial_lib.docx_numbering


#============================================
def add_bookmark(paragraph: object, slug: str, identifier: int) -> None:
	start = docx.oxml.OxmlElement("w:bookmarkStart")
	start.set(docx.oxml.ns.qn("w:id"), str(identifier))
	start.set(docx.oxml.ns.qn("w:name"), tutorial_lib.docx_inline.bookmark_name(slug))
	end = docx.oxml.OxmlElement("w:bookmarkEnd")
	end.set(docx.oxml.ns.qn("w:id"), str(identifier))
	paragraph._p.insert(0, start)
	paragraph._p.append(end)


#============================================
def add_heading(output: object, token: object, inline: object, document: object,
	identifier: int) -> None:
	"""Use explicit generated labels and native outline heading styles."""
	heading = token.meta.get("heading")
	if heading is None:
		paragraph = output.add_paragraph(style=f"Heading {min(int(token.tag[1:]), 9)}")
		tutorial_lib.docx_inline.render(paragraph, inline.children or [], document)
		return
	styles = {"part": "Tutorial Part", "step": "Tutorial Step",
		"substep": "Tutorial Substep", "title": "Tutorial Title"}
	style = styles.get(heading.kind, f"Heading {min(heading.level, 9)}")
	if heading.level == 1:
		style = "Tutorial Title"
	paragraph = output.add_paragraph(style=style)
	# Remove only the authored structural prefix; keep title emphasis and links native.
	children = list(inline.children or [])
	if heading.kind in ("part", "step", "substep"):
		prefix = heading.display[:-len(heading.title)] if heading.title else heading.display
		paragraph.add_run(prefix)
		if children and children[0].type == "text":
			children[0] = copy.copy(children[0])
			children[0].content = re.sub(
				r"^(Part|Step|Substep)(?: [0-9.]+)?:\s*", "", children[0].content,
			)
	tutorial_lib.docx_inline.render(paragraph, children, document)
	add_bookmark(paragraph, heading.slug, identifier)


#============================================
def keep_label_with_entry(output: object, document: tutorial_lib.model.Document,
	position: int, action: tutorial_lib.model.Action | None) -> None:
	"""Keep an adjacent list label and its right-hand result on the same page."""
	if action is None or action.kind not in ("enter", "replace") or position < 5:
		return
	neighbors = [document.tokens[index]
		for index in document.content_token_indices[position - 5:position]]
	# Only sibling list paragraphs qualify; prose, charts and headings break the pair.
	if [token.type for token in neighbors] != ["inline", "paragraph_close",
		"list_item_close", "list_item_open", "paragraph_open"]:
		return
	previous = neighbors[0]
	if previous.level != document.tokens[document.content_token_indices[position]].level:
		return
	label = previous.meta.get("action")
	if label is None or label.kind != "label" or label.target is None or action.target is None:
		return
	left, right = label.target, action.target
	if (left.start_row == left.end_row == right.start_row == right.end_row
		and left.start_column == left.end_column
		and right.start_column == right.end_column == left.start_column + 1
		and left.sheet == right.sheet):
		output.paragraphs[-2].paragraph_format.keep_with_next = True


#============================================
def render_tokens(output: object, document: tutorial_lib.model.Document) -> None:
	"""Walk selected block tokens while retaining list and table structure."""
	lists = []
	items = []
	paragraph = None
	table = None
	row = None
	cell = None
	column = 0
	quote_depth = 0
	action = None
	headings = {item.token_index: item for item in document.headings}
	actions = {item.token_index: item for item in document.actions}
	indices = document.content_token_indices
	for position, index in enumerate(indices):
		token = document.tokens[index]
		kind = token.type
		if kind == "heading_open":
			# The compiler also exposes the heading map for exporter consumers.
			if "heading" not in token.meta and index in headings:
				# Never mutate the compiled token model.
				token = copy.copy(token)
				token.meta = dict(token.meta, heading=headings[index])
			add_heading(output, token, document.tokens[indices[position + 1]], document, index)
		elif kind == "inline":
			if position and document.tokens[indices[position - 1]].type == "heading_open":
				continue
			if paragraph is None:
				raise ValueError("Inline tutorial content has no containing paragraph")
			action = token.meta.get("action", actions.get(index))
			tutorial_lib.docx_inline.render(paragraph, token.children or [], document, action)
			if cell is None:
				keep_label_with_entry(output, document, position, action)
		elif kind in ("bullet_list_open", "ordered_list_open"):
			# Keep a parent label with its first child, without locking the whole list.
			if lists and items and position:
				previous = document.tokens[indices[position - 1]]
				if previous.type == "paragraph_close":
					output.paragraphs[-1].paragraph_format.keep_with_next = True
			start = int(token.attrGet("start") or 1)
			number = tutorial_lib.docx_numbering.create_list(
				output, kind == "ordered_list_open", start, len(lists),
			)
			lists.append(number)
		elif kind in ("bullet_list_close", "ordered_list_close"):
			lists.pop()
		elif kind == "list_item_open":
			items.append(False)
			action = token.meta.get("action", actions.get(index))
		elif kind == "list_item_close":
			items.pop()
			action = None
		elif kind == "paragraph_open":
			action = token.meta.get("action", actions.get(index, action))
			style = "Tutorial Instruction" if items else "Tutorial Body"
			if quote_depth:
				style = "Tutorial Quote"
			paragraph = cell.paragraphs[0] if cell is not None else output.add_paragraph(style=style)
			if items and cell is None:
				if not items[-1]:
					tutorial_lib.docx_numbering.apply_list(paragraph, lists[-1])
					items[-1] = True
				else:
					paragraph.paragraph_format.left_indent = docx.shared.Inches(
						tutorial_lib.docx_styles.LIST_INDENT_INCHES * len(lists),
					)
		elif kind == "paragraph_close":
			paragraph = None
		elif kind in ("fence", "code_block"):
			if output.paragraphs:
				output.paragraphs[-1].paragraph_format.keep_with_next = True
			paragraph = output.add_paragraph(style="Tutorial Formula")
			# Markdown fences carry a parser-added final newline, outside the formula.
			paragraph.add_run(token.content.removesuffix("\n"))
			paragraph = None
		elif kind == "blockquote_open":
			quote_depth += 1
		elif kind == "blockquote_close":
			quote_depth -= 1
		elif kind == "table_open":
			# Count the header's cells, without inferring spreadsheet semantics.
			columns = 0
			for following in indices[position + 1:]:
				if document.tokens[following].type == "tr_close":
					break
				if document.tokens[following].type in ("th_open", "td_open"):
					columns += 1
			table = output.add_table(rows=0, cols=columns)
			table.style = "Table Grid"
		elif kind == "tr_open":
			row = table.add_row()
			properties = row._tr.get_or_add_trPr()
			# A row that exceeds a page can still flow; ordinary rows stay intact.
			properties.append(docx.oxml.OxmlElement("w:cantSplit"))
			if len(table.rows) == 1:
				properties.append(docx.oxml.OxmlElement("w:tblHeader"))
			column = 0
		elif kind in ("th_open", "td_open"):
			cell = row.cells[column]
			paragraph = cell.paragraphs[0]
			if kind == "th_open":
				tutorial_lib.docx_styles.shade(
					cell._tc.get_or_add_tcPr(), tutorial_lib.docx_styles.TABLE_HEADER_FILL,
				)
		elif kind in ("th_close", "td_close"):
			cell = None
			paragraph = None
			column += 1
		elif kind == "table_close":
			table = None
		elif kind not in ("heading_close", "tr_close", "thead_open", "thead_close",
			"tbody_open", "tbody_close"):
			raise ValueError(f"Unsupported DOCX block token: {kind}")


#============================================
def write_document(document: tutorial_lib.model.Document, output_path: str | pathlib.Path) -> None:
	"""Write a compiled tutorial as editable DOCX without altering the model."""
	if document.has_errors:
		raise ValueError("Cannot render a tutorial with semantic errors")
	output = docx.Document()
	tutorial_lib.docx_styles.configure(output)
	output.core_properties.title = document.title
	output.core_properties.subject = "Spreadsheet tutorial"
	render_tokens(output, document)
	output.save(output_path)
