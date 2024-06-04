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

    def despertar(self):
        print('Despertador do celular tocando')


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

    def despertar(self):
        print('Despertador do relógio tocando')


relogio1 = Smartwatch('xiaomi', 'MI band', 'Preto', False)

print(f'Marca: {relogio1.marca}')
print(f'Modelo: {relogio1.modelo}')
print(f'Cor: {relogio1.cor}')
print(f'Sensor de Bússola: {relogio1.bussula}')
relogio1.status()
relogio1.despertar()
print()
print('+++++++++')

celular1 = Smartphones('Sansung', 'A22', 'Azul')
print('INFO CELULAR')
print()
celular1.despertar()
