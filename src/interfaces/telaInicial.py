import customtkinter as ctk
from PIL import Image, ImageTk
import pywinstyles


class TelaInicial(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.geometry("800x600")
        self.master.state("normal")
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
            dark_image=background,
            size=(400, 600)
        )

        # Criação do Frame que comportará o conteúdo do frame direito
        self.background_label = ctk.CTkLabel(self.frame_direito, text='', image=self.background)
        self.background_label.grid(row=0, column=0, sticky='nsew')#.place(x=0, y=0, relwidth=1, relheight=1)#
        #pywinstyles.set_opacity(self.background_label, color='#FFFBEC', value=0.8)


        self.conteudo_frame = ctk.CTkFrame(self.background_label, fg_color='#FFFBEC')
        self.conteudo_frame.grid(row=0, column=0)
        pywinstyles.set_opacity(self.conteudo_frame, color='#FFFBEC', value=1)

        # self.conteudo_frame.grid_columnconfigure(0, weight=1)
        # self.conteudo_frame.grid_columnconfigure(1, weight=1)

        # Conteúdo do frame direito
        self.texto_frame = ctk.CTkFrame(self.conteudo_frame, fg_color='transparent')
        self.texto_frame.grid(row=0, column=0)

        self.bem_vindo_label = ctk.CTkLabel(self.texto_frame, text="Bem-vindo ao", text_color='black', font=('Poppins', 22), anchor='w')
        self.bem_vindo_label.grid(row=0, column=0, sticky='w')#.pack(pady=10, side='left')

        self.gerador_resolucoes_label = ctk.CTkLabel(self.texto_frame, text="Gerador de Resoluções", width=300, text_color='#587800', font=('Poppins', 22, 'bold'), anchor='w')
        self.gerador_resolucoes_label.grid(row=1, column=0, sticky='w')#.pack(pady=5, side='left')

        self.ppgcta_label = ctk.CTkLabel(self.texto_frame, text="do PPGCTA",
                                                     text_color='#587800', font=('Poppins', 22, 'bold'), anchor='w')
        self.ppgcta_label.grid(row=2, column=0, sticky='w')  # .pack(pady=5, side='left')


        self.botoes_frame = ctk.CTkFrame(self.conteudo_frame, fg_color='transparent')
        self.botoes_frame.grid(row=1, column=0, pady=(50,0))
        #pywinstyles.set_opacity(self.botoes_frame, color='transparent', value=1)

        criar_icon = Image.open('src/static/img/criar icon.png')
        self.criar_icon = ctk.CTkImage(
            light_image=criar_icon,
            dark_image=criar_icon,
            size=(30, 30)
        )

        self.criar_button = ctk.CTkButton(self.botoes_frame, text="Criar Resoluções", image=self.criar_icon, compound='left', fg_color='#749619', border_color='black', hover_color='#4F6416', border_width=2, width=250, height=80, font=('Manrope', 22), corner_radius=15)
        self.criar_button.grid(row=0, column=0, pady=10)

        gerenciar_icon = Image.open('src/static/img/gerencia icon.png')
        self.gerenciar_icon = ctk.CTkImage(
            light_image=gerenciar_icon,
            dark_image=gerenciar_icon,
            size=(30, 30)
        )

        self.gerenciar_button = ctk.CTkButton(self.botoes_frame, text="Gerenciar", image=self.gerenciar_icon, compound='left', fg_color='#749619', border_color='black', hover_color='#4F6416', border_width=2, width=250, height=80, font=('Manrope', 22), corner_radius=15,
                                              command=self.master.exibir_tela_gerencia)
        self.gerenciar_button.grid(row=1, column=0)

        self.logo_frame = ctk.CTkFrame(self.conteudo_frame, fg_color='transparent')
        self.logo_frame.grid(row=2, column=0, pady=(60, 0), sticky='e')

        img_logo = Image.open('src/static/img/PPGCTA.png')
        # self.img_principal = ImageTk.PhotoImage(img)

        self.logo = ctk.CTkImage(
            light_image=img_logo,
            dark_image=img_logo,
            size=(110, 65)
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