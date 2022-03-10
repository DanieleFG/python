nome = input('Digite o nome ')
idade = int(input("Digite a idade  "))
if idade >= 18:
    print(f'{nome} maior de idade com {idade} anos')
else:
    print(f'{nome} menor de idade com {idade} anos')