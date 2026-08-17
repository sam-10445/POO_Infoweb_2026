import json
from enum import Enum
from datetime import datetime


class Grupo(Enum):
    A = 1
    B = 2
    C = 3
    D = 4
    E = 5
    F = 6
    G = 7
    H = 8
    I = 9
    J = 10
    K = 11
    L = 12


class Fase(Enum):
    Grupos = 1
    DezesseisAvos = 2
    Oitavas = 3
    Quartas = 4
    Semifinais = 5
    TerceirosLugar = 6
    Final = 7


class Pais:
    def __init__(self, id, nome, sigla, grupo):
        self.set_id(id)
        self.set_nome(nome)
        self.set_sigla(sigla)
        self.set_grupo(grupo)

    def set_id(self, id):
        if id < 0:
            raise ValueError(":/ ID deve ser positivo.")
        self.__id = id

    def set_nome(self, nome):
        if len(nome) == 0:
            raise ValueError(":/ O nome não pode ser vazio.")
        self.__nome = nome

    def set_sigla(self, sigla):
        if len(sigla) == 0:
            raise ValueError(":/ A sigla deve ser informada.")
        self.__sigla = sigla

    def set_grupo(self, grupo):
        if not isinstance(grupo, Grupo):
            raise ValueError(":/ Grupo inválido.")
        self.__grupo = grupo

    def get_id(self):
        return self.__id

    def get_nome(self):
        return self.__nome

    def get_sigla(self):
        return self.__sigla

    def get_grupo(self):
        return self.__grupo

    def __str__(self):
        return f"ID: {self.__id} | Nome: {self.__nome} | Sigla: {self.__sigla} | Grupo: {self.__grupo.name}"

    def to_json(self):
        return {
            "id": self.__id,
            "nome": self.__nome,
            "sigla": self.__sigla,
            "grupo": self.__grupo.name
        }

    @staticmethod
    def from_json(dic):
        return Pais(
            dic["id"],
            dic["nome"],
            dic["sigla"],
            Grupo[dic["grupo"]]
        )


class PaisUI:
    __paises = []

    @classmethod
    def salvar(cls):
        arquivo = open("paises.json", "w")

        json.dump(
            cls.__paises,
            arquivo,
            default=Pais.to_json,
            indent=2
        )

        arquivo.close()

    @classmethod
    def abrir(cls):
        try:
            arquivo = open("paises.json", "r")

            lista_dic = json.load(arquivo)

            arquivo.close()

            cls.__paises = []

            for dic in lista_dic:
                cls.__paises.append(Pais.from_json(dic))

        except FileNotFoundError:
            pass

    @classmethod
    def pesquisar(cls, id):
        for pais in cls.__paises:
            if pais.get_id() == id:
                return pais
        return None

    @classmethod
    def inserir(cls):
        print("\n=== Cadastro de País ===")

        id = int(input("ID: "))
        nome = input("Nome: ")
        sigla = input("Sigla: ")

        print("\nGrupos:")
        for g in Grupo:
            print(f"{g.value} - {g.name}")

        grupo = Grupo(int(input("Grupo: ")))

        if cls.pesquisar(id) != None:
            print("Já existe um país com esse ID.")
            return

        pais = Pais(id, nome, sigla, grupo)

        cls.__paises.append(pais)

        cls.salvar()

        print("País cadastrado com sucesso!")

    @classmethod
    def listar(cls):
        if len(cls.__paises) == 0:
            print("Nenhum país cadastrado.")
        else:
            print()
            for pais in cls.__paises:
                print(pais)

class Jogo:
    def __init__(self, id, id_pais1, id_pais2, gols1, gols2, fase, data_hora):
        self.set_id(id)
        self.set_id_pais1(id_pais1)
        self.set_id_pais2(id_pais2)
        self.set_gols1(gols1)
        self.set_gols2(gols2)
        self.set_fase(fase)
        self.set_data_hora(data_hora)

    def set_id(self, id):
        if id < 0:
            raise ValueError(":/ O ID não pode ser negativo.")
        self.__id = id

    def set_id_pais1(self, id_pais1):
        if PaisUI.pesquisar(id_pais1) is None:
            raise ValueError(":/ País 1 não cadastrado.")
        self.__id_pais1 = id_pais1

    def set_id_pais2(self, id_pais2):
        if PaisUI.pesquisar(id_pais2) is None:
            raise ValueError(":/ País 2 não cadastrado.")
        self.__id_pais2 = id_pais2

    def set_gols1(self, gols1):
        if gols1 < 0:
            raise ValueError(":/ Quantidade de gols inválida.")
        self.__gols1 = gols1

    def set_gols2(self, gols2):
        if gols2 < 0:
            raise ValueError(":/ Quantidade de gols inválida.")
        self.__gols2 = gols2

    def set_fase(self, fase):
        if not isinstance(fase, Fase):
            raise ValueError(":/ Fase inválida.")
        self.__fase = fase

    def set_data_hora(self, data_hora):
        if not isinstance(data_hora, datetime):
            raise ValueError(":/ Data inválida.")
        self.__data_hora = data_hora

    def get_id(self):
        return self.__id

    def get_id_pais1(self):
        return self.__id_pais1

    def get_id_pais2(self):
        return self.__id_pais2

    def get_gols1(self):
        return self.__gols1

    def get_gols2(self):
        return self.__gols2

    def get_fase(self):
        return self.__fase

    def get_data_hora(self):
        return self.__data_hora

    def __str__(self):
        pais1 = PaisUI.pesquisar(self.__id_pais1)
        pais2 = PaisUI.pesquisar(self.__id_pais2)

        nome1 = pais1.get_nome() if pais1 else "Desconhecido"
        nome2 = pais2.get_nome() if pais2 else "Desconhecido"

        return (
            f"ID: {self.__id} | "
            f"{nome1} ({self.__gols1}) x ({self.__gols2}) {nome2} | "
            f"Fase: {self.__fase.name} | "
            f"Data: {self.__data_hora.strftime('%d/%m/%Y %H:%M')}"
        )

    def to_json(self):
        return {
            "id": self.__id,
            "id_pais1": self.__id_pais1,
            "id_pais2": self.__id_pais2,
            "gols1": self.__gols1,
            "gols2": self.__gols2,
            "fase": self.__fase.name,
            "data_hora": self.__data_hora.strftime("%d/%m/%Y %H:%M")
        }

    @staticmethod
    def from_json(dic):
        return Jogo(
            dic["id"],
            dic["id_pais1"],
            dic["id_pais2"],
            dic["gols1"],
            dic["gols2"],
            Fase[dic["fase"]],
            datetime.strptime(
                dic["data_hora"],
                "%d/%m/%Y %H:%M"
            )
        )
    
class JogoUI:
    __jogos = []

    @staticmethod
    def main():
        PaisUI.abrir()
        JogoUI.abrir()

        op = -1
        while op != 0:
            op = JogoUI.menu()

            if op == 1:
                PaisUI.inserir()

            elif op == 2:
                PaisUI.listar()

            elif op == 3:
                JogoUI.inserir()

            elif op == 4:
                JogoUI.listar()

        print("Programa encerrado...")

    @staticmethod
    def menu():
        print("\n========== COPA DO MUNDO 2026 ==========")
        print("[1] Cadastrar país")
        print("[2] Listar países")
        print("[3] Cadastrar jogo")
        print("[4] Listar jogos")
        print("[0] Sair")

        return int(input("Opção: "))

    @classmethod
    def salvar(cls):
        arquivo = open("jogos.json", "w")

        json.dump(
            cls.__jogos,
            arquivo,
            default=Jogo.to_json,
            indent=2
        )

        arquivo.close()

    @classmethod
    def abrir(cls):
        try:
            arquivo = open("jogos.json", "r")

            lista_dic = json.load(arquivo)

            arquivo.close()

            cls.__jogos = []

            for dic in lista_dic:
                cls.__jogos.append(Jogo.from_json(dic))

        except FileNotFoundError:
            pass

    @classmethod
    def inserir(cls):
        print("\n=== Cadastro de Jogo ===")

        id = int(input("ID do jogo: "))

        print("\nPaíses cadastrados:")
        PaisUI.listar()

        id_pais1 = int(input("\nID do País 1: "))
        id_pais2 = int(input("ID do País 2: "))

        gols1 = int(input("Gols do País 1: "))
        gols2 = int(input("Gols do País 2: "))

        print("\nFases:")
        for f in Fase:
            print(f"{f.value} - {f.name}")

        fase = Fase(int(input("Fase: ")))

        data_hora = datetime.strptime(
            input("Data e Hora (dd/mm/aaaa hh:mm): "),
            "%d/%m/%Y %H:%M"
        )

        jogo = Jogo(
            id,
            id_pais1,
            id_pais2,
            gols1,
            gols2,
            fase,
            data_hora
        )

        cls.__jogos.append(jogo)

        cls.salvar()

        print("Jogo cadastrado com sucesso!")

    @classmethod
    def listar(cls):
        if len(cls.__jogos) == 0:
            print("Nenhum jogo cadastrado.")
        else:
            print()
            for jogo in cls.__jogos:
                print(jogo)


JogoUI.main()