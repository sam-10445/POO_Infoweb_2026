from models.cliente import Cliente
from models.clientedao import ClienteDAO
from models.servico import Servico
from models.servicodao import ServicoDAO


class Service:

    __clienteDAO = ClienteDAO()
    __servicoDAO = ServicoDAO()

    @staticmethod
    def cliente_inserir(id, nome, email, fone):
        Service.__clienteDAO.inserir(Cliente(id, nome, email, fone))

    @staticmethod
    def cliente_listar(): return Service.__clienteDAO.listar()

    @staticmethod
    def cliente_listar_id(id): return Service.__clienteDAO.listar_id(id)

    @staticmethod
    def cliente_atualizar(id, nome, email, fone):
        Service.__clienteDAO.atualizar(Cliente(id, nome, email, fone))

    @staticmethod
    def cliente_excluir(id):
        Service.__clienteDAO.excluir(id)

    @staticmethod
    def servico_inserir(id, descricao, valor):
        Service.__servicoDAO.inserir(Servico(id, descricao, valor))

    @staticmethod
    def servico_listar(): return Service.__servicoDAO.listar()

    @staticmethod
    def servico_listar_id(id): return Service.__servicoDAO.listar_id(id)

    @staticmethod
    def servico_atualizar(id, descricao, valor):
        Service.__servicoDAO.atualizar(Servico(id, descricao, valor))

    @staticmethod
    def servico_excluir(id):
        Service.__servicoDAO.excluir(id)