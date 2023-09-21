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

# 3 - Solicitando dados do usuário

name = str(input("Informe o nome do filme: "))
year = int(input("Informe ano do filme: "))
score = float(input("Informe a nota do filme: "))

# 4 - Inserindo dados
cursor.execute("""
    INSERT INTO movies (name, year, score)
    VALUES (?, ?, ?)
                """, (name, year, score))

# 5 - Gravando dados no DB
connection.commit()
print("Dados inseridos com sucesso!")

# 6 - Fechando a conexão
connection.close()