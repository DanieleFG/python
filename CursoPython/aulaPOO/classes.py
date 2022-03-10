class Cliente:
    #self variavel global
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade =idade

    def reclamar(self):
        print(f'{self.nome} esta reclamando')

class Aluno(Cliente):  # definindo a Classe Aluno extendendo a Cliente
    def estudar(self):
        print(f'{self.nome} está estudando.')

class Pessoa(Cliente): # definindo a Classe Pessoa extendendo a Cliente
    def fofocar(self):
        print(f'{self.nome} gosta de fofocar.')

class ClienteVip(Cliente):
    def __init__(self, nome, idade, sobrenome):
        Cliente.__init__(self, nome, idade)
        self.sobrenome = sobrenome


    def reclamar(self):
        print(f'{self.nome} {self.sobrenome} Cliente Vip esta reclamando')
    