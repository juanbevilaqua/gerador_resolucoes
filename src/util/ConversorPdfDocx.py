from docx import Document
from pdf2docx import Converter
import io


def converter(pdf_path):
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