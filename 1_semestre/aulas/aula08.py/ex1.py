class Triangulo:
    #métodos mágicos do python (__metodo__) ex: __init__, __str__
    def __init__(self, b, h):
        self.__b = b
        self.__h = h
    def __str__(self): #pega informação do objeto e transformar em texto
        return f"Eu sou um triângulo, minha base é {self.__b} e minha altura é {self.__h}"
    
x = Triangulo(10, 20)
print(x)