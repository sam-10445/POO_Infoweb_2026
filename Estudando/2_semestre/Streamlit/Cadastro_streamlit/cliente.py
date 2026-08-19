from datetime import datetime

class Cliente:
    def __init__(self, id, nome, email, nasc):
        self.set_id(id)
        self.set_nome(nome)
        self.set_email(email)
        self.set_nasc(nasc)

    def set_id(self, id):
        if len(id) == 0: raise ValueError(':/ Preencher ID')
        self.__id = id
    def set_nome(self, nome):
        if len(nome) == 0: raise ValueError(':/ Preencher NOME')
        self.__nome = nome
    def set_email(self, email):
        if len(email) == 0: raise ValueError(':/ Preencher E-MAIL')
        self.__email = email
    def set_nasc(self, nasc):
        if nasc > datetime.now(): raise ValueError(':/ Data de nascimento no FUTURO')
        self.__nasc = nasc

    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_email(self): return self.__email
    def get_nasc(self): return self.__nasc

    #calcular idade
    def idade(self):
        x = datetime.now() - self.get_nasc()
        dias = x.days #todos os dias que essa pessoa já viveu
        anos = dias // 365

        return f"Idade: {anos} ano(s)"

    def __str__(self):
        return f"ID: {self.__id} | Nome: {self.__nome} | E-mail: {self.__email} | Data de nascimento: {self.__nasc.strftime('%d/%m/%Y')}"