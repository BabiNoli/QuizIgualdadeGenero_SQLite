import tkinter as tk
from tkinter import messagebox
from Quiz_package.Quiz import Quiz
from Quiz_package.TelaResultado import TelaResultado


class TelaPerguntas(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        """invoca o método construtor (o __init__) da classe base, 
        que neste caso é tk.Frame. Como a classe TelaPerguntas herda de tk.Frame, 
        é necessário inicializar a parte de widget da classe pai para que todos 
        os comportamentos e propriedades do Frame sejam corretamente configurados."""
        self.master = master
        self.config(bg=self.master.cor_fundo)

        self.master.quiz = Quiz(self.master.db, self.master.jogador)
        self.total_perguntas = len(self.master.quiz.perguntas)

        self.label_numero = tk.Label(
            self,
            text="",
            bg=self.master.cor_fundo,
            fg=self.master.cor_texto,
            font=('Arial', 12, 'bold')
        )
        self.label_numero.pack(pady=5)

        self.label_pergunta = tk.Label(
            self,
            text="",
            wraplength=850,
            bg=self.master.cor_fundo,
            fg=self.master.cor_texto,
            font=('Arial', 14, 'bold')
        )
        self.label_pergunta.pack(pady=20)

        self.frame_opcoes = tk.Frame(self, bg=self.master.cor_fundo)
        self.frame_opcoes.pack()

        msgs = self.master.jogador.mensagens
        self.btn_proxima = tk.Button(
            self,
            text=msgs.btn_proxima,
            width=70,
            wraplength=850,
            bg=self.master.cor_botao,
            fg=self.master.cor_texto_botao,
            font=('Arial', 12, 'bold'),
            command=self.avancar
        )
        self.btn_proxima.pack(pady=15)

        self.pergunta_atual = None
        self.opcao_var = None
        self.indice_local = 0

        self.exibir_pergunta()

    def exibir_pergunta(self):
        self.pergunta_atual = self.master.quiz.proxima_pergunta()
        if not self.pergunta_atual:
            self.master.mudar_tela(TelaResultado)
            return

        for w in self.frame_opcoes.winfo_children():
            w.destroy()

        self.indice_local += 1
        self.label_numero.config(text=f"{self.indice_local}/{self.total_perguntas}")

        self.label_pergunta.config(text=self.pergunta_atual.texto)
        self.opcao_var = tk.IntVar(value=-1)

        for i, alt in enumerate(self.pergunta_atual.alternativas):
            rb = tk.Radiobutton(
                self.frame_opcoes,
                text=alt.texto,
                variable=self.opcao_var,
                value=i,
                bg=self.master.cor_fundo,
                fg=self.master.cor_texto,
                wraplength=850,
                font=('Arial', 12),
                anchor="w"
            )
            rb.pack(anchor="w", padx=10, pady=5)

    def avancar(self):
        if not self.pergunta_atual:
            self.master.mudar_tela(TelaResultado)
            return

        indice = self.opcao_var.get()
        if indice == -1:
            msgs = self.master.jogador.mensagens
            messagebox.showwarning(msgs.titulo_aviso, msgs.mensagem_invalida())
            return

        peso = self.pergunta_atual.alternativas[indice].peso
        self.master.quiz.incrementar_pontuacao(peso)
        self.exibir_pergunta()

