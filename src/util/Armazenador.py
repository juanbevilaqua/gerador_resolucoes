#import ConversorDocxPdf
from util import ManipuladorDeArquivos
import os
import yaml

#PLACE = 'LOCAL'
PLACE = 'DRIVE_DESKTOP'

def salvar(diretorio, document, titulo):
    if PLACE == 'LOCAL':
        titulo_docx_path = f'./resolucoes/{diretorio}/{titulo}'
        titulo_pdf_path = f'./resolucoes/{diretorio}'
    elif PLACE == 'DRIVE_DESKTOP':
        titulo_docx_path = f'G:/Meu Drive/Coordenadoria/Resoluções/{diretorio}/{titulo}'
        titulo_pdf_path = f'G:/Meu Drive/Documentos p  Assinatura PPGCTA/P  Assinar/Resoluções'


    print("Tentando salvar em:", os.path.abspath(titulo_docx_path))


    # titulo_path = f'../../resolucoes/{diretorio}/{titulo}'
    # document.save(titulo_path)
    # ConversorDocxPdf.converter(titulo_path, f'../../resolucoes/{diretorio}')

    with open('./src/config/configs.yaml', "r", encoding="utf-8") as file:
        configs = list(yaml.safe_load_all(file))

    pdf = configs[1]['pdf_autosave']

    try:
        document.save(titulo_docx_path)
        if pdf:
            print(ManipuladorDeArquivos.converterDocxPdf(titulo_docx_path, titulo_pdf_path))
    except FileNotFoundError:
        print(f"Diretório '{diretorio}' não encontrado. Criando o diretório...")

        # Cria o diretório e tenta salvar o documento novamente
        novo_diretorio = titulo_docx_path.rsplit('/', 1)[0] # Ex: ./resolucoes/{diretorio}
        os.makedirs(novo_diretorio, exist_ok=True)
        document.save(titulo_docx_path)
        if pdf:
            ManipuladorDeArquivos.converterDocxPdf(titulo_docx_path, titulo_pdf_path)
    except Exception as e:
        print(f"Ocorreu um erro ao salvar o arquivo: {e}")
