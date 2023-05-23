from view import *
from model import *

class Controller:
    def __init__(self) -> None:
        
        self.model = Model()
        self.view = LoginWindow(self)

    def register_in_db(self, code, description, price, category):
        try:
            return self.model.register_product(code.get(), description.get(), price.get(), category.get())
        except Error as erro:
            return erro
        
    def query_in_db(self, entry: Entry):
        query_return = self.model.query_product(entry.get())
        print(query_return)
        if len(query_return) < 1:
            return [query_return]
        else: return query_return

    def approve_login_in_db(self, user: Entry, passord: Entry):
        self.model.aprove_login(user.get(), passord.get())

    def register_new_user_in_db(self, user: Entry, passord: Entry):
        return self.model.register_user(user.get(), passord.get())

if __name__ == "__main__":
    controller = Controller()