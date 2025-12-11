import customtkinter as ctk
from tkinter import messagebox
from datetime import datetime

def numeroParaMes(numero):
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

def coletaData(data, extenso):

    #data = input(f'Data {tipo}(DD/MM/AAAA): ')
    dia, mes, ano = data.split('/')

    if extenso:
        nome_mes = numeroParaMes(int(mes))
        return dia + ' DE ' + nome_mes + ' DE ' + ano
    else:
        return data

def validar_data(entry):
    data = entry.get()

    try:
        datetime.strptime(data, "%d/%m/%Y")
    except ValueError:
        messagebox.showerror("Erro", "Formato de data inválido. Use: dd/mm/aaaa")

# *** formato de data DD/MM/AA e usa split para dividir a data e utilzar o valor das variaveis


