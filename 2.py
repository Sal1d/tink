import fitz  # Импортируем библиотеку PyMuPDF (fitz)
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

def create_pdf_with_custom_font(text, font_path, output_path, font_name="CustomFont", font_size=15, right_edge_x=500, text_y=750, page_size=(595.28, 841.89), text_color=(0, 0, 0)):
    """
    Создает PDF файл с заданным текстом, используя указанный шрифт.
    
    :param text: Текст для добавления в PDF.
    :param font_path: Путь к файлу шрифта (.ttf).
    :param output_path: Путь для сохранения созданного PDF файла.
    :param font_name: Имя шрифта для регистрации в ReportLab.
    :param font_size: Размер шрифта для текста.
    :param text_x: X-координата для размещения текста.
    :param text_y: Y-координата для размещения текста.
    """
    # Регистрация шрифта
    pdfmetrics.registerFont(TTFont(font_name, font_path))
    

    c = canvas.Canvas(output_path, pagesize=page_size)
    c.setFont(font_name, font_size)  # Установка шрифта и размера шрифта
    c.setFillColor(text_color)
    c.drawRightString(right_edge_x, text_y, text)
    c.save()

def merge_pdfs(base_pdf_path, overlay_pdf_path, output_path):
    """
    Объединяет два PDF файла в один.
    
    :param base_pdf_path: Путь к исходному PDF файлу.
    :param overlay_pdf_path: Путь к PDF файлу, который будет добавлен.
    :param output_path: Путь для сохранения итогового PDF файла.
    """
    base_pdf = fitz.open(base_pdf_path)
    overlay_pdf = fitz.open(overlay_pdf_path)
    
    for page_num in range(len(base_pdf)):
        page = base_pdf[page_num]
        # Наложение страницы из overlay_pdf на текущую страницу в base_pdf
        page.show_pdf_page(page.rect, overlay_pdf, 0)
    
    base_pdf.save(output_path)


def replace_text_custom(pdf_path, output_path, replacements, font_path, new_size, new_color, output_path_2):

    """
    pdf_path: путь к исходному PDF файлу
    output_path: путь для сохранения измененного PDF файла
    replacements: список кортежей, где каждый кортеж определяет текст для замены, новый текст, и метод замены
    fontfile: путь к файлу пользовательского шрифта, который будет использоваться для вставки нового текста
    new_size: размер шрифта для нового текста
    new_color: цвет шрифта для нового текста в формате RGB (по умолчанию черный)
    """
    doc = fitz.open(pdf_path)  # Открытие исходного PDF файла
    for page in doc:  # Перебираем все страницы в документе
        for text_to_replace, new_text, method in replacements:
            # Ищем вхождения текста для замены на текущей странице
            text_instances = page.search_for(text_to_replace)

            for i, inst in enumerate(text_instances):  # Перебираем все найденные инстансы текста
                if method == 1 and i == 0:  # Для первого вхождения и первого метода замены
                    page.add_redact_annot(inst, fill=(1,1,1))
                    # Применение аннотации
                    page.apply_redactions()
                    # Расчет нового положения текста, прижатого к правой части прямоугольника
                    # Этот шаг требует доработки в зависимости от длины текста и размера шрифта
                    
                    new_x0 = inst[0]  # Начальная x-координата остаётся прежней
                    new_y0 = inst[3]  # Начальная y-координата остаётся прежней
                    print(new_x0, new_y0)
                    create_pdf_with_custom_font("500", font_path, output_path, font_path, 16, inst[2], page.rect.height - inst[3] + 5, (page.rect.width, page.rect.height), (0.2,0.2,0.2))
                    merge_pdfs(pdf_path, output_path, output_path_2)
                    # Вставка нового текста с позиционированием в расчетном прямоугольнике
                    #page.insert_text((new_x0, new_y0), new_text, fontsize=new_size, fontname="Helvetica", color=new_color)  # fontname может потребовать корректировки

                    print("мы тут были")
                elif method == 2:  # Для всех вхождений с вторым методом замены
                    # Аналогичная логика "стирания", но с другим стилем вставки текста
                    page.add_redact_annot(inst, fill=(1,1,1))
                    page.apply_redactions()
                    new_rect = fitz.Rect(inst[0], inst[1], inst[2], inst[3])
                    page.insert_textbox(new_rect, new_text, fontsize=new_size, fontfile=fontfile, color=new_color, align=fitz.TEXT_ALIGN_CENTER)

    #doc.save(output_path_2)  # Сохраняем измененный документ

# Пример использования функции:
text = "400"
pdf_path = "d/tink-sbp-out.pdf"  # Путь к исходному PDF файлу
output_path = "C:/Users/HOME/Desktop/питончик/ломов/modified_document.pdf"  # Путь для сохранения измененного PDF файла
output_path_2 = "C:/Users/HOME/Desktop/питончик/ломов/modified_document_2.pdf"  # Путь для сохранения измененного PDF файла

font_path = "d/fonts/EEX.ttf"  # Путь к пользовательскому шрифту
replacements = [
    ("500", "2 000", 1),  # Замена текста "Text1" на "Replacement1" с методом 1
]
new_size = 15  # Размер шрифта для нового текста
new_color = (0.2,0.2,0.2)  # Цвет шрифта для нового текста

replace_text_custom(pdf_path, output_path, [replacements[0]], font_path, new_size, new_color, output_path_2)
