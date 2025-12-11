import os

def buscarResolucao(resolucao):
    partes = resolucao.split('-')
    pasta_ano = f"./resolucoes/{partes[-1]}"
    prefixo_resolucao = f"Resolução nº {partes[0]}"
    arquivo_encontrado = None
    for nome_arquivo in os.listdir(pasta_ano):
        if nome_arquivo.startswith(prefixo_resolucao) and nome_arquivo.endswith(".pdf"):
            arquivo_encontrado = nome_arquivo
            break  # para no primeiro que encontrar

    if arquivo_encontrado:
        caminho_res = os.path.normpath(os.path.join(pasta_ano, arquivo_encontrado))

        print(f"Arquivo encontrado: {caminho_res}")
        return caminho_res
    else:
        print("Nenhum arquivo encontrado com esse prefixo.")