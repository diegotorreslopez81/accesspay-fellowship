#!/usr/bin/env python3
"""Convert markdown files to clean PDFs via Chrome headless."""
import subprocess
import sys
from pathlib import Path
import markdown

ROOT = Path(__file__).resolve().parent.parent
BUILD = ROOT / "build"
BUILD.mkdir(exist_ok=True)
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

CSS = """
@page { size: A4 portrait; margin: 22mm 20mm 22mm 20mm; }
:root {
  --ink: #1A1A1A;
  --ink-soft: #444;
  --red: #DA291C;
  --gray-200: #DDD;
  --gray-100: #F6F6F6;
}
* { box-sizing: border-box; }
body {
  font-family: -apple-system, 'Segoe UI', Helvetica, Arial, sans-serif;
  color: var(--ink);
  font-size: 10.5pt;
  line-height: 1.5;
  max-width: 170mm;
  margin: 0 auto;
}
h1, h2, h3, h4 {
  font-family: 'Fraunces', Georgia, serif;
  color: #0A0A0A;
  letter-spacing: -0.01em;
  page-break-after: avoid;
}
h1 { font-size: 22pt; font-weight: 800; margin: 0 0 8pt 0; border-bottom: 3px solid var(--red); padding-bottom: 6pt; }
h2 { font-size: 14pt; font-weight: 700; margin: 18pt 0 6pt 0; border-bottom: 1px solid var(--gray-200); padding-bottom: 3pt; }
h3 { font-size: 12pt; font-weight: 700; margin: 14pt 0 5pt 0; color: var(--red); }
h4 { font-size: 11pt; font-weight: 700; margin: 10pt 0 4pt 0; }
p { margin: 0 0 8pt 0; }
ul, ol { margin: 0 0 8pt 0; padding-left: 18pt; }
li { margin-bottom: 3pt; }
strong { color: #0A0A0A; }
code {
  background: var(--gray-100);
  padding: 1pt 4pt;
  border-radius: 2pt;
  font-size: 9.5pt;
  font-family: 'SF Mono', Menlo, monospace;
}
pre {
  background: var(--gray-100);
  padding: 8pt;
  border-radius: 3pt;
  border-left: 2pt solid var(--red);
  overflow-x: auto;
  page-break-inside: avoid;
  font-size: 9pt;
}
pre code { background: none; padding: 0; }
blockquote {
  border-left: 3pt solid var(--red);
  padding: 2pt 0 2pt 10pt;
  margin: 8pt 0;
  color: var(--ink-soft);
  font-style: italic;
}
table {
  width: 100%;
  border-collapse: collapse;
  margin: 8pt 0;
  page-break-inside: avoid;
  font-size: 9.5pt;
}
th, td {
  border: 1px solid var(--gray-200);
  padding: 5pt 7pt;
  text-align: left;
  vertical-align: top;
}
th {
  background: var(--gray-100);
  font-weight: 700;
}
a { color: var(--red); text-decoration: none; }
hr { border: 0; border-top: 1px solid var(--gray-200); margin: 14pt 0; }
.footer {
  margin-top: 18pt;
  padding-top: 6pt;
  border-top: 1px solid var(--gray-200);
  font-size: 8.5pt;
  color: var(--ink-soft);
  text-align: center;
}
"""

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>{title}</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Fraunces:wght@700;800&display=swap" rel="stylesheet">
<style>{css}</style>
</head>
<body>
{body}
<div class="footer">Diego Torres Lopez · Interledger Foundation 2026 Fellowship · AccessPay</div>
</body>
</html>
"""


def convert(md_path: Path, pdf_name: str, title: str) -> None:
    text = md_path.read_text()
    body = markdown.markdown(
        text,
        extensions=["tables", "fenced_code", "toc", "sane_lists"],
    )
    html = HTML_TEMPLATE.format(title=title, css=CSS, body=body)
    html_path = BUILD / f"{pdf_name}.html"
    pdf_path = BUILD / f"{pdf_name}.pdf"
    html_path.write_text(html)
    subprocess.run(
        [
            CHROME,
            "--headless",
            "--disable-gpu",
            "--no-sandbox",
            f"--print-to-pdf={pdf_path}",
            "--no-pdf-header-footer",
            "--virtual-time-budget=5000",
            f"file://{html_path}",
        ],
        check=True,
        capture_output=True,
    )
    print(f"OK  {pdf_name}.pdf ({pdf_path.stat().st_size // 1024}KB)")


TARGETS = [
    (ROOT / "docs" / "proposal.md", "01-proposal", "AccessPay Fellowship Proposal"),
    (ROOT / "cv" / "diego_torres_fellowship_cv.md", "02-cv-diego-torres", "Diego Torres · CV"),
    (ROOT / "references" / "letter_simon_lee.md", "03-letter-simon-lee-DRAFT", "Reference Letter · Simon Lee (DRAFT)"),
    (ROOT / "references" / "letter_alberto_zamora.md", "04-letter-alberto-zamora-DRAFT", "Reference Letter · Dr. Alberto Zamora (DRAFT)"),
    (ROOT / "docs" / "research-plan.md", "05-research-plan", "Research Plan"),
    (ROOT / "docs" / "technical-plan.md", "06-technical-plan", "Technical Plan"),
    (ROOT / "docs" / "advocacy-plan.md", "07-advocacy-plan", "Advocacy Plan"),
    (ROOT / "docs" / "roadmap.md", "08-roadmap", "Roadmap"),
    (ROOT / "docs" / "ai-use.md", "09-ai-use", "AI Use Disclosure"),
]

if __name__ == "__main__":
    for md, name, title in TARGETS:
        if md.exists():
            convert(md, name, title)
        else:
            print(f"SKIP (not found) {md}")
