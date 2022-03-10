"""nomes = ['Julia', 'Joao', 'Marcos']
for nome in nomes:
    print(nome)
else:
    print('Todos os nomes forem listados com sucesso')

palavra = 'Vamos estudar Python'
for letra in palavra:
    print(letra) 

pessoas = [({'nome': 'Joao', 'cidade':'Ceilandia'}),
           ({'nome':'Maria', 'cidade': 'Taguatinga'}),
           ({'nome': 'Daniele', 'cidade': 'Planaltina'})]
contador = 0
for pessoa in pessoas:
    contador +=1
    print(contador, pessoa['nome'], ' mora na cedade de ', pessoa['cidade'])
    #break
    #print(contador) 

for numero in range(6):
    if numero %2 ==0:
        print('O numero ', numero, " e par") """

for i, j in enumerate(range(10, 1, -1)):
    print(i,j)