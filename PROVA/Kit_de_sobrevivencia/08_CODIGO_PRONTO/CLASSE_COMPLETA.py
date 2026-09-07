# ============================================================
# CLASSE COMPLETA — MODELO DO PROJETO
# ============================================================
#
# Quando o professor pedir uma nova classe:
#
# 1. Copie este código.
# 2. Troque o nome da classe.
# 3. Troque os atributos.
# 4. Altere getters/setters.
# 5. Confira to_json e from_json.
#
# ============================================================


class NomeDaClasse:

    def __init__(self, id, atributo1, atributo2, atributo3):

        self.set_id(id)
        self.set_atributo1(atributo1)
        self.set_atributo2(atributo2)
        self.set_atributo3(atributo3)

    # -----------------------------
    # SETTERS
    # -----------------------------

    def set_id(self, id):
        if id < 0:
            raise ValueError("Id deve ser positivo")
        self.__id = id

    def set_atributo1(self, atributo1):
        if atributo1 == "":
            raise ValueError("Atributo deve ser informado")
        self.__atributo1 = atributo1

    def set_atributo2(self, atributo2):
        if atributo2 == "":
            raise ValueError("Atributo deve ser informado")
        self.__atributo2 = atributo2

    def set_atributo3(self, atributo3):
        if atributo3 == "":
            raise ValueError("Atributo deve ser informado")
        self.__atributo3 = atributo3

    # -----------------------------
    # GETTERS
    # -----------------------------

    def get_id(self):
        return self.__id

    def get_atributo1(self):
        return self.__atributo1

    def get_atributo2(self):
        return self.__atributo2

    def get_atributo3(self):
        return self.__atributo3

    # -----------------------------
    # STR
    # -----------------------------

    def __str__(self):
        return (
            f"{self.__id} - "
            f"{self.__atributo1} - "
            f"{self.__atributo2} - "
            f"{self.__atributo3}"
        )

    # -----------------------------
    # OBJETO → DICIONÁRIO
    # -----------------------------

    def to_json(self):

        return {
            "id": self.__id,
            "atributo1": self.__atributo1,
            "atributo2": self.__atributo2,
            "atributo3": self.__atributo3
        }

    # -----------------------------
    # DICIONÁRIO → OBJETO
    # -----------------------------

    @staticmethod
    def from_json(dic):

        return NomeDaClasse(
            dic["id"],
            dic["atributo1"],
            dic["atributo2"],
            dic["atributo3"]
        )