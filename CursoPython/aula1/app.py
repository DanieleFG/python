print('primeiro projeto')
#Conmentario Linear
"""
Oi comentario em bloco
"""
##Concatena
print('Estou concatenando', 'hoje a primeira linha', sep='-')
print('Estou concatenando', 'hoje a primeira linha', sep='-', end='***')
print('772', '558', '333', sep='.', end='-')
print('20')
print ("texto 'entre aspas simples'")
print('joao', type('joao'))
print(10, type(10))
print(325.80, type(325.80))
print(10 == 11, type(10 == 10))
print('J' == 'J', type ('J' == 'J'))

print ('soma + ', 10+2)
print ('subtracao - ', 10-2)
print('multiplicacao *', 10*2)
print('divisao / ', 10/2)
print('Forcando divisao com inteiros // ', 10.88 //2)
print('Potenciacao ** ', 2**10)
print('Mod % resta da divisao ',10%2 )

"""Declaracao de variavel dinamica"""
nome = 'Joao'
numero = 10
salario = 3000.00
idade = 28
resultado_boleano =  idade > 30
print(nome, ' idade = ', numero, ' salario = ', salario)
print('resultado boleano', resultado_boleano)

#regra imc peso dividido por altura  ao quadrado
peso = 65
altura = 1.79
imc = peso/(altura **2)
print('IMC', imc)

#formatada casa decimais com F-strings
nome = input('digite um numero=  ')
print(f'O numero digitado foi{nome}')

