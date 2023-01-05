from tkinter import *

interface = Tk()

def ConfiguraçõesDoLayout():
    interface.geometry("1000x650")

    interface.title("Logística de Produtos da Vosper")

    interface.configure(background="lightgray")

TextoUrlDosProdutos = Label(interface, text="Adicionar a URL do produto:", background="gray", width=35, font=20)
TextoUrlDosProdutos.place(x=50, y=20)

Texto2 = Entry(interface, text="Adicionar a URL do produto:", background="gray", width=35, font=20)
Texto2.place(x=100, y=200)

urlDosProdutos = Entry(interface)
urlDosProdutos.place(x =50 , y = 50, width=300, height=30)

# print(urlDosProdutos.get())
submit = Button(background="red" , width=25, height=0, text="Cadastrar Produto" , font=20)
submit.place(x=300,y=200)

def Cadastro(event):
    MensagemDeCadastro = str(urlDosProdutos.get())
    print(MensagemDeCadastro)

submit.bind("<Button-1>", Cadastro)
submit.pack()

ConfiguraçõesDoLayout()

interface.client()

interface.mainloop()