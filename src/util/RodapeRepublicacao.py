from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Pt
import yaml

def geraRodapeRepublicacao(document):
    with open('./src/config/configs.yaml', "r", encoding="utf-8") as file:
        configs = list(yaml.safe_load_all(file))

    infos = configs[1]['republicacao']

    data = infos[1]
    motivo = infos[2]

    p1 = document.add_paragraph()
    p1_format = p1.paragraph_format
    p1_format.space_after = Pt(10)
    rodape = document.add_paragraph(f'Resolução republicada em {data} para realização de {motivo}.')
    rodape_run = rodape.runs[0]
    rodape_run.font.size = Pt(10)
    rodape_run.italic = True
    rodape.alignment = WD_ALIGN_PARAGRAPH.CENTER