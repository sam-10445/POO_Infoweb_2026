class Departamento:
    def __init__(self, id, nome, diretor, fone):
        self.set_id(id)
        self.set_nome(nome)
        self.set_diretor(diretor)
        self.set_fone(fone)
   
    def set_id(self, id):
        if id < 0: raise ValueError("Id deve ser positivo")
        self.__id = id
    def set_nome(self, nome):
        if nome == "": raise ValueError("Nome deve ser informado")
        self.__nome = nome
    def set_diretor(self, diretor):
        if diretor == "": raise ValueError("Diretor deve ser informado")
        self.__diretor = diretor
    def set_fone(self, fone):
        if fone == "": raise ValueError("Fone deve ser informado")
        self.__fone = fone

    def get_id(self) : return self.__id
    def get_nome(self) : return self.__nome
    def get_diretor(self) : return self.__diretor
    def get_fone(self) : return self.__fone

    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__diretor} - {self.__fone}"
   
    def to_json(self):
        return { "id":self.__id, "nome":self.__nome, "diretor":self.__diretor, "fone":self.__fone }
   
    @staticmethod
    def from_json(dic):
        return Departamento(dic["id"], dic["nome"], dic["diretor"], dic["fone"])
    
# Sobrecarga de método

#x = Cliente(1, "nome1", "email1", "fone1")   # Cliente.__init__()
#y = Cliente.from_json({ "id":1, "nome":"nome1", "email":"email1", "fone":"fone1" })