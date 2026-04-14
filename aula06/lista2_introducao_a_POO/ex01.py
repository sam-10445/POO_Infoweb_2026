class Água:
    def __init__(self): #dados
        self.mes = ''
        self.ano = 0
        self.cons = 0
    def calc_conta(self): #calculos
        if self.cons <= 10:
            return 38.00
        elif self.cons <= 20:
            return 38.00 + (self.cons - 10) * 5
        else:
            return 38.00 + (10 * 5) + (self.cons - 20) * 6
        
print('*CALCULAR O VALOR DA CONTA DE ÁGUA*')
x = Água()
x.mes = input('Digite o mês: ')
x.ano = input('Digite o ano: ')
x.cons = float(input('Qual foi o consumo desse mês de água, em m³? '))
print('-'*30)
print(f'O total a ser pago no mês de {x.mes} do ano de {x.ano} é de {x.calc_conta():.2f}')
