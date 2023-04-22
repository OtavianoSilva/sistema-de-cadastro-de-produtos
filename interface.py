from tkinter import *
from sqlite3 import *

def cadastra():
    with banco:
        try:
            cursor = banco.cursor()
            cursor.execute(f'''
            insert into produtos (codigo, descricao, preco, categoria)
            values ({entrada_codigo.get()}, '{entrada_descricao.get()}', '{entrada_preco.get()}', 
            '{entrada_categoria.get()}')
            ''')
            banco.commit()
        except Error as erro:
            texto_de_erro: Label = Label(janela, text=f'Ocorreu um erro ao executar: {erro}',
                                         font='arial', bg='#dde').place(x=20, y=425)
        else:
            texto_adicionado: Label = Label(janela, text='Cadastrado com sucesso!', font='arial',
                                            bg='#dde').place(x=100, y=425)

### Estabelecendo conexão com o banco de dados ###
banco = connect('cadastro_produtos.db')

### Definições da janela tk ###
janela:Tk = Tk()
janela.geometry('400x550')
janela.title('Cadastro de produtos')
janela.configure(bg='#dde')

### Textos da janela ###
texto_inicial: Label = Label(janela, text='Cadastro de produtos: ', font='arial', bg='#dde')
texto_inicial.place(x=120, y=40)

texto_codigo: Label = Label(janela, text='Código: ', font='arial', bg='#dde')
texto_codigo.place(x=50, y=100)

texto_descricao: Label = Label(janela, text='Descrição: ', font='arial', bg='#dde')
texto_descricao.place(x=50, y=160)

texto_preco: Label = Label(janela, text='Preço: ', font='arial', bg='#dde')
texto_preco.place(x=50, y=220)

texto_categoria:Label = Label(janela, text='Categoria: ', font='arial', bg='#dde')
texto_categoria.place(x=50, y=280)

### Caixas para entrada de texto ###
entrada_codigo: Entry = Entry(janela)
entrada_codigo.place(x=150, y=100, width=200, height=30)

entrada_descricao: Entry = Entry(janela)
entrada_descricao.place(x=150, y=160, width=200, height=30)

entrada_preco: Entry = Entry(janela)
entrada_preco.place(x=150, y=220, width=200, height=30)


### Entrada de categoria ###

entrada_categoria: StringVar = StringVar()

info_radio: Radiobutton = Radiobutton(janela, text='Informática', bg='#dde', value='informatica',
                                      variable=entrada_categoria)
info_radio.place(x=150, y=280)

ali_radio: Radiobutton = Radiobutton(janela, text='Alimento', bg='#dde', value='alimento',
                                     variable=entrada_categoria)
ali_radio.place(x=150, y=320)

elet_radio: Radiobutton = Radiobutton(janela, text='Eletronico', bg='#dde', value='eletronico',
                                      variable=entrada_categoria)
elet_radio.place(x=150, y=360)

### Botão de cadastro ###
botao_cadastrar: Button = Button(janela, text='Cadastrar', font='arial', command=cadastra)
botao_cadastrar.place(x=150, y=480)

janela.mainloop()