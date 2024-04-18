import fitz 
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
import random
import time 

def generate_rrn():
    milliseconds = int(round(time.time() * 1000))
    rrn = str(milliseconds)[-12:]
    if len(rrn) < 12:
        rrn = str(random.randint(100000000000, 999999999999))[-(12 - len(rrn)):] + rrn
    return rrn

def generate_random_string(original_string):
    parts = original_string.split('-')
    prefix = original_string[:4]
    random_part = '-'.join([str(random.randint(100, 999)) for _ in range(3)])
    result = prefix + '-' + random_part
    return result

def create_pdf_with_custom_font(text, font_path, output_path, font_name="CustomFont", font_size=15, right_edge_x=500, text_y=750, page_size=(595.28, 841.89), text_color=(0, 0, 0)):

    pdfmetrics.registerFont(TTFont(font_name, font_path))
    

    c = canvas.Canvas(output_path, pagesize=page_size)
    c.setFont(font_name, font_size)  
    c.setFillColor(text_color)
    c.drawRightString(right_edge_x, text_y, text)
    c.save()

def merge_pdfs(base_pdf_path, overlay_pdf_path, output_path):

    base_pdf = fitz.open(base_pdf_path)
    overlay_pdf = fitz.open(overlay_pdf_path)
    
    for page_num in range(len(base_pdf)):
        page = base_pdf[page_num]
   
        page.show_pdf_page(page.rect, overlay_pdf, 0)
    
    base_pdf.save(output_path)


def replace_text_custom(pdf_path, output_path, replacements, font_path, new_size, new_color, output_path_2, output_path_3):

    doc = fitz.open(pdf_path)  
    page = doc[0]
    for text_to_replace, new_text, method in replacements:

        text_instances = page.search_for(text_to_replace)

        for i, inst in enumerate(text_instances):  #
            if method == 1 and i == 0:  
                page.add_redact_annot(inst, fill=(1,1,1))
                
                page.apply_redactions(images=0,graphics=0)
                new_x0 = inst[0]  
                new_y0 = inst[3]  
                print(new_x0, new_y0)
                doc.save(output_path_2)
                create_pdf_with_custom_font(new_text, font_path, output_path, font_path, new_size, inst[2], page.rect.height - inst[3] + 5 , (page.rect.width, page.rect.height), new_color)
                merge_pdfs(output_path_2, output_path, output_path_3)
                print("мы тут были")
            elif method == 2: 
                page.add_redact_annot(inst, fill=(1,1,1))
                page.apply_redactions()
                new_rect = fitz.Rect(inst[0], inst[1], inst[2], inst[3])
                page.insert_textbox(new_rect, new_text, fontsize=new_size, fontfile=fontfile, color=new_color, align=fitz.TEXT_ALIGN_CENTER)



def replace_text_custom_2(pdf_path, output_path, replacements, font_path, new_size, new_color, output_path_2, output_path_3, gap):

    doc = fitz.open(pdf_path)  
    page = doc[0]
    for text_to_replace, new_text, method in replacements:
        text_instances = page.search_for(text_to_replace)

        for i, inst in enumerate(text_instances):  
            if method == 1 and i == 0: 
                page.add_redact_annot(inst, fill=(1,1,1))
               
                page.apply_redactions(images=0,graphics=0)
              
                new_x0 = inst[0]  
                new_y0 = inst[3]  
                print(new_x0, new_y0)
                doc.save(output_path_2)
                create_pdf_with_custom_font(new_text, font_path, output_path, font_path, new_size, inst[2], page.rect.height - inst[3] + gap , (page.rect.width, page.rect.height), new_color)
                merge_pdfs(output_path_2, output_path, output_path_3)
                
                print("мы тут были")
            elif method == 2:  
                page.add_redact_annot(inst, fill=(1,1,1))
                page.apply_redactions()
                new_rect = fitz.Rect(inst[0], inst[1], inst[2], inst[3])
                page.insert_textbox(new_rect, new_text, fontsize=new_size, fontfile=fontfile, color=new_color, align=fitz.TEXT_ALIGN_CENTER)

text = "400"
pdf_path = "ReceiptFont/tink-tink-in/Integer.pdf"  
output_path = "modified_document.pdf" 
output_path_2 = "modified_document_2.pdf"  
output_path_3 = "result.pdf"
output_path_4 = "result_2.pdf"  
output_path_5 = "result_3.pdf"
output_path_6 = "result_4.pdf"
output_path_7 = "final.pdf"
font_path = "d/fonts/EEX.ttf"  
original_string = "2-12-064-577-913"
generated_string = generate_random_string(original_string)
generated_rrn = generate_rrn()
replacements = [
    ("300", "300", 1), 
    ("01.03.2024  14:45:18", "01.03.2024  14:55:18", 1),
    ("5404050596", "5404050596", 1),
    ("012064577913", generated_rrn, 1),
    (original_string, generated_string, 1)
]
new_size = 16.25  
new_color = (0.2,0.2,0.2)  

# replace_text_custom(pdf_path, output_path, [replacements[0]], "ТЗ на чеки/ReceiptFont/sbp-tink-in/Heading.ttf", new_size, new_color, output_path_2, output_path_3)
# replace_text_custom_2(output_path_3, output_path, [replacements[1]], "d/fonts/dsText/400.ttf", 8, (0.5647058823529412, 0.5647058823529412, 0.5647058823529412), output_path_2, output_path_4, 2.75)
# replace_text_custom_2(output_path_4, output_path, [replacements[2]], "d/fonts/dsText/400.ttf", 9, new_color, output_path_2, output_path_5, 2.75)
# replace_text_custom_2(output_path_5, output_path, [replacements[3]], "d/fonts/dsText/400.ttf", 9, new_color, output_path_2, output_path_6, 2.75)
# replace_text_custom_2(output_path_6, output_path, [replacements[4]], "d/fonts/dsText/400.ttf", 8, new_color, output_path_2, output_path_7, 2.75)