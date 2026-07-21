import os

md_file = 'statistics_ch3_vi.md'
with open(md_file, 'r', encoding='utf-8') as f:
    text = f.read()

target = """   - (a) Tỷ lệ phần trăm những người hút 10 điếu thuốc trở xuống mỗi ngày là khoảng 

            - 1 _._ 5% 15% 30% 50% 

   - (b) Tỷ lệ phần trăm những người hút hơn một bao một ngày, nhưng không quá 2 bao, là khoảng 

            - 1 _._ 5% 15% 30% 50% 1 _._ 5% 15% 30% 50% 

      - (Có 20 điếu thuốc trong một bao.) 

   - (c) Tỷ lệ phần trăm những người hút hơn một bao một ngày là khoảng 

   - (d) Tỷ lệ phần trăm những người hút hơn 3 bao một ngày là khoảng 

         - 0 _._ 25 của 1% 0 _._ 5 của 1% 10% 

         - Tỷ lệ phần trăm những người hút 15 điếu thuốc mỗi ngày là khoảng 0 _._ 35 của 1% 0 _._ 5 của 1% 1 _._ 5% 3 _._ 5% 10% 

   - (e) Tỷ lệ phần trăm những người hút 15 điếu thuốc mỗi ngày là khoảng """

replacement = """   - (a) Tỷ lệ phần trăm những người hút 10 điếu thuốc trở xuống mỗi ngày là khoảng 
<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1,5% &nbsp;&nbsp;&nbsp;&nbsp; 15% &nbsp;&nbsp;&nbsp;&nbsp; 30% &nbsp;&nbsp;&nbsp;&nbsp; 50%

   - (b) Tỷ lệ phần trăm những người hút hơn một bao một ngày, nhưng không quá 2 bao, là khoảng 
<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1,5% &nbsp;&nbsp;&nbsp;&nbsp; 15% &nbsp;&nbsp;&nbsp;&nbsp; 30% &nbsp;&nbsp;&nbsp;&nbsp; 50%

     (Có 20 điếu thuốc trong một bao.)

   - (c) Tỷ lệ phần trăm những người hút hơn một bao một ngày là khoảng 
<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1,5% &nbsp;&nbsp;&nbsp;&nbsp; 15% &nbsp;&nbsp;&nbsp;&nbsp; 30% &nbsp;&nbsp;&nbsp;&nbsp; 50%

   - (d) Tỷ lệ phần trăm những người hút hơn 3 bao một ngày là khoảng 
<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0,25 của 1% &nbsp;&nbsp;&nbsp;&nbsp; 0,5 của 1% &nbsp;&nbsp;&nbsp;&nbsp; 10%

   - (e) Tỷ lệ phần trăm những người hút 15 điếu thuốc mỗi ngày là khoảng 
<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0,35 của 1% &nbsp;&nbsp;&nbsp;&nbsp; 0,5 của 1% &nbsp;&nbsp;&nbsp;&nbsp; 1,5% &nbsp;&nbsp;&nbsp;&nbsp; 3,5% &nbsp;&nbsp;&nbsp;&nbsp; 10%"""

text = text.replace(target, replacement)

with open(md_file, 'w', encoding='utf-8') as f:
    f.write(text)

print("Replaced successfully.")
