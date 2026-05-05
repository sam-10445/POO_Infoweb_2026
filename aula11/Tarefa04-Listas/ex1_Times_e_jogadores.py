class Time:
    def __init__(self, id, nome, estado):
        self.set_id(id)
        self.set_nome(nome)
        self.set_estado(estado)
    #sets
    def set_id(self, id):
        if id < 0: raise ValueError()
        self.__id = id

    def set_nome(self, nome):
        if len(nome) < 3: raise ValueError()
        self.__nome = nome

    def set_estado(self, estado):
        if len(estado) < 2: raise ValueError()
        self.__estado = estado

    #gets
    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_estado(self): return self.__estado