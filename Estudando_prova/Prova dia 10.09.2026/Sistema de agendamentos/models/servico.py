class Servico:
    def __init__(self, id, desc, valor):
        self.set_id(id)
        self.set_desc(desc)
        self.set_valor(valor)

    def set_id(self, id):
        if id < 0: raise ValueError()
        self.__id = id
    def set_desc(self, desc):
        if len(desc) == 0: raise ValueError()
        self.__desc = desc
    def set_valor(self, valor):
        if valor < 0: raise ValueError()
        self.__valor = valor

    def get_id(self): return self.__id
    def get_desc(self): return self.__desc
    def get_valor(self): return self.__valor

    def __str__(self):
        return f"ID: {self.__id} | Descrição: {self.__desc} | Valor: {self.__valor:.2f}"

    def to_json(self):
        return {"id": self.__id, "desc": self.__desc, "valor": self.__valor}

    def from_json(dic):
        return Servico(dic["id"], dic["desc"], dic["valor"])