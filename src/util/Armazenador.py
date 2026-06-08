#import ConversorDocxPdf
from util import ManipuladorDeArquivos
import os
import yaml
import sys

def get_base_path():
    if getattr(sys, "frozen", False):
        # Se estiver rodando como .exe
        return os.path.dirname(sys.executable)
    else:
        # Se estiver rodando pela IDE
        return os.path.abspath(os.getcwd())

def salvar(diretorio, document, titulo):
    with open('./src/config/configs.yaml', "r", encoding="utf-8") as file:
        configs = list(yaml.safe_load_all(file))

    if configs[1]["gdrive_save"] is True:
        PLACE = 'DRIVE_DESKTOP'
    else:
        PLACE = 'LOCAL'

    base_path = get_base_path()
    base_resolucoes = os.path.join(base_path, "resolucoes")

    if PLACE == 'LOCAL':
        # titulo_docx_path = f"{configs[2]['path_local']}/{diretorio}/{titulo}"
        # titulo_pdf_path = f"{configs[2]['path_local']}/{diretorio}"

        titulo_docx_path = os.path.join(base_resolucoes, diretorio, titulo)
        titulo_pdf_path = os.path.join(base_resolucoes, diretorio)
    elif PLACE == 'DRIVE_DESKTOP':
        titulo_docx_path = f"{configs[2]['path_drive_docx']}/{diretorio}/{titulo}"
        titulo_pdf_path = f"{configs[2]['path_drive_pdf']}/{configs[2]['final_directory_drive_pdf']}"


    print("Tentando salvar em:", os.path.abspath(titulo_docx_path))


    pdf = configs[1]['pdf_autosave']

    # Garante que o diretório pai existe antes de tentar salvar
    novo_diretorio = os.path.dirname(titulo_docx_path)
    if not os.path.exists(novo_diretorio):
        print(f"Diretório '{diretorio}' não encontrado. Criando o diretório...")
        os.makedirs(novo_diretorio, exist_ok=True)

    try:
        document.save(titulo_docx_path)
        if pdf:
            print(ManipuladorDeArquivos.converterDocxPdf(titulo_docx_path, titulo_pdf_path))
    except Exception as e:
        raise e