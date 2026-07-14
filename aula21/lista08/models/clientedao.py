from models.cliente import Cliente
import json

class ClienteDAO:
    def __init__(self):
        self.__arquivo = "clientes.json"
        self.__objetos = []
        self.__abrir()

    def inserir(self, obj):
        self.__objetos.append(obj)
        self.__salvar()

    def listar(self): return self.__objetos

    def listar_id(self, id):
        for obj in self.__objetos:
            if obj.get_id() == id:
                return obj
        return None

    def atualizar(self, obj):
        aux = self.listar_id(obj.get_id())

        if aux != None:
            self.__objetos.remove(aux)
            self.__objetos.append(obj)
            self.__salvar()

    def excluir(self, id):
        aux = self.listar_id(id)

        if aux != None:
            self.__objetos.remove(aux)
            self.__salvar()

    def __abrir(self):
        try:
            arquivo = open(self.__arquivo, "r")
            lista = json.load(arquivo)
            arquivo.close()

            self.__objetos = []

            for dic in lista:
                self.__objetos.append(Cliente.from_json(dic))

        except FileNotFoundError:
            pass

    def __salvar(self):
        arquivo = open(self.__arquivo, "w")

        json.dump(
            self.__objetos,
            arquivo,
            default=Cliente.to_json,
            indent=2
        )

        arquivo.close()