from sqlite3 import *

banco = connect('cadastro_produtos.db')

with banco:
    # criando a tabela de produtos:
    # obs: o sqlite3 tem problemas com números decimais,
    # então vou armazenas o preço como texto mesmo
    cursor = banco.cursor()
    cursor.execute('''
    create table if not exists produtos (
    id integer, codigo integer unique, descricao text, preco text, categoria text,
    primary key (id autoincrement)
    )
    ''')