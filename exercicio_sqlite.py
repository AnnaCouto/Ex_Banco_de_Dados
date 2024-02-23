import sqlite3

banco = sqlite3.connect('exercicio_entregar.db')

cursor = banco.cursor()

#cursor.execute("CREATE TABLE alunos (id integer, nome text, idade integer, curso text)")

#cursor.execute("INSERT INTO alunos VALUES (1,'Ísis El Rafih', 22,'Sociologia')")
#cursor.execute("INSERT INTO alunos VALUES (2,'Calíope El Rafih', 21,'História')")
#cursor.execute("INSERT INTO alunos VALUES (3,'Simba El Rafih', 20,'Matemática')")
#cursor.execute("INSERT INTO alunos VALUES (4,'Minerva El Rafih', 22,'Física')")
#cursor.execute("INSERT INTO alunos VALUES (5,'Rhasmye El Rafih', 31,'Direito')")
#cursor.execute("INSERT INTO alunos VALUES (6,'Anna Couto', 31,'Engenharia')")
#cursor.execute("INSERT INTO alunos VALUES (7,'Netuno El Rafih', 20,'Engenharia')")

#Consultas SQL - Para selecionar todos os registros da tabela "alunos"
""" cursor.execute("SELECT * FROM alunos")
print(cursor.fetchall())  """

#Consultas SQL - Para selecionar nome e idade dos alunos com mais de 20 anos
""" cursor.execute("SELECT nome,idade FROM alunos GROUP BY nome HAVING idade>20")
print(cursor.fetchall()) """

#Consultas SQL - Para selecionar os alunos do curso de "Engenharia" em ordem alfabética
""" cursor.execute("SELECT * FROM alunos WHERE curso = 'Engenharia'")
print(cursor.fetchall()) """

#Consultas SQL - Para contar o número total de alunos na tabela 
""" cursor.execute("SELECT COUNT() FROM alunos")
print(cursor.fetchall()) """

#Atualização e Remoção - Atualize a idade de um aluno especifico na tabela
""" cursor.execute("UPDATE alunos SET nome = 'Jupiter' WHERE nome = 'Anna'") """

#Atualização e Remoção - Remova um aluno pelo seu ID
""" cursor.execute("DELETE FROM alunos WHERE id=6") """

banco.commit()
banco.close()