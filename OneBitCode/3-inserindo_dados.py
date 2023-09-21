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

# 3 - Inserindo dados
cursor.execute("""
    INSERT INTO movies (name, year, score)
    VALUES ('Home Alone', 1990, 7.7)
                """)

# 4 - Gravando dados no DB
connection.commit()
print("Dados inseridos com sucesso!")

# 5 - Fechando a conexão
connection.close()