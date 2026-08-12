import os
import glob
import re

output_file = "statistics_ch11_vi.md"

with open(output_file, "w", encoding="utf-8") as outfile:
    for i in range(1, 5):
        chunk_file = f"stat_chunk11_{i}_vi.md"
        if os.path.exists(chunk_file):
            with open(chunk_file, "r", encoding="utf-8") as infile:
                outfile.write(infile.read())
                outfile.write("\n\n")

# Remove extra newlines that sometimes occur when joining
with open(output_file, 'r', encoding='utf-8') as f:
    text = f.read()

# Replace 3 or more consecutive newlines with 2 newlines
text = re.sub(r'\n{3,}', '\n\n', text)

with open(output_file, 'w', encoding='utf-8') as f:
    f.write(text)

# Cleanup extracted text files and chunk files
for f in glob.glob("stat_chunk11_*.md"):
    os.remove(f)

print(f"Combined successfully into {output_file} and cleaned up.")
