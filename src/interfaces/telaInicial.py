import customtkinter as ctk


class TelaInicial(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        #self.janela = ctk.CTk()
        #self.title("Gerador de Resoluções - Tela Inicial")
        #self.janela.geometry("950x750")
        #self.janela.resizable(width=False, height=False)

        self.criar_widgets()

    def criar_widgets(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        # self.janela.grid_rowconfigure(0, weight=1)
        # self.janela.grid_rowconfigure(1, weight=1)

        self.titulo_janela_label = ctk.CTkLabel(self, text="Seja bem-vindo ao Gerador de Resoluções do PPGCTA", font=('Segoe UI', 25))
        self.titulo_janela_label.grid(row=0, column=0, columnspan=2, pady=10)

        self.tela_principal_button = ctk.CTkButton(self, text="Criar Resoluções", height=60, font=('Segoe UI', 15), command=self.master.exibir_tela_principal)\
            .grid(row=1, column=0, sticky='ew', pady=20, padx=(10, 10))
        self.tela_gerencia_button = ctk.CTkButton(self, text="Gerenciar", height=60, font=('Segoe UI', 15), command=self.master.exibir_tela_gerencia)\
            .grid(row=1, column=1, sticky='ew', pady=20, padx=(10, 10))

    # def redirecionar(self, tela):
    #     if tela == 'PRINCIPAL':
    #         TelaPrincipal().iniciar()
    #         self.janela.after(100, self.janela.destroy())
    #
    #     else:
    #         TelaGerencia().iniciar()
    #         self.janela.destroy()

    def iniciar(self):
        self.janela.mainloop()