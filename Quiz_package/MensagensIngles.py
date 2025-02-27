from Quiz_package.MensagensInteracaoUsuario import MensagensInteracaoUsuario


class MensagensIngles(MensagensInteracaoUsuario):
    def __init__(self, nome):
        super().__init__()
        self.idioma = "2"
        self.nome = nome


    def mensagem_invalida(self):
        return "Invalid entry. Please try again."

    def mensagem_invalida_pin(self):
        return "Invalid Pin entry. The Pin must be up to 8 numeric digits."

    def mensagem_resultado_final(self, porcentagem, nome):
        if porcentagem >= 90:
            return f"Congratulations {nome}! You are a great leader! Your consciousness of equal gender inspires others to change paradigms that have been surpassed. Keep it up!!!"

        elif porcentagem >= 70:
            return f"Good job, {nome}. You have a solid understanding of the subject."

        elif porcentagem >= 40:
            return f"You are on the right path, {nome}. Search a bit more about this topic!"

        else:
            return f"Wow, {nome}. I didn't expect that!!! Think about it, do some research and talk to the people around you. It's never too late to learn."

    def mensagem_resultado_porcentagem(self, porcentagem):
        return f"Your final score is {porcentagem:.2f}%."

    def mensagem_pontuacao_maxima(self, pontuacao_maxima):
        return f"Your highest score so far: {pontuacao_maxima:.2f}%"

    def mensagem_registro_sucesso(self):
        return "User successfully registered!"

    def mensagem_login_sucesso(self):
        return "Login successful!"


    @property
    def titulo_aviso(self):
        return "Warning"

    @property
    def titulo_erro(self):
        return "Error"

    @property
    def titulo_info(self):
        return "Information"

    # Botões

    @property
    def btn_continuar(self):
        return "Continue"

    @property
    def btn_proxima(self):
        return "Next Question"

    @property
    def btn_jogar_novamente(self):
        return "Play Again"

    @property
    def btn_sair(self):
        return "Exit"

    # Radiobutton
    @property
    def radio_login(self):
        return "Login"

    @property
    def radio_registro(self):
        return "Register"

    @property
    def radio_sem_registro(self):
        return "Play without registration"

    # Labels
    @property
    def label_nome(self):
        return "Name:"

    @property
    def label_idade(self):
        return "Age:"

    @property
    def label_genero(self):
        return "Gender (1:Female / 2:Male / 3:Neutral):"

    @property
    def label_pin(self):
        return "PIN:"

    def titulo_login_registro(self):
        return "Login / Register"
