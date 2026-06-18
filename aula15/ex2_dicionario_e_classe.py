import json

class Cliente:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome
    def __str__(self):
        return f"{self.id} - {self.nome}"
    def to_json(self):
        return {"id": self.id, "nome:": self.nome}
    @staticmethod
    def from_json(dic):
        return Cliente(dic["id"], dic["nome"])

def salvar():
    a = Cliente(1, "Douglas Crockford") #chamando o __init__
    b = Cliente(2, "Jon Bosak")
    c = Cliente.from_json({"id": 3, "nome" : "Alan Turing"})

    lista = [a, b, c]

    arquivo = open("clientes.json", mode = "w")
    json.dump(lista, arquivo, default = Cliente.to_json)
    arquivo.close()

    #TRANSFORMAR UM OBJETO EM UM DICIONÁRIO
    #formas já criadas: 
    print(a)
    print(b)
    print(c)
    print(a.__dict__)
    print(b.__dict__)
    print(vars(a))
    print(vars(b))

    #criar uma função criar o dicionário
    print(a.to_json())
    print(b.to_json())

    #TRANSFORMAR UM DICIONÁRIO EM UM OBJETO
    print(c.to_json())

salvar()
