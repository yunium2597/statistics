import pymupdf4llm
import pathlib
import os

if not os.path.exists("images"):
    os.makedirs("images")

md_text = pymupdf4llm.to_markdown("chapter_1.pdf", write_images=True, image_path="images", image_format="png", dpi=300)
pathlib.Path("chapter_1.md").write_text(md_text, encoding="utf-8")
print("Done extracting to chapter_1.md")
