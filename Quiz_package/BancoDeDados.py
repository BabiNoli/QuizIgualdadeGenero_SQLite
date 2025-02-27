import os
import sys
import sqlite3
from Quiz_package.util import get_persistent_db_path

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



class BancoDeDados:
    def __init__(self, db_path=None):
        # Se não for passado um caminho, utiliza o bdQuiz.db a partir do resource_path.
        if db_path is None:
            db_path = get_persistent_db_path("bdQuiz.db")
        self.database_path = db_path
        self.connection = self.create_connection()


    def create_connection(self):
        try:
            connection = sqlite3.connect(self.database_path)
            connection.row_factory = sqlite3.Row  # Configura para retornar sqlite3.Row
            print("Conexão com o banco de dados SQLite estabelecida!")
            return connection
        except sqlite3.Error as e:
            print("Erro ao conectar com o banco de dados:", e)
            return None


    def buscar_perguntas(self, idioma):
        if not self.connection:
            return []
        # Adapta a consulta para SQLite: ORDER BY RANDOM()
        if idioma == "1":
            query = """SELECT id_pergunta, texto_pergunta AS texto_pergunta, tipo_pergunta 
                       FROM perguntas ORDER BY RANDOM() LIMIT 10"""
        elif idioma == "2":
            query = """SELECT id_pergunta, texto_pergunta_ingles AS texto_pergunta, tipo_pergunta 
                       FROM perguntas ORDER BY RANDOM() LIMIT 10"""
        else:
            query = """SELECT id_pergunta, texto_pergunta_alemao AS texto_pergunta, tipo_pergunta 
                       FROM perguntas ORDER BY RANDOM() LIMIT 10"""

        cursor = self.connection.cursor()
        cursor.execute(query)
        # Converte cada linha para um dicionário
        results = [dict(row) for row in cursor.fetchall()]
        return results


    def buscar_alternativas(self, id_pergunta, tipo_pergunta, idioma):
        if not self.connection:
            return []
        if idioma == "1":  # Português
            if tipo_pergunta == 1:
                query = """SELECT texto_resposta, peso 
                           FROM resposta_multipla 
                           WHERE Perguntas_id_pergunta = ? ORDER BY RANDOM()"""
            else:
                query = """SELECT texto_resposta, peso 
                           FROM verdadeiro_falso 
                           WHERE Perguntas_id_pergunta = ? ORDER BY RANDOM()"""
        elif idioma == "2":  # Inglês
            if tipo_pergunta == 1:
                query = """SELECT texto_resposta_ingles AS texto_resposta, peso 
                           FROM resposta_multipla 
                           WHERE Perguntas_id_pergunta = ? ORDER BY RANDOM()"""
            else:
                query = """SELECT texto_resposta_ingles AS texto_resposta, peso 
                           FROM verdadeiro_falso 
                           WHERE Perguntas_id_pergunta = ? ORDER BY RANDOM()"""
        else:  # Alemão
            if tipo_pergunta == 1:
                query = """SELECT texto_resposta_alemao AS texto_resposta, peso 
                           FROM resposta_multipla 
                           WHERE Perguntas_id_pergunta = ? ORDER BY RANDOM()"""
            else:
                query = """SELECT texto_resposta_alemao AS texto_resposta, peso 
                           FROM verdadeiro_falso 
                           WHERE Perguntas_id_pergunta = ? ORDER BY RANDOM()"""

        cursor = self.connection.cursor()
        cursor.execute(query, (id_pergunta,))
        results = [dict(row) for row in cursor.fetchall()]
        return results

    def registrar_usuario(self, nome, idade, genero, pin):
        if not self.connection:
            return False
        try:
            cursor = self.connection.cursor()
            query = "INSERT INTO usuario (nome, idade, genero, pin) VALUES (?, ?, ?, ?)"
            cursor.execute(query, (nome, idade, genero, pin))
            self.connection.commit()
            return True
        except sqlite3.Error as e:
            print("Erro ao registrar usuário:", e)
            return False

    def login_usuario(self, nome, pin):
        if not self.connection:
            return None
        try:
            cursor = self.connection.cursor()
            query = "SELECT * FROM usuario WHERE nome = ? AND pin = ?"
            cursor.execute(query, (nome, pin))
            row = cursor.fetchone()
            if row:
                return dict(row)
            else:
                return None
        except sqlite3.Error as e:
            print("Erro no login:", e)
            return None

    def atualizar_pontuacao(self, nome, pin, pontuacao_atual):
        if not self.connection:
            return
        try:
            cursor = self.connection.cursor()
            # Utiliza a função max() do SQLite para comparar valores
            query = """
                UPDATE usuario
                SET pont_max = max(pont_max, ?),
                    pont_atual = ?
                WHERE nome = ? AND pin = ?
            """
            cursor.execute(query, (pontuacao_atual, pontuacao_atual, nome, pin))
            self.connection.commit()
        except sqlite3.Error as e:
            print("Erro ao atualizar pontuação:", e)

    def buscar_pontuacao_maxima(self, nome, pin):
        if not self.connection:
            return 0
        try:
            cursor = self.connection.cursor()
            query = "SELECT pont_max FROM usuario WHERE nome = ? AND pin = ?"
            cursor.execute(query, (nome, pin))
            result = cursor.fetchone()
            if result and result[0] is not None:
                return result[0]
            else:
                return 0
        except sqlite3.Error as e:
            print("Erro ao buscar pontuação máxima:", e)
            return 0

