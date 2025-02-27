import os
import sys
import shutil

def resource_path(relative_path):
    """
    Retorna o caminho absoluto para um recurso.
    Se estiver congelado (executável onefile), usa sys._MEIPASS;
    caso contrário, usa o diretório atual.
    """
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


def get_persistent_db_path(filename="bdQuiz.db"):
    """
    Retorna o caminho para o banco de dados persistente.
    Se não existir, copia o arquivo embutido (via resource_path) para o diretório do executável.
    """
    if getattr(sys, 'frozen', False):
        # Diretório onde o executável está localizado
        persistent_dir = os.path.dirname(sys.executable)
    else:
        persistent_dir = os.path.abspath(".")

    persistent_path = os.path.join(persistent_dir, filename)

    # Se o arquivo persistente não existir, copie-o a partir do recurso embutido.
    if not os.path.exists(persistent_path):
        from Quiz_package.util import resource_path  # ajuste conforme sua estrutura
        source_path = resource_path(filename)
        try:
            shutil.copy2(source_path, persistent_path)
            print(f"Banco de dados copiado para: {persistent_path}")
        except Exception as e:
            print(f"Erro ao copiar o banco de dados: {e}")

    return persistent_path
