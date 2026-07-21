import fitz
import pymupdf4llm
import pathlib
import os
import re

pdf_path = "statistics-fourth-edition.pdf"
doc = fitz.open(pdf_path)

# Chapter 2 is from page index 29 (page 30) to 47 (page 48)
doc_ch2 = fitz.Document()
doc_ch2.insert_pdf(doc, from_page=29, to_page=47)
doc_ch2.save("stat_ch2.pdf")
doc_ch2.close()

if not os.path.exists("images"):
    os.makedirs("images")

print("Extracting markdown with images...")
md_text = pymupdf4llm.to_markdown("stat_ch2.pdf", write_images=True, image_path="images", image_format="png", dpi=300)

print("Preprocessing markdown...")
# Remove picture text blocks
pattern_picture_text = r"<!--\s*Start of picture text\s*-->.*?<!--\s*End of picture text\s*-->\n*"
md_text = re.sub(pattern_picture_text, "", md_text, flags=re.DOTALL)

# Remove backticks around LaTeX math
pattern_math = r"`(\${1,2}[^`]+?\${1,2})`"
md_text = re.sub(pattern_math, r"\1", md_text)

pathlib.Path("stat_ch2.md").write_text(md_text, encoding="utf-8")
print(f"Extracted Chapter 2 to stat_ch2.md. Length: {len(md_text.splitlines())} lines.")

print("Splitting into chunks...")
lines = md_text.splitlines(keepends=True)
num_chunks = 5
target_lines_per_chunk = len(lines) // num_chunks

chunks = []
current_chunk = []
for i, line in enumerate(lines):
    current_chunk.append(line)
    
    if len(current_chunk) >= target_lines_per_chunk and len(chunks) < num_chunks - 1:
        # split at empty line or heading
        if i + 1 < len(lines) and (lines[i+1].startswith("#") or lines[i+1].strip() == ""):
            chunks.append(current_chunk)
            current_chunk = []
            
if current_chunk:
    chunks.append(current_chunk)

for idx, chunk in enumerate(chunks, 1):
    with open(f"stat_chunk2_{idx}.md", "w", encoding="utf-8") as f:
        f.writelines(chunk)
    print(f"stat_chunk2_{idx}.md created with {len(chunk)} lines")

