import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog, END, ACTIVE
from collections import defaultdict
from src import modelos
import yaml
from src.controladores import controladorProfessor, controladorDisciplina
import os
#NOVO
class TelaPrincipal(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        #self.janela = ctk.CTk()
        #self.janela.title("Gerador de Resoluções")
        #self.janela.geometry("950x750")
        #self.janela.resizable(width=False, height=False)

        self.tipos_resolucao = {
            "Adiamento de Reunião": "AdiamentoReuniao", "Afastamento de Discente": "Afastamento",
            "Aprovação de Banca": "AprovacaoBanca", "Aproveitamento de Suficiência": "AproveitamentoSuficiencia",
            "Calendário de Reuniões": "CalendarioReunioes", "Cancelamento de Oferta de Disciplina": "CancelamentoOfertaDisciplina",
            "Cancelamento de Matrícula": "CancelamentoMatricula",
            "Cancelamento de Orientação": "CancelamentoOrientacao", "Composição de Comissão": "ComposicaoDeComissao",
            "Contratação de Professor Visitante": "ContratacaoProfessorVisitante",
            "Convalidação de Suficiência": "ConvalidacaoSuficiencia", "Credenciamento de Docente": "CredenciamentoDocente",
            "Descredenciamento de Docente": "DescredenciamentoDocente",
            "Desligamento de Discente": "Desligamento", "Homologação de Ad Referendum": "HomologacaoAdReferendum",
            "Inclusão de Coorientação": "InclusaoCoorientacao", "Licença Maternidade": "LicencaMaternidade",
            "Número de Vagas Para Processo Seletivo": "NumeroVagasPS", "Relatório de Professor Visitante": "RelatorioProfessorVisitante",
            "Prorrogação de Qualificação": "ProrrogacaoQualificacao",
            "Trancamento de Curso": "Trancamento", "Troca de Orientação": "TrocaOrientacao",
            "Troca de Projeto de Pesquisa": "TrocaProjetoPesq"
            }

        self.professores_cadastrados = controladorProfessor.ProfessorController.listar_nomes()[0] # primeiro elemento retornado (nomes)
        self.disciplinas_cadastradas = controladorDisciplina.DisciplinaController.listar_nomes()[0]
        print(self.professores_cadastrados)
        print(self.disciplinas_cadastradas)

        self.campos_dinamicos = {}  # dicionário para campos criados dinamicamente
        self.menu_config_avancadas_opened = False
        self.frame_fixo_opened = True
        self.campos_configs_avancadas = {}
        self.list_divs = []
        self.criar_widgets()

        self.cont_entry_button = 0
        self.cont_entry_for_duplicate = 0
        self.cont_entry_button_aux = 0 # utilizado p/ modelos nos estilo "Cancelamento de Matrícula"
        self.button_add = None # variavel para controle do entry_button(guarda a referencia do último botao criado para não haver repetição)

    def criar_widgets(self):
        self.grid_columnconfigure(0, weight=1)  # .janela

        # =================
        # CABEÇALHO DA TELA PRINCIPAL
        # =================
        self.cabecalho_frame = ctk.CTkFrame(self)
        self.cabecalho_frame.grid_columnconfigure(0, weight=0)
        self.cabecalho_frame.grid_columnconfigure(1, weight=1)
        self.cabecalho_frame.grid_columnconfigure(2, weight=0)
        self.cabecalho_frame.grid(row=0, column=0, sticky='ew')

        self.voltar_button = ctk.CTkButton(self.cabecalho_frame, text="⬅️", width=30, command=self.master.exibir_tela_inicial).grid(row=0, column=0, pady=10, padx=15)
        self.titulo_tela_label = ctk.CTkLabel(self.cabecalho_frame, text="TELA PRINCIPAL - CRIAR RESOLUÇÕES").grid(row=0, column=1, pady=10, sticky='ew')
        self.placeholder = ctk.CTkLabel(self.cabecalho_frame, text="", width=30)
        self.placeholder.grid(row=0, column=2, padx=5)


        # =================
        # FRAME FIXO
        # =================
        self.frame_fixo = ctk.CTkFrame(self)  # .janela
        # self.frame_fixo.pack(pady=20)
        self.frame_fixo.grid(row=1, column=0, pady=20)
        self.frame_fixo.grid_columnconfigure(0, weight=1)
        self.frame_fixo.grid_columnconfigure(1, weight=1)

        ctk.CTkLabel(self.frame_fixo, text="Nº da Resolução").grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.numero_res_entry = ctk.CTkEntry(self.frame_fixo, width=200)
        self.numero_res_entry.grid(row=0, column=1, pady=10, sticky="w")

        ctk.CTkLabel(self.frame_fixo, text="Data da Resolução").grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.data_res_entry = ctk.CTkEntry(self.frame_fixo, width=200, placeholder_text="dd/mm/aaaa")
        self.data_res_entry.grid(row=1, column=1, pady=10, sticky="w")

        default_colors_data_reuniao = {}
        self.data_reuniao_label = ctk.CTkLabel(self.frame_fixo, text="Data da Reunião")
        self.data_reuniao_label.grid(row=2, column=0, padx=10, pady=10, sticky="e")
        default_colors_data_reuniao["label"] = self.data_reuniao_label.cget("text_color")#armazena a cor padrão do label
        #default_colors_data_reuniao.append(default_color)
        self.data_reuniao_entry = ctk.CTkEntry(self.frame_fixo, width=200, placeholder_text="dd/mm/aaaa")
        self.data_reuniao_entry.grid(row=2, column=1, pady=10, sticky="w")
        default_colors_data_reuniao["entry"] = self.data_reuniao_entry.cget("fg_color")#armazena a cor padrão do entry
        #default_colors_data_reuniao.append(default_color)

        # Checkbox Ad Referendum
        self.ad_referendum_var = ctk.BooleanVar(value=False)
        self.ad_referendum_checkbox = ctk.CTkCheckBox(
            self.frame_fixo,
            text="Ad Referendum",
            variable=self.ad_referendum_var,
            command = lambda: self.alternar_ativacao_dos_campos(False, self.ad_referendum_checkbox, [self.data_reuniao_label, self.data_reuniao_entry], default_colors_data_reuniao)
        )
        self.ad_referendum_checkbox.grid(row=3, column=1, pady=10, sticky="w")

        # -----------------
        # Menu de Config. Avançadas
        # -----------------
        self.config_avancadas_frame = ctk.CTkFrame(self.frame_fixo)
        self.config_avancadas_frame.grid_columnconfigure(0, weight=1)
        self.config_avancadas_frame.grid_columnconfigure(1, weight=1)
        self.config_avancadas_frame.grid_columnconfigure(2, weight=1)

        #self.frame_fixo.grid_columnconfigure(0, weight=1)
        self.config_avancadas_button = ctk.CTkButton(self.frame_fixo, text="⚙️ Config. Avançadas ▶", fg_color="transparent", border_width=2, command=lambda: self.alternar_abertura_menu_config_avancadas())
        self.config_avancadas_button.grid(row=4, column=0, columnspan=2, pady=10)

        self.estruturar_menu_config_avancadas()

        self.guardar_dados_fixos_button = ctk.CTkButton(self.frame_fixo, text="✅ Guardar", command=lambda: self.alternar_abertura_frame_fixo())
        self.guardar_dados_fixos_button.grid(row=6, column=0, columnspan=2, pady=10)

        # =================
        # BARRA DE PESQUISA(TIPOS DE RESOLUÇÃO)
        # =================
        self.frame_pesquisa_resolucao = ctk.CTkFrame(self)#.janela
        #self.frame_pesquisa_resolucao.pack(pady=10)
        self.frame_pesquisa_resolucao.grid(row=2, column=0, pady=10)
        self.frame_pesquisa_resolucao.grid_columnconfigure(0, weight=1)
        self.frame_pesquisa_resolucao.grid_columnconfigure(1, weight=1)
        ctk.CTkLabel(self.frame_pesquisa_resolucao, text="Tipo de Resolução").grid(row=0, column=0, columnspan=2)
        #self.tipos_resolucao_entry = tk.Entry(self.frame_pesquisa_resolucao, width=35, font=15)
        #self.tipo_var = ctk.StringVar()
        self.tipos_resolucao_entry = ctk.CTkEntry(self.frame_pesquisa_resolucao, height=40, width=275, font=('Segoe UI', 15), border_color="#0088E3", placeholder_text="Selecione o tipo de resolução")
        self.tipos_resolucao_entry.grid(row=1, column=0)

        self.carregar_modelo_resolucao_button = ctk.CTkButton(self.frame_pesquisa_resolucao, text="Carregar", height=40, width=30, command=self.check_tipo_res)
        self.carregar_modelo_resolucao_button.grid(row=1, column=1)

        self.tipos_resolucao_listbox = tk.Listbox(
            self.frame_pesquisa_resolucao,
            width=35,
            font=15,
            bg="#D4D7D9",  # fundo branco "#E6E8E8"
            fg="#333333",  # texto escuro, mas não preto
            selectbackground="#0078D7",
            selectforeground="#FFFFFF",  # texto branco quando selecionado
            highlightthickness=0,  # remove borda padrão
            relief="flat"
        )
        #self.tipos_resolucao_listbox.pack(pady=20)

        self.tipos_resolucao_entry.bind("<FocusIn>", lambda event: self.exibir_tipos_resolucao_listbox(True, event))
        self.tipos_resolucao_entry.bind("<FocusOut>", lambda event: self.exibir_tipos_resolucao_listbox(False, event))
        self.atualizar_listbox_resolucoes(self.tipos_resolucao.keys())
        self.tipos_resolucao_listbox.bind("<<ListboxSelect>>", self.preencher_tipos_resolucao_entry)
        self.tipos_resolucao_entry.bind("<KeyRelease>", self.filtrar_tipos_res)

        self.placeholder_active = True

        if hasattr(self, 'frame_dinamico'):
            self.frame_dinamico.destroy()

        # =================
        # FRAME DINÂMICO
        # =================
        self.frame_dinamico = ctk.CTkScrollableFrame(self, height=400)#.janela
        #self.frame_dinamico.pack(padx=20, pady=20, fill="x", expand=True)#, fill="both", expand=True
        self.frame_dinamico.grid(row=3, column=0, pady=20, sticky="ew")
        self.frame_dinamico.grid_rowconfigure(0, weight=0)  # frame central
        self.frame_dinamico.grid_rowconfigure(1, weight=1)  # linha dos frames esquerdo/direito
        self.frame_dinamico.grid_columnconfigure(0, weight=1)  # frame esquerdo
        self.frame_dinamico.grid_columnconfigure(1, weight=1)  # frame direito

        self.frame_dinamico.bind("<Button-1>", self.focar_frame_dinamico)

        # =================
        # BOTÃO GERAR RESOUÇÃO
        # =================
        # Desabilitado inicialmente
        self.botao_gerar = ctk.CTkButton(self, text="Gerar Resolução", command=self.gerar_resolucao)#.janela
        #self.botao_gerar.pack(pady=10)
        self.botao_gerar.grid(row=4, column=0)
        self.botao_gerar.configure(state="disabled")  # ativa só após escolher tipo

    def focar_frame_dinamico(self, event=None):
        self.frame_dinamico.focus_set()

    def exibir_tipos_resolucao_listbox(self, exibir, event):
        if exibir:
            self.tipos_resolucao_listbox.grid(row=2, column=0, columnspan=2)
        else:
            self.tipos_resolucao_listbox.grid_forget()
    def atualizar_listbox_resolucoes(self, lista_tipos_resolucoes):

        self.tipos_resolucao_listbox.delete(0, END)

        for tipo in lista_tipos_resolucoes:
            self.tipos_resolucao_listbox.insert(END, tipo)
    def preencher_tipos_resolucao_entry(self, event=None):
        self.after(10, self._atualizar_valor_entry(self.tipos_resolucao_listbox, self.tipos_resolucao_entry))#.janela

    #novo
    def _atualizar_valor_entry(self, listbox, entry): # listbox e entry
        selecao = listbox.curselection()

        if selecao:
            indice = selecao[0]
            valor = listbox.get(indice)
            entry.delete(0, END)
            entry.insert(0, valor)

    # def _atualizar_tipos_res_entry(self): # listbox e entry
    #     selecao = self.tipos_resolucao_listbox.curselection()
    #
    #     if selecao:
    #         indice = selecao[0]
    #         valor = self.tipos_resolucao_listbox.get(indice)
    #         self.tipos_resolucao_entry.delete(0, END)
    #         self.tipos_resolucao_entry.insert(0, valor)

    # reutilizar
    def filtrar_tipos_res(self, event=None):
        termo = self.tipos_resolucao_entry.get()

        if termo == "":
            data = self.tipos_resolucao.keys()
        else:
            data = []
            for tipo in self.tipos_resolucao.keys():
                if termo.lower() in tipo.lower():
                    data.append(tipo)

        self.atualizar_listbox_resolucoes(data)

    def gera_barra_pesq_professores(self, frame):
        frame_pesquisa_professor = ctk.CTkFrame(frame)
        #self.frame_pesquisa_professor.grid(row=row, column=0, pady=10)
        frame_pesquisa_professor.pack(pady=10)
        #self.frame_pesquisa_professor.grid_columnconfigure(0, weight=1)
        #self.frame_pesquisa_professor.grid_columnconfigure(1, weight=1)
        #ctk.CTkLabel(self.frame_pesquisa_professor, text="Tipo de Resolução").grid(row=0, column=0, columnspan=2)
        professores_entry = ctk.CTkEntry(frame_pesquisa_professor, height=30, width=200,
                                                  #font=('Segoe UI', 15), border_color="#0088E3",
                                                  placeholder_text="Digite o nome do professor")
        professores_entry.grid(row=0, column=0)

        professores_listbox = tk.Listbox(
            frame_pesquisa_professor,
            width=25,
            font=10,
            bg="#D4D7D9",  # fundo branco "#E6E8E8"
            fg="#333333",  # texto escuro, mas não preto
            selectbackground="#0078D7",
            selectforeground="#FFFFFF",  # texto branco quando selecionado
            highlightthickness=0,  # remove borda padrão
            relief="flat"
        )

        def exibir_professores_listbox(exibir, event):
            if exibir:
                professores_listbox.grid(row=1, column=0, columnspan=2)
            else:
                professores_listbox.grid_forget()

        def atualizar_listbox_professores(lista_professores):

            professores_listbox.delete(0, END)

            if len(lista_professores) > 0:
                for professor in lista_professores:
                    professores_listbox.insert(END, professor)

                # Garante que o listbox apareça quando há dados
                if not professores_listbox.winfo_ismapped():
                    professores_listbox.grid(row=1, column=0, columnspan=2)

            else: # se a lista estiver vazia, o listbox desaparece p/ liberar espaço de tela
                professores_listbox.grid_forget()
                #self.frame_dinamico.focus_set()
                #professores_entry.focus_set()

        def preencher_professor_entry(event=None):
            self.after(10, self._atualizar_valor_entry(professores_listbox, professores_entry))
            professores_listbox.grid_forget()
            self.frame_dinamico.focus_set()

        def filtrar_professores(event=None):
            termo = professores_entry.get()

            if termo == "":
                data = self.professores_cadastrados
            else:
                data = []
                for professor in self.professores_cadastrados:
                    if termo.lower() in professor.lower():
                        data.append(professor)

            #if len(data) > 0:
            atualizar_listbox_professores(data)

        def fechar_listbox_professores(event=None):
            professores_listbox.grid_forget()
            self.frame_dinamico.focus_set()


        #professores_entry.bind("<Button-1>", lambda event: exibir_professores_listbox(True, event))
        #professores_entry.bind("<FocusOut>", lambda event: exibir_professores_listbox(False, event))
        #atualizar_listbox_professores(self.professores_cadastrados)
        professores_listbox.bind("<<ListboxSelect>>", preencher_professor_entry)
        professores_entry.bind("<KeyRelease>", filtrar_professores)
        professores_entry.bind("<Escape>", fechar_listbox_professores)

        return professores_entry

    def gera_barra_pesq_disciplinas(self, frame):
        frame_pesquisa_disciplina = ctk.CTkFrame(frame)
        frame_pesquisa_disciplina.pack(pady=10)
        disciplinas_entry = ctk.CTkEntry(frame_pesquisa_disciplina, height=30, width=200,
                                                  placeholder_text="Digite o nome da disciplina")
        disciplinas_entry.grid(row=0, column=0)

        disciplinas_listbox = tk.Listbox(
            frame_pesquisa_disciplina,
            width=25,
            font=8,
            bg="#D4D7D9",  # fundo branco "#E6E8E8"
            fg="#333333",  # texto escuro, mas não preto
            selectbackground="#0078D7",
            selectforeground="#FFFFFF",  # texto branco quando selecionado
            highlightthickness=0,  # remove borda padrão
            relief="flat"
        )

        def exibir_disciplinas_listbox(exibir, event):
            if exibir:
                disciplinas_listbox.grid(row=1, column=0, columnspan=2)
            else:
                disciplinas_listbox.grid_forget()

        def atualizar_listbox_disciplinas(lista_disciplinas):
            disciplinas_listbox.delete(0, END)

            if len(lista_disciplinas) > 0:
                for disciplina in lista_disciplinas:
                    disciplinas_listbox.insert(END, disciplina)

                    # Garante que o listbox apareça quando há dados
                    if not disciplinas_listbox.winfo_ismapped():
                        disciplinas_listbox.grid(row=1, column=0, columnspan=2)

            else:  # se a lista estiver vazia, o listbox desaparece p/ liberar espaço de tela
                disciplinas_listbox.grid_forget()

        def preencher_disciplina_entry(event=None):
            self.after(10, self._atualizar_valor_entry(disciplinas_listbox, disciplinas_entry))
            disciplinas_listbox.grid_forget()
            self.frame_dinamico.focus_set()

        def filtrar_disciplinas(event=None):
            termo = disciplinas_entry.get()

            if termo == "":
                data = self.disciplinas_cadastradas
            else:
                data = []
                for disciplina in self.disciplinas_cadastradas:
                    if termo.lower() in disciplina.lower():
                        data.append(disciplina)

            atualizar_listbox_disciplinas(data)

        def fechar_listbox_disciplinas(event=None):
            disciplinas_listbox.grid_forget()
            self.frame_dinamico.focus_set()

        #disciplinas_entry.bind("<FocusIn>", lambda event: exibir_disciplinas_listbox(True, event))
        #disciplinas_entry.bind("<FocusOut>", lambda event: exibir_disciplinas_listbox(False, event))
        #atualizar_listbox_disciplinas(self.disciplinas_cadastradas)
        disciplinas_listbox.bind("<<ListboxSelect>>", preencher_disciplina_entry)
        disciplinas_entry.bind("<KeyRelease>", filtrar_disciplinas)
        disciplinas_entry.bind("<Escape>", fechar_listbox_disciplinas)


        return disciplinas_entry
    def alternar_ativacao_dos_campos(self, ativacao, checkbox, campos, default_colors):
        """
        Utilizado em casos em que é necessário ativar e inativar campos com base em uma seleção.
        Ex: Ad Referendum -> se marcado, desativa o campo "Data da Reunião".
        """
        # desativado
        if checkbox.get() != ativacao:
            for campo in campos:
                if isinstance(campo, ctk.CTkLabel):
                    campo.configure(text_color="gray")
                else:# elementos clicáveis
                    campo.configure(state="disabled")# desabilita se marcado
                    campo.configure(fg_color="#4F4F4F")
        # ativado
        else:
            for campo in campos:
                if isinstance(campo, ctk.CTkLabel):
                    campo.configure(text_color=default_colors["label"])
                elif isinstance(campo, ctk.CTkEntry):# elementos clicáveis
                    campo.configure(state="normal")
                    campo.configure(fg_color=default_colors["entry"])
                elif isinstance(campo, ctk.CTkOptionMenu):# elementos clicáveis
                    campo.configure(state="normal")# desabilita se marcado
                    campo.configure(fg_color=default_colors["dropdown"])

    def ocultar_frame(self, element, frame_extra):# irá incluir/retirar campo(s) mediante seleção
        #element é um elemento gráfico que pode ser: checkbox ou dropdown

        valor = element.get()
        frame = frame_extra["frame"]

        if not valor or isinstance(element, ctk.CTkOptionMenu) and valor not in frame_extra["palavra_ativacao"]:#(isinstance(element, ctk.CTkOptionMenu) and valor != element._values[-1]):#pega o último valor por padrão
            for widget in frame.winfo_children():#limpa os valores preenchdios nos entries
                if isinstance(widget, ctk.CTkEntry):
                    widget.delete(0, ctk.END)
                    widget.insert(0, "null")# atribui um valor padrão p/ verif. que o campo foi ignorado(fica apenas no background)
            frame.pack_forget()
        else:
            for widget in frame.winfo_children():
                if isinstance(widget, ctk.CTkEntry):# limpa o campo p/ não exibir o valor "null" na interface
                    widget.delete(0, ctk.END)
            frame.pack(pady=10)

    def duplicar_elementos(self, elementos, botao, frame):

        frame_container_for_duplicate = ctk.CTkFrame(frame)
        frame_container_for_duplicate.pack(padx=20, pady=10)#anchor="w",

        botao.destroy()  # destrói a última referência de botão '+' criado
        botao = None
        for elemento in elementos:
            self.criar_campo(elemento, tipo='entry_for_duplicate', flag_list=True, frame=frame_container_for_duplicate)

        botao = ctk.CTkButton(self.frame_direito_inferior, text="+", width=50,
                                              command=lambda: self.duplicar_elementos(elementos, botao,
                                                                                      frame))
        botao.pack(pady=10)

    def excluir_botoes(self, frame_pai, frame_alvo):# apaga as referência de botão de um frame específico para evitar erros na interface
        for widget in frame_pai.winfo_children():
            if isinstance(widget, (ctk.CTkFrame, ctk.CTkScrollableFrame)):
                if getattr(widget, "tipo", None)==frame_alvo:  #
                    for subwidget in widget.winfo_children():
                        if isinstance(subwidget, ctk.CTkButton):
                            subwidget.destroy()
                self.excluir_botoes(widget, frame_alvo)#chama a função recursivamente para acessar os próximos frames

    def excluir_frame(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()

    def excluir_grupo_frames(self, frame_base):
        '''
        Exclui frames relacionados da interface e remove suas respectivas referências.

        Ex. de uso: excluir um aluno inserido incorretamente da interface
        '''
        #self.cont_entry_button -= 1 # decrementa o cont para controle

        self.list_divs[-1].destroy() # remoção das divisórias da interface(fins visuais)
        self.list_divs.pop(-1)

        grupo = [frame_base]
        parent = frame_base.master

        # percorre a estrutura hierárquica, analisando os irmãos do frame_base
        for widget in parent.winfo_children():
            info = widget.grid_info()
            if info and "row" in info:
                try:
                    base_row = frame_base.grid_info().get("row")
                    # se a linha do frame base for igual à do irmão, inclui na lista, pois estão relacionados
                    if info["row"] == base_row and widget != frame_base:
                        grupo.append(widget)
                except:
                    pass

        # Exclusão do frame_base e seus irmãos
        for frame in grupo:
            frame.destroy()

        # Inclusão das referências guardadas no dicionario(campos_dinamicos) numa lista de exclusão p/ evitar erro na captura de dados
        chaves_para_remover = []
        for nome, widget in list(self.campos_dinamicos.items()):
            #try:
            if not widget.winfo_exists():#hasattr(widget, "name") and
                chaves_para_remover.append(nome)
                # else:
                #     for frame in grupo:
                #         if frame in widget.winfo_ancestors():
                #             chaves_para_remover.append(nome)
                #             break
            # except: # assume que o widget não existe mais e inclui p/ remoção da referência também
            #     chaves_para_remover.append(nome)

        print("**Dicionario Original: ", self.campos_dinamicos)
        print("**Chaves para remover: ", chaves_para_remover)

        # exclusão segura das referências
        for chave in chaves_para_remover:
            self.campos_dinamicos.pop(chave, None)

    def selecionar_arquivo(self, entry):
        caminho = filedialog.askopenfilename(
            title="Selecione um arquivo",
            filetypes=[("PDF", "*.pdf")]
        )
        if caminho:
            entry.delete(0, "end")
            entry.insert(0, caminho)
            #entry.configure(state="disabled")

    def check_tipo_res(self):#, _
        # Limpa frame dinâmico e campos anteriores
        for widget in self.frame_dinamico.winfo_children():
            widget.destroy()
        # self.entry_button_container = ctk.CTkFrame(self.frame_dinamico)
        # self.entry_button_container.pack(padx=10, pady=10, fill="x")
        self.campos_dinamicos.clear()

        # caso exista, é necessário excluir o atributo da classe. Lógica utilizada para implementar
        # o botão de "adicionar" aos tipos de resolução que possuem entry_button
        if hasattr(self, "frame_entry_button_container"):
            del self.frame_entry_button_container
        self.cont_entry_button = 0
        self.tipo_var = self.tipos_resolucao_entry # representa o tipo de resolucao selecionado
        self.estruturar_frame_dinamico(self.tipo_var.get(), 1, True)#

        # Ativa botão gerar resolução
        self.botao_gerar.configure(state="normal")

    def alternar_abertura_menu_config_avancadas(self):
        # Fechar Menu
        if self.menu_config_avancadas_opened:
            self.config_avancadas_frame.grid_remove()
            self.config_avancadas_button.configure(text="⚙️ Config. Avançadas ▶")
        else:
        # Abrir Menu
            self.config_avancadas_frame.grid(row=5, column=0, pady=10, columnspan=2, sticky="")#,
            self.config_avancadas_button.configure(text="⚙️ Config. Avançadas ▼")

        self.menu_config_avancadas_opened = not self.menu_config_avancadas_opened

    def alternar_abertura_frame_fixo(self):
        if self.frame_fixo_opened:
            self.frame_fixo.grid_remove()

            self.frame_fixo_reduzido = ctk.CTkFrame(self)#.janela
            self.frame_fixo_reduzido.grid(row=1, column=0, pady=20)
            numero_res = self.numero_res_entry.get()
            data_res = self.data_res_entry.get()
            data_reuniao = self.data_reuniao_entry.get()
            ad_referendum = self.ad_referendum_var.get()
            if not ad_referendum:
                text_campos_fixos = f", de {data_res} (Reunião em {data_reuniao})"
            else:
                text_campos_fixos = f", de {data_res} (AD REFERENDUM)"

            self.dados_fixos_label = ctk.CTkLabel(self.frame_fixo_reduzido, text="Resolução", font=("Segou UI", 20))
            self.dados_fixos_label.grid(row=0, column=0)
            self.numero_res_entry_reduzido = ctk.CTkEntry(self.frame_fixo_reduzido, width=50, font=("Segou UI", 20))
            self.numero_res_entry_reduzido.insert(0, numero_res)
            self.numero_res_entry_reduzido.grid(row=0, column=1, padx=3)
            self.dados_fixos_label = ctk.CTkLabel(self.frame_fixo_reduzido, text=text_campos_fixos, font=("Segou UI", 20))
            self.dados_fixos_label.grid(row=0, column=2, padx=3)

            self.ampliar_frame_fixo_button = ctk.CTkButton(self.frame_fixo_reduzido, text="Ampliar", width=70, command=lambda: self.alternar_abertura_frame_fixo())
            self.ampliar_frame_fixo_button.grid(row=0, column=3, padx=10)

        else:
            numero_res = self.numero_res_entry_reduzido.get()
            self.numero_res_entry.delete(0, END)
            self.numero_res_entry.insert(0, numero_res)
            self.frame_fixo_reduzido.grid_remove()
            self.frame_fixo.grid(row=1, column=0, pady=20)

        self.frame_fixo_opened = not self.frame_fixo_opened

    def estruturar_menu_config_avancadas(self):
        self.vice_coordenador_var = ctk.BooleanVar(value=False)
        vice_coordenador_checkbox = ctk.CTkCheckBox(self.config_avancadas_frame, text="Vice-Coordenador?", variable=self.vice_coordenador_var)
        vice_coordenador_checkbox.grid(row=0, column=0, padx=10, sticky="w")

        default_colors = {}
        self.data_republicacao_entry = ctk.CTkEntry(self.config_avancadas_frame, placeholder_text="DD/MM/AAAA")
        self.data_republicacao_entry.configure(state="disabled")
        default_colors["entry"] = self.data_republicacao_entry.cget("fg_color")
        self.data_republicacao_entry.grid(row=1, column=1, padx=10, pady=5)#, columnspan=1
        self.motivo_republicacao_var = ctk.StringVar(value="Selecione")
        motivo_republicacao_dropdown = ctk.CTkOptionMenu(self.config_avancadas_frame, values=['Correção', 'Complementação'], variable=self.motivo_republicacao_var, width=120)
        motivo_republicacao_dropdown.configure(state="disabled")
        default_colors["dropdown"] = motivo_republicacao_dropdown.cget("fg_color")
        motivo_republicacao_dropdown.grid(row=2, column=1, padx=10, pady=5)
        self.republicacao_var = ctk.BooleanVar(value=False)
        republicacao_checkbox = ctk.CTkCheckBox(self.config_avancadas_frame, text="Republicação?",
                                                variable=self.republicacao_var,
                                                command=lambda: self.alternar_ativacao_dos_campos(True, republicacao_checkbox, [self.data_republicacao_entry, motivo_republicacao_dropdown], default_colors))
        republicacao_checkbox.grid(row=0, column=1, padx=10, sticky="w")

        self.pdf_autosave_switch_var = ctk.BooleanVar(value=True)
        pdf_autosave_switch = ctk.CTkSwitch(self.config_avancadas_frame, text="Gerar Versão PDF", variable=self.pdf_autosave_switch_var, onvalue=True, offvalue=False)
        pdf_autosave_switch.grid(row=0, column=2, padx=10, sticky="w")

    def estruturar_frame_dinamico(self,tipo, line, primeira_chamada):
        #self.tipo_var = self.tipos_resolucao_entry
        if self.tipo_var.get() == "Adiamento de Reunião":
            self.criar_campo("Nº. da Reunião")
            self.criar_campo("Data Inicial", tipo='entry_placeholder')
            self.criar_campo("Resolução de Aprovação", tipo='entry_placeholder')
            self.criar_campo("Data da Resolução Original", tipo='entry_placeholder')
            frame_nova_data = ctk.CTkFrame(self.frame_dinamico)
            frame_extra_dict = {}
            frame_extra_dict["frame"] = frame_nova_data
            self.criar_campo("Previsão da Nova Data?", tipo='checkbox', frame_extra=frame_extra_dict)
            frame_nova_data.pack(pady=10)
            self.criar_campo("Data Atualizada", tipo='entry_placeholder', frame=frame_nova_data)

        elif self.tipo_var.get() == "Afastamento de Discente":
            self.criar_campo("Nível do Discente", tipo='dropdown', opcoes=["Mestrado", "Doutorado"])
            self.criar_campo("Nome do Discente")
            self.criar_campo("Nº. de Dias de Afastamento")
            self.criar_campo("Data de Início", tipo='entry_placeholder')
            self.criar_campo("Data de Finalização", tipo='entry_placeholder')
            frame_motivo = ctk.CTkFrame(self.frame_dinamico)
            frame_extra_dict = {}
            frame_extra_dict["frame"] = frame_motivo
            frame_extra_dict["palavra_ativacao"] = ["Outro(s)"]#palavra_ativacao é o que definirá se o frame será exibido ou não
            self.criar_campo("Motivo", tipo='dropdown', opcoes=["Particular", "Saúde", "Outro(s)"], frame_extra=frame_extra_dict)
            self.criar_campo("Outro", frame=frame_motivo)

        elif self.tipo_var.get() == "Aprovação de Banca":
            self.frame_entry_file_container = ctk.CTkFrame(self.frame_dinamico)
            self.frame_entry_file_container.pack(anchor="w", padx=10, pady=(5, 0))
            #self.frame_entry_file_container.grid(row=line, column=0, padx=10, pady=10)
            self.criar_campo("Solicitação de Banca", tipo='entry_file')

            self.criar_campo("Nível do Discente", tipo='dropdown', opcoes=["Mestrado", "Doutorado"])
            self.criar_campo("Nome do Discente")
            self.criar_campo("Tipo de Trabalho", tipo='dropdown', opcoes=["Dissertação", "Tese"])
            self.criar_campo("Título do Trabalho")
            self.criar_campo("Tipo de Apresentação", tipo='dropdown', opcoes=["Qualificação", "Defesa"])
            self.criar_campo("Data da Apresentação", tipo='entry_placeholder')

        elif self.tipo_var.get() == "Aproveitamento de Suficiência":
            if primeira_chamada:
                self.frame_superior = ctk.CTkFrame(self.frame_dinamico)  # cria um novo frame p/ o container
                # self.frame_entry_button_container.pack(side="left", padx=10, pady=10)#, fill="y"
                #self.frame_superior.place(relx=0.5)
                self.frame_superior.grid(row=0, column=0, columnspan=2, pady=(10, 20), sticky="n")
                self.criar_campo("Língua", tipo = 'dropdown', opcoes = ["Inglês", "Espanhol"], frame=self.frame_superior)#, linha=0

            self.frame_entry_button_container = ctk.CTkFrame(self.frame_dinamico)#cria um novo frame p/ o container
            #self.frame_entry_button_container.pack(side="left", padx=10, pady=10)#, fill="y"
            self.frame_entry_button_container.grid(row=line, column=0, padx=10, pady=10)#, sticky="nsew"

            # Frame da direita (campo de língua)
            self.frame_direito = ctk.CTkFrame(self.frame_dinamico)
            #self.frame_lingua.pack(side="left", padx=10, pady=10)#, fill="y"
            self.frame_direito.grid(row=line, column=1, padx=10, pady=10)#, sticky="nsew")#row=line, column=1, padx=(0, 10), pady=10
            self.criar_campo("Nome do Discente", tipo='entry_button', frame=self.frame_entry_button_container)
            self.criar_campo("Data do Exame", tipo='entry_placeholder', frame=self.frame_direito, flag_list=True)# linha=1,
            self.criar_campo("Resolução de Aprovação", tipo='entry_placeholder', frame=self.frame_direito, flag_list=True)#linha=2

        elif self.tipo_var.get() == "Calendário de Reuniões":
            if primeira_chamada:
                self.frame_superior = ctk.CTkFrame(self.frame_dinamico)  # cria um novo frame p/ o container
                self.frame_superior.grid(row=0, column=0, columnspan=2, pady=(10, 20), sticky="n")
                self.criar_campo("Ano Vigente", frame=self.frame_superior)

            self.frame_entry_button_container = ctk.CTkFrame(self.frame_dinamico)  # cria um novo frame p/ o container
            self.frame_entry_button_container.grid(row=line, column=0, padx=10, pady=10)  # , sticky="nsew"

            self.frame_direito = ctk.CTkFrame(self.frame_dinamico)
            self.frame_direito.grid(row=line, column=1, padx=10, pady=10)
            entry_n_reuniao = self.criar_campo("Nº da Reunião", tipo='entry_button', frame=self.frame_entry_button_container)
            n_reuniao = self.cont_entry_button+1
            entry_n_reuniao.insert(0, f"{n_reuniao}ª Ordinária")
            entry_n_reuniao.configure(state="disabled")  # desabilita se marcado
            entry_n_reuniao.configure(fg_color="#4F4F4F")
            self.criar_campo("Data da Reunião", tipo='entry_placeholder', frame=self.frame_direito, flag_list=True)


        elif self.tipo_var.get() == "Cancelamento de Oferta de Disciplina":
            self.criar_campo("Nome da Disciplina", tipo='entry_listbox')
            self.criar_campo("Professor Responsável", tipo='entry_listbox') # NOVO TIPO: ENTRY LISTBOX
            self.criar_campo("Semestre(ano-nº semestre)")

            frame_motivo = ctk.CTkFrame(self.frame_dinamico)
            frame_extra_dict = {}
            frame_extra_dict["frame"] = frame_motivo
            frame_extra_dict["palavra_ativacao"] = ["Outro(s)"]
            self.criar_campo("Motivo", tipo='dropdown',
                             opcoes=["Inexistência de Matriculados", "Outro(s)"],
                             frame=self.frame_dinamico,
                             frame_extra=frame_extra_dict)

            self.criar_campo(f"Outro", frame=frame_motivo)

        elif self.tipo_var.get() == "Cancelamento de Matrícula":
            if primeira_chamada:
                self.frame_superior = ctk.CTkFrame(self.frame_dinamico)  # cria um novo frame p/ o container
                self.frame_superior.grid(row=0, column=0, columnspan=2, pady=(10, 20), sticky="n")
                self.criar_campo("ano-semestre", frame=self.frame_superior)

            self.frame_entry_button_container = ctk.CTkFrame(self.frame_dinamico)  # cria um novo frame p/ o container
            self.frame_entry_button_container.grid(row=line, column=0, padx=10, pady=10)  # , sticky="nsew"

            self.frame_direito = ctk.CTkFrame(self.frame_dinamico)
            self.frame_direito.grid(row=line, column=1, padx=10, pady=10)
            self.criar_campo("Nome do Discente", tipo='entry_button', frame=self.frame_entry_button_container)

            self.frame_direito_superior = ctk.CTkFrame(self.frame_direito)  # cria um novo frame p/ o container
            #self.frame_direito_superior.grid(row=0, column=0, padx=10, pady=10)
            self.frame_direito_superior.pack(pady=10)
            self.criar_campo("Nível do Discente", tipo='dropdown', flag_list=True, opcoes=["Mestrado", "Doutorado"], frame=self.frame_direito_superior)

            self.frame_direito_inferior = ctk.CTkFrame(self.frame_direito)  # cria um novo frame p/ o container
            self.frame_direito_inferior.tipo = "direito_inferior"
            #self.frame_direito_inferior.grid(row=1, column=0, padx=10, pady=10)
            self.frame_direito_inferior.pack(pady=10, fill="x", anchor="w")

            self.excluir_botoes(self.frame_dinamico, "direito_inferior")

            elementos_frame_for_duplicate = []
            frame_container_for_duplicate = ctk.CTkFrame(self.frame_direito_inferior)
            frame_container_for_duplicate.pack(padx=20, pady=10)  #
            self.criar_campo("Disciplina", tipo='entry_for_duplicate', flag_list=True, frame=frame_container_for_duplicate)#self.frame_direito_inferior
            elementos_frame_for_duplicate.append("Disciplina")
            self.criar_campo("Professor", tipo='entry_for_duplicate', flag_list=True, frame=frame_container_for_duplicate)
            elementos_frame_for_duplicate.append("Professor")

            button_add_disciplina = ctk.CTkButton(self.frame_direito_inferior, text="+", width=50, command=lambda: self.duplicar_elementos(elementos_frame_for_duplicate, button_add_disciplina, self.frame_direito_inferior) )
            button_add_disciplina.pack(pady=20)

            #ctk.CTkLabel(self.frame_direito_inferior, text="Disciplina Teste").pack(anchor="w")


            # self.frame_direito_inferior_dir = ctk.CTkFrame(self.frame_direito)  # cria um novo frame p/ o container
            # self.frame_direito_inferior_dir.grid(row=1, column=1, padx=10, pady=10)
            # self.criar_campo("Professor", frame=self.frame_direito_inferior_dir)

        elif self.tipo_var.get() == "Cancelamento de Orientação":
            self.criar_campo("Nome do Orientador", tipo='entry_listbox')
            self.criar_campo("Nome do Aluno")
            self.criar_campo("Prazo Para Regularização(em dias)")

        elif self.tipo_var.get() == "Composição de Comissão":
            if primeira_chamada:
                self.frame_superior = ctk.CTkFrame(self.frame_dinamico)  # cria um novo frame p/ o container
                self.frame_superior.grid(row=0, column=0, columnspan=2, pady=(10, 20), sticky="n")
                self.criar_campo("Nome da Comissão", frame=self.frame_superior)

            self.frame_entry_button_container = ctk.CTkFrame(self.frame_dinamico)  # cria um novo frame p/ o container
            self.frame_entry_button_container.grid(row=line, column=0, padx=10, pady=10)  # , sticky="nsew"

            self.frame_direito = ctk.CTkFrame(self.frame_dinamico)
            self.frame_direito.grid(row=line, column=1, padx=10, pady=10)
            self.criar_campo("Professor Membro", tipo='entry_button_listbox', frame=self.frame_entry_button_container)
            self.criar_campo("Tipo de Participação", tipo='dropdown', opcoes = ["Presidente", "Membro Titular", "Membro Suplente"], frame=self.frame_direito, flag_list=True)

        elif self.tipo_var.get() == "Contratação de Professor Visitante":
            self.criar_campo("Nome do Professor")
            self.criar_campo("Classificação no Processo Seletivo")
            self.criar_campo("Nº Edital PROPP")
            self.criar_campo("Data Publicação Edital PROPP", tipo='entry_placeholder')
            self.criar_campo("Cadastro de Reserva?", tipo='dropdown', opcoes=['Sim', 'Não'])

        elif self.tipo_var.get() == "Convalidação de Suficiência":
            self.criar_campo("Nível do Discente", tipo='dropdown', opcoes=["Mestrado", "Doutorado"])
            self.criar_campo("Nome do Discente")
            self.criar_campo("Língua", tipo='dropdown', opcoes=["Inglês", "Espanhol"])
            frame_exame = ctk.CTkFrame(self.frame_dinamico)
            frame_extra_dict = {}
            frame_extra_dict["frame"] = frame_exame
            frame_extra_dict["palavra_ativacao"] = ["Outro"]
            self.criar_campo("Exame", tipo='dropdown', opcoes=["ITP-TOEFL", "Outro"],
                             frame_extra=frame_extra_dict)
            self.criar_campo("Outro", frame=frame_exame)

        elif self.tipo_var.get() == "Credenciamento de Docente":
            self.criar_campo("Nome do Professor")
            self.criar_campo("Modalidade", tipo='dropdown', opcoes=['Colaborador', 'Permanente', 'Voluntário'])

        elif self.tipo_var.get() == "Descredenciamento de Docente":
            self.criar_campo("Nome do Professor", tipo='entry_listbox')
            self.criar_campo("Modalidade", tipo='dropdown', opcoes=['colaboradores', 'permanentes', 'voluntários'])

            frame_motivo = ctk.CTkFrame(self.frame_dinamico)
            frame_extra_dict = {}
            frame_extra_dict["frame"] = frame_motivo
            frame_extra_dict["palavra_ativacao"] = ["Outro(s)"]
            self.criar_campo("Motivo", tipo='dropdown',
                             opcoes=["Solicitação do(a) docente", "Outro(s)"],
                             flag_list=True, frame=self.frame_dinamico,
                             frame_extra=frame_extra_dict)

            self.criar_campo(f"Outro", frame=frame_motivo)

        elif self.tipo_var.get() == "Desligamento de Discente":
            self.frame_entry_button_container = ctk.CTkFrame(self.frame_dinamico)
            self.frame_entry_button_container.grid(row=line, column=0, padx=10, pady=10)
            self.frame_direito = ctk.CTkFrame(self.frame_dinamico)
            self.frame_direito.grid(row=line, column=1, padx=10,
                                    pady=10)

            self.criar_campo("Nome do Discente", tipo='entry_button', frame=self.frame_entry_button_container)
            self.criar_campo("Nível do Discente", tipo='dropdown', opcoes=["Mestrado", "Doutorado"], flag_list=True, frame=self.frame_direito)
            frame_motivo = ctk.CTkFrame(self.frame_direito)
            frame_extra_dict = {}
            frame_extra_dict["frame"] = frame_motivo
            frame_extra_dict["palavra_ativacao"] = ["Não realização de matrícula", "Outro(s)"]
            self.criar_campo("Motivo", tipo='dropdown', opcoes=["Solicitado pelo discente", "Não realização de matrícula", "Outro(s)"], flag_list=True, frame=self.frame_direito,
                             frame_extra=frame_extra_dict)

            self.criar_campo("- Se 'não realização de matrícula', informe ano-semestre\n- Se 'Outro(s), informe o motivo'", tipo = 'label', frame=frame_motivo)
            self.criar_campo(f"Complemento", flag_list=True, frame=frame_motivo)

        elif self.tipo_var.get() == "Homologação de Ad Referendum":
            self.frame_entry_button_container = ctk.CTkFrame(self.frame_dinamico)
            self.frame_entry_button_container.pack(pady=10)
            self.criar_campo("Resolução", tipo='entry_button', frame=self.frame_entry_button_container)

        elif self.tipo_var.get() == "Inclusão de Coorientação":
            self.criar_campo("Nível do Discente", tipo='dropdown', opcoes=["Mestrado", "Doutorado"])
            self.criar_campo("Nome do Discente")
            self.criar_campo("Coorientador(a)", tipo='entry_listbox')
            self.criar_campo("Universidade", tipo='entry_placeholder')

        elif self.tipo_var.get() == "Licença Maternidade":
            self.criar_campo("Nível do Discente", tipo='dropdown', opcoes=["Mestrado", "Doutorado"])
            self.criar_campo("Nome do Discente")
            self.criar_campo("Nº. de Meses da Licença(por extenso. Ex: seis)")
            self.criar_campo("Ano de Ingresso")
            self.criar_campo("Data Fim da Licença", tipo='entry_placeholder')
            self.criar_campo("Data Inicial de Defesa", tipo='entry_placeholder')
            self.criar_campo("Data Limite Para Defesa Ajustada", tipo='entry_placeholder')

        elif self.tipo_var.get() == "Número de Vagas Para Processo Seletivo":
            #self.criar_campo("Processo Seletivo")
            self.criar_campo("Vagas de Mestrado")
            self.criar_campo("Vagas de Doutorado")
            self.criar_campo("Semestre(ano-nº semestre)")
            frame_processo = ctk.CTkFrame(self.frame_dinamico)
            frame_extra_dict = {}
            frame_extra_dict["frame"] = frame_processo
            frame_extra_dict["palavra_ativacao"] = [
                "Outro"]  # palavra_ativacao é o que definirá se o frame será exibido ou não
            self.criar_campo("Processo Seletivo", tipo='dropdown',
                             opcoes=["Processo Seletivo de Alunos Regulares", "Programa GCUB-MOB", "Programa Move La America", "Outro"],
                             frame_extra=frame_extra_dict)
            self.criar_campo("Outro", frame=frame_processo)

        elif self.tipo_var.get() == "Prorrogação de Qualificação":
            self.criar_campo("Nível do Discente", tipo='dropdown', opcoes=["Mestrado", "Doutorado"])
            self.criar_campo("Nome do Discente")
            self.criar_campo("Ano de Ingresso")
            self.criar_campo("Data Limite Aprovada", tipo='entry_placeholder')

        elif self.tipo_var.get() == "Relatório de Professor Visitante":
            self.criar_campo("Nome do Professor", tipo='entry_listbox')
            self.criar_campo("Data de Início das Atividades", tipo='entry_placeholder')
            self.criar_campo("Data de Finalização das Atividades", tipo='entry_placeholder')
            frame_tipo_relatorio = ctk.CTkFrame(self.frame_dinamico)
            frame_extra_dict = {}
            frame_extra_dict["frame"] = frame_tipo_relatorio
            frame_extra_dict["palavra_ativacao"] = ["Com Renovação"]#palavra_ativacao é o que definirá se o frame será exibido ou não
            self.criar_campo("Tipo de Aprovação", tipo='dropdown', opcoes=["Com Renovação", "Sem Renovação"], frame_extra=frame_extra_dict)
            self.criar_campo("Data de Início da Renovação", tipo='entry_placeholder', frame=frame_tipo_relatorio)
            self.criar_campo("Data Final da Renovação", tipo='entry_placeholder', frame=frame_tipo_relatorio)
            self.criar_campo("Professor Supervisor", tipo='entry_listbox', frame=frame_tipo_relatorio)

        elif self.tipo_var.get() == "Trancamento de Curso":
            self.criar_campo("Nível do Discente", tipo='dropdown', opcoes=["Mestrado", "Doutorado"])
            self.criar_campo("Nome do Discente")
            self.criar_campo("RGA")
            self.criar_campo("Semestre de Trancamento(ano-semestre)")
            frame_motivo = ctk.CTkFrame(self.frame_dinamico)
            frame_extra_dict = {}
            frame_extra_dict["frame"] = frame_motivo
            frame_extra_dict["palavra_ativacao"] = ["Outro(s)"]
            self.criar_campo("Motivo", tipo='dropdown',
                             opcoes=["Motivos Particulares", "Motivos de Saúde", "Motivos Profissionais", "Motivos Acadêmicos", "Outro(s)"],
                             frame=self.frame_dinamico,
                             frame_extra=frame_extra_dict)
            self.criar_campo("Outro(s)", frame=frame_motivo)

        elif self.tipo_var.get() == "Troca de Orientação":
            self.criar_campo("Nível do Discente", tipo='dropdown', opcoes=["Mestrado", "Doutorado"])
            self.criar_campo("Nome do Discente")
            self.criar_campo("Orientador Atual", tipo='entry_listbox')
            self.criar_campo("Novo Orientador", tipo='entry_listbox')

        elif self.tipo_var.get() == "Troca de Projeto de Pesquisa":
            self.criar_campo("Nível do Discente", tipo='dropdown', opcoes=["Mestrado", "Doutorado"])
            self.criar_campo("Nome do Discente")
            self.criar_campo("Projeto Atual")
            self.criar_campo("Novo Projeto")

        # Cria/Recria o Botão para adição de frames
        if hasattr(self, "frame_entry_button_container"):

            if self.button_add:
                self.button_add.destroy()
            self.div = ttk.Separator(self.frame_dinamico, orient="horizontal")
            self.list_divs.append(self.div)
            line_div = line+1
            line_button = line+2

            self.div.grid(row=line_div, column=0, columnspan=2, sticky="ew")

            self.button_add = ctk.CTkButton(self.frame_dinamico, text="➕", width=50, height=50, corner_radius=50, fg_color=("#000000", "#1E90FF"),
                                            command = lambda: self.estruturar_frame_dinamico(self.tipo_var.get(), line_button, False))
            self.button_add.grid(row=line_button, column=1, pady=15, padx=25, sticky="e")
            self.cont_entry_button += 1

            # if frame_container_for_duplicate.winfo_exists():
            #     print("ENTROU FOR DUPLICATE")
            #     self.cont_entry_button -= 1


    def criar_campo(self, nome, tipo='entry', opcoes=None, frame=None, flag_list=False, frame_extra=None):
        if frame is None:
            frame = self.frame_dinamico

        if tipo == 'label':
            label = ctk.CTkLabel(frame, text=nome)
            label.pack(anchor="w", padx=10, pady=(5, 0))
        elif tipo == 'entry':
            label = ctk.CTkLabel(frame, text=nome)
            #label.grid(row=linha, column=0, pady=10, padx=(5, 0))#padx=(0, 0), , sticky="w"
            label.pack(anchor="w", padx=10, pady=(5, 0))#side=pos,

            entry = ctk.CTkEntry(frame, width=200)
            print("PRINT DO ENTRY: ", entry)
            #entry.grid(row=linha, column=1, pady=10, padx=(0, 5))#padx=(0, 0),
            entry.pack(padx=10, pady=(0,10))#side=pos,

            if flag_list is True:
                nome = f"{nome} {self.cont_entry_button}"
                # self.campos_dinamicos[] = entry
            # else:
            #     self.campos_dinamicos[nome] = entry

            self.campos_dinamicos[nome] = entry

            return label, entry

        elif tipo == 'entry_for_duplicate':

            label = ctk.CTkLabel(frame, text=nome)
            #label.grid(row=i, column=0, pady=10, padx=(0, 5))#padx=(0, 0),
            label.pack(side="left", padx=2, pady=(5, 0))

            entry = ctk.CTkEntry(frame, width=150)
            #entry.grid(row=i, column=1, pady=10, padx=(0, 5))#padx=(0, 0),
            entry.pack(side="left", padx=2, pady=(0, 10))
            self.cont_entry_for_duplicate += 1

            if flag_list is True:
                self.campos_dinamicos[f"{nome} {self.cont_entry_button_aux}_{self.cont_entry_for_duplicate}"] = entry
            else:
                self.campos_dinamicos[nome] = entry
        elif tipo == 'entry_button':
            frame_entry_button = ctk.CTkFrame(frame)#self.frame_entry_button_container
            frame_entry_button.pack(padx=20, pady=10)#, fill="x"
            #frame_entry_button.pack(anchor="w", padx=10, pady=(5, 0))

            label = ctk.CTkLabel(frame_entry_button, text=nome)#frame_entry_button
            label.pack(side="left", padx=2, pady=(5, 0))

            entry = ctk.CTkEntry(frame_entry_button, width=150)
            entry.pack(side="left", padx=(0, 2))
            self.campos_dinamicos[f"{nome} {self.cont_entry_button}"] = entry
            self.cont_entry_button_aux += 1 # cont auxiliar que será utilizado exclusivamente p/ o modelo "Cancelamento de Matrícula"(e caso surjam modelos na mesma esttutura posteriormente)

            if self.button_add:
                self.button_add.destroy()# destrói a última referência de botão + criado
                self.button_add = None

            self.button_add = ctk.CTkButton(frame_entry_button, text="➕", width=40, command=lambda: self.estruturar_frame_dinamico(self.tipo_var.get(), self.cont_entry_button + 1, False))
            #self.button_add.pack(pady=15)#side="left"
            button_add_name = self.button_add.winfo_name()
            print("Botão add: ", button_add_name)

            self.button_delete = ctk.CTkButton(frame_entry_button, text="❌", width=40, command=lambda: self.excluir_grupo_frames(frame))
            self.button_delete.pack(side="left")
            button_delete_name = self.button_delete.winfo_name()
            print("Botão delete: ", button_add_name)

            return entry
        elif tipo == 'entry_file':
            frame_entry_file = ctk.CTkFrame(self.frame_entry_file_container)
            frame_entry_file.pack(padx=20, pady=10)  # , fill="x"

            label = ctk.CTkLabel(frame_entry_file, text=nome)  # frame_entry_button
            label.pack(side="left", padx=10, pady=(5, 0))

            entry = ctk.CTkEntry(frame_entry_file, width=200)
            entry.pack(side="left", padx=(0, 10))

            if flag_list is True:
                nome = f"{nome} {self.cont_entry_button}"

            self.campos_dinamicos[nome] = entry#f"{nome} {self.cont_entry_button}"
            #self.cont_entry_button += 1

            # if self.button_add:
            #     self.button_add.destroy()  # destrói a última referência de botão + criado
            #     self.button_add = None

            self.button_search_file = ctk.CTkButton(frame_entry_file, text="Buscar", width=100,
                                            command=lambda: self.selecionar_arquivo(entry))
            self.button_search_file.pack(side="left")

        elif tipo == 'entry_listbox':
            if flag_list is True:
                nome = f"{nome} {self.cont_entry_button}"
                # self.campos_dinamicos[] = entry
            # else:
            #     self.campos_dinamicos[nome] = entry

            label = ctk.CTkLabel(frame, text=nome)
            # label.grid(row=linha, column=0, pady=10, padx=(5, 0))#padx=(0, 0), , sticky="w"
            label.pack(anchor="w", padx=10, pady=(5, 0))  # side=pos,

            # CRIAÇÃO DO ENTRY NO FORMATO BARRA DE PESQUISA
            if any(termo in nome.lower() for termo in ("professor", "docente", "orientador")):
                professores_entry = self.gera_barra_pesq_professores(frame)

                self.campos_dinamicos[nome] = professores_entry

            elif any(termo in nome.lower() for termo in ("disciplina")):
                disciplinas_entry = self.gera_barra_pesq_disciplinas(frame)

                self.campos_dinamicos[nome] = disciplinas_entry
            # entry.grid(row=linha, column=1, pady=10, padx=(0, 5))#padx=(0, 0),
            #entry.pack(padx=10, pady=(0, 10))  # side=pos,

        elif tipo == 'entry_button_listbox':
            frame_entry_button = ctk.CTkFrame(frame)#self.frame_entry_button_container
            frame_entry_button.pack(padx=20, pady=10)#, fill="x"
            frame_barra_pesq = ctk.CTkFrame(frame_entry_button, fg_color='transparent')

            #frame_entry_button.pack(anchor="w", padx=10, pady=(5, 0))

            label = ctk.CTkLabel(frame_entry_button, text=nome)#frame_entry_button
            label.pack(side="left", padx=2, pady=(10, 0))
            frame_barra_pesq.pack(side="left")

            if any(termo in nome.lower() for termo in ("professor", "docente", "orientador")):
                professores_entry = self.gera_barra_pesq_professores(frame_barra_pesq)

                self.campos_dinamicos[f"{nome} {self.cont_entry_button}"] = professores_entry

            elif any(termo in nome.lower() for termo in ("disciplina")):
                disciplinas_entry = self.gera_barra_pesq_disciplinas(frame_barra_pesq)

                self.campos_dinamicos[f"{nome} {self.cont_entry_button}"] = disciplinas_entry

            #entry = ctk.CTkEntry(frame_entry_button, width=150)
            #entry.pack(side="left", padx=(0, 2))
            #self.campos_dinamicos[f"{nome} {self.cont_entry_button}"] = entry
            self.cont_entry_button_aux += 1 # cont auxiliar que será utilizado exclusivamente p/ o modelo "Cancelamento de Matrícula"(e caso surjam modelos na mesma esttutura posteriormente)

            if self.button_add:
                self.button_add.destroy()# destrói a última referência de botão + criado
                self.button_add = None

            self.button_add = ctk.CTkButton(frame_entry_button, text="➕", width=40, command=lambda: self.estruturar_frame_dinamico(self.tipo_var.get(), self.cont_entry_button + 1, False))
            #self.button_add.pack(pady=15)#side="left"
            button_add_name = self.button_add.winfo_name()
            print("Botão add: ", button_add_name)

            self.button_delete = ctk.CTkButton(frame_entry_button, text="❌", width=40, command=lambda: self.excluir_grupo_frames(frame))
            self.button_delete.pack(side="left")
            button_delete_name = self.button_delete.winfo_name()
            print("Botão delete: ", button_add_name)

            #return entry


        elif tipo == 'entry_placeholder':
                label = ctk.CTkLabel(frame, text=nome)
                # label.grid(row=linha, column=0, pady=10, padx=(5, 0))#padx=(0, 0), , sticky="w"
                label.pack(anchor="w", padx=10, pady=(5, 0))  # side=pos,

                partes_nome = nome.split()
                if partes_nome[0] == "Data":
                    entry = ctk.CTkEntry(frame, width=200, placeholder_text="dd/mm/aaaa")
                    entry.pack(padx=10, pady=(0, 10))  # side=pos,
                #elif partes_nome[0] == "Resolução":
                elif partes_nome[0] == "Universidade":
                    entry = ctk.CTkEntry(frame, width=200, placeholder_text="nome(sigla)")
                    entry.pack(padx=10, pady=(0, 10))
                else:#formato para resolução
                    entry = ctk.CTkEntry(frame, width=200, placeholder_text="nº-ano")
                    entry.pack(padx=10, pady=(0, 10))  # side=pos,

                if flag_list is True:
                    nome = f"{nome} {self.cont_entry_button}"

                self.campos_dinamicos[nome] = entry

        elif tipo == 'dropdown':
            label = ctk.CTkLabel(frame, text=nome)#self.frame_dinamico
            label.pack(anchor="w", padx=10, pady=(5, 0))

            if not opcoes:
                opcoes = ["Opção 1", "Opção 2"]# caso não sejam fornecidas opções como parametro
            var = ctk.StringVar(value="Selecione")
            #var = ctk.StringVar(value=opcoes[0])
            if frame_extra is None:
                dropdown = ctk.CTkOptionMenu(frame, values=opcoes, variable=var, width=300)#self.frame_dinamico
            else:
                dropdown = ctk.CTkOptionMenu(frame, values=opcoes, variable=var, width=300, command=lambda valor: self.ocultar_frame(dropdown, frame_extra))#self.frame_dinamico
            dropdown.pack(padx=10, pady=(0, 10))

            # if flag_list is True:
            #     self.campos_dinamicos[f"{nome} {self.cont_entry_button}"] = var
            # else:
            #     self.campos_dinamicos[nome] = var
            # #self.campos_dinamicos[nome] = var
            print("PRINT DO VALOR DO DROPDOWN: ", dropdown.get())

            if flag_list is True:
                nome = f"{nome} {self.cont_entry_button}"

            self.campos_dinamicos[nome] = dropdown

            return var.get()

        elif tipo == 'checkbox':
            checkbox_var = ctk.BooleanVar(value=True)
            checkbox = ctk.CTkCheckBox(
                frame,
                text=nome,
                variable=checkbox_var,
                command=lambda: self.ocultar_frame(checkbox, frame_extra)
            )
            checkbox.pack(pady=10)

    def gerar_popup(self, msg, type):
        popup = ctk.CTkToplevel()
        width = 300
        height = 150
        # centralizar o popup
        x = (popup.winfo_screenwidth() // 2) - (width // 2)
        y = (popup.winfo_screenheight() // 2) - (height // 2)
        popup.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        popup.resizable(False, False)

        if type == 'warning':
            icon = '⚠️'
        elif type == 'succes':
            icon = '✅'
        else:
            icon = '✉️'

        popup.title(f"{icon} Mensagem")

        label = ctk.CTkLabel(popup, text=f'{icon} {msg}', wraplength=250)
        label.pack(pady=20)

        button = ctk.CTkButton(popup, text="OK", command=popup.destroy)
        button.pack(pady=10)

        popup.grab_set()

    def capturar_dados(self):

        # LEITURA DOS DADOS FIXOS
        numero_res = self.numero_res_entry.get() if self.frame_fixo_opened else self.numero_res_entry_reduzido.get()
        data_res = self.data_res_entry.get()
        data_reuniao = self.data_reuniao_entry.get()

        if not numero_res or not data_res:
            print("** Existem dados fixos sem preenchimento")
            self.gerar_popup("Existem campos sem preenchimento!!", "warning")
            return
        ad_referendum = self.ad_referendum_var.get()

        # LEITURA DAS CONFIGURAÇÕES
        configs_avancadas = {
           "vice_coordenador" : self.vice_coordenador_var.get(),
            "republicacao" : [self.republicacao_var.get(), self.data_republicacao_entry.get(), self.motivo_republicacao_var.get()] if self.republicacao_var.get() else self.republicacao_var.get(),
            "pdf_autosave": self.pdf_autosave_switch_var.get()
        }

        # GRAVAÇÃO NO ARQUIVO DE CONFIGURAÇÕES (.yaml)
        CAMINHO_CONFIG = './src/config/configs.yaml'
        print("CAMINHO CONFIG: ", CAMINHO_CONFIG)

        with open(CAMINHO_CONFIG, "r", encoding="utf-8") as file:
            file_parts = list(yaml.safe_load_all(file))
        file_parts[1] = configs_avancadas

        with open(CAMINHO_CONFIG, "w", encoding="utf-8") as file:
            yaml.dump_all(file_parts, file, sort_keys=False, allow_unicode=True)

        # LEITURA DOS DADOS DINÂMICOS
        #valores_dinamicos = {nome: campo.get() for nome, campo in self.campos_dinamicos.items()}
        valores_dinamicos = {}
        dict_dados_aux = defaultdict(list)#dicionario de listas aux
        dict_dados_tipo_atr_aux = defaultdict(lambda: defaultdict(list)) # lambda informa qual será o valor padrão quando a chave ainda não existe.
        for nome, widget in self.campos_dinamicos.items():
            if isinstance(widget, (ctk.CTkEntry, ctk.CTkOptionMenu)):
                valor = widget.get()

                if not valor or valor == 'Selecione':
                    print("**Existem campos sem preenchimento**")
                    self.gerar_popup("Existem campos sem preenchimento!!", "warning")
                    return

                partes_nome = nome.split()
                chave_dicionario = " ".join(partes_nome[:-1])# nome da variavel sem o contador

                if partes_nome[-1].replace("_", "").isdigit():# verifica se há um cont acoplado ao nome do identificador

                    # tratamento para campos repetidos(2 contadores). Ex: Disciplina 1 3(1=refere-se ao atributo principal,
                    #aluno que a disciplina está vinculada, por ex // 3= refere-ao cont da disciplina em si
                    if "_" in partes_nome[-1]:
                        indices = partes_nome[-1].split("_")
                            #list(partes_nome[-1])
                        dict_dados_tipo_atr_aux[chave_dicionario][indices[0]].append(valor)

                        print("DICIONÁRIO", dict_dados_tipo_atr_aux)
                        #conversão de dicionário de lista em lista de lista
                        valores = list(dict_dados_tipo_atr_aux[chave_dicionario].values())

                        print("LISTA DE VALORES:", valores)

                        valores_dinamicos[chave_dicionario] = valores

                    # tratamento p/ atributos com cont acoplado simples. Ex: Aluno 1, Aluno 2, etc
                    else:
                        # cont_discentes = int(partes_nome[-1])
                        # valores_dinamicos["cont_discentes"] = cont_discentes#**posteriomente, posso usar o con_entry_button, após add um botão de remoção**
                        dict_dados_aux[chave_dicionario].append(valor)#armazena os valores em um dicionario de listas auxiliar
                        valores_dinamicos[chave_dicionario] = dict_dados_aux[chave_dicionario]#atualiza os valores dinamicos com os valores do dicionario aux
                else:#se não houver cont, significa que é uma string simples e não utiliza lista
                    #valores_dinamicos[nome] = None if valor == "Selecione" else valor
                    valores_dinamicos[nome] = valor

                    # else:
                    #     valores_dinamicos[nome] = valor


        # Debug: imprimir dados
        print("Número da Resolução:", numero_res)
        print("Data da Resolução:", data_res)
        print("Data da Reunião:", data_reuniao)
        print("Ad Referendum:", ad_referendum)
        print("Campos dinâmicos:")
        for nome, valor in valores_dinamicos.items():
            print(f"  {nome}: {valor}")

        return numero_res, data_res, data_reuniao, ad_referendum, valores_dinamicos, configs_avancadas

    def gerar_resolucao(self):
        # Captura os dados
        numero_res, data_res, data_reuniao, ad_referendum, valores_dinamicos, configs_avancadas = self.capturar_dados()
        print("**VALORES DINAMICOS: ", valores_dinamicos)

        # modelos.tipo_resolução.geraModelo
        getattr(modelos, self.tipos_resolucao[self.tipo_var.get()]).geraModelo(
            numero_res, data_res, ad_referendum, data_reuniao, valores_dinamicos, configs_avancadas)

    # def iniciar(self):
    #     self.janela.mainloop()