import os
import re
from PIL import Image

md_file = 'statistics_ch4_vi.md'
with open(md_file, 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
pattern = re.compile(r'!\[.*?\]\((images/stat_ch4\.pdf-.*?\.png)\)')

removed_count = 0
for line in lines:
    match = pattern.search(line)
    if match:
        img_path = match.group(1)
        if os.path.exists(img_path):
            try:
                img = Image.open(img_path)
                w, h = img.size
                if w <= 20 or h <= 20:
                    removed_count += 1
                    continue # Skip this line
            except Exception as e:
                pass
    new_lines.append(line)

with open(md_file, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print(f"Removed {removed_count} line-image markdown tags.")
