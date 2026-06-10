import subprocess
from docx import Document
from pdf2docx import Converter
import io
from PyPDF2 import PdfMerger
import os


def converterDocxPdf(input_path, output_path):
    try:
        possiveis_caminhos = [
            r"C:\Program Files\LibreOffice\program\soffice.exe",
            r"C:\Program Files (x86)\LibreOffice\program\soffice.exe",
            "soffice"  # fallback se estiver no PATH
        ]

        soffice_path = None
        for caminho in possiveis_caminhos:
            if os.path.exists(caminho):
                soffice_path = caminho
                break

        if soffice_path is None:
            print("LibreOffice não encontrado.")
            return

        subprocess.run([soffice_path, '--headless', '--convert-to', 'pdf', input_path, '--outdir', output_path])
        print(f"Arquivo PDF gerado: {output_path}")
    except Exception as e:
        print(f"Erro ao gerar PDF: {e}")
def converterPdfDocx(pdf_path):
    # Criar um buffer de memória
    buffer = io.BytesIO()

    # Cria um conversor
    cv = Converter(pdf_path)

    # Converte o arquivo PDF para o buffer em memória
    cv.convert(buffer, start=0, end=None)  # start e end podem definir páginas específicas

    # Fecha o conversor
    cv.close()

    # Carregar o conteúdo do buffer no documento DOCX
    buffer.seek(0)  # Retorna ao início do buffer
    document = Document(buffer)

    # Fecha o buffer
    buffer.close()

    # Retorna o documento carregado
    return document


def unirPdfs(lista_pdfs, output_path):
    # Cria um objeto para gerenciar a fusão dos PDFs
    merger = PdfMerger()

    # Itera por cada PDF e o adiciona ao merger
    for pdf in lista_pdfs:
        merger.append(pdf)

    # Salva o PDF final no local desejado
    merger.write(output_path)
    merger.close()
    print(f"PDFs unidos com sucesso em '{output_path}'")