"""Retain source payloads on ordinary Markdown links used as machine bindings."""

import re
import urllib.parse
import markdown_it.rules_inline.link


KINDS = frozenset(("label", "enter", "replace", "fill", "select"))


def scalar_payload(raw: str, parser: object, kind: str) -> str:
	"""Decode label Markdown while preserving Enter/Replace scalar syntax."""
	text = raw.strip()
	# Remove only emphasis that encloses the entire payload. Its contents may be
	# JSON or a formula, whose own escapes and operators must remain source bytes.
	while True:
		children = parser.parseInline(text)[0].children
		children = [child for child in children if child.type != "text" or child.content]
		if len(children) < 2 or children[0].type not in ("strong_open", "em_open"):
			break
		opening = children[0]
		if (children[-1].type != opening.type.replace("_open", "_close")
			or any(child.level <= opening.level for child in children[1:-1])):
			break
		width = len(opening.markup)
		text = text[width:-width].strip()
	# Quotes in labels are prose, not JSON delimiters. Decode their Markdown
	# normally; code spans and formula tokens still retain their literal bytes.
	if text.startswith("=") or kind != "label" and text.startswith('"'):
		return text
	pieces = []
	for child in children:
		if child.type in ("strong_open", "strong_close", "em_open", "em_close"):
			continue
		if child.type == "html_inline":
			if re.fullmatch(r"<br\s*/?>", child.content, re.IGNORECASE) is None:
				raise ValueError("Only br markup is allowed in workbook scalars")
			pieces.append("\n")
		elif child.type in ("text", "code_inline", "softbreak"):
			pieces.append(child.content)
		else:
			raise ValueError("Only text, emphasis, or code is allowed in binding scalars")
	value = "".join(pieces).strip()
	return value


def binding_kind(href: str) -> str | None:
	decoded = urllib.parse.unquote(href)
	match = re.match(r"([A-Za-z]+):", decoded)
	kind = match[1].lower() if match is not None else None
	return kind if kind in KINDS else None


def inline_binding(state: object, silent: bool) -> bool:
	"""Delegate Markdown geometry while retaining JSON escapes and formula operators."""
	if state.src[state.pos] != "[":
		return False
	start = state.pos
	end = state.md.helpers.parseLinkLabel(state, start, True)
	if end < 0:
		return False
	before = len(state.tokens)
	matched = markdown_it.rules_inline.link(state, silent)
	if not matched or silent:
		return matched
	for token in state.tokens[before:]:
		if token.type == "link_open" and binding_kind(token.attrGet("href")) is not None:
			token.meta["binding_payload"] = state.src[start + 1:end]
			break
	return True
