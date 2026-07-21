import fitz
import os

pdf_path = "chapter_1.pdf"
doc = fitz.open(pdf_path)

if not os.path.exists("images"):
    os.makedirs("images")

pages_to_extract = [1, 2, 3, 4]

for pno in pages_to_extract:
    page = doc[pno]
    draw_rect = fitz.Rect()
    
    # 1. Bounding box of all drawings
    paths = page.get_drawings()
    for p in paths:
        draw_rect |= p["rect"]
        
    # 2. Bounding box of all images (sometimes points in scatter plot are images)
    for img in page.get_images():
        img_rect = page.get_image_bbox(img[0])
        draw_rect |= img_rect
        
    # 3. Expand the rect by a margin to catch axis labels (e.g. 40 points)
    expanded_rect = draw_rect + (-40, -40, 40, 40)
    
    final_rect = fitz.Rect(draw_rect)
    
    # 4. Filter text blocks to see if they overlap this expanded rect.
    blocks = page.get_text("blocks")
    for b in blocks:
        b_rect = fitz.Rect(b[:4])
        text = b[4].strip()
        
        # If the text block intersects our expanded drawing rect
        if b_rect.intersects(expanded_rect):
            # Exclude caption
            if text.startswith("FIGURE") or text.startswith("Left:") or text.startswith("Center:") or text.startswith("Right:"):
                continue
            # Exclude page header (usually at the very top, e.g. y < 70)
            if b_rect.y0 < 70:
                continue
                
            final_rect |= b_rect
            
    # Add a small padding around the final figure
    final_rect = final_rect + (-5, -5, 5, 5)
    
    # Now set the cropbox
    final_rect.intersect(page.rect)
    page.set_cropbox(final_rect)
    
    svg = page.get_svg_image()
    
    out_name = f"images/chapter_1.pdf-{pno+1:04d}-01.svg"
    with open(out_name, "w", encoding="utf-8") as f:
        f.write(svg)
        
print("SVG crop done")
