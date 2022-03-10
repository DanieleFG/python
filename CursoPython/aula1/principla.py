from dados import produtos , clientes

# for produto in produtos:
#     print(produto)

# precos = map(lambda p: p['preco'], produtos)

# for preco in precos:
#     print(preco)

# nova_lista = filter(lambda indice: indice['preco'] > 100, produtos)

# for produto in nova_lista:
#     print(produto)


def filtrando(produto):
    if produto['preco'] > 50:
        return True

nova_lista =filter (filtrando, produtos)

for produto in nova_lista:
    print(produto)