from classes import Cliente,Aluno, ClienteVip,Pessoa


#Limpar a tela
import os
clear = lambda: os.system('clear')
clear()


objeto_clie1 = Cliente('Joao', 48)
print(objeto_clie1.nome, "Nasceu em :",(2021-objeto_clie1.idade))
objeto_clie1.reclamar()
print("\n")


objeto_clie2 = Cliente("Daniele", 28)
print(objeto_clie2.nome, "Nasceu em :", (2021-objeto_clie2.idade))
print("\n")

objeto_aluno = Aluno("Maria", 57)
print(objeto_aluno.nome, "Nasceu em: ", (2021-objeto_aluno.idade))
objeto_aluno.estudar()
print("\n")

objeto_pessoa = Pessoa("Bruno", 27)
print(objeto_pessoa.nome, "Nasceu em : ", (2021-objeto_pessoa.idade))
objeto_pessoa.fofocar()
print("\n")

objeto_clienteVip = ClienteVip("Laryssa", 10, "Crhistinny")
print(objeto_clienteVip.nome,objeto_clienteVip.sobrenome, "Nasceu em : ", (2021-objeto_clienteVip.idade))
objeto_clienteVip.reclamar()