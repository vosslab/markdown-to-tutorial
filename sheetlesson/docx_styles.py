"""Central style definitions for native, editable tutorial documents."""

import docx.enum.style
import docx.oxml
import docx.oxml.ns
import docx.shared


BODY_FONT = "Calibri"
CODE_FONT = "Consolas"
BODY_SIZE = 11
CODE_SIZE = 9
PAGE_MARGIN = 0.8
IMAGE_WIDTH = 6.8
LIST_INDENT_TWIPS = 360
LIST_HANGING_TWIPS = 240
LIST_INDENT_INCHES = 0.25
TABLE_HEADER_FILL = "E7E6E6"


#============================================
def shade(element: object, color: str) -> None:
	"""Apply an OOXML background without replacing the native content."""
	fill = docx.oxml.OxmlElement("w:shd")
	fill.set(docx.oxml.ns.qn("w:fill"), color)
	element.append(fill)


#============================================
def configure(document: object) -> None:
	"""Install all tutorial paragraph and character styles in one place."""
	for section in document.sections:
		section.top_margin = docx.shared.Inches(PAGE_MARGIN)
		section.bottom_margin = docx.shared.Inches(PAGE_MARGIN)
		section.left_margin = docx.shared.Inches(PAGE_MARGIN)
		section.right_margin = docx.shared.Inches(PAGE_MARGIN)
	styles = document.styles
	normal = styles["Normal"]
	normal.font.name = BODY_FONT
	normal.font.size = docx.shared.Pt(BODY_SIZE)
	normal.paragraph_format.space_after = docx.shared.Pt(6)
	normal.paragraph_format.line_spacing = 1.08
	paragraphs = {
		"Tutorial Title": "Title", "Tutorial Part": "Heading 1",
		"Tutorial Step": "Heading 2", "Tutorial Substep": "Heading 3",
		"Tutorial Body": "Normal", "Tutorial Instruction": "Normal",
		"Tutorial Formula": "Normal", "Tutorial Quote": "Normal",
	}
	for name, base in paragraphs.items():
		style = styles.add_style(name, docx.enum.style.WD_STYLE_TYPE.PARAGRAPH)
		style.base_style = styles[base]
		if base.startswith("Heading"):
			style.paragraph_format.keep_with_next = True
			style.paragraph_format.space_before = docx.shared.Pt(14)
			style.paragraph_format.space_after = docx.shared.Pt(6)
			style.font.color.rgb = docx.shared.RGBColor.from_string("203864")
	formula = styles["Tutorial Formula"]
	formula.font.name = CODE_FONT
	formula.font.size = docx.shared.Pt(CODE_SIZE)
	formula.paragraph_format.left_indent = docx.shared.Inches(0.12)
	formula.paragraph_format.right_indent = docx.shared.Inches(0.12)
	formula.paragraph_format.space_before = docx.shared.Pt(5)
	formula.paragraph_format.space_after = docx.shared.Pt(8)
	shade(formula.element.get_or_add_pPr(), "F2F2F2")
	# Word paragraph borders provide visible padding and a non-color cue.
	borders = docx.oxml.OxmlElement("w:pBdr")
	for edge in ("top", "left", "bottom", "right"):
		border = docx.oxml.OxmlElement(f"w:{edge}")
		for key, value in {"val": "single", "sz": "4", "space": "5", "color": "B7B7B7"}.items():
			border.set(docx.oxml.ns.qn(f"w:{key}"), value)
		borders.append(border)
	formula.element.get_or_add_pPr().append(borders)
	styles["Tutorial Quote"].paragraph_format.left_indent = docx.shared.Inches(0.25)
	for name in ("Tutorial Cell Reference", "Tutorial Menu", "Tutorial Code", "Tutorial Link"):
		style = styles.add_style(name, docx.enum.style.WD_STYLE_TYPE.CHARACTER)
		if name != "Tutorial Link":
			style.font.name = CODE_FONT
			style.font.size = docx.shared.Pt(CODE_SIZE)
		if name in ("Tutorial Cell Reference", "Tutorial Menu"):
			style.font.bold = True
		if name == "Tutorial Link":
			style.font.underline = True
			style.font.color.rgb = docx.shared.RGBColor.from_string("174F91")
