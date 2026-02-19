import csv

import customtkinter as ctk
from tkinter import filedialog
from src.controladores.controladorDisciplina import DisciplinaController
from functools import partial

class SecaoDisciplinas(ctk.CTkFrame):
    def __init__(self, master, gerenciador):
        super().__init__(master)
        self.gerenciador = gerenciador

        self.criar_widgets_disciplinas()

    def criar_widgets_disciplinas(self):
        self.grid_columnconfigure(0, weight=1)
        #self.grid_columnconfigure(1, weight=1)  # coluna do conteúdo (expande)
        self.grid_rowconfigure(1, weight=0)

        # =================
        # FRAME DINAMICO
        # =================

        self.carregar_disciplinas_button = ctk.CTkButton(self, text="⬇️ Carregar Disciplinas", text_color="white",
                                                        command=self.carregar_disciplinas)
        self.carregar_disciplinas_button.grid(row=0, column=0, pady=10, sticky='e')

        self.disciplinas_cadastradas_frame = ctk.CTkFrame(self)
        self.disciplinas_cadastradas_frame.grid(row=1, column=0, sticky='ew', pady=20)
        self.listar_disciplinas_cadastradas()

    def gera_campos_professor(self, frame):
        """
        Centraliza os campos necessários para cadastro/edição de um professor.
        """

        self.dict_areas_concentracao = {
            'CIÊNCIA AMBIENTAL': ['DESENVOLVIMENTO DE MÉTODOS E MATERIAIS PARA O CONTROLE AMBIENTAL',
                                  'MONITORAMENTO FÍSICO, QUÍMICO E BIOLÓGICO PARA O ESTUDO DE IMPACTOS AMBIENTAIS'],
            'TECNOLOGIA AMBIENTAL': ['TECNOLOGIAS LIMPAS NA PRODUÇÃO E NA TRANSFORMAÇÃO DE MATERIAIS',
                                     'POTENCIAL TECNOLÓGICO DE MATÉRIAS-PRIMAS E DE RESÍDUOS AGROINDUSTRIAIS']
        }

        self.nome_professor_label = ctk.CTkLabel(frame, text="Nome do Professor").grid(row=0, column=0, padx=5,
                                                                                       pady=10)
        self.nome_professor_entry = ctk.CTkEntry(frame)
        self.nome_professor_entry.grid(row=0, column=1, padx=5, pady=10)

        self.area_concentracao_professor_label = ctk.CTkLabel(frame, text="Área de Concentração").grid(row=1,
                                                                                                       column=0,
                                                                                                       padx=5,
                                                                                                       pady=5)
        self.area_concentracao_var = ctk.StringVar(value="Selecione")
        self.area_concentracao_professor_dropdown = ctk.CTkOptionMenu(frame, values=list(
            self.dict_areas_concentracao.keys()), variable=self.area_concentracao_var, command=lambda
            valor: self.atualizar_dropdown_linhas_pesquisa())
        self.area_concentracao_professor_dropdown.grid(row=1, column=1, padx=5, pady=10)

        self.linha_pesquisa_professor_label = ctk.CTkLabel(frame, text="Linha de Pesquisa").grid(row=2, column=0,
                                                                                                 padx=5, pady=5)
        frame_aux_linha = ctk.CTkFrame(frame, width=350, height=30)
        frame_aux_linha.grid(row=2, column=1, padx=5, pady=10, sticky='ew')
        frame_aux_linha.grid_propagate(False)
        self.linha_pesquisa_var = ctk.StringVar(value="Selecione")
        self.linha_pesquisa_professor_dropdown = ctk.CTkOptionMenu(frame_aux_linha, values=[],
                                                                   variable=self.linha_pesquisa_var,
                                                                   font=("Segoe UI", 10))
        self.linha_pesquisa_professor_dropdown.grid(row=0, column=0, sticky='ew')
        # self.linha_pesquisa_professor_dropdown.grid(row=2, column=1, padx=5, pady=10)

        # frame.after(100, lambda: self.linha_pesquisa_professor_dropdown.configure(width=150))

        return 3  # linha atual do grid

    def listar_disciplinas_cadastradas(self):

        disciplinas = DisciplinaController.listar_todos()[0]

        # Limpa conteúdo anterior
        for widget in self.disciplinas_cadastradas_frame.winfo_children():
            widget.destroy()

        # =========================
        # CONFIGURAÇÃO DAS COLUNAS (UMA ÚNICA VEZ)
        # =========================
        self.disciplinas_cadastradas_frame.grid_columnconfigure(0, minsize=50)  # ID
        self.disciplinas_cadastradas_frame.grid_columnconfigure(1, weight=3)  # Nome
        self.disciplinas_cadastradas_frame.grid_columnconfigure(2, minsize=120)  # Carga Horária
        self.disciplinas_cadastradas_frame.grid_columnconfigure(3, minsize=100)  # Créditos

        headers = ["ID", "Nome", "Carga-Horária", "Créditos"]

        # =========================
        # HEADER (linha 0)
        # =========================
        for col, header in enumerate(headers):
            ctk.CTkLabel(
                self.disciplinas_cadastradas_frame,
                text=header,
                text_color="white",
                font=("Arial", 14, "bold"),
                fg_color="#4F6416"
            ).grid(row=0, column=col, padx=5, pady=8, sticky="ew")

        # =========================
        # REGISTROS
        # =========================
        for row_index, disciplina in enumerate(disciplinas, start=1):

            cor_fundo = ["transparent", "#E6E6E6"]

            for col_index, atr in enumerate(disciplina):
                atr = self.gerenciador.encurta_texto(atr, 75)

                ctk.CTkLabel(
                    self.disciplinas_cadastradas_frame,
                    text=atr,
                    fg_color=cor_fundo[row_index % 2],
                    anchor="center"
                ).grid(
                    row=row_index,
                    column=col_index,
                    padx=5,
                    pady=5,
                    sticky="ew"
                )

    def selecionar_csv(self):
        caminho = filedialog.askopenfilename(
            title="Selecione o relatório de discplinas do SCPG",
            filetypes=[("CSV", "*.csv")]
        )
        if caminho:
            return caminho
        else:
            return None

    def carregar_disciplinas(self):
        disciplinas = [] #lista de listas que armazenará apenas os atributos que interessam p/ o BD

        caminho_csv = self.selecionar_csv()

        if caminho_csv:
            self.resetar_disciplinas()  # apaga a base de dados atual p/ liberar o banco p/ os dados dos csv

        with open(caminho_csv, "r", encoding="utf-8") as relatorio_csv:
            relatorio_disciplinas = csv.reader(relatorio_csv, delimiter=";")
            for i, disciplina in enumerate(relatorio_disciplinas):
                if i != 0:
                    disciplina_reduzido = []
                    for i, attr in enumerate(disciplina):
                        if i in (2, 3, 4): # Nome, CH, créditos
                            disciplina_reduzido.append(attr)
                    #print("Disciplinas Reduzido: ", disciplina_reduzido)
                    disciplinas.append(disciplina_reduzido)

        for disciplina in disciplinas:
            print(disciplina)

            self.cadastrar_disciplina(disciplina)

        self.atualizar_listagem_disciplinas()

    def cadastrar_disciplina(self, disciplina):
        nome = disciplina[0]
        carga_horaria = disciplina[1]
        creditos = str(disciplina[2])

        result, msg = DisciplinaController.cadastrar(nome, carga_horaria, creditos)

        return result, msg

    def resetar_disciplinas(self):
        result, msg = DisciplinaController.deletar_todos()

        return result, msg

    def atualizar_listagem_disciplinas(self):
        # Atualiza lista de professores cadastrados
        for widget in self.disciplinas_cadastradas_frame.winfo_children():  # limpeza da tela
            widget.destroy()
        self.listar_disciplinas_cadastradas()  # Recria os frames com os registro do banco

    def spam_top_level(self, action, infos=None):
        self.top_level = ctk.CTkToplevel()
        width = 500 if action in ("cadastrar", "editar") else 300
        height = 300 if action in ("cadastrar", "editar") else 150
        # centralizar o popup
        x = (self.top_level.winfo_screenwidth() // 2) - (width // 2)
        y = (self.top_level.winfo_screenheight() // 2) - (height // 2)
        self.top_level.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        self.top_level.resizable(False, False)

        if action == "cadastrar":
            self.top_level.title('📝 Cadastrar Registro')
            self.top_level.columnconfigure(0, weight=1)
            self.top_level.columnconfigure(1, weight=1)

            def confirm_action():
                # chamada do método
                result, msg = self.cadastrar_professor()

                if result is True:
                    self.top_level.destroy()
                else:
                    self.gerenciador.spam_warning(msg)

            line = self.gera_campos_professor(self.top_level)

            buttons_frame = ctk.CTkFrame(self.top_level)
            buttons_frame.grid(row=line, column=0, pady=50, columnspan=2)
            ok_button = ctk.CTkButton(buttons_frame, text="OK", width=80, command=confirm_action)
            ok_button.grid(row=0, column=0, padx=5)

            cancel_button = ctk.CTkButton(buttons_frame, text="Cancelar", command=self.top_level.destroy, width=80)
            cancel_button.grid(row=0, column=1, padx=5)

        elif action == "editar":
            self.top_level.title('📝 Editar Registro')
            self.top_level.columnconfigure(0, weight=1)
            self.top_level.columnconfigure(1, weight=1)

            def confirm_action():
                # captura dos dados atualizados
                nome = self.nome_professor_entry.get()
                area = self.area_concentracao_var.get()
                linha = self.linha_pesquisa_var.get()

                # chamada do método
                result, msg = self.editar_professor(infos['id'], nome, area, linha)

                if result is True:
                    self.top_level.destroy()
                else:
                    self.gerenciador.spam_warning(msg)

            line = self.gera_campos_professor(self.top_level)

            buttons_frame = ctk.CTkFrame(self.top_level)
            buttons_frame.grid(row=line, column=0, pady=50, columnspan=2)
            ok_button = ctk.CTkButton(buttons_frame, text="OK", width=80, command=confirm_action)
            ok_button.grid(row=0, column=0, padx=5)

            cancel_button = ctk.CTkButton(buttons_frame, text="Cancelar", command=self.top_level.destroy, width=80)
            cancel_button.grid(row=0, column=1, padx=5)

            # inserção dos dados do professor selecionado nos campos
            self.nome_professor_entry.insert(0, infos['nome'])
            self.area_concentracao_var.set(infos['area'])
            self.atualizar_dropdown_linhas_pesquisa()
            self.linha_pesquisa_var.set(infos['linha'])

        else:
            self.top_level.title('⚠️ Atenção')
            self.top_level.columnconfigure(0, weight=1)
            self.top_level.columnconfigure(1, weight=1)

            def confirm_action():
                result, msg = self.excluir_professor(infos["id"])

                if result is True:
                    self.top_level.destroy()
                else:
                    self.gerenciador.spam_warning(msg)

            self.confirmacao_exclusao_label = ctk.CTkLabel(self.top_level,
                                                           text="Deseja mesmo excluir o item selecionado?")
            self.confirmacao_exclusao_label.grid(row=0, column=0, pady=10, columnspan=2)
            ok_button = ctk.CTkButton(self.top_level, text="Excluir", command=confirm_action)
            ok_button.grid(row=1, column=0)

            cancel_button = ctk.CTkButton(self.top_level, text="Cancelar", command=self.top_level.destroy)
            cancel_button.grid(row=1, column=1)
        self.top_level.grab_set()