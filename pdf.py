from pypdf import PdfReader, PdfWriter

def extract_pages(input_pdf, output_pdf, start_page, end_page):
    reader = PdfReader(input_pdf)
    writer = PdfWriter()
    
    # Chuyển đổi từ số trang thực tế sang index của Python (bắt đầu từ 0)
    # Ví dụ: start_page = 3 -> index = 2
    for page_num in range(start_page - 1, end_page):
        writer.add_page(reader.pages[page_num])
        
    # Ghi file mới ra ổ đĩa
    with open(output_pdf, "wb") as output_file:
        writer.write(output_file)
    print(f"Đã cắt xong đoạn từ trang {start_page} đến {end_page}!")

# Sử dụng: Lấy từ trang 3 đến trang 10 của file 'giao_trinh.pdf'
extract_pages("ISLRv2_corrected_June_2023.pdf", "chapter_13.pdf",562,604)