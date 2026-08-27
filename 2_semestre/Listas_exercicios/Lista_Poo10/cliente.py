class Cliente:
    def __init__(self, id, nome, email, fone):
        self.set_id(id)
        self.set_nome(nome)
        self.set_email(email)
        self.set_fone(fone)

    def set_id(self, id):
        if id < 0: raise ValueError('ID não pode ser negativo')
        self.__id = id
    def set_nome(self, nome):
        if len(nome) == 0: raise ValueError('Preencha o campo "nome')
        self.__nome = nome
    def set_email(self, email):
        if len(email) == 0: raise ValueError('Preencha o campo "e-mail"')
        self.__email = email
    def set_fone(self, fone):
        if len(fone) == 0: raise ValueError('Preencha o campo "telefone"')
        self.__fone = fone

    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_email(self): return self.__email
    def get_fone(self): return self.__fone