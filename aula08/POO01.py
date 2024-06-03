class SmartPhones:
    marca = 'apple'
    modelo = 'iphone 13'
    cor = 'branco'

    def email(acao):
        print('Enviando um email...')


print('++++Program de Classe I+++++')
print()

celular1 = SmartPhones()

print(f'Marca: {celular1.marca}')
print(f'Modelo: {celular1.modelo}')
print(f'Cor: {celular1.cor}')
print()
celular1.email()
print()
celular2 = SmartPhones()
print('+++++++++++++++++++')
#cadastrando
celular2.marca = input('Digite a marca: ')
celular2.modelo = input('Digite o modelo: ')
celular2.cor = input('Digite a cor: ')
print()
print(f'Marca: {celular2.marca}')
print(f'Modelo: {celular2.modelo}')
print(f'Cor: {celular2.cor}')

