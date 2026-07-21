import os

with open("chapter_2.md", "r", encoding="utf-8") as f:
    lines = f.readlines()

num_chunks = 5
target_lines_per_chunk = len(lines) // num_chunks

chunks = []
current_chunk = []
for i, line in enumerate(lines):
    current_chunk.append(line)
    
    # If we are past the target line count, try to split at a blank line before a heading
    if len(current_chunk) >= target_lines_per_chunk and len(chunks) < num_chunks - 1:
        # Check if the next line is a heading
        if i + 1 < len(lines) and lines[i+1].startswith("#"):
            chunks.append(current_chunk)
            current_chunk = []
            
# Append any remaining lines
if current_chunk:
    chunks.append(current_chunk)

for idx, chunk in enumerate(chunks, 1):
    with open(f"chunk_{idx}.md", "w", encoding="utf-8") as f:
        f.writelines(chunk)
    print(f"chunk_{idx}.md created with {len(chunk)} lines")

