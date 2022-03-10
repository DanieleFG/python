num = input('Digite um numero inteiro=  ')
if num.isdigit():
    num = int(num)
    if num % 2 == 0:
        print(f'{num} e par')
    else:
        print(f'{num} e impar')
else:
    print('nao e possivel converter este valor para inteiro')