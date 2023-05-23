from tkinter import *
from tkinter import ttk


class View(Tk):
    def __init__(self, controller) -> None:
        super().__init__()
        self.controller = controller

        self.geometry('400x550')
        self.title('Cadastro de produtos')
        self.configure(bg='#dde')

class LoginWindow(View):
    def __init__(self, controller) -> None:
        super().__init__(controller)

        self.title('Login')
        self.header_text: Label = Label(self, text="Bem vindo ao controle de estoque\nAntes de tudo, faça login:", font='arial', bg='#dde')
        self.header_text.pack()

        self.login_frame: Frame = Frame(self, height=250, width=300, bg='#dde')
        self.login_frame.place(x=60, y=70)

        self._create_login_field()
        self._create_new_login_button()
        self._login_loop()

    def _approve_login(self, user: Entry, password: Entry):
        self.controller.approve_login_in_db(user, password)

    def _create_login_field(self):
        self.user_text: Label = Label(self.login_frame, text='Digite seu nome de usuário', font='arial', bg='#dde')
        self.user_text.place(x=30, y=10)

        self.user_entry: Entry = Entry(self.login_frame)
        self.user_entry.place(x=30, y=40, width=190, height=25)

        self.password_text: Label = Label(self.login_frame, text='Digite sua senha', font='arial', bg='#dde')
        self.password_text.place(x=30, y=70)

        self.password_entry: Entry = Entry(self.login_frame)
        self.password_entry.place(x=30, y=100, width=190, height=25)

        self.login_button: Button = Button(self.login_frame, text='Fazer login', font='arial', command= lambda user = self.user_entry, password = self.password_entry: self._approve_login(user, password))
        self.login_button.place(x=30, y=140)

    def _create_new_login_button(self):
        self.create_login_intruction: Label = Label(self, text='Não possui uma conta?', font='arial', bg='#dde')
        self.create_login_intruction.place(x=90, y=300)

        self.button_load_login_page: Button = Button(self, text='Registe-se', font='arial', command= lambda controller = self.controller:CreateUserWindow(controller))
        self.button_load_login_page.place(x=90, y=350)

    def _login(self):
        pass

    def _login_loop(self):
        self.mainloop()
class CreateUserWindow(View):
    def __init__(self, controller) -> None:
        super().__init__(controller)

        self.title('Criar usuário')
        self.create_user_text:Label = Label(self, text='Para criar seu usuário, informe: ', font='arial', bg='#dde')
        self.create_user_text.place(x=90, y=20)

        self._create_sign_up_field()
        self._create_user_loop()

    def _create_sign_up_field(self):
        self.user_text_info: Label = Label(self, text='Informe um usuário: ', font='arial', bg='#dde')
        self.user_text_info.place(x=90, y=50)

        self.entry_create_user: Entry = Entry(self)
        self.entry_create_user.place(x=90, y=70, width=190, height=25)

        self.password_text_info: Label = Label(self, text='Informe uma senha: ', font='arial', bg='#dde')
        self.password_text_info.place(x=90, y=100)

        self.entry_create_password: Entry = Entry(self)
        self.entry_create_password.place(x=90, y=120, width=190, height=25)

        self.signup_button: Button = Button(self, text='Registrar', font='arial', bg='#dde', command=lambda user= self.entry_create_user, password= self.entry_create_password: self._register_new_user(user, password))
        self.signup_button.place(x=90, y=150)

    def _register_new_user(self, user: Entry, passord: Entry):
        register = self.controller.register_new_user_in_db(user, passord)

        self.return_text: Label = Label(self, text=register, font='arial', bg='#dde')
        self.return_text.place(x=90, y=200)

    def _create_user_loop(self):
        self.mainloop()


class QueryWindow(View):
    def __init__(self, controller) -> None:
        super().__init__(controller)

        self.title('Pesquisar por produto')
        self._create_grid()
        self._create_search_entry()
        self._create_pdf_button()
        self._query_loop()

    def _request_pdf_generate(self):
        pass

    def _request_query(self, entry: Entry):
        query = self.controller.query_in_db(entry)
        self.search_entry.delete(0, 'end')
        self._fill_tree(query)

    def _fill_tree(self, query):
        self.tree_view.delete(*self.tree_view.get_children())
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

    def _create_search_entry(self):

        search_text: Label = Label(self, text='Psquisar por: ', font='arial',bg='#dde').place(x=50, y=260)

        self.search_entry: Entry = Entry(self)
        self.search_entry.place(x=50, y=300)

        search_button: Button = Button(self, text='Pesquisar', font='arial', bg='#dde', command= lambda entry = self.search_entry: self._request_query(entry))
        
        search_button.place(x=50, y=340)
        


    def _create_pdf_button(self):
        pdf_button: Button = Button(self, text='Gerar PDF', font='arial', command=self._request_pdf_generate)
        pdf_button.place(x= 150, y= 470)


    def _query_loop(self):
        self.mainloop()

class RegistryWindow(View):
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
