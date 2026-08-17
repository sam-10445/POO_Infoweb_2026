class Pais:
    def __init__(self, id, nome, populacao, area):
        self.set_id(id)
        self.set_nome(nome)
        self.set_populacao(populacao)
        self.set_area(area)

    def set_id(self, id):
        if id < 0: raise ValueError("Id inválido")
        self.__id = id

    def set_nome(self, nome):
        if nome == "": raise ValueError("Nome vazio")
        self.__nome = nome

    def set_populacao(self, populacao):
        if populacao < 0: raise ValueError("População inválida")
        self.__populacao = populacao

    def set_area(self, area):
        if area <= 0: raise ValueError("Área inválida")
        self.__area = area

    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_populacao(self): return self.__populacao
    def get_area(self): return self.__area

    def densidade(self):
        return self.__populacao / self.__area

    def __str__(self):
        return f"{self.__id} - {self.__nome} - Pop: {self.__populacao} - Área: {self.__area} - Densidade: {self.densidade():.2f}"


class PaisUI:
    paises = []

    @staticmethod
    def main():
        op = 0
        while op != 7:
            op = PaisUI.menu()
            if op == 1: PaisUI.inserir()
            elif op == 2: PaisUI.listar()
            elif op == 3: PaisUI.atualizar()
            elif op == 4: PaisUI.excluir()
            elif op == 5: PaisUI.mais_populoso()
            elif op == 6: PaisUI.mais_povoado()
        print("Fim.")

    @staticmethod
    def menu():
        print('\n1- Inserir')
        print('2- Listar')
        print('3- Atualizar')
        print('4- Excluir')
        print('5- Mais populoso')
        print('6- Mais povoado')
        print('7- Sair')
        return int(input('Opção: '))

    @classmethod
    def inserir(cls):
        id = int(input("Id: "))
        nome = input("Nome: ")
        pop = int(input("População: "))
        area = float(input("Área: "))
        cls.paises.append(Pais(id, nome, pop, area))

    @classmethod
    def listar(cls):
        if len(cls.paises) == 0:
            print("Lista vazia")
        else:
            for p in cls.paises:
                print(p)

    @classmethod
    def atualizar(cls):
        id = int(input("Id do país: "))
        for p in cls.paises:
            if p.get_id() == id:
                p.set_nome(input("Novo nome: "))
                p.set_populacao(int(input("Nova população: ")))
                p.set_area(float(input("Nova área: ")))
                return
        print("Não encontrado")

    @classmethod
    def excluir(cls):
        id = int(input("Id do país: "))
        for i in range(len(cls.paises)):
            if cls.paises[i].get_id() == id:
                cls.paises.pop(i)
                print("Removido")
                return
        print("Não encontrado")

    @classmethod
    def mais_populoso(cls):
        if len(cls.paises) == 0:
            print("Lista vazia")
            return

        maior = cls.paises[0]
        for p in cls.paises:
            if p.get_populacao() > maior.get_populacao():
                maior = p

        print("Mais populoso:", maior)

    @classmethod
    def mais_povoado(cls):
        if len(cls.paises) == 0:
            print("Lista vazia")
            return

        maior = cls.paises[0]
        for p in cls.paises:
            if p.densidade() > maior.densidade():
                maior = p

        print("Mais povoado:", maior)

PaisUI.main()