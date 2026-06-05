import sqlite3
from src.database.databaseConfigs import connect
from dataclasses import dataclass
import datetime

@dataclass
class Coordenador:
    id: int or None
    nome: str
    modalidade: str
    inicio_vigencia: datetime
    fim_vigencia: datetime

    @staticmethod
    def list_all():
        conn = connect()
        cursor = conn.cursor()

        query = 'SELECT * FROM Coordenadores'

        try:
            cursor.execute(query)
            coordenadores = cursor.fetchall()
            return coordenadores
        except sqlite3.Error as e:
            print(f"Erro ao BUSCAR coordenadores cadastrados: {e}")
            return None
        finally:
            conn.close()

    @staticmethod
    def list_actives():
        conn = connect()
        cursor = conn.cursor()

        hoje = datetime.datetime.now().strftime("%Y-%m-%d")

        query = 'SELECT * FROM Coordenadores WHERE inicio_vigencia <= ? AND fim_vigencia >= ?'

        try:
            cursor.execute(query, (hoje, hoje))
            coordenadores = cursor.fetchall()
            return coordenadores
        except sqlite3.Error as e:
            print(f"Erro ao BUSCAR coordenadores ativos: {e}")
            return None
        finally:
            conn.close()

    @staticmethod
    def list_main_active(): #busca o coordeandor titular ativo
        conn = connect()
        cursor = conn.cursor()

        hoje = datetime.datetime.now().strftime("%Y-%m-%d")

        query = "SELECT * FROM Coordenadores WHERE inicio_vigencia <= ? AND fim_vigencia >= ? AND modalidade = 'Coordenador Titular'"

        try:
            cursor.execute(query, (hoje, hoje))
            coordenador = cursor.fetchone()
            return coordenador
        except sqlite3.Error as e:
            print(f"Erro ao BUSCAR coordenador titular ativo: {e}")
            return None
        finally:
            conn.close()

    @staticmethod
    def list_vice_active():  # busca o vice-coordeandor ativo
        conn = connect()
        cursor = conn.cursor()

        hoje = datetime.datetime.now().strftime("%Y-%m-%d")

        query = "SELECT * FROM Coordenadores WHERE inicio_vigencia <= ? AND fim_vigencia >= ? AND modalidade = 'Vice-Coordenador'"

        try:
            cursor.execute(query, (hoje, hoje))
            coordenador = cursor.fetchone()
            return coordenador
        except sqlite3.Error as e:
            print(f"Erro ao BUSCAR vice-coordenador ativo: {e}")
            return None
        finally:
            conn.close()

    @staticmethod
    def get_by_id(id):
        conn = connect()
        cursor = conn.cursor()

        query = 'SELECT * FROM Coordenadores WHERE id_coordenador = ?'

        try:
            cursor.execute(query, id)
            coordenador = cursor.fetchone()
            return coordenador
        except sqlite3.Error as e:
            print(f"Erro ao BUSCAR coordenador: {e}")
            return None
        finally:
            conn.close()

    def create(self):
        conn = connect()
        cursor = conn.cursor()

        query = 'INSERT INTO Coordenadores (nome, modalidade, inicio_vigencia, fim_vigencia) VALUES (?, ?, ?, ?)'

        try:
            cursor.execute(query, (self.nome, self.modalidade, self.inicio_vigencia, self.fim_vigencia))
            conn.commit()
            return True, "Coordenador cadastrado com sucesso"
        except sqlite3.Error as e:
            print(f"Erro ao CRIAR coordenador: {e}")
            conn.rollback()
            return False, e
        finally:
            conn.close()

    @staticmethod
    def update(id, nome = None, modalidade = None, inicio_vigencia = None, fim_vigencia = None):
        conn = connect()
        cursor = conn.cursor()

        attr_to_update = []
        attr_values = []

        if nome:
            attr_to_update.append('nome = ?')
            attr_values.append(nome)
        if modalidade:
            attr_to_update.append('modalidade = ?')
            attr_values.append(modalidade)
        if inicio_vigencia:
            attr_to_update.append('inicio_vigencia = ?')
            attr_values.append(inicio_vigencia)
        if fim_vigencia:
            attr_to_update.append('fim_vigencia = ?')
            attr_values.append(fim_vigencia)


        if not attr_to_update:
            return False

        attr_values.append(id)

        query = f"UPDATE Coordenadores SET {', '.join(attr_to_update)} WHERE id_coordenador = ?"

        try:
            cursor.execute(query, attr_values)
            conn.commit()
            return True, "Coordenador ATUALIZADO com sucesso"
        except sqlite3.Error as e:
            print(f"Erro ao ALTERAR coordenador: {e}")
            conn.rollback()
            return False, e
        finally:
            conn.close()

    @staticmethod
    def delete(id):
        conn = connect()
        cursor = conn.cursor()

        query = 'DELETE FROM Coordenadores WHERE id_coordenador = ?'

        try:
            cursor.execute(query, id)
            conn.commit()
            return True, "Coordenador REMOVIDO com sucesso"
        except sqlite3.Error as e:
            print(f"Erro ao DELETAR coordenador: {e}")
            conn.rollback()
            return False, e
        finally:
            conn.close()

    def to_tuple(self):
        return (self.id, self.nome, self.modalidade, self.inicio_vigencia, self.fim_vigencia)