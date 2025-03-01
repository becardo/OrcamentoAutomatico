import sqlite3

# Conexão com o banco de dados
def criar_tabela():
    conexao = sqlite3.connect("orcamentos.db")
    cursor = conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS orcamento (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_cliente TEXT NOT NULL,
            tipo_produto TEXT NOT NULL,
            classe_produto TEXT NOT NULL,
            tipo_fio TEXT NOT NULL,
            valor_fio REAL NOT NULL,
            quantidade_novelos INTEGER NOT NULL,
            horas_trabalhadas INTEGER NOT NULL
        )
    """)
    conexao.commit()
    conexao.close()

def salvar_orcamento(nome, tipo_produto, classe_produto, tipo_fio, valor_fio, qnt_novelos, horas):
    conexao = sqlite3.connect("orcamentos.db")
    cursor = conexao.cursor()
    cursor.execute("""
        INSERT INTO orcamento (nome_cliente, tipo_produto, classe_produto, tipo_fio, valor_fio, quantidade_novelos, horas_trabalhadas)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (nome, tipo_produto, classe_produto, tipo_fio, valor_fio, qnt_novelos, horas))
    conexao.commit()
    conexao.close()

def buscar_orcamentos():
    conexao = sqlite3.connect("orcamentos.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM orcamento")
    resultados = cursor.fetchall()
    conexao.close()
    return resultados

# Cria a tabela na inicialização
criar_tabela()
