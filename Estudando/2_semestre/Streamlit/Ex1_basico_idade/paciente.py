from datetime import datetime

class Paciente:
    def __init__(self, nome, cpf, fone, nasc):
        self.set_nome(nome)
        self.set_cpf(cpf)
        self.set_fone(fone)
        self.set_nasc(nasc)

    def set_nome(self, nome):
        if len(nome) == 0: raise ValueError('Nome não preenchido')
        self.__nome = nome
    def set_cpf(self, cpf):
        if len(cpf) == 0: raise ValueError('CPF não preenchido')
        self.__cpf = cpf
    def set_fone(self, fone):
        if len(fone) == 0: raise ValueError('Telefone não preenchido')
        self.__fone = fone
    def set_nasc(self, nasc):
        if nasc > datetime.now(): raise ValueError('Data de nascimento no futuro.')
        self.__nasc = nasc

    def get_nome(self): return self.__nome
    def get_cpf(self): return self.__cpf
    def get_fone(self): return self.__fone
    def get_nasc(self): return self.__nasc

    def idade(self):
        x = datetime.now() - self.get_nasc() # pega a idade
        dias = x.days #todos os dias que essa pessoa já viveu
        anos = dias // 365 #quantos anos inteiros eles dão
        meses = dias % 365 // 30 #quantos meses inteiros eles dão

        return f"{anos} ano(s) e {meses} mes(es)"

    def __str__(self):
        return f"Nome: {self.__nome} | CPF: {self.__cpf} | Telefone: {self.__fone} | Data de nascimento: {self.__nasc.strftime('%d/%m/%Y')}"