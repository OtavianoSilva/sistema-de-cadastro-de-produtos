from tkinter import *
from tkinter import ttk


class View(Tk):
    def __init__(self, controller) -> None:
        super().__init__()
        self.controller = controller

        self.geometry('400x550')
        self.title('Cadastro de produtos')
        self.configure(bg='#dde')


class QueryWindow(View):
    def __init__(self, controller) -> None:
        super().__init__(controller)
        self.search_value = StringVar()


        self.title('Pesquisar por produto')
        self._create_grid()
        self._create_pdf_button()
        self._query_loop()

    def _request_pdf_generate(self):
        pass

    def _request_query(self):
        pass

    def _fill_tree(self):
        self.tree_view.delete(*self.tree_view.get_children())
        query = self.request_query()
        for i in query:
            self.tree_view.insert('', 'end', values=i)

    def _create_grid(self):
        self.tree_grid = LabelFrame(self, text='Produtos')
        self.tree_grid.pack(fill='y', expand=False, padx=10, pady=10)

        self.tree_view = ttk.Treeview(self.tree_grid, columns=('Código', 'Descrição', 'Preço', 'Categoria'), show='headings')
        
        self.tree_view.column('Código', minwidth=0, width=60)
        self.tree_view.column('Descrição', minwidth=0, width=120)
        self.tree_view.column('Preço', minwidth=0, width=60)
        self.tree_view.column('Categoria', minwidth=0, width=100)

        self.tree_view.heading('Código', text='Código')
        self.tree_view.heading('Descrição', text='Descrição')
        self.tree_view.heading('Preço', text='Preço')
        self.tree_view.heading('Categoria', text='Categoria')
        
        self.tree_view.pack()

    def _create_search_radios(self):
        pass

    def _create_pdf_button(self):
        pdf_button: Button = Button(self, text='Gerar PDF', font='arial',
                                       command=self.request_pdf_generate)
        pdf_button.place(x= 150, y= 470)


    def _query_loop(self):
        self.mainloop()

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
        response = self.controller.register_in_db(code, description, price, category)

        self.price_entry.delete(0, 'end')
        self.description_entry .delete(0, 'end')
        self.code_entry.delete(0, 'end')
        self.code_entry.focus()

        response_text: Label = Label(self, text=f'{response}', font='arial',
                                                bg='#dde')
        response_text.place(x=100, y=425)

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

        botao_listar: Button = Button(self, text='Pesquisar produto', font='arial', command=
                                      lambda: QueryWindow(self.controller))
        botao_listar.place(x=70, y=480)

    def _main(self):
        self.mainloop()
