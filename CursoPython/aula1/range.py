# for numero in range(11):
#     if numero %2 == 0:
#         print("O numero", numero,  ' é par')

# for i, j in enumerate(range(10, 1, -1)):  #10 = até qual numero , 1 de um em um, -1 decrementando, enumerate cria contador 
#     print( i, j)

# for numero_coluna in range(2,10): #começa com 2 até 5
#     print("Tabuada do ", numero_coluna)
#     for numero_coluna2 in range(0,10):
#         print(numero_coluna, ' X ', numero_coluna2, ' = ', numero_coluna*numero_coluna2)

# import time
# import os
# import winsound

# for h in range(1, 24):
#     for m in range (1,60):
#         print("h: ", h, "m: ", m, "s: ", s)
#         time.sleep(1)
#         os.system("cls")
#         frequency = 200  #set frequency to 2500 hertz
#         durantion = 1000  #set duration to 1000 ms ==1 second
#         winsound.Beep(frequency, durantion)

contador = 0
while(contador < 50) :
    print(contador)
    contador +=1