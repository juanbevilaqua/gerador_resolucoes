#Afastamento, AdiamentoReuniao, AproveitamentoSuficiencia, AprovacaoBanca, \
#     ConvalidacaoSuficiencia, CalendarioReunioes, CancelamentoMatricula, TrocaOrientacao, TrocaProjetoPesq, Desligamento, \
#     ProrrogacaoQualificacao, InclusaoCoorientacao, Trancamento, LicencaMaternidade, HomologacaoAdReferendum, ComposicaoDeComissao, \
#     CredenciamentoDocente

import customtkinter as ctk
from src.interfaces import telaInicial, telaPrincipal
from interfaces.telasGerencia import telaGerencia


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Sistema Gerador de Resoluções")
        self.geometry("950x750")
        self.resizable(width=False, height=False)

        self.tela_atual = None
        self.exibir_tela_inicial()

    def exibir_tela_inicial(self):
        self.redirecionar(telaInicial.TelaInicial)

    def exibir_tela_principal(self):
        self.redirecionar(telaPrincipal.TelaPrincipal)

    def exibir_tela_gerencia(self):
        self.redirecionar(telaGerencia.TelaGerencia)

    def redirecionar(self, classe_tela):
        if self.tela_atual:
            self.tela_atual.destroy()
        self.tela_atual = classe_tela(self)
        self.tela_atual.pack(fill="both", expand=True)

if __name__ == '__main__':
    app = App()
    app.mainloop()



# ********************************
# def menu():
#     pass
#
# def ver(palavra):
#     p = input("Ver?")
#
#     if p == "s":
#         print("Palavra: ",palavra)
#
# if __name__ == '__main__':
#     #menu()
#     #tela = telaPrincipal.TelaPrincipal()
#     tela = telaInicial.TelaInicial()
#     tela.iniciar()

    #palavra = telaPrincipal.tela()

    #ver(palavra)

    #print(palavra)



