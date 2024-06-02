roupas = ['Camisa', 'Vestidos', 'Saia', 'Bermuda', 'Calça']

item = input('Digite o item: ').capitalize()

if item in roupas:
    print('Encontrado!')
else:
    print('Não Encontrado!')
