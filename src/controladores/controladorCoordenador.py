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
        coordenadores_conv = []

        for coordenador in coordenadores:
            coordenador_obj = Coordenador(*coordenador)
            data_inicio_conv = datetime.datetime.strptime(coordenador_obj.inicio_vigencia, "%Y-%m-%d").strftime("%d/%m/%Y")
            data_fim_conv = datetime.datetime.strptime(coordenador_obj.fim_vigencia, "%Y-%m-%d").strftime("%d/%m/%Y")
            coordenador_obj.inicio_vigencia = data_inicio_conv
            coordenador_obj.fim_vigencia = data_fim_conv

            coordenadores_conv.append(coordenador_obj.to_tuple())

        if not coordenadores:
            return [], "Nenhum coordenador encontrado."
        return coordenadores_conv, None

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
    def listar_titular_ativo():
        coordenador = Coordenador.list_main_active()
        if not coordenador:
            return None
        return coordenador

    @staticmethod
    def listar_vice_ativo():
        coordenador = Coordenador.list_vice_active()
        if not coordenador:
            return None
        return coordenador
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
            inicio_vigencia_conv = datetime.datetime.strptime(inicio_vigencia, "%Y-%m-%d")
        except ValueError:
            inicio_vigencia_conv = datetime.datetime.strptime(inicio_vigencia, "%d/%m/%Y")

        inicio_vigencia_conv = inicio_vigencia_conv.date()


        try:
            fim_vigencia_conv = datetime.datetime.strptime(fim_vigencia, "%Y-%m-%d")
        except ValueError:
            fim_vigencia_conv = datetime.datetime.strptime(fim_vigencia, "%d/%m/%Y")

        fim_vigencia_conv = fim_vigencia_conv.date()


        if inicio_vigencia_conv and fim_vigencia_conv and fim_vigencia_conv < inicio_vigencia_conv:
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


