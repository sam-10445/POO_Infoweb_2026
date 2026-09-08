from datetime import datetime

class Atendimento:
    def __init__(self, id, data, queixa_principal, historico_saude, avaliacao, prescricao):
        self.set_id(id)
        self.set_data(data)
        self.set_queixa_principal(queixa_principal)
        self.set_historico_saude(historico_saude)
        self.set_avaliacao(avaliacao)
        self.set_prescricao(prescricao)
        self.set_id_horario(0)
   
    def set_id(self, id):
        if id < 0: raise ValueError("Id deve ser positivo")
        self.__id = id
    def set_data(self, data):
        if data > datetime.now(): raise ValueError('Data está no futuro')
        self.__data = data

    def set_queixa_principal(self, queixa_principal):
        if queixa_principal == "": raise ValueError("E-mail deve ser informado")
        self.__queixa_principal = queixa_principal

    def set_historico_saude(self, historico_saude):
        if historico_saude == "": raise ValueError("E-mail deve ser informado")
        self.__historico_saude = historico_saude

    def set_avaliacao(self, avaliacao):
        if avaliacao == "": raise ValueError("E-mail deve ser informado")
        self.__avaliacao = avaliacao

    def set_prescricao(self, prescricao):
        if prescricao == "": raise ValueError("E-mail deve ser informado")
        self.__prescricao = prescricao

    def set_id_horario(self, id_horario):
        if id_horario == "": raise ValueError("E-mail deve ser informado")
        self.__id_horario = id_horario
    

    def get_id(self) : return self.__id
    def get_data(self) : return self.__data
    def get_queixa_principal(self) : return self.__queixa_principal
    def get_historico_saude(self) : return self.__historico_saude
    def get_avaliacao(self) : return self.__avaliacao
    def get_prescricao(self) : return self.__prescricao
    def get_id_horario(self) : return self.__id_horario

    def __str__(self):
        return f"{self.__id} - {self.__data} - {self.__queixa_principal} - {self.__historico_saude} - {self.__avaliacao} - {self.__prescricao} - {self.__id_horario}"
   
    def to_json(self):
        return { "id":self.__id, "data": self.__data.strftime("%d/%m/%Y %H:%M"), "queixa":self.__queixa_principal, "historico":self.__historico_saude, "avaliacao":self.__avaliacao, "prescricao":self.__prescricao, "id_horario":self.__id_horario}
   
    @staticmethod
    def from_json(dic):
        return Atendimento(dic["id"], dic["data"], dic["queixa"], dic["historico"], dic["avaliacao"], dic["prescricao"], dic["id_horario"])
    
# Sobrecarga de método

#x = Cliente(1, "nome1", "email1", "fone1")   # Cliente.__init__()
#y = Cliente.from_json({ "id":1, "nome":"nome1", "email":"email1", "fone":"fone1" })