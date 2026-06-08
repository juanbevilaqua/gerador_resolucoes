def converteNivelString(nivel): # Converte a seleção do nivel(M e D) para MESTRADO ou DOUTORADO
    nivel.upper()
    if nivel == 'M':
        nivel = 'Mestrado'
    else:
        nivel = 'Doutorado'

    return nivel

def encurtaNome(nome):
    partes = nome.split()
    # Verifica se há mais de uma palavra no nome
    if len(partes) > 1:
        nome_encurtado = partes[0] + ' ' + partes[-1]
        return nome_encurtado.upper()
    else:
        return partes[0].upper() # Caso o nome seja composto por apenas uma palavra

