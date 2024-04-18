import fitz
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
import random


def generate_random_string(original_string):
    parts = original_string.split('-')
    prefix = original_string[:4]
    random_part = '-'.join([str(random.randint(100, 999)) for _ in range(3)])
    result = prefix + '-' + random_part
    return result


def create_pdf_with_custom_font(text, font_path, output_path, font_name="CustomFont", font_size=15, right_edge_x=500,
                                text_y=750, page_size=(595.28, 841.89), text_color=(0, 0, 0)):
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


def replace_text_custom(pdf_path, output_path, replacements, font_path, new_size, new_color, output_path_2,
                        output_path_3):
    doc = fitz.open(pdf_path)
    page = doc[0]
    for text_to_replace, new_text, method in replacements:

        text_instances = page.search_for(text_to_replace)

        for i, inst in enumerate(text_instances):  #
            if method == 1 and i == 0:
                page.add_redact_annot(inst, fill=(1, 1, 1))

                page.apply_redactions(images=0, graphics=0)
                new_x0 = inst[0]
                new_y0 = inst[3]
                print(new_x0, new_y0)
                doc.save(output_path_2)
                create_pdf_with_custom_font(new_text, font_path, output_path, font_path, new_size, inst[2],
                                            page.rect.height - inst[3] + 5, (page.rect.width, page.rect.height),
                                            new_color)
                merge_pdfs(output_path_2, output_path, output_path_3)
                print("мы тут были")
            elif method == 2:
                page.add_redact_annot(inst, fill=(1, 1, 1))
                page.apply_redactions()
                new_rect = fitz.Rect(inst[0], inst[1], inst[2], inst[3])
                page.insert_textbox(new_rect, new_text, fontsize=new_size, fontfile=fontfile, color=new_color,
                                    align=fitz.TEXT_ALIGN_CENTER)


def replace_text_custom_2(pdf_path, output_path, replacements, font_path, new_size, new_color, output_path_2,
                          output_path_3, gap):
    doc = fitz.open(pdf_path)
    page = doc[0]
    for text_to_replace, new_text, method in replacements:
        text_instances = page.search_for(text_to_replace)

        for i, inst in enumerate(text_instances):
            if method == 1 and i == 0:
                page.add_redact_annot(inst, fill=(1, 1, 1))

                page.apply_redactions(images=0, graphics=0)

                new_x0 = inst[0]
                new_y0 = inst[3]
                print(new_x0, new_y0)
                doc.save(output_path_2)
                create_pdf_with_custom_font(new_text, font_path, output_path, font_path, new_size, inst[2],
                                            page.rect.height - inst[3] + gap, (page.rect.width, page.rect.height),
                                            new_color)
                merge_pdfs(output_path_2, output_path, output_path_3)

                print("мы тут были")
            elif method == 2:
                page.add_redact_annot(inst, fill=(1, 1, 1))
                page.apply_redactions()
                new_rect = fitz.Rect(inst[0], inst[1], inst[2], inst[3])
                page.insert_textbox(new_rect, new_text, fontsize=new_size, fontfile=fontfile, color=new_color,
                                    align=fitz.TEXT_ALIGN_CENTER)


text = "400"
pdf_path = "ReceiptFont/tink-sbp-out/FloatWithComment.pdf"
output_path = "modified_document.pdf"
output_path_2 = "modified_document_2.pdf"
output_path_3 = "check/result.pdf"
output_path_4 = "check/result_2.pdf"
output_path_5 = "check/result_3.pdf"
output_path_6 = "check/result_4.pdf"
output_path_7 = "check/result_5.pdf"
output_path_8 = "check/result_6.pdf"
output_path_9 = "check/result_7.pdf"
output_path_10 = "check/result_8.pdf"
output_path_11 = "final.pdf"

font_path = "d/fonts/EEX.ttf"
original_string = "1-14-304-448-003"
generated_string = generate_random_string(original_string)
replacements = [
    ("12", "10", 1),
    (",30", ",10", 1),
    ("04.04.2024  11:46:03", "04.04.2024  11:46:03", 1),
    ("12,30", "1,30", 1),
    ("Владислав Скрябин", "Примерный гражданин", 1),
    ("+7 (981) 121-88-27", "+7 (911) 199-10-58", 1),
    ("Станислав К.", "Милана Б.", 1),
    ("Сбербанк", "Сбербанк", 1),
    ('привет', 'куча текста для теста туда сюда раз два три четые пять', 1),
    (original_string, generated_string, 1)
]
new_size = 16
new_color = (0.2, 0.2, 0.2)

replace_text_custom(pdf_path, output_path, [replacements[0]], font_path, new_size, new_color, output_path_2,
                    output_path_3)
replace_text_custom(output_path_3, output_path, [replacements[1]], font_path, 16,
                    (0.5647058823529412, 0.5647058823529412, 0.5647058823529412), output_path_2, output_path_4)
replace_text_custom_2(output_path_4, output_path, [replacements[2]], "d/fonts/dsHeading/400.ttf", 8,
                      (0.5647058823529412, 0.5647058823529412, 0.5647058823529412), output_path_2, output_path_5, 2.5)
replace_text_custom_2(output_path_5, output_path, [replacements[3]], "d/fonts/dsHeading/400.ttf", 9, new_color,
                      output_path_2, output_path_6, 2.5)
replace_text_custom_2(output_path_6, output_path, [replacements[4]], "d/fonts/dsHeading/400.ttf", 9, new_color,
                      output_path_2, output_path_7, 3)
replace_text_custom_2(output_path_7, output_path, [replacements[5]], "d/fonts/dsHeading/400.ttf", 9, new_color,
                      output_path_2, output_path_8, 3)
replace_text_custom_2(output_path_8, output_path, [replacements[6]], "d/fonts/dsHeading/400.ttf", 9, new_color,
                      output_path_2, output_path_9, 2.5)
replace_text_custom_2(output_path_9, output_path, [replacements[7]], "d/fonts/dsHeading/400.ttf", 9, new_color,
                      output_path_2, output_path_10, 3)
replace_text_custom_2(output_path_10, output_path, [replacements[8]], "d/fonts/dsHeading/400.ttf", 9, new_color,
                      output_path_2, output_path_11, 2.5)