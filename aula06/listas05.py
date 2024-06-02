roupas = [10, 20, 10, 40]
soma = 0
for itens in roupas:
    print(itens)
    soma += itens
print(f'soma é {soma}')

print('=='*8)

soma = sum(roupas)

print(f'soma é {soma}')

print('=='*8)

maior = max(roupas)

print(f'o maior valor é {maior}')

print('=='*8)

maior = min(roupas)

print(f'o menor valor é {maior}')
