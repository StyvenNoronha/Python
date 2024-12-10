import sqlite3

#criando o banco de dados
connection = sqlite3.connect("title.db")

#Verifica se ouve alterações 
print(connection.total_changes)
