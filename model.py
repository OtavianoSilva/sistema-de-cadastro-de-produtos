from sqlite3 import *

class Model:
    def __init__(self) -> None:
        self.data = connect('cadastro_produtos.db')

        with self.data:
            self.cursor = self.data.cursor()
            self.cursor.execute('''
            create table if not exists produtos (
            id integer, codigo integer unique, descricao text, preco text, categoria text,
            primary key (id autoincrement)
            )
            ''')

    def register(self, code, description, price, category):
        with self.data:
            try:
                self.cursor = self.data.cursor()
                self.data.execute(f'''
                insert into produtos (codigo, descricao, preco, categoria)
                values ({code}, '{description.lower()}', '{eval(price)}', 
                '{category}')
                ''')
                self.data.commit()
            except Error as erro:
                return erro
            else:
                return 'Item cadastrado com sucesso! :)'
                                                