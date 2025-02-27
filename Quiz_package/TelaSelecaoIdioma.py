import tkinter as tk
from tkinter import messagebox, ttk
from Quiz_package.MensagensPortugues import MensagensPortugues
from Quiz_package.MensagensIngles import MensagensIngles
from Quiz_package.MensagensAlemao import MensagensAlemao
from Quiz_package.TelaLogin import TelaLogin


class TelaSelecaoIdioma(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.config(bg=self.master.cor_fundo)

        label_instr = tk.Label(
            self,
            text="Escolha seu idioma / Choose your language / Wähle deine Sprache:",
            bg=self.master.cor_fundo,
            fg=self.master.cor_texto,
            font=("Arial", 14, "bold"),
            wraplength=850
        )
        label_instr.pack(pady=10)

        self.opcoes_idioma = {"Português": "1", "English": "2", "Deutsch": "3"}
        self.idioma_var = tk.StringVar()
        self.combo_idioma = ttk.Combobox(
            self,
            textvariable=self.idioma_var,
            values=list(self.opcoes_idioma.keys()),
            state="readonly",
            width=30
        )
        self.combo_idioma.pack(pady=10)
        self.combo_idioma.current(0)

        btn_confirmar = tk.Button(
            self,
            text="Confirm",
            width=70,
            wraplength=850,
            bg=self.master.cor_botao,
            fg=self.master.cor_texto_botao,
            font=('Arial', 12, 'bold'),
            command=self.definir_idioma
        )
        btn_confirmar.pack(pady=20)

    def definir_idioma(self):
        escolha = self.combo_idioma.get()
        if escolha in self.opcoes_idioma:
            idioma_escolhido = self.opcoes_idioma[escolha]
            self.master.jogador.idioma = idioma_escolhido

            if idioma_escolhido == "1":
                self.master.jogador.mensagens = MensagensPortugues(self.master.jogador.nome)
            elif idioma_escolhido == "2":
                self.master.jogador.mensagens = MensagensIngles(self.master.jogador.nome)
            else:
                self.master.jogador.mensagens = MensagensAlemao(self.master.jogador.nome)

            self.master.mudar_tela(TelaLogin)
        else:
            messagebox.showwarning("Aviso", "Seleção de idioma inválida.")
