import os
import glob
import re

output_file = "statistics_ch5_vi.md"

with open(output_file, "w", encoding="utf-8") as outfile:
    for i in range(1, 5):
        chunk_file = f"stat_chunk5_{i}_vi.md"
        if os.path.exists(chunk_file):
            with open(chunk_file, "r", encoding="utf-8") as infile:
                outfile.write(infile.read())
                outfile.write("\n\n")

# Cleanup extracted text files and chunk files
for f in glob.glob("stat_chunk5_*.md"):
    os.remove(f)
if os.path.exists("stat_ch5.pdf"):
    os.remove("stat_ch5.pdf")
if os.path.exists("stat_ch5.md"):
    os.remove("stat_ch5.md")

# Remove page headers
pattern = re.compile(r'^\s*\d+\s+[A-ZÀÁẠẢÃÂẦẤẬẨẪĂẰẮẶẲẴÈÉẸẺẼÊỀẾỆỂỄÌÍỊỈĨÒÓỌỎÕÔỒỐỘỔỖƠỜỚỢỞỠÙÚỤỦŨƯỪỨỰỬỮỲÝỴỶỸĐ\s]+(\[.*?\])?\s*$|^\s*[A-ZÀÁẠẢÃÂẦẤẬẨẪĂẰẮẶẲẴÈÉẸẺẼÊỀẾỆỂỄÌÍỊỈĨÒÓỌỎÕÔỒỐỘỔỖƠỜỚỢỞỠÙÚỤỦŨƯỪỨỰỬỮỲÝỴỶỸĐ\s]+\s+\d+\s*$|^\s*\[CH.*?\]\s*$')

with open(output_file, 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    if not pattern.match(line):
        new_lines.append(line)

with open(output_file, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print(f"Combined successfully into {output_file} and cleaned up.")
