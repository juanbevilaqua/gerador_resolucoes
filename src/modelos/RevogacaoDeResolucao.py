from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Pt

import util.Data
from src.util.Cabecalho import geraCabecalho
from src.util.Titulo import geraTitulo
from src.util import Armazenador, ColetorDeDados, Assinatura, FormatadorTexto
from util.RodapeRepublicacao import geraRodapeRepublicacao
import yaml

def geraModelo(n_res, data_res, ad_referendum, data_reuniao, dados_dinamicos):

    resolucao = dados_dinamicos["Nº. da Resolução"]
    data_res = dados_dinamicos["Data da Resolução"]

    with open('./src/config/configs.yaml', "r", encoding="utf-8") as file:
        file_parts = list(yaml.safe_load_all(file))
    document = Document(str(file_parts[0]['timbre_res']))

    geraTitulo(document, n_res, data_res)

    geraCabecalho(document, ad_referendum, data_reuniao)

    list_itens = []

    #list_itens.append(FormatadorTexto.add_texto_negrito(p1, f"        Revogar a resolução PPGCTA nº. {resolucao}, de {data_res};", f"{resolucao}"))
    list_itens.append(f"Revogar a resolução PPGCTA nº. {resolucao}, de {data_res};")
    list_itens.append("Informar que esta resolução entra em vigor na data de sua publicação.")
    #p1.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

    FormatadorTexto.add_lista_ordenada(document, list_itens)

    p1 = document.add_paragraph()
    p1_format = p1.paragraph_format
    p1_format.space_after = Pt(100)

    Assinatura.geraCampoAssinatura(document)

    if isinstance(file_parts[1]['republicacao'], list):
        geraRodapeRepublicacao(document)

    partes_data_res = data_res.split('/')
    ano = partes_data_res[-1]

    # Define o diretório e título da resolução que será salva
    dir_res = util.Data.extraiAnoResolucao(data_res)
    if ad_referendum:
        titulo_doc = f'Resolução nº {n_res} - AD REFERENDUM Revoga resolução nº. {resolucao} ({ano}).docx'
    else:
        titulo_doc = f'Resolução nº {n_res} - Revoga resolução nº. {resolucao} ({ano}).docx'

    Armazenador.salvar(dir_res, document, titulo_doc)