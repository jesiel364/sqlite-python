import sqlite3

conn = sqlite3.connect('clientes.db')
cursor = conn.cursor()


id_cliente = 1
novo_fone = '11-1000-1024'
novo_criado_em = '2014-06-11'


# alterando dados da tabela
cursor.execute('''
UPDATE clientes
SET fone = ?, criado_em = ?
WHERE id = ?
''', (novo_fone, novo_criado_em, id_cliente))


conn.commit()


print('dados atualizados com sucesso.')

conn.close()