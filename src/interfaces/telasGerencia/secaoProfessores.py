import customtkinter as ctk
from src.controladores.controladorProfessor import ProfessorController
from functools import partial


class SecaoProfessores(ctk.CTkFrame):
    def __init__(self, master, gerenciador):
        super().__init__(master)
        self.gerenciador = gerenciador
        # self.grid_columnconfigure(0, weight=1)
        # self.grid_rowconfigure(0, weight=1)

        self.criar_widgets_professores()

    def criar_widgets_professores(self):
        self.grid_columnconfigure(0, weight=1)
        #self.grid_columnconfigure(1, weight=1)  # coluna do conteúdo (expande)
        self.grid_rowconfigure(1, weight=0)

        # =================
        # FRAME DINAMICO
        # =================
        # self.frame_dinamico = ctk.CTkScrollableFrame(self, fg_color="black")
        # self.frame_dinamico.grid(row=1, column=1, sticky='nsew')

        self.cadastrar_professor_button = ctk.CTkButton(self, text="➕ Adicionar Professor", text_color="white",
                                                        command=lambda: self.spam_top_level('cadastrar'), anchor='e')
        self.cadastrar_professor_button.grid(row=0, column=0, padx=(0, 5), pady=10, sticky='e')

        self.professores_cadastrados_frame = ctk.CTkFrame(self)
        self.professores_cadastrados_frame.grid_columnconfigure(0, weight=1)
        #self.professores_cadastrados_frame.grid_rowconfigure(0, weight=0)
        #self.professores_cadastrados_frame.grid_rowconfigure(1, weight=1)
        self.professores_cadastrados_frame.grid(row=1, column=0, sticky='ew', pady=20)
        self.listar_professores_cadastrados()

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

    def atualizar_dropdown_linhas_pesquisa(self):

        if self.area_concentracao_var.get() == 'Selecione':
            options = []
        elif self.area_concentracao_var.get() == 'CIÊNCIA AMBIENTAL':
            options = list(self.dict_areas_concentracao['CIÊNCIA AMBIENTAL'])
        else:
            options = list(self.dict_areas_concentracao['TECNOLOGIA AMBIENTAL'])

        self.linha_pesquisa_professor_dropdown.configure(values=options, width=150)
        self.linha_pesquisa_var.set("Selecione")

        # força atualização visual
        # self.linha_pesquisa_professor_dropdown.update_idletasks()

    def atualizar_listagem_professores(self):
        # Atualiza lista de professores cadastrados
        for widget in self.professores_cadastrados_frame.winfo_children():  # limpeza da tela
            widget.destroy()
        self.listar_professores_cadastrados()  # Recria os frames com os registro do banco

    def cadastrar_professor(self):
        nome = self.nome_professor_entry.get()
        area_concentracao = self.area_concentracao_var.get()
        linha_pesquisa = self.linha_pesquisa_var.get()

        result, msg = ProfessorController.cadastrar(nome, area_concentracao, linha_pesquisa)

        self.atualizar_listagem_professores()

        return result, msg

    # @staticmethod
    def excluir_professor(self, id):

        print('ID DO PROFESSOR', id)
        result, msg = ProfessorController.deletar(id)

        print("MENSAGEM: ", msg)

        self.atualizar_listagem_professores()

        return result, msg

    def editar_professor(self, id, nome=None, area=None, linha=None):

        result, msg = ProfessorController.atualizar(id, nome, area, linha)
        self.atualizar_listagem_professores()

        return result, msg

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

    def listar_professores_cadastrados(self):

        professores = ProfessorController.listar_todos()[0]

        # Limpa o conteúdo anterior (caso esteja recarregando)
        for widget in self.professores_cadastrados_frame.winfo_children():
            widget.destroy()

        # =========================
        # CONFIGURAÇÃO DAS COLUNAS (UMA ÚNICA VEZ)
        # =========================
        self.professores_cadastrados_frame.grid_columnconfigure(0, minsize=60)  # ID
        self.professores_cadastrados_frame.grid_columnconfigure(1, weight=2)  # Nome
        self.professores_cadastrados_frame.grid_columnconfigure(2, weight=2)  # Área
        self.professores_cadastrados_frame.grid_columnconfigure(3, weight=2)  # Linha
        self.professores_cadastrados_frame.grid_columnconfigure(4, minsize=120)  # Operações

        headers = ["ID", "Nome", "Área de Concentração", "Linha de Pesquisa", "Operações"]

        # =========================
        # HEADER (linha 0)
        # =========================
        for col, header in enumerate(headers):
            ctk.CTkLabel(
                self.professores_cadastrados_frame,
                text=header,
                text_color="white",
                font=("Arial", 14, "bold"),
                fg_color="#4F6416"
                #anchor="w"
            ).grid(row=0, column=col, padx=5, pady=8, sticky="ew")

        # =========================
        # REGISTROS
        # =========================
        for row_index, professor in enumerate(professores, start=1):
            cor_fundo = ["transparent", "#E6E6E6"]

            # Dados do professor
            for col_index, atr in enumerate(professor):
                atr = self.gerenciador.encurta_texto(atr, 35)

                ctk.CTkLabel(
                    self.professores_cadastrados_frame,
                    text=atr,
                    fg_color=cor_fundo[row_index % 2]
                    #anchor="center"
                ).grid(row=row_index, column=col_index, padx=5, pady=5, sticky="ew")

            # =========================
            # BOTÕES DE OPERAÇÃO
            # =========================
            operacoes_frame = ctk.CTkFrame(
                self.professores_cadastrados_frame,
                fg_color=cor_fundo[row_index % 2]
            )

            operacoes_frame.grid(row=row_index, column=4, sticky="e", padx=(0, 5))

            update_button = ctk.CTkButton(
                operacoes_frame,
                fg_color="orange",
                hover_color="dark orange",
                text='📝',
                width=30,
                command=partial(
                    self.spam_top_level,
                    "editar",
                    {
                        'id': professor[0],
                        'nome': professor[1],
                        'area': professor[2],
                        'linha': professor[3]
                    }
                )
            )
            update_button.grid(row=0, column=0, padx=5)

            delete_button = ctk.CTkButton(
                operacoes_frame,
                fg_color="red",
                hover_color="dark red",
                text='❌',
                width=30,
                command=partial(
                    self.spam_top_level,
                    "excluir",
                    {'id': professor[0]}
                )
            )
            delete_button.grid(row=0, column=1, padx=5)

    #def listar_professores_cadastrados(self):

        # professores = ProfessorController.listar_todos()[0]
        #
        # self.headers_professores_frame = ctk.CTkFrame(self.professores_cadastrados_frame)
        # #self.headers_professores_frame.grid_columnconfigure(0, weight=1)
        # self.headers_professores_frame.grid(row=0, column=0, sticky="ew")#, columnspan=1)
        # self.headers_professores_frame.grid_columnconfigure(0, minsize=50)  # ID
        # self.headers_professores_frame.grid_columnconfigure(1, minsize=200, weight=1)  # Nome
        # self.headers_professores_frame.grid_columnconfigure(2, minsize=200, weight=1)  # Área
        # self.headers_professores_frame.grid_columnconfigure(3, minsize=250, weight=1)
        #
        # headers = ["ID", "Nome", "Área de Concentração", "Linha de Pesquisa", "Operações"]
        #
        # tam_cols = [50, 150, 200, 250, 100]
        # qtde_headers = len(headers)
        #
        # # CONSTRÓI CABEÇALHO
        # for i, header in enumerate(headers):
        #     ctk.CTkLabel(self.headers_professores_frame, text=header, font=("Arial", 14, "bold"),
        #                  width=tam_cols[i]).grid(row=0, column=i, padx=5, pady=5, sticky='ew')
        #
        # # CONSTRÓI REGISTROS
        # # Loop p/ cada professor
        # for index, professor in enumerate(professores):
        #     id_professor = professor[0]
        #     nome_frame = f"frame_professor_{id_professor}"
        #
        #     self.professor_cadastrado_frame = ctk.CTkFrame(self.professores_cadastrados_frame)
        #     # print("Nome Frame: ", nome)
        #     self.professor_cadastrado_frame.grid(row=index + 1, column=0, pady=5, columnspan=1, sticky='ew')
        #
        #     self.professor_cadastrado_frame.grid_columnconfigure(0, minsize=50)  # ID
        #     self.professor_cadastrado_frame.grid_columnconfigure(1, minsize=200, weight=1)  # Nome
        #     self.professor_cadastrado_frame.grid_columnconfigure(2, minsize=200, weight=1)  # Área
        #     self.professor_cadastrado_frame.grid_columnconfigure(3, minsize=250, weight=1)  # Linha
        #     self.professor_cadastrado_frame.grid_columnconfigure(qtde_headers, weight=1)
        #
        #     # Loop p/ cada atributo
        #     for i, atr in enumerate(professor):
        #         atr = self.gerenciador.encurta_texto(atr, 25)
        #         ctk.CTkLabel(self.professor_cadastrado_frame, text=atr, width=tam_cols[i]).grid(row=0, column=i,
        #                                                                                         padx=5)
        #
        #     self.operacoes_frame = ctk.CTkFrame(self.professor_cadastrado_frame, fg_color='transparent')
        #     self.operacoes_frame.grid(row=0, column=qtde_headers, sticky='')
        #
        #     self.update_button = ctk.CTkButton(self.operacoes_frame, fg_color="orange", text='📝', width=30,
        #                                        command=partial(self.spam_top_level, "editar",
        #                                                        {'id': professor[0], 'nome': professor[1],
        #                                                         'area': professor[2], 'linha': professor[3]}))
        #     self.update_button.grid(row=0, column=0, padx=5)
        #     self.delete_button = ctk.CTkButton(self.operacoes_frame, fg_color="red", text='❌', width=30,
        #                                        command=partial(self.spam_top_level, "excluir", {'id': professor[
        #                                            0]}))  # partial(self.excluir_professor, professor[0]))
        #     # self.dict_frames_professores[self.delete_button.winfo_name()] = professor[0]
        #
        #     self.delete_button.grid(row=0, column=1, padx=5)



        # professores = ProfessorController.listar_todos()[0]
        #
        # # =========================
        # # FRAME DO HEADER
        # # =========================
        # self.headers_professores_frame = ctk.CTkFrame(self.professores_cadastrados_frame)
        # self.headers_professores_frame.grid(row=0, column=0, sticky="ew")
        #
        # # Configuração padronizada das colunas
        # def configurar_colunas(frame):
        #     frame.grid_columnconfigure(0, minsize=60)  # ID (fixo)
        #     frame.grid_columnconfigure(1, weight=2)  # Nome
        #     frame.grid_columnconfigure(2, weight=2)  # Área
        #     frame.grid_columnconfigure(3, weight=2)  # Linha
        #     frame.grid_columnconfigure(4, minsize=120)  # Operações (fixo)
        #
        # configurar_colunas(self.headers_professores_frame)
        #
        # headers = ["ID", "Nome", "Área de Concentração", "Linha de Pesquisa", "Operações"]
        #
        # # Construção do cabeçalho
        # for i, header in enumerate(headers):
        #     ctk.CTkLabel(
        #         self.headers_professores_frame,
        #         text=header,
        #         font=("Arial", 14, "bold")#,
        #         #anchor = "w"
        #     ).grid(row=0, column=i, padx=5, pady=5, sticky="ew")
        #
        # # =========================
        # # CONSTRUÇÃO DOS REGISTROS
        # # =========================
        # for index, professor in enumerate(professores):
        #
        #     self.professor_cadastrado_frame = ctk.CTkFrame(self.professores_cadastrados_frame)
        #     self.professor_cadastrado_frame.grid(
        #         row=index + 1,
        #         column=0,
        #         pady=5,
        #         sticky="ew"
        #     )
        #
        #     configurar_colunas(self.professor_cadastrado_frame)
        #
        #     # Dados do professor
        #     for i, atr in enumerate(professor):
        #         atr = self.gerenciador.encurta_texto(atr, 25)
        #
        #         ctk.CTkLabel(
        #             self.professor_cadastrado_frame,
        #             text=atr#,
        #             #anchor = "w"
        #         ).grid(row=0, column=i, padx=5, sticky="ew")
        #
        #     # =========================
        #     # OPERAÇÕES
        #     # =========================
        #     self.operacoes_frame = ctk.CTkFrame(
        #         self.professor_cadastrado_frame,
        #         fg_color="transparent"
        #     )
        #
        #     self.operacoes_frame.grid(row=0, column=4, sticky="e", padx=(0, 5))
        #
        #     self.update_button = ctk.CTkButton(
        #         self.operacoes_frame,
        #         fg_color="orange",
        #         text='📝',
        #         width=30,
        #         command=partial(
        #             self.spam_top_level,
        #             "editar",
        #             {
        #                 'id': professor[0],
        #                 'nome': professor[1],
        #                 'area': professor[2],
        #                 'linha': professor[3]
        #             }
        #         )
        #     )
        #     self.update_button.grid(row=0, column=0, padx=5)
        #
        #     self.delete_button = ctk.CTkButton(
        #         self.operacoes_frame,
        #         fg_color="red",
        #         text='❌',
        #         width=30,
        #         command=partial(
        #             self.spam_top_level,
        #             "excluir",
        #             {'id': professor[0]}
        #         )
        #     )
        #     self.delete_button.grid(row=0, column=1, padx=5)
