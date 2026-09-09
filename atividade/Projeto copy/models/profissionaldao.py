# DAO COMPLETO

from models.profissional import Profissional
import json


class ProfissionalDAO:

    def __init__(self):

        self.__arquivo = "profissional.json"
        self.__objetos = []

        self.__abrir()

    # INSERIR

    def inserir(self, obj):

        id = 0

        if len(self.__objetos) > 0:

            for aux in self.__objetos:

                if aux.get_id() > id:
                    id = aux.get_id()

        obj.set_id(id + 1)

        self.__objetos.append(obj)

        self.__salvar()

    # LISTAR

    def listar(self):

        return self.__objetos

    # LISTAR POR ID

    def listar_id(self, id):

        for obj in self.__objetos:

            if obj.get_id() == id:
                return obj

        return None

    # ATUALIZAR

    def atualizar(self, obj):

        aux = self.listar_id(obj.get_id())

        if aux != None:

            self.__objetos.remove(aux)

            self.__objetos.append(obj)

            self.__salvar()

    # EXCLUIR

    def excluir(self, id):

        aux = self.listar_id(id)

        if aux != None:

            self.__objetos.remove(aux)

            self.__salvar()

    # ABRIR JSON

    def __abrir(self):

        try:

            arquivo = open(
                self.__arquivo,
                mode="r"
            )

            list_dic = json.load(arquivo)

            arquivo.close()

            self.__objetos = []

            for dic in list_dic:

                obj = Profissional.from_json(dic)

                self.__objetos.append(obj)

        except FileNotFoundError:

            pass

    # SALVAR JSON

    def __salvar(self):

        arquivo = open(
            self.__arquivo,
            mode="w"
        )

        json.dump(
            self.__objetos,
            arquivo,
            default=Profissional.to_json,
            indent=2
        )

        arquivo.close()