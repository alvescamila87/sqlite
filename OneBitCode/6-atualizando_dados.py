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
id = int(input("Informe o ID do filme que se deseja atualizar: "))
score = float(input("Informe a NOVA NOTA do filme: "))

# 4 - Atualizando dados
cursor.execute("""
    UPDATE movies SET score = ?
    WHERE id = ? 
               """, (score, id))

connection.commit()
print("Dados atualizados com sucesso!")

# 6 - Fechando a conexão
connection.close()