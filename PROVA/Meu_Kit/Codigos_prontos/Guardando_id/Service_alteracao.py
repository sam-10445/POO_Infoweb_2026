## ATENDIMENTO
@staticmethod
def atendimento_inserir(data, queixa_principal, historico_saude, avaliacao, prescricao, id_horario):
    c = Atendimento(0, data, queixa_principal, historico_saude, avaliacao, prescricao)
    c.set_id_horario(id_horario)
    AtendimentoDAO().inserir(c)

@staticmethod
def atendimento_listar():
    return AtendimentoDAO().listar()

@staticmethod
def atendimento_listar_id(id):
    return AtendimentoDAO().listar_id(id)

@staticmethod
def atendimento_atualizar(id, data, queixa_principal, historico_saude, avaliacao, prescricao, id_horario):
    c = Atendimento(id, data, queixa_principal, historico_saude, avaliacao, prescricao)
    c.set_id_horario(id_horario)
    AtendimentoDAO().atualizar(c)

@staticmethod
def atendimento_excluir(id):
    AtendimentoDAO().excluir(id)