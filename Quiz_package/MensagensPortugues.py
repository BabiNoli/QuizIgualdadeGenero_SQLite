from Quiz_package.MensagensInteracaoUsuario import MensagensInteracaoUsuario


class MensagensPortugues(MensagensInteracaoUsuario):
    def __init__(self, nome):
        super().__init__()
        self.idioma = "1"
        self.nome = nome


    def mensagem_invalida(self):
        return "Entrada inválida. Por favor tente novamente."

    def mensagem_invalida_pin(self):
        return "Entrada inválida do Pin. O Pin deve ser de até 8 digitos numéricos."

    def mensagem_resultado_final(self, porcentagem, nome):
        if porcentagem >= 90:
            return f"Parabéns {nome}, você arrasou! Sua consciência de igualdade de gênero inspira outros a mudar paradigmas ultrapassados. Continue assim!!!"

        elif porcentagem >= 70:
            return f"Muito bem {nome}, Você tem uma boa base sobre o assunto."

        elif porcentagem >= 40:
            return f"Você está no caminho certo, {nome}, pesquise um pouco mais sobre o tema!"

        else:
            return f"Poxa {nome}, não esperava por isso!!! Reflita sobre o tema, pesquise e conversa com as pessoas a sua volta. Nunca é tarde para aprender."

    def mensagem_resultado_porcentagem(self, porcentagem):
        return f"Sua pontuação foi de {porcentagem:.2f}%."

    def mensagem_pontuacao_maxima(self, pontuacao_maxima):
        return f"Sua maior pontuação salva é: {pontuacao_maxima:.2f}%"

    def mensagem_registro_sucesso(self):
        return "Utilizador registrado com sucesso!"

    def mensagem_login_sucesso(self):
        return "Login bem-sucedido!"

    # Títulos (messagebox)
    @property
    def titulo_aviso(self):
        return "Aviso"

    @property
    def titulo_erro(self):
        return "Erro"

    @property
    def titulo_info(self):
        return "Informação"

    # Botões

    @property
    def btn_continuar(self):
        return "Continuar"

    @property
    def btn_proxima(self):
        return "Próxima Pergunta"

    @property
    def btn_jogar_novamente(self):
        return "Jogar Novamente"

    @property
    def btn_sair(self):
        return "Sair"

    # Radiobutton
    @property
    def radio_login(self):
        return "Login"

    @property
    def radio_registro(self):
        return "Registro"

    @property
    def radio_sem_registro(self):
        return "Jogar sem registro"

    # Labels
    @property
    def label_nome(self):
        return "Nome:"

    @property
    def label_idade(self):
        return "Idade:"

    @property
    def label_genero(self):
        return "Gênero (1:Feminino / 2:Masculino / 3:Neutro):"

    @property
    def label_pin(self):
        return "PIN:"

    def titulo_login_registro(self):
        return "Login / Registro"



