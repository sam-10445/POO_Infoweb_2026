class País:
    def __init__(self, nome, pop, area):
        self.set_nome = ''
        self.set_pop = 0
        self.set_area = 0.0
    #Sets
    def set_nome(self, v):
        if v >= 5: self.__nome = v
        else: ValueError()
    def set_pop(self, v):
        if v > 0: self.__pop = v
        else: ValueError()
    def set_area(self, v):
        if v > 0: self.__area = v
        else: ValueError()
    #Gets
    def get_nome(self):
        return self.__nome
    def get_pop(self):
        return self.__pop
    def get_area(self):
        return self.__area