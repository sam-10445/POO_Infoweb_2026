# A CLASSE
class Cliente: 
    #init
    def __init__(self, id, nome, email, fone, senha):
        self.set_id(id)
        self.set_nome(nome)
        self.set_email(email)
        self.set_fone(fone)
        self.set_senha(senha)
    #set
    def set_id(self, id):
        if id < 0: raise ValueError()
        self.__id = id
    def set_nome(self, nome):
        if len(nome) == 0: raise ValueError()
        self.__nome = nome
    def set_email(self, email):
        if len(email) == 0: raise ValueError()
        self.__email = email
    def set_fone(self, fone):
        if len(fone) == 0: raise ValueError()
        self.__fone = fone
    def set_senha(self, senha):
        if len(senha) == 0: raise ValueError()
        self.__senha = senha
    #get
    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_email(self): return self.__email
    def get_fone(self): return self.__fone
    def get_senha(self): return self.__senha
    #ToString
    def __str__(self):
        return f"ID: {self.__id} | Nome: {self.__nome} | E-mail: {self.__email} | Telefone: {self.__fone} | Senha: {self.__senha}"
    #to_json
    #from_json