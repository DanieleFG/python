


def soma(num1, num2):
    return print(f"Soma: {num1} + {num2} = ", num1+num2)
def subtracao(num1, num2):
    return print (f"Subtração: {num1} - {num2} = ", num1-num2)
def multiplicacao (num1, num2):
    return print (f"Multiplicação: {num1} * {num2} = ", num1*num2)
def divisao(num1, num2):
    return print (f"Divisão: {num1} / {num2} = ", num1/num2)
sair ='N'

while (sair == 'N'):

    print('--------------------------------')
    print('--------------------------------')
    print('      --  Calculadora   --    ')
    print('--------------------------------')
    num1 = int(input('Digite o primeito numero: '))
    num2 = int(input('Digite o segundo numero: '))


    print (' ( + ) adição')
    print (' ( - ) subtração')
    print (' ( * ) multiplicação')
    print (' ( / ) divisão')
    operador = input ('Escolha uma operação :')

    if operador == '+':
        soma(num1, num2)
    elif operador == '-':
         subtracao(num1, num2)
    elif operador == '*':
         multiplicacao(num1, num2)
    elif operador == '/':
         divisao(num1, num2)
    else:
        print('Operador desconhecido')
    print(' ')
    print(' ')
    print('---------------------------------------------------------------------')
    sair = input('Deseja sair da calculadora: ( S ) para sim e ( N ) para não  :')
    print('---------------------------------------------------------------------')