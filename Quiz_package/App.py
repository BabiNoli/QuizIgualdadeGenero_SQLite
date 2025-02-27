import os, sys

# Remover quaisquer definições existentes
os.environ.pop("TCL_LIBRARY", None)
os.environ.pop("TK_LIBRARY", None)

if getattr(sys, 'frozen', False):
    # Se estiver congelado, use os diretórios extraídos
    os.environ['TCL_LIBRARY'] = os.path.join(sys._MEIPASS, "_tcl_data")
    os.environ['TK_LIBRARY']  = os.path.join(sys._MEIPASS, "_tk_data")
else:
    # Se não estiver congelado, use a variável personalizada ou o caminho padrão do Python 3.12
    tcl_base = os.environ.get("TCL_LIBRARY_312", r"C:\Users\barba\AppData\Local\Programs\Python\Python312\tcl")
    os.environ['TCL_LIBRARY'] = os.path.join(tcl_base, "tcl8.6")
    os.environ['TK_LIBRARY']  = os.path.join(tcl_base, "tk8.6")

print("TCL_LIBRARY:", os.environ['TCL_LIBRARY'])
print("TK_LIBRARY:", os.environ['TK_LIBRARY'])
print("Python executável:", sys.executable)
print("Versão do Python:", sys.version)



import tkinter as tk
from Quiz_package.util import resource_path
from Quiz_package.Jogador import Jogador
from Quiz_package.BancoDeDados import BancoDeDados
from Quiz_package.TelaSelecaoIdioma import TelaSelecaoIdioma
from Quiz_package.Musica import Musica

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.cor_fundo = "#ECECEC"
        self.cor_texto = "#333333"
        self.cor_botao = "#4CAF50"
        self.cor_texto_botao = "#FFFFFF"

        self.title("Quiz Igualdade de Gênero")
        # Janela para perguntas
        self.geometry("1000x550")
        self.configure(bg=self.cor_fundo)
        self.option_add('*Font', 'Arial')

        # Cria gerenciador de música
        self.musica = Musica()
        # Cria botão de som no canto superior direito
        self.btn_som = tk.Button(
            self, text="🔊🎵", font=("Arial", 14, "bold"),
            bg="white", fg="black", command=self.alternar_musica
        )
        self.btn_som.place(x=925, y=20, width=55, height=40)

        # Aplica imagem a janela (se disponível)
        try:
            logo_path = resource_path("logo2.png")
            print("Caminho para logo:", logo_path)
            self.icone_app = tk.PhotoImage(file=logo_path)
            self.label_icone = tk.Label(self, image=self.icone_app, bg=self.cor_fundo)
            self.label_icone.pack(pady=10)  # Adiciona a label na interface
        except Exception as e:
            print("Erro ao carregar logo:", e)

        # Cria a conexão com o banco SQLite (arquivo local)
        self.db = BancoDeDados()
        self.jogador = Jogador()
        self.quiz = None

        self._frame_atual = None
        self.mudar_tela(TelaSelecaoIdioma)

    def alternar_musica(self):
        # Liga ou desliga a música de fundo e atualiza o botão.
        self.musica.alternar_musica()
        self.btn_som.config(text='🔊🎵' if self.musica.musica_ativa else '🔇🎵')

    def mudar_tela(self, classe_tela):
        if self._frame_atual is not None:
            self._frame_atual.destroy()
        self._frame_atual = classe_tela(self)
        self._frame_atual.pack(pady=5)


if __name__ == "__main__":
    app = App()
    app.mainloop()
