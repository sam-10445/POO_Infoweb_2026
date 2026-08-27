class Profissional:
    def __init__(self, id, nome, email, especialidade):
        self.set_id(id)
        self.set_nome(nome)
        self.set_email(email)
        self.set_especialidade(especialidade)

    def set_id(self, id):
        if id < 0: raise ValueError('ID não pode ser NEGATIVO')
        self.__id = id
    def set_nome(self, nome):
        if len(nome) == 0: raise ValueError('Nome deve ser PREENCHIDO')
        self.__nome = nome
    def set_email(self, email):
        if len(email) == 0: raise ValueError('E-mail deve ser PREENCHIDO')
        self.__email = email
    def set_especialidade(self, especialidade):
        if len(especialidade) == 0: raise ValueError('A especialidade deve ser PREENCHIDA')
        self.__especialidade = especialidade

    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_email(self): return self.__email
    def get_especialidade(self): return self.__especialidade
