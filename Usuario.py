from Banco import Banco

class Usuario:
    def __init__(self, idUsuario = 0, nome = '', email = '',  senha = ''):
        self.idUsuario = idUsuario
        self.nome = nome
        self.email = email
        self.senha = senha

    def inserirUsuario(self):
        banco = Banco()

        try:
            c = banco.conexao.cursor()
            c.execute("""insert into usuarios(nome, email, senha) values('"+self.nome+"',
            '"+self.email+"', '"+self.senha+"')""")

            banco.conexao.commit()
            c.close()

            return 'Cadastrado com sucesso'
        except:
            return 'Não foi possivel fazer o cadastro'

    # Atualizar usuário já cadastrado
    def atualizarUsuario(self):
        banco = Banco()

        try:
            c =banco.conexao.cursor()

            c.execute("""update usuarios set nome = '"+self.nome+"',
             email  = '"+self.email+"', senha = '"+self.senha+"' """)
            banco.conexao.commit()
            c.close()

            return 'Atualizado com sucesso'

        except:
            return 'Não foi possivel atualizar'


    # Apagar contato existente
    def deletarUsuario(self):
        banco = Banco()

        try:
            c = banco.conexao.cursor()

            c.execute("""delete from usuarios where idUsuario( = '"+self.idUsuario+"' """)
            banco.conexao.commit()
            c.close()

            return 'Usuário excluido com sucesso'

        except:
            return 'Houve um erro na exclusão do usuário'


    def buscarUsuario(self):
        banco = Banco()

        try:
            c = banco.conexao.cursor()

            c.execute(""" select * from usuarios = '"+idUsuario+"' """)
            for linha in c:
                self.idUsuario[0]
                self.nome[1]
                self.email[2]
                self.senha[3]

            c.close()
            return 'Busca feita com sucesso'

        except:
            return 'Houve um erro na busca'





