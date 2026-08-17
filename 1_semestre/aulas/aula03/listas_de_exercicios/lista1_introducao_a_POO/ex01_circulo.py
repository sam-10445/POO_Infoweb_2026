class Circulo:
    #método - dados
    def __init__(self):
        self.r = 0 #raio do circulo
    def calc_circ(self):
        area = 3.14 * self.r ** 2 #(A = pi x r²)
        c = 2 * 3.14 * self.r #(C = 2 x pi x r)
        return area, c

print("CALCULAR A ÁREA E A CIRCUNFERÊNCIA DE UM CÍRCULO")
x = Circulo
x.r = float(input("Informe o raio: "))

print(f"Área: {x.calc_circ()}")
print(f"Circunferência: {x.calc_circ()}")
#INCOMPLETO (com erro)