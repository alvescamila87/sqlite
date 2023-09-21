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

# 3 - Criando a tabela

cursor.execute('''
    CREATE TABLE movies (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
        name TEXT NOT NULL,
        year INTEGER NOT NULL,
        score REAL NOT NULL
    );        
            ''')

# 4 - Fechando a conexão
print("Tabela criada com sucesso!")
connection.close()