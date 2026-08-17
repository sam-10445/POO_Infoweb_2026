import json
from datetime import datetime

class Contato:
    def __init__(self, id, nome, email, fone, nasc):
        self.set_id(id)
        self.set_nome(nome)
        self.set_email(email)
        self.set_fone(fone)
        self.set_nasc(nasc)

    def set_id(self, id):
        if id < 0: raise ValueError("Id deve ser positivo")
        self.__id = id

    def set_nome(self, nome):
        if nome == "": raise ValueError("Nome deve ser informado")
        self.__nome = nome

    def set_email(self, email):
        if email == "": raise ValueError("E-mail deve ser informado")
        self.__email = email

    def set_fone(self, fone):
        if fone == "": raise ValueError("Fone deve ser informado")
        self.__fone = fone

    def set_nasc(self, nasc):
        if nasc > datetime.now(): raise ValueError()
        self.__nasc = nasc

    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_email(self): return self.__email
    def get_fone(self): return self.__fone
    def get_nasc(self): return self.__nasc

    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__email} - {self.__fone} - {self.__nasc.strftime('%d/%m/%Y')}"

    def to_json(self):
        return {
            "id": self.__id,
            "nome": self.__nome,
            "email": self.__email,
            "fone": self.__fone,
            "nasc": self.__nasc.strftime('%d/%m/%Y')
        }

    @staticmethod
    def from_json(dic):
        # Converter a data que eu digito que está em string (dd/mm/aaaa) em datetime
        # porque o arquivo contatos.json trata a data como datetime, ent vai dá erro se não fizer
        nasc = datetime.strptime(dic["nasc"], "%d/%m/%Y")
        return Contato(dic["id"], dic["nome"], dic["email"], dic["fone"], nasc)


class ContatoUI:
    __contatos = []

    @staticmethod
    def main():
        ContatoUI.abrir()
        op = 0
        while op != 9:
            op = ContatoUI.menu()
            if op == 1: ContatoUI.inserir()
            if op == 2: ContatoUI.listar()
            if op == 3: ContatoUI.listar_id()
            if op == 4: ContatoUI.atualizar()
            if op == 5: ContatoUI.excluir()
            if op == 6: ContatoUI.pesquisar()
            if op == 7: ContatoUI.aniver()

    @staticmethod
    def menu():
        print("1-Inserir, 2-Listar, 3-Listar com id, 4-Atualizar, 5-Excluir")
        print("6-Pesquisar, 7-Ver aniversáriante(s) - 9-SAIR")
        return int(input("Escolha uma opção: "))

    @classmethod
    def salvar(cls):
        arquivo = open("contatos.json", mode="w")
        json.dump(cls.__contatos, arquivo, default=Contato.to_json, indent=2)
        arquivo.close()
        print("O arquivo contatos.json foi salvo")

    @classmethod
    def abrir(cls):
        try:
            arquivo = open("contatos.json", mode="r")
            list_dic = json.load(arquivo)
            arquivo.close()
            cls.__contatos = []
            for dic in list_dic:
                x = Contato.from_json(dic)
                cls.__contatos.append(x)
            print("O arquivo contatos.json foi aberto")
        except FileNotFoundError:
            pass

    @classmethod
    def inserir(cls):
        id = int(input("Informe o id: "))
        nome = input("Informe o nome: ")
        email = input("Informe o e-mail: ")
        fone = input("Informe o telefone: ")
        nasc = datetime.strptime(input('Data de nascimento: '), "%d/%m/%Y")
        x = Contato(id, nome, email, fone, nasc)
        cls.__contatos.append(x)
        ContatoUI.salvar()

    @classmethod
    def listar(cls):
        if len(cls.__contatos) == 0:
            print("Nenhum contato cadastrado")
        else:
            for x in cls.__contatos:
                print(x)

    @classmethod
    def listar_id(cls):
        id = int(input('ID do contado do Contato: '))
        for x in cls.__contatos:
            if x.get_id() == id:
                print(x)

    @classmethod
    def atualizar(cls):
        for x in cls.__contatos:
            print(x)
        id = int(input("Informe o id do cliente a ser atualizado: "))
        for x in cls.__contatos:
            if x.get_id() == id:
                nome = input("Informe o novo nome: ")
                email = input("Informe o novo e-mail: ")
                fone = input("Informe o novo telefone: ")
                nasc = datetime.strptime(input('Informe a nova data de nascimento: '), "%d/%m/%Y")
                x.set_nome(nome)
                x.set_email(email)
                x.set_fone(fone)
                x.set_nasc(nasc)
                ContatoUI.salvar()

    @classmethod
    def excluir(cls):
        for x in cls.__contatos:
            print(x)
        id = int(input("Informe o id do cliente a ser excluído: "))
        for x in cls.__contatos:
            if x.get_id() == id:
                cls.__contatos.remove(x)
                ContatoUI.salvar()

    @classmethod
    def pesquisar(cls):
        s = input('As iniciais do paciente: ')
        for x in cls.__contatos:
            if x.get_nome().startswith(s):
                print(x)

    @classmethod
    def aniver(cls):
        m = int(input('O mês para listar os aniversariantes: '))
        for x in cls.__contatos:
            if x.get_nasc().month == m:
                print(x)


ContatoUI.main()