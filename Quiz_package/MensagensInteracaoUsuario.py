class MensagensInteracaoUsuario:
    def __init__(self):
        self.idioma = None


    def mensagem_invalida(self):
        raise NotImplementedError

    def mensagem_invalida_pin(self):
        raise NotImplementedError

    def mensagem_resultado_final(self, porcentagem, nome):
        raise NotImplementedError

    def mensagem_resultado_porcentagem(self, porcentagem):
        raise NotImplementedError

    def mensagem_pontuacao_maxima(self, pontuacao_maxima):
        return NotImplementedError

    def mensagem_registro_sucesso(self):
        raise NotImplementedError

    def mensagem_login_sucesso(self):
        raise NotImplementedError

    # Títulos messagebox
    @property
    def titulo_aviso(self):
        raise NotImplementedError

    @property
    def titulo_erro(self):
        raise NotImplementedError

    @property
    def titulo_info(self):
        raise NotImplementedError

    # Botões
    @property
    def btn_confirmar(self):
        raise NotImplementedError

    @property
    def btn_continuar(self):
        raise NotImplementedError

    @property
    def btn_proxima(self):
        raise NotImplementedError

    @property
    def btn_jogar_novamente(self):
        raise NotImplementedError

    @property
    def btn_sair(self):
        raise NotImplementedError

    # Radiobutton
    @property
    def radio_login(self):
        raise NotImplementedError

    @property
    def radio_registro(self):
        raise NotImplementedError

    @property
    def radio_sem_registro(self):
        raise NotImplementedError

    # Labels para Nome, Idade, Gênero, PIN
    @property
    def label_nome(self):
        raise NotImplementedError

    @property
    def label_idade(self):
        raise NotImplementedError

    @property
    def label_genero(self):
        raise NotImplementedError

    @property
    def label_pin(self):
        raise NotImplementedError

    # Título principal da TelaLogin
    def titulo_login_registro(self):
        raise NotImplementedError

