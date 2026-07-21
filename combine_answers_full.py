import os
import glob

output_file = "statistics_answers_full_vi.md"

with open(output_file, "w", encoding="utf-8") as outfile:
    for i in range(1, 16):
        chunk_file = f"stat_ans_chunk_{i}_vi.md"
        if os.path.exists(chunk_file):
            with open(chunk_file, "r", encoding="utf-8") as infile:
                outfile.write(infile.read())
                outfile.write("\n\n")

# Cleanup extracted text files and chunk files
for f in glob.glob("stat_ans_chunk_*.md"):
    os.remove(f)
if os.path.exists("stat_answers_full.pdf"):
    os.remove("stat_answers_full.pdf")
if os.path.exists("stat_answers_full.md"):
    os.remove("stat_answers_full.md")

print(f"Combined successfully into {output_file} and cleaned up.")
