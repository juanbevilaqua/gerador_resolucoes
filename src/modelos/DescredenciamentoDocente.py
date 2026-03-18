from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Pt

import util.Data
from src.util.Cabecalho import geraCabecalho
from src.util.Titulo import geraTitulo
from src.util import Armazenador, CarregadorDeConfigs, Assinatura, FormatadorTexto
from util.RodapeRepublicacao import geraRodapeRepublicacao
import yaml

def geraModelo(n_res, data_res, ad_referendum, data_reuniao, dados_dinamicos):

    nome_professor = dados_dinamicos["Nome do Professor"]
    modalidade = dados_dinamicos["Modalidade"]
    motivo = dados_dinamicos["Motivo"]
    outro = dados_dinamicos["Outro"]

    if outro == 'null': # motivo = solicitado pelo docente
        motivo = "a pedido"
    else:
        motivo = outro


    file_parts = CarregadorDeConfigs.carregar_config()
    document = Document(str(file_parts[0]['timbre_res']))

    geraTitulo(document, n_res, data_res)

    geraCabecalho(document, ad_referendum, data_reuniao)

    p1 = document.add_paragraph()

    FormatadorTexto.add_texto_negrito(p1, f"        Manifestar-se favoravelmente ao descredenciamento,", "Manifestar-se favoravelmente")
    FormatadorTexto.add_texto_sublinhado(p1, f" {motivo}, do(a) docente ", f"{motivo}")
    FormatadorTexto.add_texto_negrito(p1, f"{nome_professor}(do quadro de {modalidade}), do Programa de Pós-Graduação em Ciência e "
                                          f"Tecnologia Ambiental da UFGD.", f"{nome_professor}")
    p1.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

    p1_format = p1.paragraph_format
    p1_format.space_after = Pt(100)

    Assinatura.geraCampoAssinatura(document)

    if isinstance(file_parts[1]['republicacao'], list):
        geraRodapeRepublicacao(document)

    # Define o diretório e título da resolução que será salva
    dir_res = util.Data.extraiAnoResolucao(data_res)
    if ad_referendum:
        titulo_doc = f'Resolução nº {n_res} - AD REFERENDUM Aprova descredenciamento({modalidade}) - {nome_professor}.docx'
    else:
        titulo_doc = f'Resolução nº {n_res} - Aprova descredenciamento({modalidade}) - {nome_professor}.docx'

    Armazenador.salvar(dir_res, document, titulo_doc)