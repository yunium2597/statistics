import os

output_file = "chapter_2_vi.md"

with open(output_file, "w", encoding="utf-8") as outfile:
    for i in range(1, 6):
        chunk_file = f"chunk_{i}_vi.md"
        if os.path.exists(chunk_file):
            with open(chunk_file, "r", encoding="utf-8") as infile:
                outfile.write(infile.read())
                outfile.write("\n\n")

print(f"Combined successfully into {output_file}")
