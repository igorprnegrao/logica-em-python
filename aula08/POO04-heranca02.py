#criando classes através de construtores
class Smartphones:
    def __init__(self, marca, modelo, cor):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor

    #função Ligar
    @staticmethod
    def ligar():
        print('fazendo chamada...')


print()
#Estrutura smartwatch herda da estrutura pai
#(smartwatch)


class Smartwatch(Smartphones):
    def __init__(self, marca, modelo, cor, bussula):
        super().__init__(marca, modelo, cor)
        self.bussula = bussula

    @staticmethod
    def status():
        print('mostrando status de atividades...')


marc = input('Digite a marca: ')
model = input('Digite o modelo: ')
color = input('Digite a cor: ')
buss = input('sim ou não: ')

relogio1 = Smartwatch(marc, model, color, buss)

print(f'Marca: {relogio1.marca}')
print(f'Modelo: {relogio1.modelo}')
print(f'Cor: {relogio1.cor}')
print(f'Sensor de Bússola: {relogio1.bussula}')
relogio1.status()
