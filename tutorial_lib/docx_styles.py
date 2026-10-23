"""Central style definitions for native, editable tutorial documents."""

import docx.enum.text
import docx.oxml
import docx.oxml.ns
import docx.shared


BODY_FONT = "PT Sans"
NARROW_FONT = "PT Sans Narrow"
CODE_FONT = "Roboto Mono"
BODY_SIZE = 11
CODE_SIZE = 9
PAGE_MARGIN = 0.8
IMAGE_WIDTH = 6.8
LIST_INDENT_TWIPS = 360
LIST_HANGING_TWIPS = 240
LIST_INDENT_INCHES = 0.25
TABLE_HEADER_FILL = "E7E6E6"
FORMULA_COLOR = "188038"


#============================================
def _set_explicit_font(style: object, font_name: str) -> None:
	"""Set a font family and remove theme selectors that override it in exports."""
	style.font.name = font_name
	r_fonts = style._element.get_or_add_rPr().get_or_add_rFonts()
	for theme_attribute in ("asciiTheme", "hAnsiTheme", "eastAsiaTheme", "cstheme"):
		r_fonts.attrib.pop(docx.oxml.ns.qn(f"w:{theme_attribute}"), None)
	for attribute in ("ascii", "hAnsi", "eastAsia", "cs"):
		r_fonts.set(docx.oxml.ns.qn(f"w:{attribute}"), font_name)


#============================================
def format_run(run: object, role: str | None = None, linked: bool = False,
	font_name: str | None = None) -> None:
	"""Apply portable role formatting directly, without custom character styles."""
	if role in ("code", "cell", "menu", "formula"):
		font_name = CODE_FONT
		run.font.size = docx.shared.Pt(CODE_SIZE)
	# Ordinary text inherits its editable paragraph style; only roles override fonts.
	if font_name is not None:
		_set_explicit_font(run, font_name)
	if role in ("cell", "menu"):
		run.bold = True
	if linked:
		run.font.underline = True
		run.font.color.rgb = docx.shared.RGBColor.from_string("174F91")
	if role == "formula":
		run.font.color.rgb = docx.shared.RGBColor.from_string(FORMULA_COLOR)


#============================================
def format_list(paragraph: object) -> None:
	"""Compact every paragraph within a list, including continuation paragraphs."""
	paragraph.paragraph_format.space_before = docx.shared.Pt(0)
	paragraph.paragraph_format.space_after = docx.shared.Pt(2)
	paragraph.paragraph_format.line_spacing = 1.0


#============================================
def shade(element: object, color: str) -> None:
	"""Apply an OOXML background without replacing the native content."""
	fill = docx.oxml.OxmlElement("w:shd")
	fill.set(docx.oxml.ns.qn("w:fill"), color)
	element.append(fill)


#============================================
def add_page_number(paragraph: object) -> None:
	"""Add a native Word PAGE field to a footer paragraph."""
	paragraph.style = "Normal"
	paragraph.alignment = docx.enum.text.WD_ALIGN_PARAGRAPH.RIGHT
	run = paragraph.add_run()
	field = docx.oxml.OxmlElement("w:fldSimple")
	field.set(docx.oxml.ns.qn("w:instr"), "PAGE")
	result = docx.oxml.OxmlElement("w:r")
	text = docx.oxml.OxmlElement("w:t")
	text.text = "1"
	result.append(text)
	field.append(result)
	run._r.addnext(field)


#============================================
def configure(document: object) -> None:
	"""Configure the six standard paragraph styles used by tutorial content."""
	for section in document.sections:
		section.top_margin = docx.shared.Inches(PAGE_MARGIN)
		section.bottom_margin = docx.shared.Inches(PAGE_MARGIN)
		section.left_margin = docx.shared.Inches(PAGE_MARGIN)
		section.right_margin = docx.shared.Inches(PAGE_MARGIN)
		add_page_number(section.footer.paragraphs[0])
	styles = document.styles
	normal = styles["Normal"]
	_set_explicit_font(normal, BODY_FONT)
	normal.font.size = docx.shared.Pt(BODY_SIZE)
	normal.paragraph_format.space_after = docx.shared.Pt(6)
	normal.paragraph_format.line_spacing = 1.08
	for name in ("Title", "Subtitle", "Heading 1", "Heading 2", "Heading 3"):
		style = styles[name]
		_set_explicit_font(style, BODY_FONT)
		if name.startswith("Heading"):
			level = int(name[-1])
			size = {1: 18, 2: 15, 3: 12}[level]
			style.font.size = docx.shared.Pt(size)
			style.font.bold = True
			style.paragraph_format.keep_with_next = True
			style.paragraph_format.space_before = docx.shared.Pt(14)
			style.paragraph_format.space_after = docx.shared.Pt(6)
			style.font.color.rgb = docx.shared.RGBColor.from_string("203864")


#============================================
def format_formula(paragraph: object) -> None:
	"""Keep editable formula blocks visually distinct using direct formatting."""
	paragraph.paragraph_format.left_indent = docx.shared.Inches(0.12)
	paragraph.paragraph_format.right_indent = docx.shared.Inches(0.12)
	paragraph.paragraph_format.space_before = docx.shared.Pt(5)
	paragraph.paragraph_format.space_after = docx.shared.Pt(8)
	properties = paragraph._p.get_or_add_pPr()
	shade(properties, "F2F2F2")
	# Word paragraph borders provide visible padding and a non-color cue.
	borders = docx.oxml.OxmlElement("w:pBdr")
	for edge in ("top", "left", "bottom", "right"):
		border = docx.oxml.OxmlElement(f"w:{edge}")
		for key, value in {"val": "single", "sz": "4", "space": "5", "color": "B7B7B7"}.items():
			border.set(docx.oxml.ns.qn(f"w:{key}"), value)
		borders.append(border)
	properties.append(borders)
