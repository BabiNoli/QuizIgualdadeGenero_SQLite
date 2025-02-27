from Quiz_package.Alternativa import Alternativa
from Quiz_package.Pergunta import Pergunta


class Quiz:
    def __init__(self, banco_dados, jogador):
        self.banco_dados = banco_dados
        self.jogador = jogador
        self.idioma = jogador.idioma
        self.perguntas = []
        self.pontuacao = 0
        self.indice_atual = 0
        self.carregar_perguntas()

    def carregar_perguntas(self):
        perguntas_banco = self.banco_dados.buscar_perguntas(self.idioma)
        for p in perguntas_banco:
            id_pergunta = p['id_pergunta']
            tipo_pergunta = p['tipo_pergunta']
            texto_pergunta = p['texto_pergunta']

            alts_banco = self.banco_dados.buscar_alternativas(id_pergunta, tipo_pergunta, self.idioma)
            alts = [Alternativa(alt['texto_resposta'], alt['peso']) for alt in alts_banco]

            pergunta = Pergunta(texto_pergunta, alts)
            self.perguntas.append(pergunta)

    def proxima_pergunta(self):
        if self.indice_atual < len(self.perguntas):
            p = self.perguntas[self.indice_atual]
            self.indice_atual += 1
            return p
        return None

    def incrementar_pontuacao(self, peso):
        self.pontuacao += peso

    def reiniciar_quiz(self):
        self.pontuacao = 0
        self.indice_atual = 0
        self.perguntas.clear()
        self.carregar_perguntas()
