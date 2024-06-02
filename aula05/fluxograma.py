menu = 'yes'

while menu == 'yes':
    valor = float(input('Digite um valor: '))
    porct = float(input('Digite um percentual: '))/100

    resultado = valor * porct

    print(f'O desconto é de R$ {resultado:.2f}')
    print()
    menu = input('Digiste (yes) ou (no): ')
