import customtkinter as ctk
from src.controladores.controladorCoordenador import CoordenadorController
from functools import partial
from PIL import Image

class SecaoCoordenadores(ctk.CTkFrame):
    def __init__(self, master, gerenciador):
        super().__init__(master)
        self.gerenciador = gerenciador

        self.criar_widgets_coordenadores()

    def criar_widgets_coordenadores(self):
        self.grid_columnconfigure(0, weight=1)
        #self.grid_columnconfigure(1, weight=1)  # coluna do conteúdo (expande)
        self.grid_rowconfigure(2, weight=0)

        # =================
        # FRAME DINAMICO
        # =================

        self.cadastrar_coordenador_button = ctk.CTkButton(self, text="➕ Adicionar Coordenador", text_color="white",
                                                          command=lambda: self.spam_top_level('cadastrar'))
        self.cadastrar_coordenador_button.grid(row=0, column=0, pady=10, padx=5, sticky='e')

        self.coordenadores_ativos_frame = ctk.CTkFrame(self, fg_color='transparent')
        self.coordenadores_ativos_frame.grid(row=1, column=0, pady=10)
        self.listar_coordenadores_ativos()

        self.coordenadores_cadastrados_frame = ctk.CTkFrame(self)
        self.coordenadores_cadastrados_frame.grid(row=2, column=0, sticky='ew', pady=20)
        self.listar_coordenadores_cadastrados()

    def gera_campos_coordenador(self, frame):
        """
        Centraliza os campos necessários para cadastro/edição de um coordenador.
        """

        # Configurar as colunas para expansão simétrica
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_columnconfigure(1, weight=1)

        # Nome do Coordenador
        self.nome_coordenador_label = ctk.CTkLabel(frame, text="Nome do Coordenador", font=ctk.CTkFont(weight="bold"))
        self.nome_coordenador_label.grid(row=0, column=0, padx=(5, 5), pady=10, sticky="e")

        self.nome_coordenador_entry = ctk.CTkEntry(frame, width=150)
        self.nome_coordenador_entry.grid(row=0, column=1, padx=(5, 5), pady=10, sticky="w")

        # Modalidade
        self.modalidade_label = ctk.CTkLabel(frame, text="Modalidade", font=ctk.CTkFont(weight="bold"))
        self.modalidade_label.grid(row=1, column=0, padx=(5, 5), pady=5, sticky="e")

        self.modalidade_var = ctk.StringVar(value="Selecione")
        self.modalidade_dropdown = ctk.CTkOptionMenu(frame, values=['Coordenador Titular', 'Vice-Coordenador'], width=150,
                                                     variable=self.modalidade_var)
        self.modalidade_dropdown.grid(row=1, column=1, padx=(5, 5), pady=10, sticky="w")

        # Início da Vigência
        self.inicio_vigencia_label = ctk.CTkLabel(frame, text="Início do Mandato",
                                                  font=ctk.CTkFont(weight="bold"))
        self.inicio_vigencia_label.grid(row=2, column=0, padx=(5, 5), pady=5, sticky="e")

        self.inicio_vigencia_entry = ctk.CTkEntry(frame, placeholder_text='DD/MM/AAAA', width=150)
        self.inicio_vigencia_entry.grid(row=2, column=1, padx=(5, 5), pady=10, sticky="w")

        # Fim da Vigência
        self.fim_vigencia_label = ctk.CTkLabel(frame, text="Fim do Mandato",
                                               font=ctk.CTkFont(weight="bold"))
        self.fim_vigencia_label.grid(row=3, column=0, padx=(5, 5), pady=5, sticky="e")

        self.fim_vigencia_entry = ctk.CTkEntry(frame, placeholder_text='DD/MM/AAAA', width=150)
        self.fim_vigencia_entry.grid(row=3, column=1, padx=(5, 5), pady=10, sticky="w")

        return 4  # linha atual do grid

    def listar_coordenadores_cadastrados(self):

        coordenadores = CoordenadorController.listar_todos()[0]

        # Limpa conteúdo anterior
        for widget in self.coordenadores_cadastrados_frame.winfo_children():
            widget.destroy()

        # =========================
        # CONFIGURAÇÃO DAS COLUNAS
        # =========================
        self.coordenadores_cadastrados_frame.grid_columnconfigure(0, minsize=50)  # ID
        self.coordenadores_cadastrados_frame.grid_columnconfigure(1, weight=2)  # Nome
        self.coordenadores_cadastrados_frame.grid_columnconfigure(2, weight=2)  # Modalidade
        self.coordenadores_cadastrados_frame.grid_columnconfigure(3, minsize=150)  # Início
        self.coordenadores_cadastrados_frame.grid_columnconfigure(4, minsize=150)  # Fim
        self.coordenadores_cadastrados_frame.grid_columnconfigure(5, minsize=120)  # Operações

        headers = [
            "ID",
            "Nome",
            "Modalidade",
            "Início Vigência",
            "Fim Vigência",
            "Operações"
        ]

        # =========================
        # HEADER (linha 0)
        # =========================
        for col, header in enumerate(headers):
            ctk.CTkLabel(
                self.coordenadores_cadastrados_frame,
                text=header,
                text_color="white",
                font=("Arial", 14, "bold"),
                fg_color="#4F6416"
            ).grid(row=0, column=col, padx=5, pady=8, sticky="ew")

        # =========================
        # REGISTROS
        # =========================
        for row_index, coordenador in enumerate(coordenadores, start=1):

            cor_fundo = ["transparent", "#E6E6E6"]

            # Dados do coordenador
            for col_index, atr in enumerate(coordenador):
                atr = self.gerenciador.encurta_texto(atr, 25)

                ctk.CTkLabel(
                    self.coordenadores_cadastrados_frame,
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

            # =========================
            # OPERAÇÕES
            # =========================
            operacoes_frame = ctk.CTkFrame(
                self.coordenadores_cadastrados_frame,
                fg_color=cor_fundo[row_index % 2]
            )

            operacoes_frame.grid(row=row_index, column=5, sticky="e", padx=(0, 5))

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
                        'id': coordenador[0],
                        'nome': coordenador[1],
                        'modalidade': coordenador[2],
                        'inicio_vigencia': coordenador[3],
                        'fim_vigencia': coordenador[4]
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
                    {'id': coordenador[0]}
                )
            )
            delete_button.grid(row=0, column=1, padx=5)

    def listar_coordenadores_ativos(self):

        # Limpa conteúdo anterior
        for widget in self.coordenadores_ativos_frame.winfo_children():
            widget.destroy()

        coordenadores = CoordenadorController.listar_ativos()

        dict_coordenadores = {}

        for coordenador in coordenadores:
            if coordenador[2] == 'Coordenador Titular':
                dict_coordenadores['titular'] = coordenador[1]
            else:
                dict_coordenadores['vice'] = coordenador[1]

        # =========================
        # CARD PRINCIPAL
        # =========================
        card = ctk.CTkFrame(
            self.coordenadores_ativos_frame,
            corner_radius=15,
            fg_color="#F4F6FB",
            border_width=3,
            border_color="#4F6416"
        )
        card.pack(fill="both", expand=True, padx=7, pady=7)

        # =========================
        # HEADER DO CARD
        # =========================
        header_frame = ctk.CTkFrame(card, fg_color="transparent")
        header_frame.pack(fill="x", pady=(15, 10))

        icon = ctk.CTkImage(
            light_image=Image.open('./src/static/img/active_icon.png'),
            dark_image=Image.open('./src/static/img/active_icon.png'),
            size=(28, 28)
        )

        icon_label = ctk.CTkLabel(
            header_frame,
            image=icon,
            text=""
        )
        icon_label.pack(side="left", padx=(15, 10))

        titulo_label = ctk.CTkLabel(
            header_frame,
            text="Coordenadores Ativos",
            font=("Segoe UI", 20, "bold"),
            text_color="#1F2A44"
        )
        titulo_label.pack(side="left")

        # Linha divisória
        divider = ctk.CTkFrame(card, height=2, fg_color="#DADDE5")
        divider.pack(fill="x", padx=15, pady=(0, 15))

        # =========================
        # CONTEÚDO
        # =========================
        content_frame = ctk.CTkFrame(card, fg_color="transparent")
        content_frame.pack(fill="both", expand=True, padx=20, pady=10)

        content_frame.grid_columnconfigure(0, weight=1)
        content_frame.grid_columnconfigure(1, weight=1)

        # ---- TITULAR ----
        titular_nome = dict_coordenadores.get(
            'titular',
            'Nenhum Coordenador Titular Ativo'
        )

        titular_card = ctk.CTkFrame(
            content_frame,
            corner_radius=10,
            fg_color="white"
        )
        titular_card.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        ctk.CTkLabel(
            titular_card,
            text="Coordenador Titular",
            font=("Segoe UI", 14, "bold"),
            text_color="#749619"
        ).pack(pady=(15, 5))

        ctk.CTkLabel(
            titular_card,
            text=titular_nome,
            font=("Segoe UI", 16),
            wraplength=250,
            justify="center"
        ).pack(pady=(0, 15))

        # ---- VICE ----
        vice_nome = dict_coordenadores.get(
            'vice',
            'Nenhum Vice-Coordenador Ativo'
        )

        vice_card = ctk.CTkFrame(
            content_frame,
            corner_radius=10,
            fg_color="white"
        )
        vice_card.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        ctk.CTkLabel(
            vice_card,
            text="Vice-Coordenador",
            font=("Segoe UI", 14, "bold"),
            text_color="#6C757D"
        ).pack(pady=(15, 5))

        ctk.CTkLabel(
            vice_card,
            text=vice_nome,
            font=("Segoe UI", 16),
            wraplength=250,
            justify="center"
        ).pack(pady=(0, 15))

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
                result, msg = self.cadastrar_coordenador()
                if result is True:
                    self.top_level.destroy()
                else:
                    self.gerenciador.spam_warning(msg)

            line = self.gera_campos_coordenador(self.top_level)

            buttons_frame = ctk.CTkFrame(self.top_level)
            buttons_frame.grid(row=line, column=0, pady=50, columnspan=2)
            ok_button = ctk.CTkButton(buttons_frame, text="OK", width=80, height=35, font=ctk.CTkFont(weight="bold", size=16), text_color="white", border_width=1, border_color="black", command=confirm_action)
            ok_button.grid(row=0, column=0, padx=5)

            cancel_button = ctk.CTkButton(buttons_frame, text="Cancelar", height=35, font=ctk.CTkFont(weight="bold", size=16), text_color="white", border_width=1, border_color="black", command=self.top_level.destroy, width=80)
            cancel_button.grid(row=0, column=1, padx=5)

        elif action == "editar":
            self.top_level.title('📝 Editar Registro')
            self.top_level.columnconfigure(0, weight=1)
            self.top_level.columnconfigure(1, weight=1)

            def confirm_action():
                # captura dos dados atualizados
                nome = self.nome_coordenador_entry.get()
                modalidade = self.modalidade_var.get()
                inicio_vigencia = self.inicio_vigencia_entry.get()
                fim_vigencia = self.fim_vigencia_entry.get()

                # chamada do método
                result, msg = self.editar_coordenador(infos['id'], nome, modalidade, inicio_vigencia, fim_vigencia)

                if result is True:
                    self.top_level.destroy()
                else:
                    self.gerenciador.spam_warning(msg)


            line = self.gera_campos_coordenador(self.top_level)

            buttons_frame = ctk.CTkFrame(self.top_level)
            buttons_frame.grid(row=line, column=0, pady=50, columnspan=2)
            ok_button = ctk.CTkButton(buttons_frame, text="OK", width=80, height=35, font=ctk.CTkFont(weight="bold", size=16), text_color="white", border_width=1, border_color="black", command=confirm_action)
            ok_button.grid(row=0, column=0, padx=5)

            cancel_button = ctk.CTkButton(buttons_frame, text="Cancelar",  width=80, height=35, font=ctk.CTkFont(weight="bold", size=16), text_color="white", border_width=1, border_color="black", command=self.top_level.destroy)
            cancel_button.grid(row=0, column=1, padx=5)

            # inserção dos dados do professor selecionado nos campos
            self.nome_coordenador_entry.insert(0, infos['nome'])
            self.modalidade_var.set(infos['modalidade'])
            self.inicio_vigencia_entry.insert(0, infos['inicio_vigencia'])
            self.fim_vigencia_entry.insert(0, infos['fim_vigencia'])

        else:
            self.top_level.title('⚠️ Atenção')
            self.top_level.columnconfigure(0, weight=1)
            self.top_level.columnconfigure(1, weight=1)

            def confirm_action():
                result, msg = self.excluir_coordenador(infos["id"])

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


    def atualizar_listagem_coordenadores(self):
        # Atualiza lista de coordenadores cadastrados
        for widget in self.coordenadores_cadastrados_frame.winfo_children():  # limpeza da tela
            widget.destroy()
        self.listar_coordenadores_cadastrados()  # Recria os frames com os registro do banco

    def atualizar_listagem_coordenadores_ativos(self):
        for widget in self.coordenadores_ativos_frame.winfo_children():  # limpeza da tela
            widget.destroy()
        self.listar_coordenadores_ativos()

    def cadastrar_coordenador(self):
        nome = self.nome_coordenador_entry.get()
        modalidade = self.modalidade_var.get()
        inicio_vigencia = self.inicio_vigencia_entry.get()
        fim_vigencia = self.fim_vigencia_entry.get()

        result, msg = CoordenadorController.cadastrar(nome, modalidade, inicio_vigencia, fim_vigencia)

        print(msg)

        self.atualizar_listagem_coordenadores()
        self.atualizar_listagem_coordenadores_ativos()

        return result, msg

    # @staticmethod
    def excluir_coordenador(self, id):

        result, msg = CoordenadorController.deletar(id)

        if result is False:
            self.gerenciador.spam_warning(msg, self.top_level)

        print("MENSAGEM: ", msg)

        self.atualizar_listagem_coordenadores()
        self.atualizar_listagem_coordenadores_ativos()

        return result, msg

    def editar_coordenador(self, id, nome=None, modalidade=None, inicio_vigencia=None, fim_vigencia=None):

        result, msg = CoordenadorController.atualizar(id, nome, modalidade, inicio_vigencia, fim_vigencia)
        self.atualizar_listagem_coordenadores()
        self.atualizar_listagem_coordenadores_ativos()


        return result, msg