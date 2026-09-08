from models.cliente import Cliente
from models.clientedao import ClienteDAO
from models.servico import Servico
from models.servicodao import ServicoDAO
from models.horario import Horario
from models.horariodao import HorarioDAO
from models.atendimento import Atendimento
from models.atendimentodao import AtendimentoDAO

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
    def horario_inserir(data, confirmado, id_cliente, id_servico):
        c = Horario(0, data)
        c.set_confirmado(confirmado)
        c.set_id_cliente(id_cliente)
        c.set_id_servico(id_servico)
        HorarioDAO().inserir(c)
    @staticmethod
    def horario_listar():
        return HorarioDAO().listar()
    @staticmethod
    def horario_listar_id(id):
        return HorarioDAO().listar_id(id) 
    @staticmethod
    def horario_atualizar(id, data, confirmado, id_cliente, id_servico):
        c = Horario(id, data)
        c.set_confirmado(confirmado)
        c.set_id_cliente(id_cliente)
        c.set_id_servico(id_servico)
        HorarioDAO().atualizar(c)
    @staticmethod
    def horario_excluir(id):
        HorarioDAO().excluir(id) 

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