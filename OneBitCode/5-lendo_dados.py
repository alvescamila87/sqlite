import sqlite3

# 1 - Connectar o DB
connection = sqlite3.connect('title.db')

# verificar se a conexão foi estabelecida:
print(connection)

# 2 - Criando um cursor
'''
Cursor é um interador que permite navegar
e manipular os registros em um DB

'''

cursor = connection.cursor()

# 3 - Lendo dados da tabela
data = cursor.execute("""
    SELECT name, year, score FROM movies
""")
print(data.fetchall())

# 4 - Iterando os dados
for row in cursor.execute("SELECT * FROM movies"):
    print(f"{row}")

# 5 - Ordenando os dados pelo score
for row in cursor.execute("SELECT * FROM movies ORDER BY score DESC"):
    print(f"{row}")

# 6 - Fechando a conexão
connection.close()