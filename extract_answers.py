import fitz
import pymupdf4llm
import pathlib
import os
import re

pdf_path = "statistics-fourth-edition.pdf"
doc = fitz.open(pdf_path)

# Chapter 2 answers are on pages 636, 637, 638 (indices)
# We can just extract pages 636 to 638
doc_ans = fitz.Document()
doc_ans.insert_pdf(doc, from_page=636, to_page=638)
doc_ans.save("stat_answers_ch2.pdf")
doc_ans.close()

if not os.path.exists("images"):
    os.makedirs("images")

print("Extracting markdown...")
md_text = pymupdf4llm.to_markdown("stat_answers_ch2.pdf", write_images=True, image_path="images", image_format="png", dpi=300)

print("Preprocessing markdown...")
# Remove picture text blocks
pattern_picture_text = r"<!--\s*Start of picture text\s*-->.*?<!--\s*End of picture text\s*-->\n*"
md_text = re.sub(pattern_picture_text, "", md_text, flags=re.DOTALL)

# Remove backticks around LaTeX math
pattern_math = r"`(\${1,2}[^`]+?\${1,2})`"
md_text = re.sub(pattern_math, r"\1", md_text)

# We want to stop right before "Chapter 3."
if "Chapter 3." in md_text:
    md_text = md_text[:md_text.find("Chapter 3.")]

pathlib.Path("stat_answers_ch2.md").write_text(md_text, encoding="utf-8")
print(f"Extracted Chapter 2 answers. Length: {len(md_text.splitlines())} lines.")
