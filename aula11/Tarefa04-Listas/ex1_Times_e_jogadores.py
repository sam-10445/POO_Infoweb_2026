class Time:
    def __init__(self, id, nome, estado):
        self.set_id(id)
        self.set_nome(nome)
        self.set_estado(estado)

    #sets
    def set_id(self, id):
        if id < 0: ValueError() #id negativo
        self.__id = id

    def set_nome(self, nome):
        if nome == "": ValueError()
        self.__nome = nome

    def set_estado(self, estado):
        if estado == "": ValueError()
        self.__estado = estado

    #gets
    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_estado(self): return self.__estado

    #ToString
    def __str__(self):
        return f"ID: {self.__id} | Nome: {self.__nome} | Estado: {self.__estado}"

class Jogador:
    def __init__(self, id, id_time, nome, camisa):
        self.set_id(id)
        self.set_id_time(id_time)
        self.set_nome(nome)
        self.set_camisa(camisa)

    #sets
    def set_id(self, id):
        if id < 0: ValueError()
        self.__id = id

    def set_id_time(self, id_time):
        if id_time < 0: ValueError()
        self.__id_time = id_time

    def set_nome(self, nome):
        if nome == "": ValueError()
        self.__nome = nome

    def set_camisa(self, camisa):
        if camisa < 0: ValueError()
        self.__camisa = camisa

    #gets
    def get_id(self): return self.__id

    def get_id_time(self): return self.__id_time

    def get_nome(self): return self.__nome

    def get_camisa(self): return self.__camisa

    #ToString
    def __str__(self):
        return f"ID: {self.__id} | Nome: {self.__nome} | Camisa: {self.__camisa} | Time: {self.__id_time}"

#INTERFACE DO USUÁRIO
class UI:
    times = []
    jogadores = []

    def inserir_time(self):
        id = int(input("ID do time: "))
        nome = input("Nome do time: ")
        estado = input("Estado do time: ")

        time = Time(id, nome, estado)
        self.times.append(time)
        print("Time cadastrado!\n")

    def listar_times(self):
        if len(self.times) == 0: #ver se a lista está vazia
            print("Nenhum time cadastrado.\n")
        else:
            for time in self.times: #varer a lista
                print(time)

    def atualizar_time(self):
        id = int(input("Digite o ID do time: "))

        for time in self.times:
            if time.get_id() == id:
                novo_nome = input("Novo nome: ")
                novo_estado = input("Novo estado: ")

                time.set_nome(novo_nome)
                time.set_estado(novo_estado)

                print("Time atualizado!\n")
                return

        print("Time não encontrado.\n")

    def excluir_time(self):
        id = int(input("Digite o ID do time: "))

        for time in self.times:
            if time.get_id() == id:
                self.times.remove(time)

                for jogador in self.jogadores[:]:
                    if jogador.get_id_time() == id:
                        self.jogadores.remove(jogador)

                print("Time removido!\n")
                return

        print("Time não encontrado.\n")

    def inserir_jogador(self):
        id = int(input("ID do jogador: "))
        id_time = int(input("ID do time: "))
        nome = input("Nome do jogador: ")
        camisa = int(input("Número da camisa: "))

        jogador = Jogador(id, id_time, nome, camisa)
        self.jogadores.append(jogador)

        print("Jogador cadastrado!\n")

    def listar_jogadores(self):
        if len(self.jogadores) == 0:
            print("Nenhum jogador cadastrado.\n")
        else:
            for jogador in self.jogadores:
                print(jogador)
            print()

    def atualizar_jogador(self):
        id = int(input("Digite o ID do jogador: "))

        for jogador in self.jogadores:
            if jogador.get_id() == id:
                novo_nome = input("Novo nome: ")
                nova_camisa = int(input("Nova camisa: "))

                jogador.set_nome(novo_nome)
                jogador.set_camisa(nova_camisa)

                print("Jogador atualizado!\n")
                return

        print("Jogador não encontrado.\n")

    def excluir_jogador(self):
        id = int(input("Digite o ID do jogador: "))

        for jogador in self.jogadores:
            if jogador.get_id() == id:
                self.jogadores.remove(jogador)

                print("Jogador removido!\n")
                return

        print("Jogador não encontrado.\n")

    def listar_jogadores_do_time(self):
        id_time = int(input("Digite o ID do time: "))

        encontrou = False

        for jogador in self.jogadores:
            if jogador.get_id_time() == id_time:
                print(jogador)
                encontrou = True

        if not encontrou:
            print("Nenhum jogador encontrado nesse time.")

        print()

    def transferir_jogador(self):
        id_jogador = int(input("ID do jogador: "))
        novo_time = int(input("Novo ID do time: "))

        for jogador in self.jogadores:
            if jogador.get_id() == id_jogador:
                jogador.set_id_time(novo_time)

                print("Jogador transferido!\n")
                return

        print("Jogador não encontrado.\n")
    
    #menu

    def main(self):
        opcao = 1223

        while opcao != 0:
            print("1 - Inserir time")
            print("2 - Listar times")
            print("3 - Atualizar time")
            print("4 - Excluir time")
            print("5 - Inserir jogador")
            print("6 - Listar jogadores")
            print("7 - Atualizar jogador")
            print("8 - Excluir jogador")
            print("9 - Listar jogadores de um time")
            print("10 - Transferir jogador")
            print("0 - Sair")
            opcao = int(input("Informe uma opção:  "))

            if opcao == 1: self.inserir_time()
            if opcao == 2: self.listar_times()
            if opcao == 3: self.atualizar_time()
            if opcao == 4: self.excluir_time()
            if opcao == 5: self.inserir_jogador()
            if opcao == 6: self.listar_jogadores()
            if opcao == 7: self.atualizar_jogador()
            if opcao == 8: self.excluir_jogador()
            if opcao == 9: self.listar_jogadores_do_time()
            if opcao == 10: self.transferir_jogador()
            if opcao == 0: print("Tchau :)")

# Programa principal
ui = UI()
ui.main()