from reportlab.pdfgen import canvas
from tkinter import *
from sqlite3 import *

def gerar_pdf():
    banco = connect('cadastro_produtos.db')
    with banco:

        ### conexão com o banco e puxando os dados ###
        cursor = banco.cursor()
        cursor.execute('select codigo, descricao, preco, categoria from produtos')
        produtos = cursor.fetchall()

        ### Definição e cabeçalho ###
        pdf = canvas.Canvas("cadastros_produtos.pdf")
        pdf.setFont('Times-Bold', 18)
        pdf.drawString(200, 800, "Produtos Cadastrados:")
        pdf.setFont('Times-Bold', 14)

        y = 0
        cont = 0
        for i in range(0, len(produtos)):

            if cont % 15 == 0:
                pdf.drawString(10, 750, "CÓDIGO:")
                pdf.drawString(160, 750, "DESCRIÇÃO:")
                pdf.drawString(310, 750, "PREÇO:")
                pdf.drawString(450, 750, "CATEGORIA")

            y += 45
            x = 0

            for j in range(4):
                pdf.drawString(10 + x, 750 - y, str(produtos[i][j]))
                x += 150

            cont += 1
            if cont % 15 == 0:
                y = 0
                pdf.showPage()
                pdf.setFont('Times-Bold', 14)

        pdf.save()
    banco.close()

def pagina_de_acesso():
    pass

def pagina_de_busca():
    pass

def pagina_cadastro():

    def deleta_registro(entrada: StringVar):
        print(f'deletar: {entrada.get()}')

    def listar_produtos():
        banco = connect('cadastro_produtos.db')
        with banco:

            cursor = banco.cursor()
            cursor.execute('select codigo, descricao, preco, categoria from produtos')
            produtos = cursor.fetchall()
            
            ### Definições da janela de produtos ###
            janela_produtos: Tk = Tk()
            janela_produtos.title('Lista produtos')
            janela_produtos.geometry('400x550')
            janela_produtos.configure(bg='#dde')

            i = 0
            for registro in produtos:
                for j in range(len(registro)):
                    texto_produto: Entry = Entry(janela_produtos, width=17, fg='blue')
                    texto_produto.grid(row=i, column=j+1)
                    texto_produto.insert(END, registro[j])
                    texto_produto['state'] = 'disabled'
                i += 1

            botao_pdf: Button = Button(janela_produtos, text='Gerar PDF', font='arial',
                                       command=gerar_pdf)
            botao_pdf.place(x= 150, y= 470)

            janela_produtos.mainloop()
        banco.close()



    def cadastra():
        banco = connect('cadastro_produtos.db')
        with banco:
            try:
                cursor = banco.cursor()
                cursor.execute(f'''
                insert into produtos (codigo, descricao, preco, categoria)
                values ({entrada_codigo.get()}, '{(entrada_descricao.get()).lower()}', '{entrada_preco.get()}', 
                '{entrada_categoria.get()}')
                ''')
                banco.commit()
            except Error as erro:
                texto_de_erro: Label = Label(janela_cadastro, text=f'Ocorreu um erro ao executar: {erro}',
                                            font='arial', bg='#dde').place(x=20, y=425)
            else:
                texto_adicionado: Label = Label(janela_cadastro, text='Item cadastrado com sucesso! :)', font='arial',
                                                bg='#dde').place(x=100, y=425)
                
            ### Após adicionar, limpa os campos ###
            entrada_preco.delete(0, 'end')
            entrada_descricao.delete(0, 'end')
            entrada_codigo.delete(0, 'end')
            entrada_codigo.focus()
        banco.close()


    ### Definições da janela tk ###
    janela_cadastro:Tk = Tk()
    janela_cadastro.geometry('400x550')
    janela_cadastro.title('Cadastro de produtos')
    janela_cadastro.configure(bg='#dde')


    ### Textos da janela ###
    texto_inicial: Label = Label(janela_cadastro, text='Cadastro de produtos: ', font='arial', bg='#dde')
    texto_inicial.place(x=120, y=40)

    texto_codigo: Label = Label(janela_cadastro, text='Código: ', font='arial', bg='#dde')
    texto_codigo.place(x=50, y=100)

    texto_descricao: Label = Label(janela_cadastro, text='Descrição: ', font='arial', bg='#dde')
    texto_descricao.place(x=50, y=160)

    texto_preco: Label = Label(janela_cadastro, text='Preço: ', font='arial', bg='#dde')
    texto_preco.place(x=50, y=220)

    texto_categoria:Label = Label(janela_cadastro, text='Categoria: ', font='arial', bg='#dde')
    texto_categoria.place(x=50, y=280)



    ### Caixas para entrada de texto ###
    entrada_codigo: Entry = Entry(janela_cadastro)
    entrada_codigo.place(x=150, y=100, width=200, height=30)

    entrada_descricao: Entry = Entry(janela_cadastro)
    entrada_descricao.place(x=150, y=160, width=200, height=30)

    entrada_preco: Entry = Entry(janela_cadastro)
    entrada_preco.place(x=150, y=220, width=200, height=30)


    ### Entrada de categoria ###

    entrada_categoria: StringVar = StringVar()

    info_radio: Radiobutton = Radiobutton(janela_cadastro, text='Informática', bg='#dde', value='informatica',
                                        variable=entrada_categoria)
    info_radio.place(x=150, y=280)

    ali_radio: Radiobutton = Radiobutton(janela_cadastro, text='Alimento', bg='#dde', value='alimento',
                                        variable=entrada_categoria)
    ali_radio.place(x=150, y=320)

    pape_radio: Radiobutton = Radiobutton(janela_cadastro, text='Papelaria', bg='#dde', value='papelaria',
                                        variable=entrada_categoria)
    pape_radio.place(x=150, y=360)

    ### Botão de cadastro ###
    botao_cadastrar: Button = Button(janela_cadastro, text='Cadastrar', font='arial', command=cadastra)
    botao_cadastrar.place(x=250, y=480)

    botao_listar: Button = Button(janela_cadastro, text='Listar produtos', font='arial', command=listar_produtos)
    botao_listar.place(x=70, y=480)

    janela_cadastro.mainloop()

pagina_cadastro()
janela.mainloop()
