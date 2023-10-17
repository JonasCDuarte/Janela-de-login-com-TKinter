from Usuario import Usuario
from tkinter import *

class Aplicacao:
    def __init__(self, master = None):
        #Criando função de fontes previamente configurada
        self.fonte = ('Arial', '8')
        self.txtfonte = ('Verdana', '8')

        #Primeiro bloco da página
        self.b1 = Frame(master)
        self.b1['padx'] = 10
        self.b1.pack()

        #Segundo bloco da página
        self.b2 = Frame(master)
        self.b2['padx'] = 20
        self.b2['pady'] = 5
        self.b2.pack()

        # Terceiro bloco da página
        self.b3 = Frame(master)
        self.b3['padx'] = 20
        self.b3['pady'] = 5
        self.b3.pack()

        # Quarto bloco da página
        self.b4 = Frame(master)
        self.b4['padx'] = 20
        self.b4['pady'] = 5
        self.b4.pack()

        #Quinto bloco da página
        self.b5 = Frame(master)
        self.b5['padx'] = 15
        self.b5.pack()

        # Texto do cabeçario da página
        self.titulo = Label(self.b1, font= self.fonte, text= 'Informe os dados')
        self.titulo.pack()

        # Texto de indicação para a caixa de digitação nome usuário
        self.lblNome = Label(self.b2, font= self.fonte, text= 'Nome:', width= 10)
        self.lblNome.pack(side = LEFT)

        # Caixa de texto para receber o nome do usuário
        self.txtNome = Entry(self.b2, font= self.txtfonte, width= 20)
        self.txtNome.pack(side = LEFT)

        # Texto de indicação para a caixa de digitação senha
        self.lblSenha = Label(self.b3, font= self.fonte, text= 'Senha:', width= 10)
        self.lblSenha.pack(side = LEFT)

        # Caixa de texto para receber a senha do usuário
        self.txtSenha = Entry(self.b3, font= self.txtfonte, width=20)
        self.txtSenha.pack(side = LEFT)

        # Criando o botão para validar os dados
        self.botao = Button(self.b4, font=self.fonte, width= 8, text= 'Verificar')
        #self.botao['command'] =
        self.botao.pack()

        # Caixa de texto retornando uma mensagem se os dados estão ou não no banco de dados
        self.resposta = Label(self.b5, font= self.fonte, width= 10)
        self.resposta.pack()


root = Tk()
Aplicacao(root)
root.mainloop()


