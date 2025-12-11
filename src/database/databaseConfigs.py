import sqlite3
import os

def connect():
    diretorio_db = "./src/database"

    if not os.path.exists(diretorio_db):
        os.makedirs(diretorio_db)  # Criar diretório caso não exista

    return sqlite3.connect(f"{diretorio_db}/gerador_resolucoes.db")
    #return sqlite3.connect(f"gerador_resolucoes.db")


def create_tables():
    conn = connect()
    cursor = conn.cursor()

    cursor.executescript("""
        CREATE TABLE IF NOT EXISTS Professores (
            id_professor INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            area_concentracao TEXT NOT NULL CHECK (area_concentracao IN('CIÊNCIA AMBIENTAL', 'TECNOLOGIA AMBIENTAL')),
            linha_pesquisa TEXTO NOT NULL CHECK (linha_pesquisa IN ('DESENVOLVIMENTO DE MÉTODOS E MATERIAIS PARA O CONTROLE AMBIENTAL', 'MONITORAMENTO FÍSICO, QUÍMICO E BIOLÓGICO PARA O ESTUDO DE IMPACTOS AMBIENTAIS', 'TECNOLOGIAS LIMPAS NA PRODUÇÃO E NA TRANSFORMAÇÃO DE MATERIAIS', 'POTENCIAL TECNOLÓGICO DE MATÉRIAS-PRIMAS E DE RESÍDUOS AGROINDUSTRIAIS'))
        );
    
        CREATE TABLE IF NOT EXISTS Coordenadores (
            id_coordenador INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            modalidade TEXT NOT NULL CHECK (modalidade IN ('Coordenador Titular', 'Vice-Coordenador')),
            inicio_vigencia DATETIME NOT NULL,
            fim_vigencia DATETIME NOT NULL
        );
        
        CREATE TABLE IF NOT EXISTS Disciplinas (
            id_disciplina INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            carga_horaria INTEGER NOT NULL,
            creditos INTEGER NOT NULL
        );
    
    """)

    conn.commit()
    conn.close()


def create_triggers():
    conn = connect()
    cursor = conn.cursor()

    cursor.executescript("""
        CREATE TRIGGER IF NOT EXISTS trigger_lmt_coordenadores
        BEFORE INSERT ON Coordenadores
        BEGIN
        SELECT
            CASE
                WHEN EXISTS (
                    SELECT 1
                    FROM Coordenadores
                    WHERE modalidade = NEW.modalidade
                    AND (
                        NEW.inicio_vigencia <= fim_vigencia
                        AND NEW.fim_vigencia >= inicio_vigencia
                    )                
                )
                THEN
                    RAISE(ABORT, 'Já existe um coordenador ativo nessa modalidade no período informado.')
            END;
        END;
    
        CREATE TRIGGER IF NOT EXISTS trigger_lmt_coordenadores_update
        BEFORE UPDATE ON Coordenadores
        BEGIN
            SELECT
                CASE
                    WHEN EXISTS (
                        SELECT 1
                        FROM Coordenadores
                        WHERE modalidade = NEW.modalidade
                          AND id_coordenador != OLD.id_coordenador
                          AND (
                              NEW.inicio_vigencia <= fim_vigencia
                              AND NEW.fim_vigencia >= inicio_vigencia
                          )
                    )
                    THEN
                        RAISE(ABORT, 'Já existe um coordenador ativo nessa modalidade no período informado.')
                END;
        END;

    
    """)


    conn.commit()
    conn.close()

# ======
# ESTRUTURAÇÃO DO BANCO DE DADOS
# ======
# create_tables()
# create_triggers()