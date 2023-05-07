from view import *
from model import *

class Controller:
    def __init__(self) -> None:
        
        self.model = Model()
        self.view = QueryWindow(self)

    def register_in_db(self, code, description, price, category):
        try:
            return self.model.register(code.get(), description.get(), price.get(), category.get())
        except Error as erro:
            return erro
        
    def query_in_db(self, query_str):
        return self.model.query(query_str)

if __name__ == "__main__":
    controller = Controller()