import os

from docx.shared import Pt
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx.shared import RGBColor
from docx import Document

from utils.word_to_pdf import convert_docx_to_pdf


def create_certificate(user_id, test_id, fullname, science, class_num, date):
    doc = Document("data/images/certificate.docx")

    text_to_find1 = "fullname"
    text_to_find2 = "science fani class_num-sinf testini"
    text_to_find3 = "date_time"

    text2 = text_to_find2.replace('science', science).replace('class_num', f"{class_num}")

    for paragraph in doc.paragraphs:
        if text_to_find1 in paragraph.text:
            paragraph.text = paragraph.text.replace(text_to_find1, fullname)

            for run in paragraph.runs:
                run.font.name = 'DejaVu Sans'
                run.font.size = Pt(35)
                run.bold = True
                run.italic = True
                run.underline = True
                run.font.color.rgb = RGBColor(0, 0, 128)
            paragraph.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER

        elif text_to_find2 in paragraph.text:
            paragraph.text = paragraph.text.replace(text_to_find2, text2)

            for run in paragraph.runs:
                run.font.name = 'DejaVu Sans'
                run.font.size = Pt(20)
                run.bold = True
                run.underline = False
                run.font.color.rgb = RGBColor(0, 0, 128)
            paragraph.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER

        elif text_to_find3 in paragraph.text:
            paragraph.text = paragraph.text.replace(text_to_find3, str(date))

            for run in paragraph.runs:
                run.font.name = 'Cascadia Code SemiBold'
                run.font.size = Pt(16)
                run.bold = False
                run.underline = False
                run.font.color.rgb = RGBColor(0, 0, 255)

            paragraph.alignment = WD_PARAGRAPH_ALIGNMENT.RIGHT

    output_directory = 'data/images'

    word_file_name = f"data/images/{user_id}{test_id}.docx"
    # pdf_file_name = f"data/images/{user_id}{test_id}.pdf"
    doc.save(word_file_name)

    pdf_file_name = convert_docx_to_pdf(word_file_name, output_directory)

    try:
        os.remove(word_file_name)
    except OSError as xatolik:
        print(f"{word_file_name} o'chirishda xatolik yuz berdi: {xatolik}")

    return pdf_file_name

