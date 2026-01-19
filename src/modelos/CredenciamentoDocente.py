from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Pt
from src.util.Cabecalho import geraCabecalho
from src.util.Titulo import geraTitulo
from src.util import Armazenador, ColetorDeDados, Assinatura, FormatadorTexto
from util.RodapeRepublicacao import geraRodapeRepublicacao
import yaml

def geraModelo(n_res, data_res, ad_referendum, data_reuniao, dados_dinamicos):

    nome_professor = dados_dinamicos["Nome do Professor"]
    modalidade = dados_dinamicos["Modalidade"]

    with open('./src/config/configs.yaml', "r", encoding="utf-8") as file:
        file_parts = list(yaml.safe_load_all(file))
    document = Document(str(file_parts[0]['timbre_res']))

    geraTitulo(document, n_res, data_res)

    geraCabecalho(document, ad_referendum, data_reuniao)

    p1 = document.add_paragraph()

    FormatadorTexto.add_texto_negrito(p1, f"        Aprovar o credenciamento do(a) professor(a) {nome_professor},", f"{nome_professor}")
    FormatadorTexto.add_texto_sublinhado(p1, f"como {modalidade}, no quadro de docentes do Programa de Pós-Graduação em Ciência e Tecnologia Ambiental/FACET.", f"{modalidade}")
    p1.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

    p1_format = p1.paragraph_format
    p1_format.space_after = Pt(100)

    Assinatura.geraCampoAssinatura(document)

    if isinstance(file_parts[1]['republicacao'], list):
        geraRodapeRepublicacao(document)

    # Define o diretório e título da resolução que será salva
    dir_res = ColetorDeDados.extraiAnoResolucao(data_res)
    if ad_referendum:
        titulo_doc = f'Resolução nº {n_res} - AD REFERENDUM Aprova credenciamento({modalidade}) - {nome_professor}.docx'
    else:
        titulo_doc = f'Resolução nº {n_res} - Aprova credenciamento({modalidade}) - {nome_professor}.docx'

    Armazenador.salvar(dir_res, document, titulo_doc)