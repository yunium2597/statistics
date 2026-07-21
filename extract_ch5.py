import fitz
import pymupdf4llm
import pathlib
import os
import re
from PIL import Image
import glob

pdf_path = "statistics-fourth-edition.pdf"
doc = fitz.open(pdf_path)

# Chapter 5 is from index 95 to 113
doc_ch = fitz.Document()
doc_ch.insert_pdf(doc, from_page=95, to_page=113)
doc_ch.save("stat_ch5.pdf")
doc_ch.close()

if not os.path.exists("images"):
    os.makedirs("images")

print("Extracting markdown with images...")
md_text = pymupdf4llm.to_markdown("stat_ch5.pdf", write_images=True, image_path="images", image_format="png", dpi=300)

print("Preprocessing markdown...")
# Remove picture text blocks
pattern_picture_text = r"<!--\s*Start of picture text\s*-->.*?<!--\s*End of picture text\s*-->\n*"
md_text = re.sub(pattern_picture_text, "", md_text, flags=re.DOTALL)

# Remove backticks around LaTeX math
pattern_math = r"`(\${1,2}[^`]+?\${1,2})`"
md_text = re.sub(pattern_math, r"\1", md_text)

# Remove garbage images (<20px)
lines = md_text.splitlines()
new_lines = []
pattern_img = re.compile(r'!\[.*?\]\((images/stat_ch5\.pdf-.*?\.png)\)')

for line in lines:
    match = pattern_img.search(line)
    if match:
        img_path = match.group(1)
        if os.path.exists(img_path):
            try:
                img = Image.open(img_path)
                w, h = img.size
                if w <= 20 or h <= 20:
                    continue # Skip this line
            except Exception as e:
                pass
    new_lines.append(line)

md_text = "\n".join(new_lines) + "\n"

pathlib.Path("stat_ch5.md").write_text(md_text, encoding="utf-8")
print(f"Extracted Chapter 5. Length: {len(md_text.splitlines())} lines.")

print("Splitting into 4 chunks...")
lines = md_text.splitlines(keepends=True)
num_chunks = 4
target_lines_per_chunk = len(lines) // num_chunks

chunks = []
current_chunk = []
for i, line in enumerate(lines):
    current_chunk.append(line)
    
    if len(current_chunk) >= target_lines_per_chunk and len(chunks) < num_chunks - 1:
        # split at empty line or heading, or question number
        if i + 1 < len(lines) and (lines[i+1].startswith("#") or lines[i+1].strip() == "" or re.match(r"^\d+\.", lines[i+1])):
            chunks.append(current_chunk)
            current_chunk = []
            
if current_chunk:
    chunks.append(current_chunk)

for idx, chunk in enumerate(chunks, 1):
    with open(f"stat_chunk5_{idx}.md", "w", encoding="utf-8") as f:
        f.writelines(chunk)
    print(f"stat_chunk5_{idx}.md created with {len(chunk)} lines")

