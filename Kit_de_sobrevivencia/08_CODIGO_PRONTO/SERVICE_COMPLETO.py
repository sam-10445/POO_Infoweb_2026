# SERVICE COMPLETO (Ctrl K + Ctrl U -> pra tirar o comentário de várias linhas)

from models.nomedaclasse import NomeDaClasse
from models.nomedaclasseDAO import NomeDaClasseDAO


class Service:

    # INSERIR

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


    # ASSOCIAÇÃO NO INSERIR
    #
    # Se a classe precisar receber o ID de outra classe,
    # coloque o ID como parâmetro do método.
    #
    # Exemplo:
    #
    # def horario_inserir(
    #     data,
    #     confirmado,
    #     id_cliente,     # ← ASSOCIAÇÃO
    #     id_servico      # ← ASSOCIAÇÃO
    # ):
    #
    #     obj = Horario(0, data)
    #
    #     obj.set_confirmado(confirmado)
    #
    #     # ASSOCIAÇÃO:
    #     # Guarda o ID do Cliente no Horario.
    #     obj.set_id_cliente(id_cliente)
    #
    #     # ASSOCIAÇÃO:
    #     # Guarda o ID do Serviço no Horario.
    #     obj.set_id_servico(id_servico)
    #
    #     HorarioDAO().inserir(obj)
    #

    # LISTAR

    @staticmethod
    def nomedaclasse_listar():

        return NomeDaClasseDAO().listar()

    # LISTAR POR ID

    @staticmethod
    def nomedaclasse_listar_id(id):

        return NomeDaClasseDAO().listar_id(id)


    # ATUALIZAR

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


    # ASSOCIAÇÃO NO ATUALIZAR
    #
    # Se existir associação, o ID da outra classe também deve
    # ser recebido no método de atualização.
    #
    # Exemplo:
    #
    # def horario_atualizar(
    #     id,
    #     data,
    #     confirmado,
    #     id_cliente,     # ← ASSOCIAÇÃO
    #     id_servico      # ← ASSOCIAÇÃO
    # ):
    #
    #     obj = Horario(id, data)
    #
    #     obj.set_confirmado(confirmado)
    #
    #     # ASSOCIAÇÃO:
    #     # Coloca o ID do Cliente no objeto.
    #     obj.set_id_cliente(id_cliente)
    #
    #     # ASSOCIAÇÃO:
    #     # Coloca o ID do Serviço no objeto.
    #     obj.set_id_servico(id_servico)
    #
    #     HorarioDAO().atualizar(obj)
    #


    # EXCLUIR

    @staticmethod
    def nomedaclasse_excluir(id):

        NomeDaClasseDAO().excluir(id)


    # FILTRAR

    @staticmethod
    def nomedaclasse_filtrar(valor):

        objetos = NomeDaClasseDAO().listar()

        resultado = []

        for obj in objetos:

            if obj.get_atributo1() == valor:

                resultado.append(obj)

        return resultado


    # ASSOCIAÇÃO — BUSCAR OBJETO RELACIONADO
    #
    # Quando existe associação, às vezes precisamos pegar
    # o objeto relacionado usando o ID que foi armazenado.
    #
    # Exemplo:
    #
    # horario = Service.horario_listar_id(id)
    #
    # cliente = Service.cliente_listar_id(
    #     horario.get_id_cliente()
    # )
    #
    # serviço = Service.servico_listar_id(
    #     horario.get_id_servico()
    # )
    #
    # Dessa forma:
    #
    # Horario
    #    ↓
    # id_cliente
    #    ↓
    # Cliente
    #
    # Horario
    #    ↓
    # id_servico
    #    ↓
    # Servico