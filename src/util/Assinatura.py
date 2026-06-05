from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Pt
import yaml
from src.controladores import controladorCoordenador
from src.entidades import coordenador

def geraCampoAssinatura(document):
    with open('./src/config/configs.yaml', "r", encoding="utf-8") as file:
        configs = list(yaml.safe_load_all(file))

    vice_coordenador = configs[1]['vice_coordenador']
    funcao = ''


    if vice_coordenador is False:
        assinante = controladorCoordenador.CoordenadorController.listar_titular_ativo()[1]
    else:
        assinante = controladorCoordenador.CoordenadorController.listar_vice_ativo()[1]
        funcao = ' em Exercício'

    print("**Coordenador**: ",assinante)

    assinatura = document.add_heading(assinante, 5)

    # if vice_coordenador is False:
    #     assinatura = document.add_heading('Profª. Drª. Rozanna Marques Muzzi', 5)
    # else:
    #     assinatura = document.add_heading('Prof. Dr. Cláudio Rodrigo Nogueira', 5)
    #     funcao = ' em Exercício'

    assinatura.alignment = WD_ALIGN_PARAGRAPH.CENTER
    cargo = document.add_paragraph(f'Coordenador(a){funcao} do Programa de Pós-Graduação em Ciência e Tecnologia Ambiental')
    cargo_run = cargo.runs[0]
    cargo_run.font.size = Pt(11)
    cargo.alignment = WD_ALIGN_PARAGRAPH.CENTER