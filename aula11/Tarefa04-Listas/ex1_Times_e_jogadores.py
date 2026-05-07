class Time:
    def __init__(self, id, nome, estado):
        self.set_id(id)
        self.set_nome(nome)
        self.set_estado(estado)
    #sets
    def set_id(self, id):
        if id < 0: raise ValueError()
        self.__id = id

    def set_nome(self, nome):
        if len(nome) < 3: raise ValueError()
        self.__nome = nome

    def set_estado(self, estado):
        if len(estado) < 2: raise ValueError()
        self.__estado = estado

    #gets
    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_estado(self): return self.__estado
    
    #ToString
    def __str__(self):
        return f'ID: {self.__id}, Nome: {self.__nome}, Estado: {self.__estado}'

class Jogador:
    def __init__(self, id, idTime, nome, camisa):
        self.set_id = (id)
        self.set_idTime = (idTime)
        self.set_nome = (nome)
        self.set_camisa = (camisa)
    #set
    def set_id(self, id):
        if id < 0: raise ValueError()
        self.__id = id
    def set_idTime(self, idTime): 
        if idTime < 0: raise ValueError()
        self.__idTime = idTime
    def set_nome(self, nome):
        if len(nome) < 3: raise ValueError()
        self.__nome = nome
    def set_camisa(self, camisa):
        if camisa < 1 and camisa > 99: raise ValueError()
        self.__camisa = camisa
    #get
    def get_id(self):
        return self.__id
    def get_idTime(self):
        return self.__idTime
    def get_nome(self):
        return self.__nome
    def get_camisa(self):
        return self.__camisa
    
    #ToString
    def __str__(self):
        return (f'ID: {self.__id}, Nome: {self.__nome}, Camisa: {self.__camisa}, Time: {self.__idTime}')
    
    #CLASSE UI
    class UI:
        #CRIAR AS LISTAS 
        times = []
        jogadores = []

        #CRIAR O LOOP (MAIN)
        @staticmethod
        def main(): 
            op = 0
            while op != 11:
                op = UI.menu()
                if op == 1: UI.inseir()
                if op == 1: UI.inseir()
                if op == 1: UI.inseir()
                if op == 1: UI.inseir()
                if op == 1: UI.inseir()
                if op == 1: UI.inseir()
                if op == 1: UI.inseir()
                if op == 1: UI.inseir()
                if op == 1: UI.inseir()
                if op == 1: UI.inseir()
                if op == 1: UI.inseir()

        #CRIAR O MENU
        @staticmethod
        def menu():
            print('*OPÇÕES*')
            return int(input('Informe a opção: '))