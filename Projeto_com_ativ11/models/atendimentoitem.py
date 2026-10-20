class AtendimentoItem:
    def __init__(self, id, id_atendimento, id_servico, qtd, valor):
        self.set_id(id)
        self.set_id_atendimento(id_atendimento)
        self.set_id_servico(id_servico)
        self.set_qtd(qtd)
        self.set_valor(valor)

    def set_id(self, id): self.__id = id
    def set_id_atendimento(self, id): self.__id_atendimento = id
    def set_id_servico(self, id): self.__id_servico = id

    def set_qtd(self, qtd):
        if qtd <= 0: raise ValueError("Quantidade deve ser maior que zero")
        self.__qtd = qtd

    def set_valor(self, valor):
        if valor < 0: raise ValueError("Valor deve ser positivo")
        self.__valor = valor

    def get_id(self): return self.__id
    def get_id_atendimento(self): return self.__id_atendimento
    def get_id_servico(self): return self.__id_servico
    def get_qtd(self): return self.__qtd
    def get_valor(self): return self.__valor

    def get_subtotal(self):
        return self.__qtd * self.__valor

    def to_json(self):
        return {
            "id": self.__id,
            "id_atendimento": self.__id_atendimento,
            "id_servico": self.__id_servico,
            "qtd": self.__qtd,
            "valor": self.__valor
        }

    @staticmethod
    def from_json(dic):
        return AtendimentoItem(
            dic["id"], dic["id_atendimento"], dic["id_servico"],
            dic["qtd"], dic["valor"]
        )
