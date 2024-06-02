roupas = ['Camisa', 'Vestidos', 'Saia', 'Bermuda', 'Calça']
roupas.append('Luvas')

for itens in roupas:
    print(itens)

#ordenar alfa
print('='*9)
roupas.sort()

for itens in roupas:
    print(itens)

#remover item
print('='*9)
roupas.remove('Bermuda')

for itens in roupas:
    print(itens)
#trocar intem da lista
roupas[1] = 'Jaqueta'

for itens in roupas:
    print(itens)