import sqlite3
from src.database.databaseConfigs import connect
from dataclasses import dataclass

@dataclass
class Professor:
    id: int or None
    nome: str
    area_concentracao: str
    linha_pesquisa: str

    @staticmethod
    def list_all():
        conn = connect()
        cursor = conn.cursor()

        query = 'SELECT * FROM Professores ORDER BY nome'

        try:
            cursor.execute(query)
            professores = cursor.fetchall()
            return professores
        except sqlite3.Error as e:
            print(f"Erro ao BUSCAR professores cadastrados: {e}")
            return None
        finally:
            conn.close()

    @staticmethod
    def list_all_names():
        conn = connect()
        cursor = conn.cursor()

        query = 'SELECT nome FROM Professores ORDER by nome'

        try:
            cursor.execute(query)
            professores = cursor.fetchall()
            return professores
        except sqlite3.Error as e:
            print(f"Erro ao BUSCAR nome dos professores cadastrados: {e}")
            return None
        finally:
            conn.close()

    @staticmethod
    def get_by_id(id):
        conn = connect()
        cursor = conn.cursor()

        query = 'SELECT * FROM Professores WHERE id_professor = ?'

        try:
            cursor.execute(query, id)
            professor = cursor.fetchone()
            return professor
        except sqlite3.Error as e:
            print(f"Erro ao BUSCAR professor: {e}")
            return None
        finally:
            conn.close()

    def create(self):
        conn = connect()
        cursor = conn.cursor()

        query = 'INSERT INTO Professores (nome, area_concentracao, linha_pesquisa) VALUES (?, ?, ?)'

        try:
            cursor.execute(query, (self.nome, self.area_concentracao, self.linha_pesquisa))
            conn.commit()
            return True, "Professor CADASTRADO com sucesso"
        except sqlite3.Error as e:
            print(f"Erro ao CRIAR professor: {e}")
            conn.rollback()
            return False, e
        finally:
            conn.close()

    @staticmethod
    def update(id, nome = None, area_concentracao = None, linha_pesquisa = None):
        conn = connect()
        cursor = conn.cursor()

        attr_to_update = []
        attr_values = []

        if nome:
            attr_to_update.append('nome = ?')
            attr_values.append(nome)
        if area_concentracao:
            attr_to_update.append('area_concentracao = ?')
            attr_values.append(area_concentracao)
        if linha_pesquisa:
            attr_to_update.append('linha_pesquisa = ?')
            attr_values.append(linha_pesquisa)


        if not attr_to_update:
            return False

        attr_values.append(id)

        query = f"UPDATE Professores SET {', '.join(attr_to_update)} WHERE id_professor = ?"

        try:
            cursor.execute(query, attr_values)
            conn.commit()
            return True, "Professor ATUALIZADO com sucesso"
        except sqlite3.Error as e:
            print(f"Erro ao ALTERAR professor: {e}")
            conn.rollback()
            return False, e
        finally:
            conn.close()

    @staticmethod
    def delete(id):
        conn = connect()
        cursor = conn.cursor()

        query = 'DELETE FROM Professores WHERE id_professor = ?'

        try:
            cursor.execute(query, id)
            conn.commit()
            return True, "Professor REMOVIDO com sucesso"
        except sqlite3.Error as e:
            conn.rollback()
            return False, e
        finally:
            conn.close()