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

        self.frame_direito = ctk.CTkFrame(self)
        self.frame_direito.grid(row=0, column=1, sticky="nsew")

        #img_principal_path = 'src/static/img/capa tela inicial.png'

        #self.inserir_imagem(img_principal_path)

        img = Image.open('src/static/img/capa tela inicial.png')
        #self.img_principal = ImageTk.PhotoImage(img)

        self.img_principal = ctk.CTkImage(
            light_image=img,
            dark_image=img,  # opcional, mas recomendado
            size=(400, 600)  # tamanho desejado
        )

        self.img_original_label = ctk.CTkLabel(self.frame_esquerdo, text='', image=self.img_principal)
        self.img_original_label.grid(row=0, column=0, sticky='nsew')

        # ctk.CTkLabel(
        #     self.frame_direito,
        #     text="Conteúdo do sistema",
        #     font=("Segoe UI", 22)
        # ).pack(expand=True)

        background = Image.open('src/static/img/background tela inicial.png')
        # self.img_principal = ImageTk.PhotoImage(img)

        self.background = ctk.CTkImage(
            light_image=background,
            dark_image=background,  # opcional, mas recomendado
            size=(400, 600)  # tamanho desejado
        )

        self.background_label = ctk.CTkLabel(self.frame_direito, text='', image=self.background)
        self.background_label.grid(row=0, column=0, sticky='nsew')#.place(x=0, y=0, relwidth=1, relheight=1)#

        # self.overlay_frame = ctk.CTkFrame(
        #     self.background_label,
        #     fg_color="tranpas"
        # )
        # self.overlay_frame.place(x=0, y=0, relwidth=1, relheight=1)
        #

        frame = ctk.CTkFrame(self.background_label, fg_color='transparent')
        frame.grid(row=0, column=0)

        button = ctk.CTkButton(frame, text="Botão")
        button.grid(row=0, column=0)#.place(relx=0.5, rely=0.6, anchor="center")

        button2 = ctk.CTkButton(frame, text="Botão 2")
        button2.grid(row=1, column=0)


        # self.grid_columnconfigure(0, weight=1)
        # self.grid_columnconfigure(1, weight=1)
        # # self.janela.grid_rowconfigure(0, weight=1)
        # # self.janela.grid_rowconfigure(1, weight=1)
        #
        # self.titulo_janela_label = ctk.CTkLabel(self, text="Seja bem-vindo ao Gerador de Resoluções do PPGCTA", font=('Segoe UI', 25))
        # self.titulo_janela_label.grid(row=0, column=0, columnspan=2, pady=10)
        #
        # self.tela_principal_button = ctk.CTkButton(self, text="Criar Resoluções", height=60, font=('Segoe UI', 15), command=self.master.exibir_tela_principal)\
        #     .grid(row=1, column=0, sticky='ew', pady=20, padx=(10, 10))
        # self.tela_gerencia_button = ctk.CTkButton(self, text="Gerenciar", height=60, font=('Segoe UI', 15), command=self.master.exibir_tela_gerencia)\
        #     .grid(row=1, column=1, sticky='ew', pady=20, padx=(10, 10))


    # def inserir_imagem(self, img_path):
    #
    #     self.img_original = Image.open(img_path)
    #
    #     self.bg_label = ctk.CTkLabel(self.frame_esquerdo, text="")
    #     self.bg_label.grid(row=0, column=0, sticky='nsew')
    #
    #     self.frame_esquerdo.grid_rowconfigure(0, weight=1)
    #     self.frame_esquerdo.grid_columnconfigure(0, weight=1)
    #
    #     self.frame_esquerdo.bind("<Configure>", self.redimensionar_imagem)

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