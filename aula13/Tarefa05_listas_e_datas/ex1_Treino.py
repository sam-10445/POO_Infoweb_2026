from datetime import datetime, timedelta
class Treino:
    #init
    def __init__(self, id, data, distancia, tempo):
        self.set_id(id)
        self.set_data(data)
        self.set_distancia(distancia)
        self.set_tempo(tempo)
    #set
    def set_id(self, id):
        if id < 0: raise ValueError()
        self.__id = id
    def set_data(self, data):
        if data > datetime.now(): raise ValueError()
        self.__data = data
    def set_distancia(self, distancia):
        if distancia < 0: raise ValueError()
        self.__distancia = distancia
    def set_tempo(self, tempo):
        if tempo < timedelta(0): raise ValueError()
        self.__tempo = tempo
    #get
    def get_id(self): return self.__id
    def get_data(self): return self.__data
    def get_distancia(self): return self.__distancia
    def get_tempo(self): return self.__tempo

    def Pace(self):
        pace = self.__tempo.total_segunds() / self.__distancia
        return pace

    #ToString
    def __str__(self):
        return f"ID: {self.__id} | Data: {self.__data.strftime("%d/%m/%Y")} | Distância: {self.__distancia} km | Tempo: {self.__tempo} min | Pace: {self.Pace()} min/km"

class TreinoUI:
    #listas
    treinos = []

    #main (op, while, op = TreinoUI.manu())
    @staticmethod
    def main():
        op = -1
        while op != 0:
            op = TreinoUI.menu()
            if op == 1: TreinoUI.inserir()
            if op == 2: TreinoUI.listar()
            if op == 3: TreinoUI.listar_id()
            if op == 4: TreinoUI.atualizar()
            if op == 5: TreinoUI.excluir()
            if op == 6: TreinoUI.mais_rapido()
        print('Programa Encerrado...')

    #menu
    @staticmethod
    def menu():
        print('1. Inserir')
        print('2. Listar')
        print('3. Pesquisar um treino')
        print('4. Atualizar')
        print('5. Excluir')
        print('6. Mais rápido')
        print('0. Sair')
        return int(input('Opção: '))

    @classmethod
    def inserir(cls):
        id = int(input('ID: '))
        data = datetime.strptime(input('Data (dd/mm/aaaa): '), "%d/%m/%Y")
        distancia = float(input('Distância (km): '))
        tempo = timedelta(minutes=int(input("Minutos: ")))

        x = Treino(id, data, distancia, tempo)
        cls.treinos.append(x)

    @classmethod
    def listar(cls):
        if len(cls.treinos) == 0:
            print('Não há treinos registrados...')
        else:
            for x in cls.treinos: print(x)

    @classmethod
    def listar_id(cls):
        id = int(input('ID do treino: '))
        for x in cls.treinos:
            if x.get_id() == id: print(x)

    @classmethod
    def atualizar(cls):
        id = int(input('ID do treino: '))
        for x in cls.treinos:
            if x.get_id() == id:
                data = datetime.strptime(input('Data (dd/mm/aaaa): '), "%d/%m/%Y")
                distancia = float(input('Distância (m): '))
                tempo = timedelta(minutes=int(input("Minutos: ")))

                x.set_data(data)
                x.set_distancia(distancia)
                x.get_tempo(tempo)

    @classmethod
    def excluir(cls):
        id = int(input('Id do Treino: '))
        for x in cls.treinos:
            if x.get_id() == id:
                cls.treinos.remove(x)

    @classmethod
    def mais_rapido(cls):
        paces = []
        if len(cls.treinos) == 0:
            print('Não há treinos registrados...')
        else:
            for x in cls.treinos:
                paces += x.Pace()
                min(paces)

TreinoUI.main()