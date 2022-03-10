"""def funcao(v1, v2):
    return v1 * v2


resultado = funcao(2,3)
print(resultado)"""



"""def anonima(n1, n2): return n1*n2

print(anonima(5, 5))"""

produtos = [

    ['p1', 128],
    ['p2', 198],
    ['p3', 528],
    ['p4', 438],
    ['p5', 988],

]
#utilizando o lambda para passar os produtos como parametro
# print(sorted(produtos, key=lambda index: index[0]))  #lambda tem a função de leitura
print(sorted(produtos, key=lambda index: index[1], reverse=True))  #reverse ordenamento decrescente