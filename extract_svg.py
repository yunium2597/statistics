import fitz
import os

pdf_path = "chapter_1.pdf"
doc = fitz.open(pdf_path)

if not os.path.exists("images"):
    os.makedirs("images")

# mapping based on what pymupdf4llm gave
# 0002-01 -> page 1
# 0003-01 -> page 2
# 0004-01 -> page 3
# 0005-01 -> page 4
# Since we just want the vector graphics, let's extract the whole page as SVG for those pages
# and we will use those SVGs.
# Actually, let's find the drawings and create a tight SVG around them.
def extract_svg_for_page(page_num, output_filename):
    page = doc[page_num]
    # get drawing bounding box
    paths = page.get_drawings()
    if paths:
        rect = fitz.Rect()
        for p in paths:
            rect |= p["rect"]
        # expand slightly
        rect = rect + (-5, -5, 5, 5)
        # get SVG of just this rect
        svg = page.get_svg_image()
        with open(output_filename, "w", encoding="utf-8") as f:
            f.write(svg)

extract_svg_for_page(1, "images/chapter_1.pdf-0002-01.svg")
extract_svg_for_page(2, "images/chapter_1.pdf-0003-01.svg")
extract_svg_for_page(3, "images/chapter_1.pdf-0004-01.svg")
extract_svg_for_page(4, "images/chapter_1.pdf-0005-01.svg")

print("Done extracting SVGs")
