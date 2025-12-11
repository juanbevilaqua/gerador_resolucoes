import sqlite3
from src.database.databaseConfigs import connect
from dataclasses import dataclass

@dataclass
class Disciplina:
    id: int or None
    nome: str
    carga_horaria: str
    creditos: int

    @staticmethod
    def list_all():
        conn = connect()
        cursor = conn.cursor()

        query = 'SELECT * FROM Disciplinas ORDER BY nome'

        try:
            cursor.execute(query)
            disciplinas = cursor.fetchall()
            return disciplinas
        except sqlite3.Error as e:
            print(f"Erro ao BUSCAR disciplinas cadastradas: {e}")
            return None
        finally:
            conn.close()

    @staticmethod
    def list_all_names():
        conn = connect()
        cursor = conn.cursor()

        query = 'SELECT nome FROM Disciplinas ORDER BY nome'

        try:
            cursor.execute(query)
            disciplinas = cursor.fetchall()
            return disciplinas
        except sqlite3.Error as e:
            print(f"Erro ao BUSCAR nome das disciplinas cadastradas: {e}")
            return None
        finally:
            conn.close()

    @staticmethod
    def get_by_id(id):
        conn = connect()
        cursor = conn.cursor()

        query = 'SELECT * FROM Disciplinas WHERE id_disciplina = ?'

        try:
            cursor.execute(query, id)
            professor = cursor.fetchone()
            return professor
        except sqlite3.Error as e:
            print(f"Erro ao BUSCAR disciplina: {e}")
            return None
        finally:
            conn.close()

    def create(self):
        conn = connect()
        cursor = conn.cursor()

        query = 'INSERT INTO Disciplinas (nome, carga_horaria, creditos) VALUES (?, ?, ?)'

        try:
            cursor.execute(query, (self.nome, self.carga_horaria, self.creditos))
            conn.commit()
            return True, "Disciplina CADASTRADA com sucesso"
        except sqlite3.Error as e:
            print(f"Erro ao CRIAR disciplina: {e}")
            conn.rollback()
            return False, e
        finally:
            conn.close()

    @staticmethod
    def update(id, nome = None, carga_horaria = None, creditos = None):
        conn = connect()
        cursor = conn.cursor()

        attr_to_update = []
        attr_values = []

        if nome:
            attr_to_update.append('nome = ?')
            attr_values.append(nome)
        if carga_horaria:
            attr_to_update.append('carga_horaria = ?')
            attr_values.append(carga_horaria)
        if creditos:
            attr_to_update.append('creditos = ?')
            attr_values.append(creditos)


        if not attr_to_update:
            return False

        attr_values.append(id)

        query = f"UPDATE Disciplinas SET {', '.join(attr_to_update)} WHERE id_disciplina = ?"

        try:
            cursor.execute(query, attr_values)
            conn.commit()
            return True, "Disciplina ATUALIZADA com sucesso"
        except sqlite3.Error as e:
            print(f"Erro ao ALTERAR disciplina: {e}")
            conn.rollback()
            return False, e
        finally:
            conn.close()

    @staticmethod
    def delete(id):
        conn = connect()
        cursor = conn.cursor()

        query = 'DELETE FROM Disciplinas WHERE id_disciplina = ?'

        try:
            cursor.execute(query, id)
            conn.commit()
            return True, "Disciplina REMOVIDA com sucesso"
        except sqlite3.Error as e:
            conn.rollback()
            return False, e
        finally:
            conn.close()

    @staticmethod
    def delete_all():
        conn = connect()
        cursor = conn.cursor()

        query = """
        DELETE FROM Disciplinas;
        DELETE FROM sqlite_sequence WHERE name='Disciplinas';
        """

        try:
            cursor.executescript(query)
            conn.commit()
            return True, "Base de dados de disciplinas resetada com sucesso"
        except sqlite3.Error as e:
            conn.rollback()
            return False, e
        finally:
            conn.close()