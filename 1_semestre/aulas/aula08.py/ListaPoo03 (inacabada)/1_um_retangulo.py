class Retangulo:
    def __init__(self, b, h):
        #testar dentro do init (set)
        self.set_base(b)
        self.set_altura(h)
    def set_base(self, v):
        if v >= 0: 
            self.__b = v
        else:
            raise ValueError()
    def set_altura(self, v):
        if v >= 0:
            self.__h = v
        else:
            raise ValueError()
