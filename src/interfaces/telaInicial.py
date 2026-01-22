import customtkinter as ctk
from PIL import Image, ImageTk

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
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.frame_esquerdo = ctk.CTkFrame(self)
        self.frame_esquerdo.grid(row=0, column=0, sticky="nsew")

        self.frame_direito = ctk.CTkFrame(self, fg_color='#C0B8B8')
        self.frame_direito.grid(row=0, column=1, sticky="nsew")

        # FRAME ESQUERDO
        # Inserção da imagem principal no frame esquerdo
        img = Image.open('src/static/img/capa tela inicial.png')
        #self.img_principal = ImageTk.PhotoImage(img)

        self.img_principal = ctk.CTkImage(
            light_image=img,
            dark_image=img,  # opcional, mas recomendado
            size=(400, 600)  # tamanho desejado
        )

        self.img_principal_label = ctk.CTkLabel(self.frame_esquerdo, text='', image=self.img_principal)
        self.img_principal_label.grid(row=0, column=0, sticky='nsew')


        #FRAME DIREITO

        # Configuração do background
        background = Image.open('src/static/img/background tela inicial.png')
        # self.img_principal = ImageTk.PhotoImage(img)

        self.background = ctk.CTkImage(
            light_image=background,
            dark_image=background,  # opcional, mas recomendado
            size=(400, 600)  # tamanho desejado
        )

        # Criação do Frame que comportará o conteúdo do frame direito
        self.background_label = ctk.CTkLabel(self.frame_direito, text='', image=self.background)
        self.background_label.grid(row=0, column=0, sticky='nsew')#.place(x=0, y=0, relwidth=1, relheight=1)#

        self.conteudo_frame = ctk.CTkFrame(self.background_label, fg_color='transparent')
        self.conteudo_frame.grid(row=0, column=0)

        # self.conteudo_frame.grid_columnconfigure(0, weight=1)
        # self.conteudo_frame.grid_columnconfigure(1, weight=1)

        # Conteúdo do frame direito
        self.texto_frame = ctk.CTkFrame(self.conteudo_frame, fg_color='transparent')
        self.texto_frame.grid(row=0, column=0)

        self.bem_vindo_label = ctk.CTkLabel(self.texto_frame, text="Seja bem-vindo ao", text_color='black', font=('Poppins', 22), anchor='w')
        self.bem_vindo_label.grid(row=0, column=0, sticky='w')#.pack(pady=10, side='left')

        self.gerador_resolucoes_label = ctk.CTkLabel(self.texto_frame, text="Gerador de Resoluções do PPGCTA", text_color='#587800', font=('Poppins', 22, 'bold'), anchor='w')
        self.gerador_resolucoes_label.grid(row=1, column=0, sticky='w')#.pack(pady=5, side='left')


        self.botoes_frame = ctk.CTkFrame(self.conteudo_frame, fg_color='transparent')
        self.botoes_frame.grid(row=1, column=0, pady=(50,0))

        self.criar_button = ctk.CTkButton(self.botoes_frame, text="Criar Resoluções", fg_color='#749619', border_color='black', border_width=1, width=200, height=80, font=('Manrope', 22), corner_radius=20)
        self.criar_button.grid(row=0, column=0, pady=10)

        self.gerenciar_button = ctk.CTkButton(self.botoes_frame, text="Gerenciar", fg_color='#749619', border_color='black', border_width=1, width=200, height=80, font=('Manrope', 22), corner_radius=20)
        self.gerenciar_button.grid(row=1, column=0)

        self.logo_frame = ctk.CTkFrame(self.conteudo_frame, fg_color='transparent')
        self.logo_frame.grid(row=2, column=0, pady=(20, 0))

        img_logo = Image.open('src/static/img/PPGCTA.png')
        # self.img_principal = ImageTk.PhotoImage(img)

        self.logo = ctk.CTkImage(
            light_image=img_logo,
            dark_image=img_logo,  # opcional, mas recomendado
            size=(110, 65)  # tamanho desejado
        )

        self.logo_label = ctk.CTkLabel(self.logo_frame, text='', image=self.logo, anchor='e')
        self.logo_label.grid(row=0, column=0, sticky='e')

    # def redimensionar_imagem(self, event): # fará o ajuste automático do tamanho da imagem para que ocupe o frame esquerdo
    #     w, h = event.width, event.height
    #
    #     img = self.img_original.resize(
    #         (w, h),
    #         Image.Resampling.LANCZOS
    #     )
    #
    #     self.ctk_img = ctk.CTkImage(
    #         light_image=img,
    #         dark_image=img,
    #         size=(w, h)
    #     )
    #
    #     self.bg_label.configure(image=self.ctk_img)

    # def redimensionar_imagem(self, event):
    #     if event.width <= 1 or event.height <= 1:
    #         return
    #
    #     w, h = event.width, event.height
    #
    #     img = self.img_original.resize(
    #         (w, h),
    #         Image.Resampling.LANCZOS
    #     )
    #
    #     self.ctk_img = ctk.CTkImage(
    #         light_image=img,
    #         dark_image=img,
    #         size=(event.width, event.height)
    #     )
    #
    #     self.bg_label.configure(image=self.ctk_img)
    def iniciar(self):
        self.janela.mainloop()