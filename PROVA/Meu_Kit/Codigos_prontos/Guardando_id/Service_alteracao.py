

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