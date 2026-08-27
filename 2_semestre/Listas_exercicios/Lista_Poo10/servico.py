class Servico:
    def __init__(self, id, desc, valor):
        self.set_id(id)
        self.set_desc(desc)
        self.set_valor(valor)

    def set_id(self, id): 
        if id < 0: raise ValueError('O ID não pode ser NEGATIVO')
        self.__id = id
    def set_desc(self, desc):
        if len(desc) == 0: raise ValueError('A descrição deve ser PREENCHIDA')