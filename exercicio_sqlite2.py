import sqlite3

banco = sqlite3.connect('exercicio_entregar1.db')

cursor = banco.cursor()

#cursor.execute("CREATE TABLE clientes (id INTERGER PRIMARY KEY, nome text, idade interger, saldo float)")

#cursor.execute("INSERT INTO clientes VALUES (1,'Ísis', 22, 23.5)")
#cursor.execute("INSERT INTO clientes VALUES (2,'Caliope', 21, 50.6)")
#cursor.execute("INSERT INTO clientes VALUES (3,'Minerva', 22, 100.6)")
#cursor.execute("INSERT INTO clientes VALUES (4,'Simba', 35, 110.6)")
#cursor.execute("INSERT INTO clientes VALUES (5,'Tobias', 35, 1100)")

#Consultas e Funções Agregadas
#Para selecionar o nome e a idade dos clientes com idade superior a 30 anos.
""" cursor.execute("SELECT nome, idade FROM clientes WHERE idade>30")
print(cursor.fetchall()) """

#Calcular o saldo médio dos clientes.
""" cursor.execute("SELECT AVG(saldo) saldoMedio FROM clientes")
print(cursor.fetchall()) """

#Contar quantos clientes têm saldo acima de 1000.
""" cursor.execute("SELECT COUNT() FROM clientes WHERE saldo>1000")
print(cursor.fetchall()) """

#Atualização e Remoção com Condições
#Atualizar o saldo de um cliente específico.
""" cursor.execute("UPDATE clientes SET saldo = 200 WHERE id = 1") """

#Remover um cliente pelo seu ID.
""" cursor.execute("DELETE FROM clientes WHERE id = 5") """

#Junção de Tabelas
#Crie uma segunda tabela chamada "compras" com os campos: id (chave primária), cliente_id (chave estrangeira referenciando o id da tabela "clientes"), produto (texto) e valor (real). 
#cursor.execute("CREATE TABLE compras (id INTERGER PRIMARY KEY, produto text, valor float)")

#Insira algumas compras associadas a clientes existentes na tabela "clientes".
#cursor.execute("INSERT INTO compras VALUES (1,'Bola', 13.5)")
#cursor.execute("INSERT INTO compras VALUES (2,'Tiara', 10.6)")
#cursor.execute("INSERT INTO compras VALUES (3,'Pneu', 100)")
#cursor.execute("INSERT INTO compras VALUES (4,'Banana', 0.6)")

#Escreva uma consulta para exibir o nome do cliente, o produto e o valor de cada compra.
dados = cursor.execute('SELECT nome, produto, valor FROM clientes INNER JOIN compras ON clientes.id = compras.id')
for clientes in dados:
    print(clientes)

banco.commit()
banco.close()
