#criando classes através de construtores
class Smartphones:
    def __init__(self, marca, modelo, cor):
        """
        Classe que vai receber dados de Smartphones.
        :param marca:
        :param modelo:
        :param cor:
        """
        self.marca = marca
        self.modelo = modelo
        self.cor = cor

    #função Ligar
    def ligar(acao):
        """
        Função Ligar
        :param: acao
        :return:
            Retornar um print
        """
        print('fazendo chamada...')


print('===Classe II - Constructor++++')
print()

marc = input('Digite a marca: ')
model = input('Digite o modelo: ')
color = input('Digite a cor: ')
print('++++++++++++++++')
celular1 = Smartphones(marc, model, color)
print(f'Marca: {celular1.marca}')
print(f'Modelo: {celular1.modelo}')
print(f'Cor: {celular1.cor}')
print()
celular1.ligar()
