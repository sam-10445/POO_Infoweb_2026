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

# Interface com o usuário
class UI:
    @staticmethod
    def main():
        x = Triangulo()
        x.set_base(float(input('Base: ')))
        x.set_altura(float(input('Altura: ')))
        area = x.calc_area()
        print(f"Um triângulo com a base {x.get_base()} e altura {x.get_altura()} tem área = {area}")

UI.main()