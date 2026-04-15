import math
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
        else: raise ValueError()

    def get_raio(self):
        return self.__r
    
    #calculos
    def calc_area(self):
        return math.pi * (self.__r ** 2)
    def calc_circ(self):
        return 2 * math.pi * self.__r

class Viagem:
    def __init__(self):
        self.__s = 0
        self.__h = 0

    def set_distancia(self, valor):
        if valor > 0: self.__s = valor
        else: raise ValueError()

    def set_horas(self, valor):
        if valor > 0: self.__h = valor
        else: raise ValueError()

    def get_distancia(self):
        return self.__s
    def get_horas(self):
        return self.__h
    
    #calculos
    def calc_velocidade(self):
        return self.__s/ self.__h
    
class Conta:
    def __init__(self):
         self.__nome = ''
         self.__numero = 0
         self.saldo = 0 #começa com 0? Modificado por depósitos e saques (não precisa ser testado)
         #depósito e saque:
         self.__deposito = 0
         self.__saque = 0

    #teste de validada
    def set_nome(self, v):
        if len(v) >= 4: self.__nome = v
        else: raise ValueError()

    def set_numero(self, v):
        if len(v) >= 5: self.__numero = v
        else: raise ValueError()

    def set_deposito(self, v):
        if v > 0: self.__deposito = v
        else: raise ValueError()

    def set_saque(self, v):
        if v > 0: self.__saque = v
        else: raise ValueError()

    #recuperação das variaveis
    def get_nome(self):
        return self.__nome
    def get_numero(self):
        return self.__numero
    def get_deposito(self):
        return self.__deposito
    def get_saque(self):
        return self.__saque
    
    #deposito e saque
    def set_deposito(self, v):
        self.saldo += v

    def set_saque(self, v):
        self.saldo -= v
    
# INTERFACE COM O USUÁRIO
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
        x = Circulo()
        x.set_raio(float(input('Raio: ')))
        area = x.calc_area()
        circunferencia = x.calc_circ()
        print(f'Um circulo com raio = {x.get_raio()} tem area de {area:.2f} e circunferencia de {circunferencia:.2f}')

    @staticmethod
    def viagem():
        print('-'*50)
        print('CALCULAR A DISTÂNCIA E O TEMPO DE UMA VIAGEM')
        print('-'*50)
        x = Viagem()
        x.set_distancia(float(input('Distância (km): ')))
        x.set_horas(int(input('Horas: ')))
        print(f'Em uma viagem de {x.get_distancia()} km e com duração de {x.get_horas()} horas, a velocidade média é {x.calc_velocidade():.0f} km/h')

    @staticmethod
    def conta_bancaria():
        print('-'*30)
        print('DADOS DA SUA CONTA BANCÁRIA')
        print('-'*30)
        x = Conta()
        x.set_nome(input('Nome: '))
        x.set_numero(input('Número da Conta (ex: 00000): '))
        print('\n' * 50)
        print('*Dados atualizados!*')
        print(f'Nome: {x.get_nome()}')
        print(f'Número da Conta: {x.get_numero()}')
        print(f'Saldo da conta: R${x.saldo}')
        acao = 4
        while acao != 0:
            print('''
    AÇÕES NA CONTA:
    [1] Depósito
    [2] Saque
    [0] FINALIZAR
''')
            acao = int(input('Ação desejada: '))
            if acao == 1:
                print('\n' * 50)
                x.set_deposito(int(input('Valor: R$')))
                print('\n' * 50)
                print(f'Saldo da conta: R${x.saldo}')
            elif acao == 2:
                print('\n' * 50)
                if x.saldo > 0:
                    x.set_saque(int(input('Valor: R$')))
                    print('\n' * 50)
                print(f'Saldo da conta: R${x.saldo}')
        print('*ENCERRANDO...*')


    @staticmethod
    def cinema():
        print('-'*45)
        print('COMPRA DE INGRESSOS PARA O CINEMA')
        print('-'*45)
UI.main()