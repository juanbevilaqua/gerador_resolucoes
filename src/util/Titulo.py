from docx.shared import Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH

def geraTitulo(document, n_res, data_res):
    titulo = document.add_heading(f'RESOLUÇÃO Nº. {n_res}, DE {data_res}', 1)
    run = titulo.runs[0]
    run.font.size = Pt(14)
    titulo.alignment = WD_ALIGN_PARAGRAPH.CENTER
    titulo_format = titulo.paragraph_format
    titulo_format.space_after = Pt(15)