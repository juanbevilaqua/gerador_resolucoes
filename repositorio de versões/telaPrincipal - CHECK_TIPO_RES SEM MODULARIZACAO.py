# import customtkinter as ctk
# from src.modelos import AproveitamentoSuficiencia
#
# janela = ctk.CTk()
#
# # Frame para os campos que mudam conforme o tipo
# frame_dinamico = ctk.CTkFrame(janela)
#
# def tela():
#     # frame_dinamico = ctk.CTkFrame(janela)
#
#     janela.title("Gerador de Resoluções")
#     janela.geometry("900x750")
#     janela.resizable(width=False, height=False)
#     frame = ctk.CTkFrame(janela)
#     frame.pack(pady=20)
#
#     # Frame para organizar os elementos lado a lado
#
#     numero_res_label = ctk.CTkLabel(frame, text="Nº da Resolução", width=100, height=25)
#     numero_res_label.grid(row=0, column=0, padx=(0, 10), pady=10)
#     numero_res_entry = ctk.CTkEntry(frame, width=200)
#     numero_res_entry.grid(row=0, column=1, pady=10)
#
#     data_res_label = ctk.CTkLabel(frame, text="Data da Resolução", width=100, height=25)
#     data_res_label.grid(row=1, column=0, padx=(0, 10), pady=10)
#     data_res_entry = ctk.CTkEntry(frame, width=200)
#     data_res_entry.grid(row=1, column=1, pady=10)
#
#     data_reuniao_label = ctk.CTkLabel(frame, text="Data da Reunião", width=100, height=25)
#     data_reuniao_label.grid(row=2, column=0, padx=(0, 10), pady=10)
#     data_reuniao_entry = ctk.CTkEntry(frame, width=200)
#     data_reuniao_entry.grid(row=2, column=1, pady=10)
#
#     is_ad_referendum = None
#     ad_referendum = ctk.StringVar(value="false")
#     ad_referendum_checkbox = ctk.CTkCheckBox(frame, text="Ad Referendum", variable=ad_referendum, onvalue="true",
#                                              offvalue="false",
#                                              command=lambda: check_ad_referendum(ad_referendum))  # , command=
#     ad_referendum_checkbox.grid(row=3, column=1, padx=(0, 10), pady=10)
#
#     if ad_referendum is True:
#         print("É AD REFERENDUM!!")
#
#     # data_res_entry.grid(row=1, column=1, pady=10)
#
#     # campo_label = ctk.CTkLabel(janela, text="Teste", width=100, height=25)
#     # campo_label.pack()
#
#     tipo_label = ctk.CTkLabel(janela, text="Tipo de Resolução")
#     tipo_label.pack()
#     tipo = ctk.StringVar(value="Selecione o tipo de resolução")
#     tipo_menu = ctk.CTkOptionMenu(janela,
#                                   values=["Aproveitamento Suf.", "Prorrog."],
#                                   variable=tipo,
#                                   width=250,
#                                   height=50,
#                                   corner_radius=10,
#                                   command=lambda valor: check_tipo_res(valor, numero_res_entry, data_res_entry,
#                                                                        data_reuniao_entry, ad_referendum,
#                                                                        frame_dinamico))
#
#     tipo_menu.pack()
#
#     janela.mainloop()
#     return
#
# class Documento:
#     def __init__(self, numero_res, data_res, data_reuniao):
#         self.numero_res = numero_res
#         self.data_res = data_res
#         self.data_reuniao = data_reuniao
#         self.ad_referendum = check_ad_referendum(ad_referendum)
#         self.valores_dinamicos = {}
#
#
#
# def check_ad_referendum(ad_referendum):
#     valor = ad_referendum.get()
#
#     if valor == "true":
#         return True
#     else:
#         return False
#
#         # campo_label = ctk.CTkLabel(janela, text="Teste", width=100, height=25)
#         # campo_label.pack()
#
# campos_dinamicos = {}
# def check_tipo_res(tipo, numero_res_entry, data_res_entry, data_reuniao_entry, ad_referendum, frame_dinamico):
#     frame_dinamico.pack(pady=10)# add o frame dinamico na tela
#
#     # Limpa o frame antes de adicionar novos campos
#     for widget in frame_dinamico.winfo_children():
#         widget.destroy()
#
#     # Limpa os campos antigos
#     campos_dinamicos.clear()
#
#     #tipo = combo_tipo_res.get()
#
#     if tipo == "Aproveitamento Suf.":
#         criar_campo("Língua")
#         criar_campo("Nome do Discente")
#         criar_campo("Data do Exame")
#         criar_campo("Resolução de Aprovação")
#
#         # lingua_label = ctk.CTkLabel(frame_dinamico, text="Língua", width=100, height=25)
#         # lingua_label.pack()
#         # lingua_entry = ctk.CTkEntry(frame_dinamico, width=200)
#         # lingua_entry.pack()
#         #
#         # nome_discente_label = ctk.CTkLabel(frame_dinamico, text="Nome do discente", width=100, height=25)
#         # nome_discente_label.pack()
#         # nome_discente_entry = ctk.CTkEntry(frame_dinamico, width=200)
#         # nome_discente_entry.pack()
#         #
#         # data_exame_label = ctk.CTkLabel(frame_dinamico, text="Data do exame", width=100, height=25)
#         # data_exame_label.pack()
#         # data_exame_entry = ctk.CTkEntry(frame_dinamico, width=200)
#         # data_exame_entry.pack()
#         #
#         # resolucao_label = ctk.CTkLabel(frame_dinamico, text="nº Resolução/ano", width=100, height=25)
#         # resolucao_label.pack()
#         # resolucao_entry = ctk.CTkEntry(frame_dinamico, width=200)
#         # resolucao_entry.pack()
#
#     if tipo == "Prorrog.":
#         tempo_label = ctk.CTkLabel(frame_dinamico, text="Tempo", width=100, height=25)
#         tempo_label.pack()
#         tempo_entry = ctk.CTkEntry(frame_dinamico, width=200)
#         tempo_entry.pack()
#
#     capturar_dados(numero_res_entry, data_res_entry, data_reuniao_entry)
#
#     # gerar_botao = ctk.CTkButton(frame_dinamico, text="Gerar Resolução", command=capturar_dados)
#     # gerar_botao.pack()
#
# def criar_campo(nome):
#     label = ctk.CTkLabel(frame_dinamico, text=nome)
#     label.pack()
#     entry = ctk.CTkEntry(frame_dinamico)
#     entry.pack()
#     campos_dinamicos[nome] = entry
#
#     # def capturar_dados():
#     #     numero_res = numero_res_entry.get()
#     #     data_res = data_res_entry.get()
#     #     data_reuniao = data_reuniao_entry.get()
#     #     lingua = lingua_entry.get()
#     #     nome = nome_discente_entry.get()
#     #     data = data_exame_entry.get()
#     #     resolucao = resolucao_entry.get()
#     #     print("Dados: ", numero_res, data_res, data_reuniao, lingua, nome, data, resolucao)#, Nome: {nome}, Data: {data}, Resolução: {resolucao}
#     #
#     #     ad_referendum = False
#     #     cont = 0
#     #
#     #     AproveitamentoSuficiencia.geraModelo(numero_res, data_res, ad_referendum, data_reuniao, lingua, nome, cont, data, resolucao)
#     #
#     # gerar_botao = ctk.CTkButton(frame_dinamico, text="Gerar Resolução", command=capturar_dados)
#     # gerar_botao.pack()
#
# def capturar_dados(numero_res_entry, data_res_entry, data_reuniao_entry):
#     # Dados fixos comuns (fora dos campos dinâmicos)
#     numero_res = numero_res_entry.get()
#     data_res = data_res_entry.get()
#     data_reuniao = data_reuniao_entry.get()
#
#     # Campos dinâmicos capturados automaticamente
#     valores_dinamicos = {nome: campo.get() for nome, campo in campos_dinamicos.items()}
#
#     print("Dados fixos:")
#     # print("Número:", numero_res)
#     # print("Data Resolução:", data_res)
#     # print("Data Reunião:", data_reuniao)
#     print("\nCampos dinâmicos:")
#     for nome, valor in valores_dinamicos.items():
#         print(f"{nome}: {valor}")
#
#     return valores_dinamicos
#
#
#
#         #botao = ctk.CTkButton(janela, width=300, "Pegar texto")
#         # lingua = lingua_entry.get()
#         # palavra = lingua
#         # return lingua
#         #print(lingua)
#
#
#
#     # lingua = input('Informe a língua do exame de suficiência: ')
#     # cont_discentes = 0
#     # discentes = []
#     # datas = []
#     # resolucoes = []
#     # label
#     # entry
#
#     #print("OK")
#
#
# def gerar_resolução(numero_res_entry, data_res_entry, data_reuniao_entry, ad_referendum, frame_dinamico):
#     numero_res = numero_res_entry.get()
#     data_res = data_res_entry.get()
#     data_reuniao = data_reuniao_entry.get()
#     is_ad_referendum = check_ad_referendum(ad_referendum)
#
#     gerar_botao = ctk.CTkButton(frame_dinamico, text="Gerar Resolução", command=capturar_dados)
#     gerar_botao.pack()
#
#     AproveitamentoSuficiencia.geraModelo(numero_res, data_res, is_ad_referendum, data_reuniao, lingua, nome, cont, data, resolucao)
#
# --------------------------------------------------

import customtkinter as ctk
from src.modelos import AproveitamentoSuficiencia, TrocaOrientacao

class TelaPrincipal:
    def __init__(self):
        self.janela = ctk.CTk()
        self.janela.title("Gerador de Resoluções")
        self.janela.geometry("900x750")
        self.janela.resizable(width=True, height=False)

        self.campos_dinamicos = {}  # dicionário para campos criados dinamicamente

        self.criar_widgets()

        self.cont_entry_button = 0
        self.button_add = None# variavel para controle do entry_button(guarda a referencia do último botao criado para não haver repetição)

    def criar_widgets(self):
        # Frame principal para os campos fixos
        frame = ctk.CTkFrame(self.janela)
        frame.pack(pady=20)

        # Campos fixos
        ctk.CTkLabel(frame, text="Nº da Resolução").grid(row=0, column=0, padx=10, pady=10)
        self.numero_res_entry = ctk.CTkEntry(frame, width=200)
        self.numero_res_entry.grid(row=0, column=1, pady=10)

        ctk.CTkLabel(frame, text="Data da Resolução").grid(row=1, column=0, padx=10, pady=10)
        self.data_res_entry = ctk.CTkEntry(frame, width=200)
        self.data_res_entry.grid(row=1, column=1, pady=10)


        self.default_colors_data_reuniao = []
        self.data_reuniao_label = ctk.CTkLabel(frame, text="Data da Reunião")
        self.data_reuniao_label.grid(row=2, column=0, padx=10, pady=10)
        self.default_color = self.data_reuniao_label.cget("text_color")#armazena a cor padrão do label
        self.default_colors_data_reuniao.append(self.default_color)
        self.data_reuniao_entry = ctk.CTkEntry(frame, width=200)
        self.data_reuniao_entry.grid(row=2, column=1, pady=10)
        self.default_color = self.data_reuniao_entry.cget("fg_color")#armazena a cor padrão do entry
        self.default_colors_data_reuniao.append(self.default_color)


        # Checkbox Ad Referendum
        self.ad_referendum_var = ctk.BooleanVar(value=False)
        self.ad_referendum_checkbox = ctk.CTkCheckBox(
            frame,
            text="Ad Referendum",
            variable=self.ad_referendum_var,
            command = lambda: self.alternar_estado_data_res(self.ad_referendum_checkbox, self.data_reuniao_label, self.data_reuniao_entry, self.default_colors_data_reuniao)
        )
        self.ad_referendum_checkbox.grid(row=3, column=1, pady=10, sticky="w")

        # Tipo de resolução (menu dropdown)
        ctk.CTkLabel(self.janela, text="Tipo de Resolução").pack(pady=(20,5))
        self.tipo_var = ctk.StringVar(value="Selecione o tipo de resolução")
        self.tipo_menu = ctk.CTkOptionMenu(
            self.janela,
            values=["Aproveitamento Suf.", "Troca"],
            variable=self.tipo_var,
            width=250,
            height=50,
            corner_radius=10,
            command=self.check_tipo_res
        )
        self.tipo_menu.pack()

        if hasattr(self, 'frame_dinamico'):
            self.frame_dinamico.destroy()

        # Frame para campos dinâmicos
        self.frame_dinamico = ctk.CTkScrollableFrame(self.janela)

        self.frame_dinamico.pack(pady=20, fill="x")#, fill="both", expand=True

        # Cria um frame para agrupar o entry e o botão
        # self.frame_entry_button_container = ctk.CTkFrame(self.frame_dinamico)
        # self.frame_entry_button_container.pack(padx=10, pady=10, fill="x")

        # Botão gerar resolução (desabilitado inicialmente)
        self.botao_gerar = ctk.CTkButton(self.janela, text="Gerar Resolução", command=self.gerar_resolucao)
        self.botao_gerar.pack(pady=20)
        self.botao_gerar.configure(state="disabled")  # ativa só após escolher tipo

    def alternar_estado_data_res(self, ad_referendum_checkbox, data_reuniao_label, data_reuniao_entry, default_colors):

        if ad_referendum_checkbox.get():
            print("TRUE***")
            data_reuniao_label.configure(text_color="gray")
            data_reuniao_entry.configure(state="disabled")# desabilita se marcado
            data_reuniao_entry.configure(fg_color="#4F4F4F")

        else:
            data_reuniao_entry.configure(state="normal")
            data_reuniao_label.configure(text_color=default_colors[0])
            data_reuniao_entry.configure(fg_color=default_colors[1])
    def check_tipo_res(self, tipo):
        # Limpa frame dinâmico e campos anteriores
        for widget in self.frame_dinamico.winfo_children():
            widget.destroy()
        # self.entry_button_container = ctk.CTkFrame(self.frame_dinamico)
        # self.entry_button_container.pack(padx=10, pady=10, fill="x")
        self.campos_dinamicos.clear()

        if tipo == "Aproveitamento Suf.":
            if hasattr(self, 'frame_entry_button_container'):# se existir o frame anterior, exclcui
                self.frame_entry_button_container.destroy()
            if hasattr(self, 'frame_lingua'):
                self.frame_lingua.destroy()

            self.frame_entry_button_container = ctk.CTkFrame(self.frame_dinamico)#cria um novo frame p/ o container
            #self.frame_entry_button_container.pack(side="left", padx=10, pady=10)#, fill="y"
            self.frame_entry_button_container.grid(row=0, column=0, padx=(0, 10), pady=10)

            # Frame da direita (campo de língua)
            self.frame_lingua = ctk.CTkFrame(self.frame_dinamico)
            #self.frame_lingua.pack(side="left", padx=10, pady=10)#, fill="y"
            self.frame_lingua.grid(row=0, column=1, padx=(0, 10), pady=10)


            self.criar_campo("Nome do Discente", tipo = 'entry_button', frame=self.frame_entry_button_container)
            self.criar_campo("Língua", frame = self.frame_lingua)
            self.criar_campo("Data do Exame", linha = 1 , frame=self.frame_dinamico)
            self.criar_campo("Resolução de Aprovação", linha = 2)
        elif tipo == "Troca":
            self.criar_campo("Nível Discente", tipo = 'dropdown', opcoes = ["Mestrado", "Doutorado"])
            self.criar_campo("Nome")
            self.criar_campo("Orientador Atual")
            self.criar_campo("Novo Orientador")


        # Ativa botão gerar resolução
        self.botao_gerar.configure(state="normal")

    def criar_campo(self, nome, tipo='entry', opcoes=None, linha=0, frame=None):
        if frame is None:
            frame = self.frame_dinamico

        if tipo == 'entry':
            print("Frame**", frame)
            label = ctk.CTkLabel(frame, text=nome)
            label.grid(row=linha, column=0, pady=10, padx=(5, 0))#padx=(0, 0), , sticky="w"
            #label.pack(anchor="w", padx=10, pady=(5, 0))#side=pos,

            entry = ctk.CTkEntry(frame, width=200)
            entry.grid(row=linha, column=1, pady=10, padx=(0, 5))#padx=(0, 0),
            #entry.pack(padx=10, pady=(0,10))#side=pos,
            self.campos_dinamicos[nome] = entry
        elif tipo == 'entry_button':
            frame_entry_button = ctk.CTkFrame(self.frame_entry_button_container)
            frame_entry_button.pack(padx=10, pady=10)#, fill="x"
            #frame_entry_button.pack(anchor="w", padx=10, pady=(5, 0))

            label = ctk.CTkLabel(frame_entry_button, text=nome)#frame_entry_button
            label.pack(side="left", padx=10, pady=(5, 0))

            entry = ctk.CTkEntry(frame_entry_button, width=300)
            entry.pack(side="left", padx=(0, 10))
            self.campos_dinamicos[f"nome_discente {self.cont_entry_button}"] = entry
            self.cont_entry_button += 1

            if self.button_add:
                self.button_add.destroy()# destrói a última referência de botão + criado
                self.button_add = None

            self.button_add = ctk.CTkButton(frame_entry_button, text="+", command=lambda: (self.criar_campo("Nome do Discente", tipo = 'entry_button', frame=self.frame_entry_button_container),
                                                                                           self.criar_campo("Língua", linha = self.cont_entry_button,frame = self.frame_lingua)))
            self.button_add.pack(side="left")
        elif tipo == 'dropdown':
            label = ctk.CTkLabel(frame, text=nome)#self.frame_dinamico
            label.pack(anchor="w", padx=10, pady=(5, 0))

            if not opcoes:
                opcoes = ["Opção 1", "Opção 2"]# caso não sejam fornecidas opções como parametro
            var = ctk.StringVar(value="Selecione")
            #var = ctk.StringVar(value=opcoes[0])
            dropdown = ctk.CTkOptionMenu(frame, values=opcoes, variable=var, width=300)#self.frame_dinamico
            dropdown.pack(padx=10, pady=(0, 10))
            self.campos_dinamicos[nome] = var

    def capturar_dados(self):
        numero_res = self.numero_res_entry.get()
        data_res = self.data_res_entry.get()
        data_reuniao = self.data_reuniao_entry.get()
        ad_referendum = self.ad_referendum_var.get()

        #valores_dinamicos = {nome: campo.get() for nome, campo in self.campos_dinamicos.items()}
        valores_dinamicos = {}
        lista_valores = []
        for nome, widget in self.campos_dinamicos.items():
            if isinstance(widget, ctk.CTkEntry):
                valor = widget.get()
                partes_nome = nome.split()
                if partes_nome[-1].isdigit():#verifica se há um cont acoplado ao nome do identificador
                #if nome.startswith("nome_discente") and not nome.endswith("nome_discente"):
                    lista_valores.append(valor)
                    valores_dinamicos[partes_nome[0]] = lista_valores
                else:#se não houver cont, significa que é uma string simples e não utiliza lista
                    valores_dinamicos[nome] = None if valor == "Selecione" else valor

            elif isinstance(widget, ctk.StringVar):
                valores_dinamicos[nome] = widget.get()



        # Debug: imprimir dados
        print("Número da Resolução:", numero_res)
        print("Data da Resolução:", data_res)
        print("Data da Reunião:", data_reuniao)
        print("Ad Referendum:", ad_referendum)
        print("Campos dinâmicos:")
        for nome, valor in valores_dinamicos.items():
            print(f"  {nome}: {valor}")

        return numero_res, data_res, data_reuniao, ad_referendum, valores_dinamicos

    def gerar_resolucao(self):
        print("PRONTO PARA GERAR***")
        # Captura os dados
        numero_res, data_res, data_reuniao, ad_referendum, valores_dinamicos = self.capturar_dados()

        # Exemplo: extrair campos específicos para "Aproveitamento Suf."
        if self.tipo_var.get() == "Aproveitamento Suf.":
            AproveitamentoSuficiencia.geraModelo(numero_res, data_res, ad_referendum, data_reuniao, valores_dinamicos)
        if self.tipo_var.get() == "Troca":
            TrocaOrientacao.geraModelo(numero_res, data_res, ad_referendum, data_reuniao, valores_dinamicos)
        #     lingua = valores_dinamicos.get("Língua", "")
        #     nome_discente = valores_dinamicos.get("Nome do Discente", "")
        #     data_exame = valores_dinamicos.get("Data do Exame", "")
        #     resolucao_aprovacao = valores_dinamicos.get("Resolução de Aprovação", "")
        #     cont = 0  # você pode ajustar conforme sua lógica
        #
        #     # Chamada ao método do seu modelo
        #     AproveitamentoSuficiencia.geraModelo(
        #         numero_res, data_res, ad_referendum, data_reuniao,
        #         lingua, nome_discente, cont, data_exame, resolucao_aprovacao
        #     )
        # elif self.tipo_var.get() == "Prorrog.":
        #     tempo = valores_dinamicos.get("Tempo", "")
        #     # Chamada para outro modelo se tiver
        #
        #     print(f"Gerar Prorrogação com tempo: {tempo}")
        #     # TODO: implementar chamada do modelo para Prorrogação

    def iniciar(self):
        self.janela.mainloop()
