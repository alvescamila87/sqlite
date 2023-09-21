
# 1 - Importar módulo nativo do python: SQLite
import sqlite3

# 2 - Criando o Bando de dados
connection = sqlite3.connect('title.db')

# 3 - Verificar se houve alterações no base de dados
print(connection.total_changes)

