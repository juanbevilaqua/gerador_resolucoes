import customtkinter as ctk
from functools import partial
from src.controladores.controladorProfessor import ProfessorController
from interfaces.telasGerencia.secaoProfessores import SecaoProfessores
from interfaces.telasGerencia.secaoCoordenadores import SecaoCoordenadores
from interfaces.telasGerencia.secaoDisciplinas import SecaoDisciplinas


class TelaGerencia(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        #self.master.geometry("1920x1080")
        self.master.state("zoomed")
        self.dict_frames_professores = {} # dicionário que vincular o frame de um professor ao seu ID

        self.secao_atual = None
        self.frame_dinamico = None
        self.criar_widgets()


    def criar_widgets(self):
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)  # coluna do conteúdo (expande)
        self.grid_rowconfigure(1, weight=1)

        # =================
        # CABEÇALHO DA TELA DE GERÊNCIA
        # =================
        self.cabecalho_frame = ctk.CTkFrame(self)
        self.cabecalho_frame.grid_columnconfigure(0, weight=0)
        self.cabecalho_frame.grid_columnconfigure(1, weight=1)
        self.cabecalho_frame.grid_columnconfigure(2, weight=0)
        self.cabecalho_frame.grid(row=0, column=0, columnspan=2, sticky='ew')

        self.voltar_button = ctk.CTkButton(self.cabecalho_frame, text="⬅️", width=30,
                                           command=self.master.exibir_tela_inicial).grid(row=0, column=0, pady=10,
                                                                                         padx=15)
        self.titulo_tela_label = ctk.CTkLabel(self.cabecalho_frame, text="GERÊNCIA DO SISTEMA").grid(
            row=0, column=1, pady=10, sticky='ew')
        self.placeholder = ctk.CTkLabel(self.cabecalho_frame, text="", width=30)
        self.placeholder.grid(row=0, column=2, padx=5)

        # =================
        # MENU LATERAL DE CONFIGURAÇÕES
        # =================
        self.menu_config_frame = ctk.CTkFrame(self, fg_color="#4F6416")
        self.menu_config_frame.grid(row=1, column=0, sticky='nsw')

        self.op_professores_button = ctk.CTkButton(self.menu_config_frame, text="Professores", width=60, command=lambda: self.alterar_secao('professores'))
        self.op_professores_button.grid(row=0, column=0, pady=5)
        self.op_disciplinas_button = ctk.CTkButton(self.menu_config_frame, text="Disciplinas", width=60, command= lambda: self.alterar_secao('disciplinas')).grid(row=1, column=0,
                                                                                                    pady=5)
        self.op_coordenadores_button = ctk.CTkButton(self.menu_config_frame, text="Coordenadores", width=60, command=lambda: self.alterar_secao('coordenadores'))
        self.op_coordenadores_button.grid(row=2, column=0,
                                                                                                    pady=5)

        # =================
        # FRAME DINAMICO
        # =================
        self.frame_dinamico = ctk.CTkScrollableFrame(self)
        self.frame_dinamico.grid_columnconfigure(0, weight=1)
        self.frame_dinamico.grid_rowconfigure(0, weight=1)

        self.frame_dinamico.grid(row=1, column=1, sticky='nsew')

        self.alterar_secao('professores') # a Tela de gerência exibe por padrão a secao de professores

    def alterar_secao(self, secao):
        if self.secao_atual:
            self.secao_atual.destroy()

        if secao == 'professores':
            self.secao_atual = SecaoProfessores(self.frame_dinamico, gerenciador=self)
        elif secao == 'disciplinas':
            self.secao_atual = SecaoDisciplinas(self.frame_dinamico, gerenciador=self)
        elif secao == 'coordenadores':
            self.secao_atual = SecaoCoordenadores(self.frame_dinamico, gerenciador=self)


        self.secao_atual.grid(row=0, column=0, sticky="nsew")


    @staticmethod
    def encurta_texto(atr, limite):
        """
        Adiciona '...' ao final das strings que ultrapassam o limite estabelecido
        """
        tam = len(str(atr))

        if tam <= limite:
            return atr
        else:
            atr_reduzido = atr[:limite]
            atr_reduzido = f"{atr_reduzido}..."

            return atr_reduzido

    def spam_warning(self, msg):
        self.warning_top_level = ctk.CTkToplevel()
        width = 300
        height = 150
        # centralizar o popup
        x = (self.warning_top_level.winfo_screenwidth() // 2) - (width // 2)
        y = (self.warning_top_level.winfo_screenheight() // 2) - (height // 2)
        self.warning_top_level.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        self.warning_top_level.resizable(False, False)

        self.warning_top_level.title('⚠️ Atenção')
        self.warning_top_level.columnconfigure(0, weight=1)
        self.warning_top_level.columnconfigure(1, weight=1)

        self.msg_label = ctk.CTkLabel(self.warning_top_level,
                                                       text=msg, wraplength=300)
        self.msg_label.grid(row=0, column=0, pady=30)

        ok_button = ctk.CTkButton(self.warning_top_level, text="OK", command=self.warning_top_level.destroy)
        ok_button.grid(row=1, column=0)

        self.warning_top_level.grab_set()


