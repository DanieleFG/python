
print('--------------------------------')
print('--------------------------------')
print('      --  Calculadora   --    ')
print('--------------------------------')
num1 = int(input('Digite o primeito numero: '))
num2 = int(input('Digite o segundo numero: '))


print (' ( + ) adição')
print (' ( - ) subtração')
print (' ( * ) multiplicação')
print (' ( / ) divis[ão')
operador = input ('Escolha uma operação :')

if operador == '+':
    print (f"Soma: {num1} + {num2} = ", num1+num2)
elif operador == '-':
     print (f"Subtração: {num1} - {num2} = ", num1-num2)
elif operador == '*':
     print (f"Multiplicação: {num1} * {num2} = ", num1*num2)
elif operador == '/':
     print (f"Divisão: {num1} / {num2} = ", num1/num2)
else:
    print('Operador desconhecido')
