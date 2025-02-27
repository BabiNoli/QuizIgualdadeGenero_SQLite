import tkinter as tk
from Quiz_package.MostrarResultado import MostrarResultado

class TelaResultado(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.config(bg=self.master.cor_fundo)

        quiz = self.master.quiz
        total_perguntas = len(quiz.perguntas)
        mostrar = MostrarResultado(total_perguntas, self.master.jogador, quiz.pontuacao)

        if not self.master.jogador.anonimo:
            msg_final, msg_perc, porcentagem, msg_max, pontuacao_maxima = mostrar.obter_resultado()
        if  self.master.jogador.anonimo:
            msg_final, msg_perc, porcentagem = mostrar.obter_resultado()

        lbl_final = tk.Label(
            self,
            text=msg_final,
            bg=self.master.cor_fundo,
            fg=self.master.cor_texto,
            font=('Arial', 14, 'bold'),
            wraplength=850
        )
        lbl_final.pack(pady=20)

        lbl_perc = tk.Label(
            self,
            text=msg_perc,
            bg=self.master.cor_fundo,
            fg=self.master.cor_texto,
            font=('Arial', 12),
            wraplength=850
        )
        lbl_perc.pack(pady=10)

        # Buscar pontuação máxima do jogador e exibir
        if not  self.master.jogador.anonimo:
            if self.master.jogador.nome:
                pontuacao_maxima = self.master.db.buscar_pontuacao_maxima(self.master.jogador.nome, self.master.jogador.pin)
                msg_pont_max = self.master.jogador.mensagens.mensagem_pontuacao_maxima(pontuacao_maxima)
            else:
                msg_pont_max = self.master.jogador.mensagens.mensagem_pontuacao_maxima(0)  # Caso não haja histórico


            lbl_pont_max = tk.Label(
                self,
                text=msg_pont_max,
                bg=self.master.cor_fundo,
                fg=self.master.cor_texto,
                font=('Arial', 12),
                wraplength=850
            )
            lbl_pont_max.pack(pady=10)


        # --- Aqui atualizamos a pontuação no banco ---
        # Se o jogador tiver nome (i.e., logado ou registrado),
        # atualizamos a pontuação (porcentagem) na tabela.
        if not  self.master.jogador.anonimo:
            if self.master.jogador.nome:

                self.master.db.atualizar_pontuacao(self.master.jogador.nome, self.master.jogador.pin, porcentagem)

        msgs = self.master.jogador.mensagens
        btn_jogar = tk.Button(
            self,
            text=msgs.btn_jogar_novamente,
            width=70,
            wraplength=850,
            bg=self.master.cor_botao,
            fg=self.master.cor_texto_botao,
            font=('Arial', 12, 'bold'),
            command=self.jogar_novamente
        )
        btn_jogar.pack(pady=5)

        btn_sair = tk.Button(
            self,
            text=msgs.btn_sair,
            width=70,
            wraplength=850,
            bg="#D32F2F",
            fg="#FFFFFF",
            font=('Arial', 12, 'bold'),
            command=self.master.destroy
        )
        btn_sair.pack(pady=5)

    def jogar_novamente(self):
        from Quiz_package.TelaPerguntas import TelaPerguntas
        self.master.quiz.reiniciar_quiz()
        self.master.mudar_tela(TelaPerguntas)
