import fitz
import pymupdf4llm
import pathlib
import os

pdf_path = "ISLRv2_corrected_June_2023.pdf"
doc = fitz.open(pdf_path)

# Chapter 2 starts at page index 25 (page 26 in PDF viewer usually) and ends at 68 (page 69)
# Let's extract pages 25 to 68
doc_ch2 = fitz.Document()
doc_ch2.insert_pdf(doc, from_page=25, to_page=68)
doc_ch2.save("chapter_2.pdf")
doc_ch2.close()

if not os.path.exists("images"):
    os.makedirs("images")

md_text = pymupdf4llm.to_markdown("chapter_2.pdf", write_images=True, image_path="images", image_format="png", dpi=300)
pathlib.Path("chapter_2.md").write_text(md_text, encoding="utf-8")
print(f"Extracted Chapter 2 to chapter_2.md. Length: {len(md_text.splitlines())} lines.")
