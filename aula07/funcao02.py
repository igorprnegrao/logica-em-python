#função Parâmetros
def converter(celsius):
    conversao = (celsius * 9 / 5) + 32
    return conversao


while True:
    print('Deseja fazer a coversão Celsius para Fahrenheit ')
    resposta = input('Digite Y/N: ').upper()
    if resposta == 'Y':
        graus = float(input('Digite o valor em ºC: '))
        print(f'O resultado da conversão de {graus}ºC é '
              f'{converter(graus)}ºF')
    else:
        print('Programa finalizando...')
        break
