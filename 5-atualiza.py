import sqlite3
# 1- Conectando no BD
conexao = sqlite3.connect('livros.db')
cursor = conexao.cursor()

# 2-Atualização
id = 1
cursor.execute(
    """
    UPDATE livros set nome = ?
    WHERE id = ?
    """,
    ("É assim que começa", id)
    
)
conexao.commit()