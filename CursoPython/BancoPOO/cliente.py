class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        return self._idade

class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade) # utilizando o metodo da Classe Mae
        self.conta = None

    def inserir_conta(self, conta): # passando o item conta para cadastro do cliente
        self.conta = conta