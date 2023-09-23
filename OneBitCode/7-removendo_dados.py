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

# 3 - Solicitando dados para deleção ao usuário
id = int(input("Informe o ID do filme que se deseja apagar: "))

# 4 - Removendo dados
cursor.execute("""
    DELETE FROM movies
    WHERE id = ? 
               """, (id,))

connection.commit()
print("Dados atualizados com sucesso!")

# 6 - Fechando a conexão
connection.close()