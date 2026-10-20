from datetime import datetime

class Atendimento:
    def __init__(self, id, data, queixa_principal, historico_saude,
                 avaliacao, prescricao, id_horario, total, pago):
        self.set_id(id)
        self.set_data(data)
        self.set_queixa_principal(queixa_principal)
        self.set_historico_saude(historico_saude)
        self.set_avaliacao(avaliacao)
        self.set_prescricao(prescricao)
        self.set_id_horario(id_horario)
        self.set_total(total)
        self.set_pago(pago)

    def set_id(self, id):
        if id < 0: raise ValueError("Id deve ser positivo")
        self.__id = id

    def set_data(self, data): self.__data = data

    def set_queixa_principal(self, valor):
        self.__queixa_principal = valor

    def set_historico_saude(self, valor):
        self.__historico_saude = valor

    def set_avaliacao(self, valor):
        self.__avaliacao = valor

    def set_prescricao(self, valor):
        self.__prescricao = valor

    def set_id_horario(self, id_horario):
        self.__id_horario = id_horario

    def set_total(self, total):
        if total < 0: raise ValueError("Total deve ser positivo")
        self.__total = total

    def set_pago(self, pago):
        self.__pago = pago

    def get_id(self): return self.__id
    def get_data(self): return self.__data
    def get_queixa_principal(self): return self.__queixa_principal
    def get_historico_saude(self): return self.__historico_saude
    def get_avaliacao(self): return self.__avaliacao
    def get_prescricao(self): return self.__prescricao
    def get_id_horario(self): return self.__id_horario
    def get_total(self): return self.__total
    def get_pago(self): return self.__pago

    def __str__(self):
        return f"{self.__id} - {self.__data.strftime('%d/%m/%Y %H:%M')} - R$ {self.__total:.2f} - Pago: {self.__pago}"

    def to_json(self):
        return {
            "id": self.__id,
            "data": self.__data.strftime("%d/%m/%Y %H:%M"),
            "queixa_principal": self.__queixa_principal,
            "historico_saude": self.__historico_saude,
            "avaliacao": self.__avaliacao,
            "prescricao": self.__prescricao,
            "id_horario": self.__id_horario,
            "total": self.__total,
            "pago": self.__pago
        }

    @staticmethod
    def from_json(dic):
        return Atendimento(
            dic["id"],
            datetime.strptime(dic["data"], "%d/%m/%Y %H:%M"),
            dic["queixa_principal"],
            dic["historico_saude"],
            dic["avaliacao"],
            dic["prescricao"],
            dic["id_horario"],
            dic["total"],
            dic["pago"]
        )
