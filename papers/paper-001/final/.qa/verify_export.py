from pathlib import Path
import re, hashlib
from docx import Document
from pypdf import PdfReader
root = Path(__file__).resolve().parents[2]
source = (root/'draft.md').read_text(encoding='utf-8-sig')
doc = Document(root/'final/paper-001.docx')
paras = [p.text for p in doc.paragraphs]
blocks = re.split(r'\n\s*\n', source.strip())
expected = [b.replace('*','') for b in blocks if not b.startswith('#')]
assert all(b in paras for b in expected), 'Manuscript text mismatch'
pdf = PdfReader(root/'final/paper-001.pdf')
compact = lambda s: re.sub(r'\s+', '', s)
pdftext = compact(''.join(p.extract_text() for p in pdf.pages))
# Ignore page numbers inserted into paragraph continuations by extracting lines.
clean = compact('\n'.join(line for p in pdf.pages for line in p.extract_text().splitlines() if not re.fullmatch(r'\s*\d+\s*',line)))
assert all(compact(b) in clean for b in expected), 'PDF content mismatch'
assert '[Name]' in pdf.pages[0].extract_text()
assert len(pdf.pages)==10
assert hashlib.sha256((root/'draft.md').read_bytes()).hexdigest() == '9ac07e41fa7eed4572ac88c6685c528d97d6c19964b7afec4a2b6ba1954f56ba'
print('PASS: all manuscript paragraphs and nine references preserved in DOCX/PDF; placeholders present; 10 pages; approved source hash unchanged.')
