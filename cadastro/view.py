
# Importando SQLite
import sqlite3 as conector

# CRUD

# C = Create
# R = Read
# U = Update
# D = Delete

# Criando conexão com o banco de dados
conexao = conector.connect('Sistema_de_Registros_de_Notas.db')

# Inserindo informações 
def inserir_info(i):
    with conexao: 
        cursor = conexao.cursor()
        query = "INSERT INTO RAD (Nome, Nota) VALUES(?,?)"
        cursor.execute(query, i)

# Acessar informações
def mostrar_info():
    lista = []
    with conexao: 
        cursor = conexao.cursor()
        query = "SELECT * FROM RAD"
        cursor.execute(query)
        info =  cursor.fetchall()
        
        for i in info:
            lista.append(i)
    return lista

# Atualizando informações 
def atualizar_info(i):
    with conexao: 
        cursor = conexao.cursor()
        query = "UPDATE RAD SET Nome=?, Nota=? WHERE id=?"
        cursor.execute(query, i)

# Deletando informações 
def deletar_info(i):
    with conexao: 
        cursor = conexao.cursor()
        query = "DELETE FROM RAD WHERE id=?"
        cursor.execute(query, i)
