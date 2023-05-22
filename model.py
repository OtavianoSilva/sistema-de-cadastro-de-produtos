from sqlite3 import *

class Model:
    def __init__(self) -> None:
        self.data = connect('data_base.db')

        with self.data:
            self.cursor = self.data.cursor()
            self.cursor.execute('''
            create table if not exists produtos (
            id integer, codigo integer unique, descricao text, preco text, categoria text,
            primary key (id autoincrement)
            )
            ''')

        with self.data:
            self.cursor = self.data.cursor()
            self.cursor.execute('''
            create table if not exists contas (
            id integer, usuario text unique, senha text,
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
            
    def query(self, entry: str)-> list:
        with self.data:
            try:
                self.cursor = self.data.cursor()
                self.cursor.execute('''
                select * from produtos
                ''')
                query_result = self.cursor.fetchall()
                query_return = []
                for line in query_result:
                    for item in line[1:]:
                        if str(item) == str(entry):
                            query_return.append(line[1:])
                if query_return == []: return ['Nada encontrado']
                else: return query_return
            except Error as erro: return erro

    def aprove_login(self, user: str, passord: str):
        pass