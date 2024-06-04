#criando classes através de construtores
class Smartphones:
    def __init__(self, marca, modelo, cor):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor

    #função Ligar
    def ligar(self):
        print('fazendo chamada...')


print()
#Estrutura smartwatch herda da estrutura pai
#(smartwatch)


class Smartwatch(Smartphones):
    bussula = True

    def status(self):
        print('mostrando status de atividades...')


relogio1 = Smartwatch('xiaomi', 'mi band 7', 'preto')

print(f'Marca: {relogio1.marca}')
print(f'Modelo: {relogio1.modelo}')
print(f'Cor: {relogio1.cor}')
print(f'Sensor de Bússola: {relogio1.bussula}')
relogio1.status()
