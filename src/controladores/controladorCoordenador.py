# src/controller/CoordenadorController.py
from src.entidades.coordenador import Coordenador
import datetime


#    datetime_object = datetime.strptime(date_string, format_code)
#    date_string = "2025-11-04 19:11:00"
#    format_code = "%Y-%m-%d %H:%M:%S"

class CoordenadorController:
    """Controlador responsável por intermediar a interação entre a interface e o modelo Coordenador."""

    @staticmethod
    def listar_todos():
        """Retorna todos os coordenadores cadastrados."""
        coordenadores = Coordenador.list_all()
        if not coordenadores:
            return [], "Nenhum coordenador encontrado."
        return coordenadores, None

    @staticmethod
    def listar_ativos():
        """Retorna apenas os coordenadores com vigência ativa (entre datas de início e fim)."""
        coordenadores = Coordenador.list_actives()
        if not coordenadores:
            return []
        return coordenadores

    # @staticmethod
    # def verificar_qtde_coord_ativos(inicio_vigencia, fim_vigencia):
    #     hoje = datetime.datetime.now().strftime("%Y-%m-%d")
    #
    #

    @staticmethod
    def buscar_por_id(id_coordenador: int):
        """Retorna os dados de um coordenador pelo ID."""
        if not isinstance(id_coordenador, int):
            return None, "ID inválido."

        coordenador = Coordenador.get_by_id((id_coordenador,))
        if not coordenador:
            return None, "Coordenador não encontrado."
        return coordenador, None

    @staticmethod
    def cadastrar(nome: str, modalidade: str, inicio_vigencia, fim_vigencia):
        """Cria um novo registro de coordenador."""
        if not nome or not modalidade or not inicio_vigencia or not fim_vigencia:
            return False, "ERRO AO CADASTRAR COORDENADOR:\n\nTodos os campos devem ser preenchidos."

        # Conversão do formato das datas
        inicio_vigencia_conv = datetime.datetime.strptime(inicio_vigencia, "%d/%m/%Y").strftime("%Y-%m-%d")
        fim_vigencia_conv = datetime.datetime.strptime(fim_vigencia, "%d/%m/%Y").strftime("%Y-%m-%d")

        # Valida se as datas são coerentes
        if fim_vigencia_conv < inicio_vigencia_conv:
            return False, "A data de fim da vigência deve ser posterior à data de início."

        nome = nome.strip()
        modalidade = modalidade.strip()

        novo_coordenador = Coordenador(
            id=None,
            nome=nome,
            modalidade=modalidade,
            inicio_vigencia=inicio_vigencia_conv,
            fim_vigencia=fim_vigencia_conv
        )

        sucesso, msg = novo_coordenador.create()
        if sucesso:
            return True, msg
        else:
            return False, f"ERRO AO CADASTRAR COORDENADOR:\n\n{msg}"

    @staticmethod
    def atualizar(id_coordenador: int, nome=None, modalidade=None, inicio_vigencia=None, fim_vigencia=None):
        """Atualiza os dados de um coordenador."""
        if not id_coordenador:
            return False, "ID do coordenador não informado."

        # Verficação e Conversão do formato das datas se necessário
        try:
            datetime.datetime.strptime(inicio_vigencia, "%Y-%m-%d")
            inicio_vigencia_conv = inicio_vigencia
        except ValueError: # Caso já esteja no formato %Y-%m-%d gera erro e entra na exceção
            inicio_vigencia_conv = datetime.datetime.strptime(inicio_vigencia, "%d/%m/%Y").strftime("%Y-%m-%d")

        try:
            datetime.datetime.strptime(inicio_vigencia, "%Y-%m-%d")
            fim_vigencia_conv = fim_vigencia
        except ValueError:
            fim_vigencia_conv = datetime.datetime.strptime(fim_vigencia, "%d/%m/%Y").strftime("%Y-%m-%d")


        if inicio_vigencia_conv and fim_vigencia and fim_vigencia_conv < inicio_vigencia:
            return False, "A data de fim da vigência deve ser posterior à de início."

        sucesso, msg = Coordenador.update(
            id_coordenador,
            nome.strip() if nome else None,
            modalidade.strip() if modalidade else None,
            inicio_vigencia_conv,
            fim_vigencia_conv
        )

        if sucesso:
            return True, msg
        else:
            return False, f"ERRO AO ATUALIZAR COORDENADOR:\n\n{msg}"

    @staticmethod
    def deletar(id_coordenador: int):
        """Remove um coordenador do banco de dados."""
        if not id_coordenador:
            return False, "ID do coordenador não informado."

        sucesso, msg = Coordenador.delete((id_coordenador,))
        if sucesso:
            return True, msg
        else:
            return False, f"ERRO AO REMOVER COORDENADOR:\n\n {msg}"


