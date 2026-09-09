from models.cliente import Cliente
from models.clientedao import ClienteDAO
from models.servico import Servico
from models.servicodao import ServicoDAO
from models.horario import Horario
from models.horariodao import HorarioDAO
from models.atendimento import Atendimento
from models.atendimentodao import AtendimentoDAO
from models.profissional import Profissional
from models.profissionaldao import ProfissionalDAO

class Service:
    @staticmethod
    def cliente_inserir(nome, email, fone):
        obj = Cliente(0, nome, email, fone)
        ClienteDAO().inserir(obj)
    @staticmethod
    def cliente_listar():
        return ClienteDAO().listar()
    @staticmethod
    def cliente_listar_id(id):
        return ClienteDAO().listar_id(id)
    @staticmethod
    def cliente_atualizar(id, nome, email, fone):
        obj = Cliente(id, nome, email, fone)
        ClienteDAO().atualizar(obj)
    @staticmethod
    def cliente_excluir(id):
        ClienteDAO().excluir(id)


    @staticmethod
    def servico_inserir(descricao, valor):
        obj = Servico(0, descricao, valor)
        ServicoDAO().inserir(obj)
    @staticmethod
    def servico_listar():
        return ServicoDAO().listar()
    @staticmethod
    def servico_listar_id(id):
        return ServicoDAO().listar_id(id)
    @staticmethod
    def servico_atualizar(id, descricao, valor):
        obj = Servico(id, descricao, valor)
        ServicoDAO().atualizar(obj)
    @staticmethod
    def servico_excluir(id):
        ServicoDAO().excluir(id)


    @staticmethod
    def horario_inserir(data, confirmado, id_cliente, id_servico, id_profissional):
        c = Horario(0, data)
        c.set_confirmado(confirmado)
        c.set_id_cliente(id_cliente)
        c.set_id_servico(id_servico)
        c.set_id_profissional(id_profissional)
        HorarioDAO().inserir(c)
    @staticmethod
    def horario_listar():
        return HorarioDAO().listar()
    @staticmethod
    def horario_listar_id(id):
        return HorarioDAO().listar_id(id) 
    @staticmethod
    def horario_atualizar(id, data, confirmado, id_cliente, id_servico, id_profissional):
        c = Horario(id, data)
        c.set_confirmado(confirmado)
        c.set_id_cliente(id_cliente)
        c.set_id_servico(id_servico)
        c.set_id_profissional(id_profissional)
        HorarioDAO().atualizar(c)
    @staticmethod
    def horario_excluir(id):
        HorarioDAO().excluir(id) 


# INSERIR

    @staticmethod
    def profissional_inserir(
        nome,
        email,
        especialidade
    ):

        obj = Profissional(
            0,
            nome,
            email,
            especialidade
        )

        ProfissionalDAO().inserir(obj)


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
    def profissional_listar():

        return ProfissionalDAO().listar()

    # LISTAR POR ID

    @staticmethod
    def profissional_listar_id(id):

        return ProfissionalDAO().listar_id(id)


    # ATUALIZAR

    @staticmethod
    def profissional_atualizar(
        id,
        nome,
        email,
        especialidade
    ):

        obj = Profissional(
            id,
            nome,
            email,
            especialidade
        )

        ProfissionalDAO().atualizar(obj)


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
    def profissioal_excluir(id):

        ProfissionalDAO().excluir(id)


    # FILTRAR

    @staticmethod
    def profissional_filtrar(valor):

        objetos = ProfissionalDAO().listar()

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

###### ATENDIMENTO

    @staticmethod
    def atendimento_inserir(
        data,
        queixa,
        historico,
        avaliacao,
        prescricao,
        id_horario
    ):

        obj = AtendimentoDAO(
            0,
            data,
            queixa,
            historico,
            avaliacao,
            prescricao,
            id_horario
        )

        AtendimentoDAO().inserir(obj)


    @staticmethod
    def atendimento_listar():

        return AtendimentoDAO().listar()

    @staticmethod
    def atendimento_listar_id(id):

        return AtendimentoDAO().listar_id(id)

    @staticmethod
    def atendimento_atualizar(
        id,
        data,
        queixa,
        historico,
        avaliacao,
        prescricao,
        id_horario
    ):

        obj = Atendimento(
            id,
            data,
            queixa,
            historico,
            avaliacao,
            prescricao,
            id_horario
        )

        AtendimentoDAO().atualizar(obj)


    @staticmethod
    def atendimento_excluir(id):

        AtendimentoDAO().excluir(id)


    @staticmethod
    def atendimento_filtrar(valor):

        objetos = AtendimentoDAO().listar()

        resultado = []

        for obj in objetos:

            if obj.get_atributo1() == valor:

                resultado.append(obj)

        return resultado