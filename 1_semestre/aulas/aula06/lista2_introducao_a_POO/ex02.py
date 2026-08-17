class País:
    def __init__(self):
        self.nome = input('Nome do país: ')
        self.popu = int(input('População: '))
        self.area = float(input('Área: '))
    def calc_demo(self):
        return self.popu/self.area

print('*CALCULAR A DENSIDADE DEMOGRÁFICA*')
p1 = País()
p2 = País()
p3 = País()
p4 = País()
p5 = País()
p6 = País()
p7 = País()
p8 = País()
p9 = País()
p10 = País()

maior = max(p1.calc_demo(), p2.calc_demo(), p3.calc_demo(), p4.calc_demo(), p5.calc_demo(), p6.calc_demo(), p7.calc_demo(), p8.calc_demo(), p9.calc_demo(), p10.calc_demo())

if maior == p1.calc_demo():
    pais_maior = p1.nome

if maior == p2.calc_demo():
    pais_maior = p2.nome

if maior == p3.calc_demo():
    pais_maior = p3.nome

if maior == p4.calc_demo():
    pais_maior = p4.nome

if maior == p5.calc_demo():
    pais_maior = p5.nome

if maior == p6.calc_demo():
    pais_maior = p6.nome

if maior == p7.calc_demo():
    pais_maior = p7.nome

if maior == p8.calc_demo():
    pais_maior = p8.nome

if maior == p9.calc_demo():
    pais_maior = p9.nome

if maior == p10.calc_demo():
    pais_maior = p10.nome

print(f'O país com a maior densidade demográfica é {pais_maior} com {maior} hab/km²')

