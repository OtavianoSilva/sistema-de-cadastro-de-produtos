from tkinter import *

class View(Tk):
    def __init__(self, controller) -> None:
        super().__init__()
        self.controller = controller

        self.geometry('400x550')
        self.title('Cadastro de produtos')
        self.configure(bg='#dde')


class StockList(View):
    def __init__(self, controller) -> None:
        super().__init__(controller)


class MainWindow(View):
    def __init__(self, controller) -> None:
        super().__init__(controller)

        self.value_var = StringVar()

        self._create_texts()
        self._create_entries()
        self._create_radios()
        self._create_register_button()
        self._main()

    def _registration_request(self, code, description, price, category):
        self.controller.register(code, description, price, category)

    def _create_texts(self):
        initial_text: Label = Label(self, text='Cadastro de produtos: ', font='arial', bg='#dde')
        initial_text.place(x=120, y=40)

        code_text: Label = Label(self, text='Código: ', font='arial', bg='#dde')
        code_text.place(x=50, y=100)

        description_text: Label = Label(self, text='Descrição: ', font='arial', bg='#dde')
        description_text.place(x=50, y=160)

        price_text: Label = Label(self, text='Preço: ', font='arial', bg='#dde')
        price_text.place(x=50, y=220)

        category_text:Label = Label(self, text='Categoria: ', font='arial', bg='#dde')
        category_text.place(x=50, y=280)

    def _create_entries(self):
        self.code_entry: Entry = Entry(self)
        self.code_entry.place(x=150, y=100, width=200, height=30)

        self.description_entry: Entry = Entry(self)
        self.description_entry.place(x=150, y=160, width=200, height=30)

        self.price_entry: Entry = Entry(self)
        self.price_entry.place(x=150, y=220, width=200, height=30)

    def _create_radios(self):

        info_radio: Radiobutton = Radiobutton(self, text='Informática', bg='#dde', value='informatica',
                                        variable= self.value_var)
        info_radio.place(x=150, y=280)

        ali_radio: Radiobutton = Radiobutton(self, text='Alimento', bg='#dde', value='alimento',
                                            variable= self.value_var)
        ali_radio.place(x=150, y=320)

        pape_radio: Radiobutton = Radiobutton(self, text='Papelaria', bg='#dde', value='papelaria',
                                            variable= self.value_var)
        pape_radio.place(x=150, y=360)

    def _create_register_button(self):
        register_button: Button = Button(self, text='Cadastrar', font='arial', command= lambda:
        self._registration_request(self.code_entry, self.description_entry, self.price_entry, self.value_var))
        register_button.place(x=250, y=480)

        botao_listar: Button = Button(self, text='Listar produtos', font='arial', command=StockList)
        botao_listar.place(x=70, y=480)

    def _main(self):
        self.mainloop()
