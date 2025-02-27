import tkinter as tk
from tkinter import messagebox
from Quiz_package.TelaPerguntas import TelaPerguntas


class TelaLogin(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        """invoca o método construtor (o __init__) da classe base, 
        que neste caso é tk.Frame. Como a classe TelaLogin herda de tk.Frame, 
        é necessário inicializar a parte de widget da classe pai para que todos 
        os comportamentos e propriedades do Frame sejam corretamente configurados."""
        self.master = master
        self.config(bg=self.master.cor_fundo)

        msgs = self.master.jogador.mensagens
        titulo = msgs.titulo_login_registro()

        label_titulo = tk.Label(
            self,
            text=titulo,
            bg=self.master.cor_fundo,
            fg=self.master.cor_texto,
            font=("Arial", 14, "bold"),
            wraplength=850
        )
        label_titulo.pack(pady=10)

        self.escolha_var = tk.StringVar(value="1")
        frame_radios = tk.Frame(self, bg=self.master.cor_fundo)
        frame_radios.pack()

        opcoes = [
            (msgs.radio_login, "1"),
            (msgs.radio_registro, "2"),
            (msgs.radio_sem_registro, "3"),
        ]
        for texto, valor in opcoes:
            tk.Radiobutton(
                frame_radios,
                text=texto,
                variable=self.escolha_var,
                value=valor,
                bg=self.master.cor_fundo,
                fg=self.master.cor_texto,
                font=("Arial", 12),
                anchor="w"
            ).pack(anchor="w", padx=10, pady=2)

        self.frame_campos = tk.Frame(self, bg=self.master.cor_fundo)
        self.frame_campos.pack(pady=10)

        # Nome
        lbl_nome = tk.Label(
            self.frame_campos,
            text=msgs.label_nome,
            bg=self.master.cor_fundo,
            fg=self.master.cor_texto,
            font=("Arial", 12)
        )
        lbl_nome.grid(row=0, column=0, sticky="e", padx=5, pady=5)
        self.entry_nome = tk.Entry(self.frame_campos, width=40)
        self.entry_nome.grid(row=0, column=1, padx=5, pady=5)

        # PIN
        lbl_pin = tk.Label(
            self.frame_campos,
            text=msgs.label_pin,
            bg=self.master.cor_fundo,
            fg=self.master.cor_texto,
            font=("Arial", 12)
        )
        lbl_pin.grid(row=1, column=0, sticky="e", padx=5, pady=5)
        self.entry_pin = tk.Entry(self.frame_campos, width=40, show="*")
        self.entry_pin.grid(row=1, column=1, padx=5, pady=5)

        # Idade
        lbl_idade = tk.Label(
            self.frame_campos,
            text=msgs.label_idade,
            bg=self.master.cor_fundo,
            fg=self.master.cor_texto,
            font=("Arial", 12)
        )
        lbl_idade.grid(row=2, column=0, sticky="e", padx=5, pady=5)
        self.entry_idade = tk.Entry(self.frame_campos, width=40)
        self.entry_idade.grid(row=2, column=1, padx=5, pady=5)

        # Gênero
        lbl_genero = tk.Label(
            self.frame_campos,
            text=msgs.label_genero,
            bg=self.master.cor_fundo,
            fg=self.master.cor_texto,
            font=("Arial", 12)
        )
        lbl_genero.grid(row=3, column=0, sticky="e", padx=5, pady=5)
        self.entry_genero = tk.Entry(self.frame_campos, width=40)
        self.entry_genero.grid(row=3, column=1, padx=5, pady=5)

        self.toggle_campos_extras(False)
        self.escolha_var.trace("w", self.ao_mudar_radio)

        btn_continuar = tk.Button(
            self,
            text=msgs.btn_continuar,
            width=70,
            wraplength=850,
            bg=self.master.cor_botao,
            fg=self.master.cor_texto_botao,
            font=('Arial', 12, 'bold'),
            command=self.processar_escolha
        )
        btn_continuar.pack(pady=15)

    def ao_mudar_radio(self, *args):
        escolha = self.escolha_var.get()
        if escolha == "2":
            self.toggle_campos_extras(True)
        else:
            self.toggle_campos_extras(False)

    def toggle_campos_extras(self, visivel):
        estado = "normal" if visivel else "disabled"
        self.entry_idade.config(state=estado)
        self.entry_genero.config(state=estado)


    def processar_escolha(self):
        msgs = self.master.jogador.mensagens  # Objeto de mensagens no idioma selecionado
        escolha = self.escolha_var.get()
        nome = self.entry_nome.get().strip()
        pin = self.entry_pin.get().strip()


        if escolha in ["1", "2"]:

            if not nome:
                messagebox.showwarning(msgs.titulo_aviso, msgs.mensagem_invalida())
                return

            self.master.jogador.anonimo = False
            self.master.jogador.pin = pin

            if not pin.isdigit() or len(pin) > 8:
                messagebox.showwarning(msgs.titulo_aviso, msgs.mensagem_invalida_pin())
                return

            if escolha == "1":  # LOGIN
                usuario = self.master.db.login_usuario(nome, pin)
                if usuario:
                    messagebox.showinfo(msgs.titulo_info, msgs.mensagem_login_sucesso())
                    self.master.jogador.nome = usuario['nome']
                    self.master.mudar_tela(TelaPerguntas)
                else:
                    messagebox.showerror(msgs.titulo_erro, msgs.mensagem_invalida())

            elif escolha == "2":  # REGISTRO
                idade = self.entry_idade.get().strip()
                genero = self.entry_genero.get().strip()

                if not idade or not genero:
                    messagebox.showwarning(msgs.titulo_aviso, msgs.mensagem_invalida())
                    return

                if genero not in ['1', '2', '3']:
                    messagebox.showwarning(msgs.titulo_aviso, msgs.mensagem_invalida())
                    return


                sucesso = self.master.db.registrar_usuario(nome, idade, genero, pin)
                if sucesso:
                    messagebox.showinfo(msgs.titulo_info, msgs.mensagem_registro_sucesso())
                    self.master.jogador.nome = nome
                    self.master.mudar_tela(TelaPerguntas)
                    self.master.jogador.pin = pin
                else:
                    messagebox.showerror(msgs.titulo_erro, msgs.mensagem_invalida())


        elif escolha == "3":  # JOGAR SEM REGISTRO (Sem interação com o banco de dados)
            self.master.jogador.anonimo = True
            if nome:
                self.master.jogador.nome = nome
            else:
                self.master.jogador.nome = 'User' #Nome usado por padrao caso o usuario nao insira um nome
            self.master.mudar_tela(TelaPerguntas)





