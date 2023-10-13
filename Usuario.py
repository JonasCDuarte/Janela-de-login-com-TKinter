from Banco import Banco

class Usuario:
    def __init__(self, idUsuario = 0, nome = '', email = ''):
        self.idUsuario = idUsuario
        self.nome = nome
        self.email = email

    def inserirUsuario(self):
        banco = Banco()

        try:
            c = banco.conexao.cursor()
            c.execute("""insert into usuarios(nome, email, senha) values('"+self.nome+"',
            '"+self.email+"', '"+senha+"')""")

            banco.conexao.commit()
            c.close()

            return 'Cadastrado com sucesso'
        except:
            return 'Não foi possivel fazer o cadastro'

