import sqlite3

# 1- Conectando no BD
conexao=sqlite3.connect('livros.db')

cursor=conexao.cursor()

# 2-Criação da Tabela
cursor.execute(
    """
        CREATE TABLE Livros(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,  
        nome TEXT NOT NULL,
        autor TEXT NOT NULL,
        ano INTEGER NOT NULL,
        genero TEXT NOT NULL,
        nota REAL NOT NULL
        );
    """

)
# 3- Fecha conexão
conexao.close()
print("Tabela foi criada")