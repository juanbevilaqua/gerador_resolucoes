# src/controller/ProfessorController.py
from src.entidades.professor import Professor

#    datetime_object = datetime.strptime(date_string, format_code)
#    date_string = "2025-11-04 19:11:00"
#    format_code = "%Y-%m-%d %H:%M:%S"


class ProfessorController:
    """Controlador responsável por intermediar a interação entre a interface e o modelo Professor."""

    @staticmethod
    def listar_todos():
        """Retorna todos os professores cadastrados."""
        professores = Professor.list_all()
        if not professores:
            return [], "Nenhum professor encontrado."
        # professores_formatado = [p[0] for p in professores] # retira apen nomes(p[0])
        return professores, None

    @staticmethod
    def listar_nomes():
        """Retorna todos os nomes dos professores cadastrados."""
        professores = Professor.list_all_names()
        if not professores:
            return [], "Nenhum professor encontrado."
        nomes = [p[0] for p in professores]
        return nomes, None

    @staticmethod
    def buscar_por_id(id_professor: int):
        """Retorna os dados de um professor pelo ID."""
        if not isinstance(id_professor, int):
            return None, "ID inválido."

        professor = Professor.get_by_id((id_professor,))
        if not professor:
            return None, "Professor não encontrado."
        return professor, None

    @staticmethod
    def cadastrar(nome: str, area_concentracao: str, linha_pesquisa: str):
        """Cria um novo registro de professor."""
        if not nome or not area_concentracao or area_concentracao == 'Selecione' or not linha_pesquisa or linha_pesquisa == 'Selecione':
            return False, "Todos os campos devem ser preenchidos."

        novo_professor = Professor(
            id=None,
            nome=nome.strip(),
            area_concentracao=area_concentracao.strip(),
            linha_pesquisa=linha_pesquisa.strip()
        )

        sucesso, msg = novo_professor.create()
        if sucesso:
            return True, msg
        else:
            return False, f"Erro ao cadastrar professor:\n\n{msg}"

    @staticmethod
    def atualizar(id_professor: int, nome=None, area_concentracao=None, linha_pesquisa=None):
        """Atualiza os dados de um professor."""
        if not id_professor:
            return False, "ID do professor não informado."

        sucesso, msg = Professor.update(id_professor, nome, area_concentracao, linha_pesquisa)
        if sucesso:
            return True, msg
        else:
            return False, f"Erro ao atualizar o professor:\n\n{msg}"

    @staticmethod
    def deletar(id_professor: int):
        """Remove um professor do banco de dados."""
        if not id_professor:
            return False, "ID do professor não informado."

        sucesso, msg = Professor.delete((id_professor,))
        if sucesso:
            return True, msg
        else:
            return False, f"Erro ao remover professor:\n\n{msg}"
