# CLASSE COMPLETA — MODELO DO PROJETO
#
# Quando o professor pedir uma nova classe:
#
# 1. Copie este código.
# 2. Troque o nome da classe.
# 3. Troque os atributos.
# 4. Altere getters/setters.
# 5. Confira to_json e from_json.


class Profissional:

    def __init__(self, id, nome, email, especialidade):

        self.set_id(id)
        self.set_nome(nome)
        self.set_email(email)
        self.set_especialidade(especialidade)

    # SETTERS

    def set_id(self, id):
        if id < 0:
            raise ValueError("Id deve ser positivo")
        self.__id = id

    def set_nome(self, nome):
        if nome == "":
            raise ValueError("nome deve ser informado")
        self.__nome = nome

    def set_email(self, email):
        if email == "":
            raise ValueError("email deve ser informado")
        self.__email = email

    def set_especialidade(self, especialidade):
        if especialidade == "":
            raise ValueError("Especialidade deve ser informado")
        self.__especialidade = especialidade

    # GETTERS

    def get_id(self):
        return self.__id

    def get_nome(self):
        return self.__nome

    def get_email(self):
        return self.__email

    def get_especialidade(self):
        return self.__especialidade

    # STR

    def __str__(self):
        return (
            f"{self.__id} - "
            f"{self.__nome} - "
            f"{self.__email} - "
            f"{self.__especialidade}"
        )

    # OBJETO → DICIONÁRIO

    def to_json(self):

        return {
            "id": self.__id,
            "nome": self.__nome,
            "email": self.__email,
            "especialidade": self.__especialidade
        }

    # DICIONÁRIO → OBJETO

    @staticmethod
    def from_json(dic):

        return Profissional(
            dic["id"],
            dic["nome"],
            dic["email"],
            dic["especialidade"]
        )