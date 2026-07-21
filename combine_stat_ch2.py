import os
import glob

output_file = "statistics_ch2_vi.md"

with open(output_file, "w", encoding="utf-8") as outfile:
    for i in range(1, 6):
        chunk_file = f"stat_chunk2_{i}_vi.md"
        if os.path.exists(chunk_file):
            with open(chunk_file, "r", encoding="utf-8") as infile:
                outfile.write(infile.read())
                outfile.write("\n\n")

# Cleanup
for f in glob.glob("stat_chunk2_*.md"):
    os.remove(f)

print(f"Combined successfully into {output_file} and cleaned up.")
