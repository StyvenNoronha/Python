import sqlite3

# 1 - Conectando no BD
connection = sqlite3.connect("title.db")

# 2 - Criando um cursor
'''
Cursor é um interador que permite
navegar e manipular os do bd.
'''
cursor = connection.cursor()

# 3 - Solicitando Dados do Usuário
id = int(input("Informe o id do filme que deseja remover\n"))

# 4 - Removendo Dados
cursor.execute("""
DELETE FROM movie
WHERE id = ?
""", (id,))
connection.commit()
print('Filme removido com sucesso.')

# 5 - Fechando conexão
connection.close()