from docx import Document

def add_texto_negrito(paragraph, text, bold_word):
    # divide em antes, a palavra(trecho) e depois
    before, middle, after = text.partition(bold_word)

    paragraph.add_run(before)  # parte normal
    paragraph.add_run(middle).bold = True  # parte em negrito
    paragraph.add_run(after)   # parte normal

def add_texto_sublinhado(paragraph, text, bold_word):
    before, middle, after = text.partition(bold_word)

    paragraph.add_run(before)  # parte normal
    paragraph.add_run(middle).underline = True
    paragraph.add_run(after)

def add_texto_italico(paragraph, text, bold_word):
    before, middle, after = text.partition(bold_word)

    paragraph.add_run(before)  # parte normal
    paragraph.add_run(middle).italic = True
    paragraph.add_run(after)

def add_lista_nao_ordenada(doc, itens):
    for item in itens:
        p = doc.add_paragraph()
        p.add_run("     • ").bold = True
        p.add_run(item)
