"""Recognize formula copy text before Markdown consumes its operators."""

import re
import markdown_it.token


ACTION = re.compile(r"\s*(?:\*\*|__)(Label|Enter|Replace)\s+.+?:(?:\*\*|__)\s*")
ATOM = re.compile(
	r'''(?:(?:'(?:[^']|'')+'|[A-Za-z_][\w.]*)!)?'''
	r'''(?:\$?[A-Za-z_][\w$]*(?:\.[\w$]+)*(?::\$?[A-Za-z_][\w$]*)?'''
	r'''|[0-9]+(?:\.[0-9]+)?(?:[Ee][+-]?[0-9]+)?|\.[0-9]+)'''
	r'''|"(?:[^"]|"")*"'''
)


#============================================
def formula_end(source: str, start: int, maximum: int) -> int:
	"""Find a bounded narrative expression, leaving prose and Markdown outside it.

	This is a copy-text boundary scanner, not spreadsheet syntax validation.
	Explicit code spans and action payloads support ambiguous/extended syntax.
	"""
	position = start + 1
	end = start
	depth = 0
	operand = True
	while position < maximum:
		character = source[position]
		if character in " \t":
			position += 1
			continue
		if operand:
			if character in "+-":
				position += 1
				continue
			if character == "(":
				depth += 1
				position += 1
				continue
			match = ATOM.match(source, position, maximum)
			if match is None:
				# Empty function argument lists are ordinary spreadsheet syntax.
				if character == ")" and depth:
					depth -= 1
					operand = False
					position += 1
					if not depth:
						end = position
					continue
				break
			position = match.end()
			if position < maximum and source[position] == "(":
				depth += 1
				position += 1
				continue
			operand = False
		else:
			if character == ")" and depth:
				depth -= 1
				position += 1
			elif character == "%":
				position += 1
			elif character in "+-*/^&=<>" or character in ",;" and depth:
				operand = True
				position += 1
				if character in "<>" and source[position:position + 1] in ("=", ">"):
					position += 1
			else:
				break
		if not operand and not depth:
			end = position
	# Do not split an unrecognized adjacent identifier or URL into a formula prefix.
	if (end > start and end < maximum and source[end] not in " \t\n.,;:!?)]}'\"*_["
		and not source.startswith("\\\n", end)):
		return start
	return end


#============================================
def inline_formula(state: object, silent: bool) -> bool:
	"""Emit formula-role code tokens before emphasis, HTML and escape handling."""
	start = state.pos
	if state.src[start] != "=":
		return False
	opening = ACTION.match(state.src)
	if opening is not None and start >= opening.end():
		payload = state.src[opening.end():state.posMax]
		if opening[1] == "Label" or payload.startswith('"'):
			return False
		if opening.end() == start:
			end = state.posMax
		else:
			end = formula_end(state.src, start, state.posMax)
	else:
		# Spaces after '=' usually denote prose equations, rather than copy text.
		if (start and state.src[start - 1] not in " \t\n('\"[*_"
			or start + 1 >= state.posMax or state.src[start + 1].isspace()):
			return False
		end = formula_end(state.src, start, state.posMax)
	if end <= start + 1:
		return False
	if not silent:
		token = state.push("code_inline", "code", 0)
		token.content = state.src[start:end]
		token.meta["role"] = "formula"
	state.pos = end
	return True


#============================================
def annotate_formulas(state: object) -> None:
	"""Give explicit code spans and formula fences the same source-level role."""
	for token in state.tokens:
		if token.type in ("fence", "code_block"):
			if token.content.startswith("="):
				token.meta["role"] = "formula"
		if token.type == "inline":
			opening = ACTION.match(token.content)
			literal = opening is not None and (opening[1] == "Label"
				or token.content[opening.end():].startswith('"'))
			if literal:
				_preserve_literal_payload(token, opening)
			for child in token.children or []:
				if child.type == "code_inline" and child.content.startswith("=") and not literal:
					child.meta["role"] = "formula"


#============================================
def _preserve_literal_payload(token: object, opening: object) -> None:
	"""Keep raw scalar syntax out of Markdown while preserving authored code spans."""
	payload = token.content[opening.end():]
	# These scalar forms retain their raw characters during semantic compilation too.
	# Other plain labels retain their existing Markdown escaping/validation rules.
	if not payload.startswith("=" if opening[1] == "Label" else '"'):
		return
	for index, child in enumerate(token.children or []):
		if child.type == "strong_close":
			separator = opening[0][len(opening[0].rstrip()):]
			text = markdown_it.token.Token("text", "", 0)
			text.content = separator + payload
			token.children = token.children[:index + 1] + [text]
			return
