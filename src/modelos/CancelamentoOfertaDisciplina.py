from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Pt

import util.Data
from src.util.Titulo import geraTitulo
from src.util.Cabecalho import geraCabecalho
from src.util import Armazenador, ColetorDeDados, Assinatura, FormatadorTabela, FormatadorTexto
from util.RodapeRepublicacao import geraRodapeRepublicacao
import yaml

def geraModelo(n_res, data_res, ad_referendum, data_reuniao, dados_dinamicos):
    disciplina = dados_dinamicos["Nome da Disciplina"]
    professor = dados_dinamicos["Professor Responsável"]
    motivo = dados_dinamicos["Motivo"]
    outro = dados_dinamicos["Outro"]
    if motivo == 'Outro(s)':
        motivo = outro
    elif motivo == "Inexistência de Matriculados":
        motivo = 'inexistência de inscritos na disciplina'

    semestre = dados_dinamicos["Semestre(ano-nº semestre)"]

    parts_semestre = semestre.split("-") # Formato: 2025.2
    if parts_semestre[-1] == "1":
        semestre_convert = f"primeiro semestre de {parts_semestre[0]}"
    else:
        semestre_convert = f"segundo semestre de {parts_semestre[0]}"

    with open('./src/config/configs.yaml', "r", encoding="utf-8") as file:
        file_parts = list(yaml.safe_load_all(file))
    document = Document(str(file_parts[0]['timbre_res']))

    geraTitulo(document, n_res, data_res)

    geraCabecalho(document, ad_referendum, data_reuniao)

    p1 = document.add_paragraph()
    FormatadorTexto.add_texto_negrito(p1, f"     APROVAR o cancelamento da disciplina “{disciplina}”, ", disciplina )
    FormatadorTexto.add_texto_sublinhado(p1, f"que seria ministrada pelo(a) docente {professor} no {semestre_convert}. Cancelamento justificado por {motivo}.", professor)
    p1.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p1_format = p1.paragraph_format
    p1_format.space_after = Pt(100)

    Assinatura.geraCampoAssinatura(document)

    if isinstance(file_parts[1]['republicacao'], list):
        geraRodapeRepublicacao(document)

    # Define o título da resolução que será salva
    dir_res = util.Data.extraiAnoResolucao(data_res)
    if ad_referendum:
        titulo_doc = f'Resolução nº {n_res} - AD REFERENDUM Aprova cancelamento de oferta de disciplina - {disciplina}({semestre}).docx'
    else:
        titulo_doc = f'Resolução nº {n_res} - Aprova cancelamento de oferta de disciplina - {disciplina}({semestre}).docx'

    Armazenador.salvar(dir_res, document, titulo_doc)