import sqlite3
# 1- Conectando no BD
conexao = sqlite3.connect('livros.db')
cursor = conexao.cursor()

# 2-Exclusão
id = (1,4)
cursor.execute(
    """
    DELETE FROM livros
    WHERE id in (?,?)
    """,
    id
)
conexao.commit()