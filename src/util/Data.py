import customtkinter as ctk
from tkinter import messagebox
from datetime import datetime

def numero_para_mes(numero):
    meses = {
        1: 'JANEIRO',
        2: 'FEVEREIRO',
        3: 'MARÇO',
        4: 'ABRIL',
        5: 'MAIO',
        6: 'JUNHO',
        7: 'JULHO',
        8: 'AGOSTO',
        9: 'SETEMBRO',
        10: 'OUTUBRO',
        11: 'NOVEMBRO',
        12: 'DEZEMBRO'

    }

    return meses.get(numero, 'Número do mês inválido')

def converter_data_extenso(data):

    dia, mes, ano = data.split('/')

    nome_mes = numero_para_mes(int(mes))
    return dia + ' DE ' + nome_mes + ' DE ' + ano

def converter_data_hifen(data):
    return data.replace("/", "-")

def validar_data(data):
    #data = entry.get()

    try:
        datetime.strptime(data, "%d/%m/%Y")
        return True
    except ValueError:
        #messagebox.showerror("Erro", "Formato de data inválido. Use: dd/mm/aaaa")
        return False

# *** formato de data DD/MM/AA e usa split para dividir a data e utilzar o valor das variaveis


def extraiAnoResolucao(data):
    try:
        datetime.strptime(data, "%d/%m/%Y") # se a data vier no formato DD/MM/AAAA, separa a string por '/'
        partes = data.split("/")
    except:
        partes = data.split() # caso contrario, separa por espaco

    return partes[-1]
