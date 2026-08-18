from datetime import datetime, timedelta

class Treino:
    #init
    def __init__(self, id, data, dist, tempo):
        self.set_id(id)
        self.set_data(data)
        self.set_dist(dist)
        self.set_tempo(tempo)

    #sets
    def set_id(self, id):
        if id < 0: raise ValueError()
        self.__id = id

    def set_data(self, data):
        #no futuro
        if data > datetime.now(): raise ValueError() 
        self.__data = data #?

    def set_dist(self, dist):
        if dist < 0: raise ValueError()
        self.__dist = dist

    def set_tempo(self, tempo):
        if tempo < timedelta(0): raise ValueError()
        self.__tempo = tempo 

    #gets
    def get_id(self): return self.__id
    def get_data(self): return self.__data #?
    def get_dist(self): return self.__dist
    def get_tempo(self): return self.__tempo

    #ToString
    def __str__(self):
        return f"ID: {self.__id} | Data: {self.__data.strftime("%d/%m/%Y")} | Distância: {self.__distancia} km | Tempo: {self.__tempo} min | Pace: {self.Pace()} min/km"