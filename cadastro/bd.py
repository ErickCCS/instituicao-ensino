# Importando SQLite
import sqlite3 as conector

# Criando conexão com o banco de dados
conexao = conector.connect('Sistema_de_Registros_de_Notas.db')

# Criando tabela
with conexao:
    cursor = conexao.cursor()
    cursor.execute(" CREATE TABLE RAD ('ID' INTEGER PRIMARY KEY AUTOINCREMENT, 'Nome' text, 'Nota' float)")
