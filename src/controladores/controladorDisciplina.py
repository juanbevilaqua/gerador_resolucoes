from src.entidades.disciplina import Disciplina


class DisciplinaController:
    """Controlador responsável por intermediar a interação entre a interface e o modelo Disciplina."""


    @staticmethod
    def listar_todos():
        """Retorna todas as disciplinas cadastradas."""
        disciplinas = Disciplina.list_all()
        if not disciplinas:
            return [], "Nenhuma disciplina encontrada."
        return disciplinas, None


    @staticmethod
    def listar_nomes():
        """Retorna somente os nomes das disciplinas."""
        disciplinas = Disciplina.list_all_names()
        if not disciplinas:
            return [], "Nenhum nome de disciplina encontrado."
        nomes = [p[0] for p in disciplinas]
        return nomes, None


    @staticmethod
    def buscar_por_id(id_disciplina: int):
        """Retorna os dados de uma disciplina pelo ID."""
        if not isinstance(id_disciplina, int):
            return None, "ID inválido."

        disciplina = Disciplina.get_by_id((id_disciplina,))
        if not disciplina:
            return None, "Disciplina não encontrada."
        return disciplina, None

    @staticmethod
    def cadastrar(nome: str, carga_horaria: str, creditos: str):
        """Cria um novo registro de disciplina."""

        # Validação
        if not nome or not carga_horaria or not creditos:
            return False, "ERRO AO CADASTRAR DISCIPLINA:\n\nTodos os campos devem ser preenchidos."

        nome = nome.strip()
        carga_horaria = carga_horaria.strip()
        creditos = creditos.strip()

        nova_disciplina = Disciplina(
            id=None,
            nome=nome,
            carga_horaria=carga_horaria,
            creditos=int(creditos)
        )

        sucesso, msg = nova_disciplina.create()
        if sucesso:
            return True, msg
        else:
            return False, f"ERRO AO CADASTRAR DISCIPLINA:\n\n{msg}"


    @staticmethod
    def atualizar(id_disciplina: int, nome=None, carga_horaria=None, creditos=None):
        """Atualiza os dados de uma disciplina."""

        if not id_disciplina:
            return False, "ID da disciplina não informado."

        sucesso, msg = Disciplina.update(
            id_disciplina,
            nome.strip() if nome else None,
            carga_horaria.strip() if carga_horaria else None,
            creditos.strip() if creditos else None
        )

        if sucesso:
            return True, msg
        else:
            return False, f"ERRO AO ATUALIZAR DISCIPLINA:\n\n{msg}"


    @staticmethod
    def deletar(id_disciplina: int):
        """Remove uma disciplina do banco de dados."""
        if not id_disciplina:
            return False, "ID da disciplina não informado."

        sucesso, msg = Disciplina.delete((id_disciplina,))
        if sucesso:
            return True, msg
        else:
            return False, f"ERRO AO REMOVER DISCIPLINA:\n\n{msg}"

    @staticmethod
    def deletar_todos():
        """Remove todas as disciplinas do banco de dados."""

        sucesso, msg = Disciplina.delete_all()
        if sucesso:
            return True, msg
        else:
            return False, f"ERRO AO REMOVER DISCIPLINAS:\n\n{msg}"
