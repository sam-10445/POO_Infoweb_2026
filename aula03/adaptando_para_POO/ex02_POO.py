#CALCULAR A ÁREA DE DOIS TRIÂNGULO EM PYTHON (com POO)
class Triangulo:
    # atributo - dados que vão ser armazenados: b (base), h (altura)
    def __init__(self):
        self.b = 10
        self.h = 20
    # método - cálculos que vão ser feitos
    def calc_area(self):
        return self.b * self.h / 2 #retorna o resultado da conta com os valores b e h

# x é a referência do objeto criado pela instrução Triangulo()
# x é o link <a href>
# Triangulo() é a página
x = Triangulo()
print("*PRIMEIRO TRIÂNGULO*")
x.b = float(input("Informe a base do triângulo: "))
x.h = float(input("Informe o valor da altura: "))

y = Triangulo()
print("*SEGUNDO TRIÂNGULO*")
y.b = float(input("Informe a base do triângulo: "))
y.h = float(input("Informe o valor da altura: "))

print('-'*30)

print(f"Primeiro triângulo: base = {x.b}, altura = {x.h}, área = {x.calc_area()}")
print(f"Primeiro triângulo: base = {y.b}, altura = {y.h}, área = {y.calc_area()}")