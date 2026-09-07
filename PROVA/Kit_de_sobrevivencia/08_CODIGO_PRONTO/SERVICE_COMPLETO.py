# ============================================================
# SERVICE COMPLETO
# ============================================================

from models.nomedaclasse import NomeDaClasse
from models.nomedaclasseDAO import NomeDaClasseDAO


class Service:

    # ========================================================
    # INSERIR
    # ========================================================

    @staticmethod
    def nomedaclasse_inserir(
        atributo1,
        atributo2,
        atributo3
    ):

        obj = NomeDaClasse(
            0,
            atributo1,
            atributo2,
            atributo3
        )

        NomeDaClasseDAO().inserir(obj)

    # ========================================================
    # LISTAR
    # ========================================================

    @staticmethod
    def nomedaclasse_listar():

        return NomeDaClasseDAO().listar()

    # ========================================================
    # LISTAR POR ID
    # ========================================================

    @staticmethod
    def nomedaclasse_listar_id(id):

        return NomeDaClasseDAO().listar_id(id)

    # ========================================================
    # ATUALIZAR
    # ========================================================

    @staticmethod
    def nomedaclasse_atualizar(
        id,
        atributo1,
        atributo2,
        atributo3
    ):

        obj = NomeDaClasse(
            id,
            atributo1,
            atributo2,
            atributo3
        )

        NomeDaClasseDAO().atualizar(obj)

    # ========================================================
    # EXCLUIR
    # ========================================================

    @staticmethod
    def nomedaclasse_excluir(id):

        NomeDaClasseDAO().excluir(id)

    # ========================================================
    # FILTRAR
    # ========================================================

    @staticmethod
    def nomedaclasse_filtrar(valor):

        objetos = NomeDaClasseDAO().listar()

        resultado = []

        for obj in objetos:

            if obj.get_atributo1() == valor:

                resultado.append(obj)

        return resultado