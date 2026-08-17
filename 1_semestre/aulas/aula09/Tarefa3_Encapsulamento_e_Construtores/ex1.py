class Viagem:
    def __init__(self, des, s, l):
        self.set_destino(des)
        self.set_distancia(s)
        self.set_litro(l)

    # métodos de verificação
    def set_destino(self, v):
        if len(v) >= 5:
            self.__des = v
        else:
            raise ValueError()

    def set_distancia(self, v):
        if v > 0:
            self.__s = v
        else:
            raise ValueError()

    def set_litro(self, v):
        if v > 0:
            self.__l = v
        else:
            raise ValueError()

    # métodos de armazenamento
    def get_destino(self):
        return self.__des

    def get_distancia(self):
        return self.__s

    def get_litro(self):
        return self.__l

    # método pra calcular
    def calc_consumo(self):
        return self.__s / self.__l

    # String de retorno
    def __str__(self):
        return (f"Destino: {self.__des}"
                f"Distância: {self.__s} km\n"
                f"Combustível: {self.__l} L\n")

# INTERFACE COM O USUÁRIO
class ViagemUI:
    @staticmethod
    def main():
        op = 0
        while op != 2:
            op = ViagemUI.menu()
            if op == 1:
                ViagemUI.calculo()
        print('Tchau! :)')

    @staticmethod
    def menu():
        print('1 - Calculo, 2 - SAIR')
        op = int(input('Escolha uma opção: '))
        return op

    @staticmethod
    def calculo():
        print('-'*30)
        print('CALCULAR O CONSUMO MÉDIO DE COMBUSTÍVEL')
        print('-'*30)

        des = input('Destino: ')
        s = float(input('Distância (km): '))
        l = float(input('Total do consumo (L): '))

        x = Viagem(des, s, l)
        
        print("\nDados da viagem:")
        print(x)

        consumo = x.calc_consumo()
        print(f"Consumo médio: {consumo} km/L")

ViagemUI.main()