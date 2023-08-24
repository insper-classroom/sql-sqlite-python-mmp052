import sqlite3
from db.db_utils import SQL

# Exercício de Python - Sqlite

# Conexão com o banco de dados dentro da pasta "db"
conn = sqlite3.connect('db/database_alunos.db')
cursor = conn.cursor()

# Vamos criar uma tabela chamada "Estudantes" com os seguintes campos:
# ID (chave primária) -  Criado automáticamente pela base de dados
# Nome
# Curso
# Ano de Ingresso

sql = SQL(conn, 'Estudantes')
# sql.cria_tabela([('Nome','TEXT NOT NULL'),('Curso','TEXT NOT NULL'),('AnoDeIngresso','INTEGER')])
# sql.inserir(['Nome','Curso','AnoDeIngresso'], [('Ana Silva', 'Computação', 2019)])
# sql.inserir(['Nome','Curso','AnoDeIngresso'], [('Pedro Mendes', 'Física', 2021)])
# sql.inserir(['Nome','Curso','AnoDeIngresso'], [('Carla Souza', 'Computação', 2020)])
# sql.inserir(['Nome','Curso','AnoDeIngresso'], [('João Alves', 'Matemática', 2018)])
# sql.inserir(['Nome','Curso','AnoDeIngresso'], [('Maria Oliveira', 'Química', 2022)])
# print(sql.selecionar())
# print(sql.selecionar(filtro=f'AnoDeIngresso == 2019 OR AnoDeIngresso == 2020'))
# sql.atualizar('AnoDeIngresso', 2020, 'Nome', 'Ana Silva')
# print(sql.selecionar())
# sql.deletar('ID','5')
# print(sql.selecionar(filtro='Curso == "Computação" AND AnoDeIngresso > 2019'))
sql.atualizar('AnoDeIngresso', 2018, 'Curso', 'Computação')
print(sql.selecionar())

conn.close()
