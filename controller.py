from view import *

class Controller:
    def __init__(self) -> None:
        self.view = MainWindow(self)

    def register(self):
        pass

if __name__ == "__main__":
    controller = Controller()