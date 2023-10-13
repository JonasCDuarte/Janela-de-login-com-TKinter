from Usuario import Usuario
from tkinter import *

class Aplicacao:
    def __init__(self, master = None):
        self.fonte = ('Arial', '8')
        self.txtFonte = ('Verdana', '8')

        self.c1 = Frame(master)
        self.c1['padx'] = 10
        self.c1.pack()

        self.c2 = Frame(master)
        self.c2['padx'] = 20
        self.c2['pady'] = 5
        self.c2.pack()

        self.c3 = Frame(master)
        self.c3['padx'] = 20
        self.c3['pady'] = 5
        self.c3.pack()

        self.c4 = Frame(master)
        self.c4['padx'] = 20
        self.c4['pady'] = 5
        self.c4.pack()

        self.c5 = Frame(master)
        self.c5['padx'] = 20
        self.c5['pady'] = 5
        self.c5.pack()

        self.c6 = Frame(master)
        self.c6['padx'] = 20
        self.c6['pady'] = 5
        self.c6.pack()

        self.titulo = Label(self.c1, text='Informe os dados', font=self.fonte)
        self.titulo.pack()

        self.lblNome = Label(self.c2, text='Nome:', font=self.fonte, width=10)
        self.lblNome.pack(side = LEFT)

        self.txtNome = Entry(self.c2, font=self.txtFonte, width= 20)
        self.txtNome.pack(side = LEFT)

        self.lblEmail = Label(self.c3, text='E-mail:', font=self.fonte, width=10)
        self.lblEmail.pack(side = LEFT)

        self.txtEmail = Entry(self.c3, font=self.txtFonte, width=20)
        self.txtEmail.pack(side = LEFT)

        self.lblSenha = Label(self.c4, text='Senha:', font=self.fonte, width=10)
        self.lblSenha.pack(side = LEFT)

        self.txtSenha = Entry(self.c4, font=self.txtFonte, width=20)
        self.txtSenha['show'] = "*"
        self.txtSenha.pack(side = LEFT)

        self.botaoInserir = Button(self.c5, text='Inserir', font=self.fonte, width=5)
        self.botaoInserir['command'] = self.inserirUsuarioo
        self.botaoInserir.pack()

        self.resposta = Label(self.c6, font=self.txtFonte, width=25)
        self.resposta.pack()

    def inserirUsuarioo(self):
        usu = Usuario()

        usu.nome = self.txtNome.get()
        usu.email = self.txtEmail.get()
        usu.senha = self.txtSenha.get()

        self.resposta['text'] = usu.inserirUsuario()

        self.txtNome.delete(0, END)
        self.txtEmail.delete(0, END)
        self.txtSenha.delete(0, END)




root = Tk()
Aplicacao(root)
root.mainloop()
