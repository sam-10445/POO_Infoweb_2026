# AGORA, APRENDER A FAZER O DAO
# (init, abrir, salvar, CRUD)

#importar a classe
from models.cliente import Cliente

class ClienteDAO:
    def __init__(self):
        self.__arquivo = "cliente.json"