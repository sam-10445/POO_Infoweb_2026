from models.cliente import Cliente
from models.clientedao import ClienteDAO
from models.servico import Servico
from models.servicodao import ServicoDAO
from models.horario import Horario
from models.horariodao import HorarioDAO
from models.departamento import Departamento
from models.departamentodao import DepartamentoDAO

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
    def servico_inserir(descricao, valor, id_departamento):
        obj = Servico(0, descricao, valor, id_departamento)
        ServicoDAO().inserir(obj)
    @staticmethod
    def servico_listar():
        return ServicoDAO().listar()
    @staticmethod
    def servico_listar_id(id):
        return ServicoDAO().listar_id(id)
    @staticmethod
    def servico_atualizar(id, descricao, valor, id_departamento):
        obj = Servico(id, descricao, valor, id_departamento)
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



    # DEPARTAMENTO
    @staticmethod
    def departamento_inserir(nome, diretor, fone):
        obj = Departamento(0, nome, diretor, fone)
        DepartamentoDAO().inserir(obj)
    @staticmethod
    def departamento_listar():
        return DepartamentoDAO().listar()
    @staticmethod
    def departamento_listar_id(id):
        return DepartamentoDAO().listar_id(id)
    @staticmethod
    def departamento_atualizar(id, nome, diretor, fone):
        obj = Departamento(id, nome, diretor, fone)
        DepartamentoDAO().atualizar(obj)
    @staticmethod
    def departamento_excluir(id):
        DepartamentoDAO().excluir(id)