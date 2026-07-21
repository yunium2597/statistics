import re
import os

files = ['statistics_ch1_vi.md', 'statistics_ch2_vi.md']
pattern = re.compile(r'^\s*\d+\s+[A-ZÀÁẠẢÃÂẦẤẬẨẪĂẰẮẶẲẴÈÉẸẺẼÊỀẾỆỂỄÌÍỊỈĨÒÓỌỎÕÔỒỐỘỔỖƠỜỚỢỞỠÙÚỤỦŨƯỪỨỰỬỮỲÝỴỶỸĐ\s]+(\[.*?\])?\s*$|^\s*[A-ZÀÁẠẢÃÂẦẤẬẨẪĂẰẮẶẲẴÈÉẸẺẼÊỀẾỆỂỄÌÍỊỈĨÒÓỌỎÕÔỒỐỘỔỖƠỜỚỢỞỠÙÚỤỦŨƯỪỨỰỬỮỲÝỴỶỸĐ\s]+\s+\d+\s*$|^\s*\[CH.*?\]\s*$')

for filepath in files:
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        new_lines = []
        for line in lines:
            if not pattern.match(line):
                new_lines.append(line)
            else:
                print(f"Removed from {filepath}: {repr(line)}")
                
        with open(filepath, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)

print("Cleanup complete.")
