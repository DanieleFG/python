# carrinho = []
# carrinho. append(('p1', 30))
# carrinho. append(('p2', 365))
# carrinho. append(('p3', 785))
# carrinho. append(('p4', 325))
# carrinho. append(('p5', 865))

# soma = sum([float(valores) for item, valores in carrinho])
# print(carrinho)
# print('Valores total dos produtos = ', soma)



pedido1 = [125, 132, 98, 10]
pedido2 = [25, 28, 102, 35, 50, 65]


#maneira peba
lista_soma = []
for i in range(len(pedido1)):
    lista_soma.append(pedido1[i] + pedido2[i])

print(lista_soma)

# maneira pro
# lista_soma_pro = [x+y for x, y in zip(pedido2, pedido1)]
# print(lista_soma_pro)

lista_soma_pro = [x+y for x, y in zip(pedido2, pedido1)]
print(lista_soma_pro)