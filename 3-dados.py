import sqlite3

# 1- Conectando no BD
conexao = sqlite3.connect('livros.db')

cursor = conexao.cursor()

# 2-Inserindo Dados
cursor.execute(
    """
        INSERT INTO livros(nome, autor, ano, genero, nota)
        VALUES ('Eu sou Malala','Malala Yousafzai', 2013, 'Autobiografia', 9.5)
    """
)

conexao.commit()
conexao.close()