class Profissional:
    def __init__(self, id, nome, email, especialidade, senha):
        self.set_id(id)
        self.set_nome(nome)
        self.set_email(email)
        self.set_especialidade(especialidade)
        self.set_senha(senha)

    def set_id(self, id):
        if id < 0: raise ValueError("Id deve ser positivo")
        self.__id = id

    def set_nome(self, nome):
        if nome is None or not nome.strip(): raise ValueError("Nome deve ser informado")
        self.__nome = nome.strip()

    def set_email(self, email):
        if email is None or not email.strip(): raise ValueError("E-mail deve ser informado")
        self.__email = email.strip()

    def set_especialidade(self, especialidade):
        if especialidade is None or not especialidade.strip(): raise ValueError("Especialidade deve ser informada")
        self.__especialidade = especialidade.strip()

    def set_senha(self, senha):
        if senha is None or not senha.strip(): raise ValueError("Senha deve ser informada")
        self.__senha = senha

    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_email(self): return self.__email
    def get_especialidade(self): return self.__especialidade
    def get_senha(self): return self.__senha

    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__email} - {self.__especialidade}"

    def to_json(self):
        return {"id": self.__id, "nome": self.__nome, "email": self.__email, "especialidade": self.__especialidade, "senha": self.__senha}

    def to_dict(self):
        return {"id": self.__id, "nome": self.__nome, "email": self.__email, "especialidade": self.__especialidade}

    @staticmethod
    def from_json(dic):
        return Profissional(dic["id"], dic["nome"], dic["email"], dic["especialidade"], dic["senha"])
