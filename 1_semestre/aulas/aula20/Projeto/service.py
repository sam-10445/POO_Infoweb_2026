from models.cliente import Cliente
from models.clientedao import ClienteDAO

from models.servico import Servico
from models.servicodao import ServicoDAO

class Service:

    __clienteDAO = ClienteDAO()
    __servicoDAO = ServicoDAO()

    @staticmethod
    def cliente_inserir(nome, email, fone):
        obj = Cliente(0, nome, email, fone)
        Service.__clienteDAO.inserir(obj)

    @staticmethod
    def cliente_listar():
        return Service.__clienteDAO.listar()
    
    @staticmethod
    def cliente_listar_id(id):
        return Service.__clienteDAO.listar_id(id)
    
    @staticmethod
    def cliente_listar_nome(nome):
        return Service.__clienteDAO.listar_nome(nome)
    
    @staticmethod
    def cliente_atualizar(id, nome, email, fone):
        obj = Cliente(id, nome, email, fone)
        Service.__clienteDAO.atualizar(obj)

    @staticmethod
    def cliente_excluir(id):
        Service.__clienteDAO.excluir(id)

    @staticmethod
    def servico_inserir(descricao, valor):
        obj = Servico(0, descricao, valor)
        Service.__servicoDAO.inserir(obj)

    @staticmethod
    def servico_listar():
        return Service.__servicoDAO.listar()
    
    @staticmethod
    def servico_listar_id(id):
        return Service.__servicoDAO.listar_id(id)
    
    @staticmethod
    def servico_listar_descricao(descricao):
        return Service.__servicoDAO.listar_descricao(descricao)
    
    @staticmethod
    def servico_atualizar(id, descricao, valor):
        obj = Servico(id, descricao, valor)
        Service.__servicoDAO.atualizar(obj)
        
    @staticmethod
    def servico_excluir(id):
        Service.__servicoDAO.excluir(id)