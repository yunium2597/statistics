import re

file_path = "chapter_2_vi.md"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Remove picture text blocks
# Pattern to match <!-- Start of picture text --> ... <!-- End of picture text -->
pattern_picture_text = r"<!--\s*Start of picture text\s*-->.*?<!--\s*End of picture text\s*-->\n*"
content = re.sub(pattern_picture_text, "", content, flags=re.DOTALL)

# 2. Remove backticks around LaTeX math
# Match `$...$` or `$$...$$`
pattern_math = r"`(\${1,2}[^`]+?\${1,2})`"
content = re.sub(pattern_math, r"\1", content)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Fixes applied successfully.")
