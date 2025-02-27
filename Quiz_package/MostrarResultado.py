class MostrarResultado:
    def __init__(self, total_perguntas, jogador, pontuacao):
        self.anonimo = jogador.anonimo
        self.nome = jogador.nome
        self.pontuacao = pontuacao
        self.total_perguntas = total_perguntas
        self.mensagens = jogador.mensagens


    def obter_resultado(self):


        global pontuacao_maxima
        if self.total_perguntas == 0:
            porcentagem = 0
        else:
            pontuacao_maxima = self.total_perguntas * 100
            porcentagem = (self.pontuacao / pontuacao_maxima) * 100

        if  self.anonimo:

            msg_final = self.mensagens.mensagem_resultado_final(porcentagem, self.nome)
            msg_perc = self.mensagens.mensagem_resultado_porcentagem(porcentagem)
            return msg_final, msg_perc, porcentagem

        if not self.anonimo:  # Só salva se o jogador estiver logado
            msg_final = self.mensagens.mensagem_resultado_final(porcentagem, self.nome)
            msg_perc = self.mensagens.mensagem_resultado_porcentagem(porcentagem)
            msg_max = self.mensagens.mensagem_pontuacao_maxima(pontuacao_maxima)
            return msg_final, msg_perc, porcentagem, msg_max, pontuacao_maxima



