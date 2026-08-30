class Cliente:
    def __init__(self, id, nome, email, fone):
        self.set_id(id)
        self.set_nome(nome)
        self.set_email(email)
        self.set_fone(fone)

    def set_id(self, id):
        if id < 0: raise ValueError('')
        self.__id = id
    def set_nome(self, nome):
        if len(nome) == 0: raise ValueError('')
        self.__nome = nome
    def set_email(self, email):
        if len(email) == 0: raise ValueError('')
        self.__email = email
    def set_fone(self, fone):
        if len(fone) == 0: raise ValueError('')
        self.__fone = fone

    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_email(self): return self.__email
    def get_fone(self): return self.__fone

    def __str__(self):
        return f"ID: {self.__id} | Nome: {self.__nome} | E-mail: {self.__email} | Telefone: {self.__fone}"

    #pega os atributos do objeto e transforma em um dicionário (Objeto → Dicionário)
    def to_json(self):
        return {"id": self.__id, "nome": self.__nome, "email": self.__email, "fone": self.__fone}

    #recebe um dicionário e extrai os valores dele (Dicionário → Dados para recriar o objeto)
    def from_json(dic):
        return Cliente(dic["id"], dic["nome"], dic["email"], dic["fone"])