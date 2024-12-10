import sqlite3

#criando o banco de dados
connection = sqlite3.connect("title.db")

#Criando um cursor
'''
Cursor é um iterador que permite
navegar e manipular os do bd.
'''
cursor = connection.cursor()
# 3 criando a tabela
cursor.execute("""
               CREATE TABLE movie(
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    year INTEGER NOT NULL,
                    score REAL NOT NULL
               );
               """)

#fechar a conexao
print("tabela criada com sucesso")
connection.close()