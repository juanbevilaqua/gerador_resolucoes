import subprocess
from docx import Document
from pdf2docx import Converter
import io
from PyPDF2 import PdfMerger
import os

def converterDocxPdf(input_path, output_path):
    # try:
    #     # Caminho absoluto para evitar problemas com espaços ou caracteres especiais
    #     abs_input = os.path.abspath(input_path)
    #     abs_output = os.path.abspath(output_path)
    #
    #     # Garante que o diretório de saída existe
    #     os.makedirs(os.path.dirname(abs_output), exist_ok=True)
    #
    #     # Comando para o LibreOffice imprimir diretamente no caminho de saída
    #     subprocess.run([
    #         'soffice',
    #         '--headless',
    #         '--convert-to', 'pdf',  # Método direto de conversão (sem impressora)
    #         '--outdir', os.path.dirname(abs_output),
    #         abs_input
    #     ], check=True)
    #
    #     # O LibreOffice gera o PDF com o mesmo nome do .docx, mas extensão .pdf
    #     pdf_gerado = os.path.join(
    #         os.path.dirname(abs_output),
    #         os.path.splitext(os.path.basename(abs_input))[0] + ".pdf"
    #     )
    #
    #     # Renomeia para o nome desejado (se necessário)
    #     if pdf_gerado != abs_output:
    #         os.rename(pdf_gerado, abs_output)
    #
    #     print(f"PDF salvo em: {abs_output}")
    #     return abs_output
    #
    # except Exception as e:
    #     print(f"Erro ao converter para PDF: {e}")
    #     return None
#-------------------------

# def converterDocxPdf(input_path, output_path):
#     try:
#         # Define o nome temporário do arquivo PDF na pasta desejada
#         abs_input = os.path.abspath(input_path)
#         abs_output = os.path.abspath(output_path)
#
#         # Usa o comando de impressão do LibreOffice, definindo a impressora Microsoft Print to PDF
#         subprocess.run([
#             'soffice',
#             '--headless',
#             '-p',  # comando para imprimir
#             abs_input
#         ], check=True)
#
#         print(f"PDF gerado via impressão virtual em: {abs_output}")
#         return abs_output
#
#     except Exception as e:
#         print(f"Erro ao imprimir para PDF: {e}")
#         return None
#-----------------------
    try:
        subprocess.run(['soffice', '--headless', '--convert-to', 'pdf', input_path, '--outdir', output_path])
        # subprocess.run([
        #     'soffice',
        #     '--headless',
        #     '--convert-to', 'pdf',  # Método direto de conversão (sem impressora)
        #     '--outdir', os.path.dirname(output_path),
        #     input_path
        # ], check=True)
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