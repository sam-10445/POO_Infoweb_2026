class Cliente:

    def __init__(self, id, nome, email, fone):
        self.set_id(id)
        self.set_nome(nome)
        self.set_email(email)
        self.set_fone(fone)

    def set_id(self, id):
        if len(id) == 0:
            raise ValueError(':/ Preencher ID')
        self.__id = id

    def set_nome(self, nome):
        if len(nome) == 0:
            raise ValueError(':/ Preencher NOME')
        self.__nome = nome

    def set_email(self, email):
        if len(email) == 0:
            raise ValueError(':/ Preencher E-MAIL')
        self.__email = email

    def set_fone(self, fone):
        if len(fone) == 0:
            raise ValueError(':/ Preencher TELEFONE')
        self.__fone = fone

    def get_id(self):
        return self.__id

    def get_nome(self):
        return self.__nome

    def get_email(self):
        return self.__email

    def get_fone(self):
        return self.__fone

    def __str__(self):
        return (
            f"ID: {self.__id} | "
            f"Nome: {self.__nome} | "
            f"E-mail: {self.__email} | "
            f"Telefone: {self.__fone}"
        )
