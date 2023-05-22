from view import *
from model import *

class Controller:
    def __init__(self) -> None:
        
        self.model = Model()
        self.view = MainWindow(self)

    def register_in_db(self, code, description, price, category):
        try:
            return self.model.register(code.get(), description.get(), price.get(), category.get())
        except Error as erro:
            return erro
        
    def query_in_db(self, entry: Entry):
        query_return = self.model.query(entry.get())
        print(query_return)
        if len(query_return) < 1:
            return [query_return]
        else: return query_return

if __name__ == "__main__":
    controller = Controller()