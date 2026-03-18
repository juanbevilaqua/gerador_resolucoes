from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Pt

import util.Data
from src.util.Cabecalho import geraCabecalho
from src.util.Titulo import geraTitulo
from src.util import Armazenador, ColetorDeDados, Assinatura, CarregadorDeConfigs
from util.RodapeRepublicacao import geraRodapeRepublicacao
import yaml

def geraModelo(n_res, data_res, ad_referendum, data_reuniao, dados_dinamicos):

    nome_aluno = dados_dinamicos["Nome do Aluno"]
    nome_professor = dados_dinamicos["Nome do Orientador"]
    prazo_regularizacao = dados_dinamicos["Prazo Para Regularização(em dias)"]


    file_parts = CarregadorDeConfigs.carregar_config()
    document = Document(str(file_parts[0]['timbre_res']))

    geraTitulo(document, n_res, data_res)

    geraCabecalho(document, ad_referendum, data_reuniao)

    p1 = document.add_paragraph(f"       APROVAR o cancelamento da orientação do(a) professor(a) {nome_professor} ao discente "
                                f"{nome_aluno}, concedendo o prazo de {prazo_regularizacao} dias ao(à) aluno(a) para apresentar o aceite de um novo orientador.")

    p1.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

    p1_format = p1.paragraph_format
    p1_format.space_after = Pt(100)

    Assinatura.geraCampoAssinatura(document)

    if isinstance(file_parts[1]['republicacao'], list):
        geraRodapeRepublicacao(document)

    # Define o diretório e título da resolução que será salva
    dir_res = util.Data.extraiAnoResolucao(data_res)
    nome_encurtado = ColetorDeDados.encurtaNome(nome_aluno)
    if ad_referendum:
        titulo_doc = f'Resolução nº {n_res} - AD REFERENDUM Aprova o cancelamento da orientação de {nome_professor} ao(à) discente - {nome_encurtado}.docx'
    else:
        titulo_doc = f'Resolução nº {n_res} - Aprova o cancelamento da orientação de {nome_professor} ao(à) discente - {nome_encurtado}.docx'

    Armazenador.salvar(dir_res, document, titulo_doc)