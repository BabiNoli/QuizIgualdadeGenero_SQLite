import sys, os

def resource_path(relative_path):
    """Retorna o caminho absoluto para um recurso.
       Se estiver congelado, usa sys._MEIPASS, caso contrário, usa o caminho atual."""
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    path = os.path.join(base_path, relative_path)
    print("resource_path:", path)  # Debug
    return path

from pygame import mixer

class Musica:
    def __init__(self, arquivo=None, volume=0.3):
        # Se não for fornecido um caminho, usa o arquivo padrão
        if arquivo is None:
            arquivo = resource_path("musica_instrumental.mp3")
        self.arquivo = arquivo
        self.volume = volume

        # Debug: imprimir o caminho calculado para a música
        print("Caminho para música:", self.arquivo)

        mixer.init()
        self.musica_ativa = True
        try:
            mixer.music.load(self.arquivo)
        except Exception as e:
            raise FileNotFoundError(f"Erro ao carregar o arquivo de música: {self.arquivo}\n{e}")
        mixer.music.set_volume(self.volume)
        mixer.music.play(-1)  # -1 significa tocar em loop

    def alternar_musica(self):
        if self.musica_ativa:
            mixer.music.pause()
        else:
            mixer.music.unpause()
        self.musica_ativa = not self.musica_ativa
