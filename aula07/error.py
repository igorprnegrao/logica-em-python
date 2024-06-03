try:
    numero = float(input('Digite um número para dividir: '))
    divisor = float(input('Digite o número dividor'))
    resultado = numero / divisor
    print(f'O resultado da divisão é {resultado:.2f}')
except ValueError:
    print('Erro de digitação, apenas número por favor')
