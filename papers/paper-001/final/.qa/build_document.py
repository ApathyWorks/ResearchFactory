from pathlib import Path
import re
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

root = Path(__file__).resolve().parents[2]
text = (root / 'draft.md').read_text(encoding='utf-8-sig')
abstract = (root / 'final/abstract.md').read_text(encoding='utf-8-sig').strip()
blocks = re.split(r'\n\s*\n', text.strip())
title = blocks[0].removeprefix('# ')
doc = Document()
section = doc.sections[0]
section.page_width, section.page_height = Inches(8.5), Inches(11)
section.top_margin = section.bottom_margin = section.left_margin = section.right_margin = Inches(1)
section.header_distance = Inches(.5)
for name in ['Normal', 'Title', 'Heading 1']:
    style = doc.styles[name]
    for node in list(style.element):
        if node.tag == qn('w:rPr'):
            style.element.remove(node)
    ppr = style.element.find(qn('w:pPr'))
    if ppr is not None:
        for node in list(ppr):
            if node.tag in [qn('w:pBdr'), qn('w:shd')]:
                ppr.remove(node)
    style.font.name = 'Times New Roman'
    style.font.size = Pt(12)
    style.font.color.rgb = RGBColor(0,0,0)
    for attr in ['eastAsia', 'cs']:
        style.element.rPr.rFonts.set(qn('w:' + attr), 'Times New Roman')
    pf = style.paragraph_format
    pf.line_spacing = 2
    pf.space_before = pf.space_after = Pt(0)
    pf.widow_control = True
doc.styles['Normal'].paragraph_format.first_line_indent = Inches(.5)
for name in ['Title', 'Heading 1']:
    doc.styles[name].font.bold = True
    doc.styles[name].paragraph_format.first_line_indent = Inches(0)
    doc.styles[name].paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    doc.styles[name].paragraph_format.keep_with_next = True
header = section.header.paragraphs[0]
header.alignment = WD_ALIGN_PARAGRAPH.RIGHT
header.paragraph_format.first_line_indent = Inches(0)
field = OxmlElement('w:fldSimple')
field.set(qn('w:instr'), 'PAGE')
header._p.append(field)
for _ in range(3):
    p = doc.add_paragraph()
    p.paragraph_format.first_line_indent = Inches(0)
doc.add_paragraph(title, 'Title')
doc.add_paragraph()
for placeholder in ['[Name]', '[Institution]', '[Course]', '[Instructor]', '[Due date]']:
    p = doc.add_paragraph(placeholder)
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.first_line_indent = Inches(0)
doc.add_page_break()
doc.add_paragraph('Abstract', 'Heading 1')
p = doc.add_paragraph(abstract)
p.paragraph_format.first_line_indent = Inches(0)
doc.add_page_break()
doc.add_paragraph(title, 'Title')
references = False
for block in blocks[1:]:
    block = block.strip()
    if block == '## Introduction':
        continue
    if block.startswith('## '):
        heading = block[3:]
        if heading == 'References':
            doc.add_page_break()
            references = True
        doc.add_paragraph(heading, 'Heading 1')
        continue
    p = doc.add_paragraph()
    if references:
        p.paragraph_format.left_indent = Inches(.5)
        p.paragraph_format.first_line_indent = Inches(-.5)
    for i, part in enumerate(re.split(r'\*([^*]+)\*', block)):
        run = p.add_run(part)
        run.italic = bool(i % 2)
doc.core_properties.title = title
doc.core_properties.author = ''
doc.core_properties.subject = 'AI-generated academic research demonstration'
doc.core_properties.keywords = 'large language models, hallucination, verification'
out = root / 'final/paper-001.docx'
doc.save(out)
print(out)
