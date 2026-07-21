import os
import glob

output_file = "statistics_intro_vi.md"

with open(output_file, "w", encoding="utf-8") as outfile:
    for i in range(1, 5):
        chunk_file = f"stat_intro_{i}_vi.md"
        if os.path.exists(chunk_file):
            with open(chunk_file, "r", encoding="utf-8") as infile:
                outfile.write(infile.read())
                outfile.write("\n\n")

# Cleanup
for f in glob.glob("stat_intro_*.md"):
    os.remove(f)

print(f"Combined successfully into {output_file} and cleaned up.")
