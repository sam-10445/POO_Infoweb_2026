# ENTIDADES -> EXECUÇÃO DE TAREFAS
class Triangulo:
    def __init__(self):
        self.__b = 0
        self.__h = 0
    def set_base(self, v):
        if v >= 0: self.__b = v
        else: raise ValueError()
    def set_altura(self, v):
        if v >= 0: self.__h = v
        else: raise ValueError()
    def get_base(self):
        return self.__b
    def get_altura(self):
        return self.__h
    def calc_area(self):
        return self.__b * self.__h / 2
    
class Circulo():
    def __init__(self): #cria uma variável pra guardar o raio
        self.__r = 0

    def set_raio(self, valor): 
        #o raio vai ser o "valor" dado pelo usuário, se ele for valido vai pra variável raio
        if valor > 0: self.__r = valor #r > 0
        else: raise ValueError

    def get__raio(self):
        return self.__r
    
    def calc_area(self):
        
    def calc_circ(self):

# Interface com o usuário
class UI:
    @staticmethod
    def main():
        op = 0
        while op != 9:
            op = UI.menu()
            if op == 1: UI.triangulo()
            if op == 2: UI.circulo()
            if op == 3: UI.viagem()
            if op == 4: UI.conta_bancaria()
            if op == 5: UI.cinema()

    @staticmethod
    def menu():
        print('-'*60)
        print("""
MENU 
[1] Calcular área do Triângulo
[2] Calcular área e circunferência do Circulo
[3] Calcular tempo e distância de uma Viagem
[4] Dados da sua Conta Bancária
[5] Compra de ingressos do Cinema
[9] SAIR
               """)
        op = int(input('Escolha uma opção: '))
        if op == 9:
            print('Tchau!! :)')
        return op

    @staticmethod
    def triangulo():
        print('-'*30)
        print('CALCULAR A ÁREA DO TRIÂNGULO')
        print('-'*30)
        x = Triangulo()
        x.set_base(float(input('Base: ')))
        x.set_altura(float(input('Altura: ')))
        area = x.calc_area()
        print(f"Um triângulo com a base {x.get_base()} e altura {x.get_altura()} tem área = {area}")

    @staticmethod
    def circulo():
        print('-'*50)
        print('CALCULAR A ÁREA E CIRCUNFERÊNCIA DE UM CIRCULO')
        print('-'*50)

    @staticmethod
    def viagem():
        print('-'*50)
        print('CALCULAR A DISTÂNCIA E O TEMPO DE UMA VIAGEM')
        print('-'*50)

    @staticmethod
    def conta_bancaria():
        print('-'*30)
        print('DADOS DA SUA CONTA BANCÁRIA')
        print('-'*30)

    @staticmethod
    def cinema():
        print('-'*45)
        print('COMPRA DE INGRESSOS PARA O CINEMA')
        print('-'*45)
UI.main()