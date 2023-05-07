from view import *
from model import *

class Controller:
    def __init__(self) -> None:
        
        self.model = Model()
        self.view = MainWindow(self)

    def register(self, code, description, price, category):
        return self.model.register(code.get(), description.get(), price.get(), category.get())

if __name__ == "__main__":
    controller = Controller()