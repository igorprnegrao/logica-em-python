contapares = 0
for i in range(5):
    valor = int(input('Digote io valor: '))
    if valor % 2 == 0:
        contapares += 1
print(f'quantidade de pares é: {contapares}')
