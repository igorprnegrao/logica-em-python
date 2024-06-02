#Função Recursivas

def fatorial(num):
    if num == 1:
        return 1
    else:
        return num * fatorial(num - 1)


while True:
    numero = int(input('Digite um número inteiro positivo: '))
    if numero >= 0:
        print(f' O valor total do fatorial é {fatorial(numero)}')
        break
    else:
        print('Digite um valor positivo!')
        continue


