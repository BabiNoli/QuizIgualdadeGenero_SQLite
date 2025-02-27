from Quiz_package.MensagensInteracaoUsuario import MensagensInteracaoUsuario


class MensagensAlemao(MensagensInteracaoUsuario):
    def __init__(self, nome):
        super().__init__()
        self.idioma = "3"
        self.nome = nome

    def mensagem_invalida(self):
        return "Ungültiger Eintrag. Bitte versuche es erneut."

    def mensagem_invalida_pin(self):
        return "Ungültiger Pin-Eintrag. Die Pin muss bis zu 8 Ziffern lang sein."

    def mensagem_resultado_final(self, porcentagem, nome):
        if porcentagem >= 90:
            return f"Glückwunsch {nome}, Du bist eine große Führungspersönlichkeit! Deine Bewusstsein für die Gleichstellung der Geschlechter inspiriert andere dazu, überkommene Paradigmen zu ändern. Mach weiter so!!!"
        elif porcentagem >= 70:
            return f"Gute Arbeit, {nome}. Du hast ein gutes Verständnis des Themas."
        elif porcentagem >= 40:
            return f"Du bist auf dem richtigen Weg, {nome}. Erkunde das Thema weiter!"
        else:
            return f"Wow {nome}, das hätte ich nicht erwartet!!! Denke darüber nach, recherchiere und sprich mit deinen Mitmenschen. Es ist nie zu spät, etwas zu lernen."

    def mensagem_resultado_porcentagem(self, porcentagem):
        return f"Dein Endergebnis beträgt {porcentagem:.2f}%."

    def mensagem_pontuacao_maxima(self, pontuacao_maxima):
        return f"Deine höchste Punktzahl bisher: {pontuacao_maxima:.2f}%"

    def mensagem_registro_sucesso(self):
        return "Benutzer erfolgreich registriert!"

    def mensagem_login_sucesso(self):
        return "Login erfolgreich!"

    @property
    def titulo_aviso(self):
        return "Warnung"

    @property
    def titulo_erro(self):
        return "Fehler"

    @property
    def titulo_info(self):
        return "Information"

    # Botões

    @property
    def btn_continuar(self):
        return "Fortfahren"

    @property
    def btn_proxima(self):
        return "Nächste Frage"

    @property
    def btn_jogar_novamente(self):
        return "Nochmal spielen"

    @property
    def btn_sair(self):
        return "Beenden"

    # Radiobutton
    @property
    def radio_login(self):
        return "Login"

    @property
    def radio_registro(self):
        return "Registrierung"

    @property
    def radio_sem_registro(self):
        return "Ohne Registrierung spielen"

    @property
    def label_nome(self):
        return "Name:"

    @property
    def label_idade(self):
        return "Alter:"

    @property
    def label_genero(self):
        return "Geschlecht (1:Weiblich / 2:Männlich / 3:Neutral):"

    @property
    def label_pin(self):
        return "PIN:"

    def titulo_login_registro(self):
        return "Login / Anmeldung"

