class Pergunta:
    def __init__(self, texto, alternativas=None):
        self.texto = texto
        self.alternativas = alternativas if alternativas else []

