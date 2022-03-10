pessoas = [
    (
        {
            'nome' : 'João',
            'cidade' : 'Ceilândia'
        }
    ),
    (
        {
            'nome' : 'Daniele',
            'cidade' : 'Planaltina-GO'
        }
    ),
    (
        {
            'nome' : 'José',
            'cidade' : 'Planaltina-DF'
        }
    )
]
#contador =0
# for pessoa in pessoas:
#     print(contador, pessoa['nome'], ' mora em ', pessoa['cidade'])
#     contador += 1

contador =0
for pessoa in pessoas:
    contador += 1
    if pessoa['nome'] == 'Daniele':
        continue
    print(contador, pessoa['nome'], ' mora em ', pessoa['cidade'])