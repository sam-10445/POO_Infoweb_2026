from models.cliente import Cliente
from models.clientedao import ClienteDAO
from models.servico import Servico
from models.servicodao import ServicoDAO
from models.horario import Horario
from models.horariodao import HorarioDAO
from models.profissional import Profissional
from models.profissionaldao import ProfissionalDAO
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

class Service:
    @staticmethod
    def _validar_email_unico(email, id_cliente=None, id_profissional=None):
        if id_cliente is not None:
            cliente_atual = Service.cliente_listar_id(id_cliente)
            if cliente_atual != None:
                if cliente_atual.get_email() == "admin" and email != "admin":
                    raise ValueError("O e-mail do administrador não pode ser alterado")

        for cliente in Service.cliente_listar():
            if cliente.get_id() != id_cliente:
                if cliente.get_email() == email:
                    raise ValueError("E-mail já cadastrado para outro cliente")

        for profissional in Service.profissional_listar():
            if profissional.get_id() != id_profissional:
                if profissional.get_email() == email:
                    raise ValueError("E-mail já cadastrado para outro profissional")

    @staticmethod
    def cliente_inserir(nome, email, fone, senha):
        obj = Cliente(0, nome, email, fone, senha)
        Service._validar_email_unico(obj.get_email())
        ClienteDAO().inserir(obj)

    @staticmethod
    def cliente_listar():
        r = ClienteDAO().listar()
        r.sort(key = lambda obj : obj.get_nome().casefold())
        return r

    @staticmethod
    def cliente_listar_id(id):
        return ClienteDAO().listar_id(id)

    @staticmethod
    def cliente_atualizar(id, nome, email, fone, senha):
        obj = Cliente(id, nome, email, fone, senha)
        Service._validar_email_unico(obj.get_email(), id_cliente=id)
        ClienteDAO().atualizar(obj)

    @staticmethod
    def cliente_excluir(id):
        horarios = Service.horario_listar_cliente(id)
        if len(horarios) > 0: raise ValueError("Não é possível excluir um cliente com horário agendado")
        ClienteDAO().excluir(id)

    @staticmethod
    def cliente_criar_admin():
        for c in Service.cliente_listar():
            if c.get_email() == "admin":
                return
        Service.cliente_inserir("admin", "admin", "fone", "1234")

    @staticmethod
    def cliente_autenticar(email, senha):
        for c in Service.cliente_listar():
            if c.get_email() == email and c.get_senha() == senha:
                return {"id": c.get_id(), "nome": c.get_nome()}
        return None


    @staticmethod
    def servico_inserir(descricao, valor):
        obj = Servico(0, descricao, valor)
        ServicoDAO().inserir(obj)

    @staticmethod
    def servico_listar():
        r = ServicoDAO().listar()
        r.sort(key = lambda obj : obj.get_descricao().casefold())
        return r

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

        Service._validar_horario_unico(c.get_data(), c.get_id_profissional())

        HorarioDAO().inserir(c)

    @staticmethod
    def horario_listar():
        r = HorarioDAO().listar()
        r.sort(key = lambda obj : obj.get_data())

        return r

    @staticmethod
    def horario_listar_id(id):
        return HorarioDAO().listar_id(id)

    @staticmethod
    def _validar_horario_unico(data, id_profissional, id=None):
        if id_profissional in [None, 0]:
            return

        for horario in Service.horario_listar():
            if horario.get_id() != id:
                if horario.get_id_profissional() == id_profissional:
                    if horario.get_data() == data:
                        raise ValueError("Já existe um horário nessa data e hora para esse profissional")

    @staticmethod
    def horario_atualizar(id, data, confirmado, id_cliente, id_servico, id_profissional):
        c = Horario(id, data)
        c.set_confirmado(confirmado)
        c.set_id_cliente(id_cliente)
        c.set_id_servico(id_servico)
        c.set_id_profissional(id_profissional)

        Service._validar_horario_unico(c.get_data(), c.get_id_profissional(), id)

        HorarioDAO().atualizar(c)

    @staticmethod
    def horario_excluir(id):
        horario = Service.horario_listar_id(id)
        if horario != None:
            if horario.get_id_cliente() not in [None, 0]:
                raise ValueError("Não é possível excluir um horário ja agendado por um cliente.")
        HorarioDAO().excluir(id)

    @staticmethod
    def horario_abrir_agenda(inicio, fim, intervalo, id_profissional):

        agora = datetime.now(
            ZoneInfo("America/Sao_Paulo")
        ).replace(tzinfo=None)

        if inicio <= agora:
            raise ValueError("A agenda deve começar em uma data futura")

        if fim <= inicio:
            raise ValueError("O horário final deve ser maior que o inicial")

        if intervalo <= 0:
            raise ValueError("O intervalo deve ser positivo")

        existentes = Service.horario_listar_profissional(
            id_profissional
        )

        novos_horarios = []
        atual = inicio

        while atual < fim:

            for h in existentes:
                if h.get_data() == atual:
                    raise ValueError(
                        f"Já existe um horário em {atual:%d/%m/%Y %H:%M}"
                    )

            novos_horarios.append(atual)
            atual += timedelta(minutes=intervalo)

        for data in novos_horarios:
            Service.horario_inserir(
                data, False, None, None, id_profissional
            )

        return len(novos_horarios)

    # Lista os horários de hoje que já foram agendados por um cliente
    # e ainda não foram confirmados. A lista fica em ordem de horário.
    @staticmethod
    def horario_listar_nao_confirmados_hoje():
        hoje = datetime.now(
            ZoneInfo("America/Sao_Paulo")
        ).date()

        r = []

        for h in Service.horario_listar():
            if h.get_data().date() == hoje \
            and h.get_id_cliente() not in [None, 0] \
            and not h.get_confirmado():
                r.append(h)

        r.sort(key=lambda h: h.get_data())

        return r

    @staticmethod
    def horario_listar_disponiveis(id_profissional):
        r = []

        agora = datetime.now(
            ZoneInfo("America/Sao_Paulo")
        ).replace(tzinfo=None)

        for h in Service.horario_listar():
            if h.get_data() >= agora and h.get_confirmado() == False \
            and h.get_id_cliente() == None and h.get_id_profissional() == id_profissional:
                r.append(h)

        r.sort(key = lambda h : h.get_data())

        return r

    @staticmethod
    def horario_listar_profissional(id_profissional):
        r = []

        for h in Service.horario_listar():
            if h.get_id_profissional() == id_profissional:
                r.append(h)

        r.sort(key = lambda h : h.get_data())

        return r

    @staticmethod
    def horario_listar_cliente(id_cliente):
        r = []

        for h in Service.horario_listar():
            if h.get_id_cliente() == id_cliente:
                r.append(h)

        r.sort(key = lambda h : h.get_data())

        return r

    @staticmethod
    def horario_listar_agendados(id_profissional):
        r = []

        for h in Service.horario_listar():
            if h.get_id_profissional() == id_profissional \
            and h.get_id_cliente() not in [None, 0] \
            and h.get_confirmado() == False:
                r.append(h)

        r.sort(key = lambda h : h.get_data())

        return r

    @staticmethod
    def cliente_alterar_senha(id, senha):
        obj = Service.cliente_listar_id(id)

        if obj != None:
            Service.cliente_atualizar(
                id,
                obj.get_nome(),
                obj.get_email(),
                obj.get_fone(),
                senha
            )


    @staticmethod
    def profissional_inserir(nome, email, especialidade, senha):
        obj = Profissional(0, nome, email, especialidade, senha)
        Service._validar_email_unico(obj.get_email())
        ProfissionalDAO().inserir(obj)

    @staticmethod
    def profissional_listar():
        r = ProfissionalDAO().listar()
        r.sort(key = lambda obj : obj.get_nome().casefold())
        return r

    @staticmethod
    def profissional_listar_id(id):
        return ProfissionalDAO().listar_id(id)

    @staticmethod
    def profissional_atualizar(id, nome, email, especialidade, senha):
        obj = Profissional(id, nome, email, especialidade, senha)
        Service._validar_email_unico(obj.get_email(),id_profissional=id)
        ProfissionalDAO().atualizar(obj)

    @staticmethod
    def profissional_excluir(id):
        horarios = Service.horario_listar_profissional(id)
        if len(horarios) > 0:raise ValueError("Não é possível excluir profissionais com horários cadastrados")
        ProfissionalDAO().excluir(id)

    @staticmethod
    def profissional_autenticar(email, senha):
        for c in Service.profissional_listar():
            if c.get_email() == email and c.get_senha() == senha:
                return {"id": c.get_id(), "nome": c.get_nome()}
        return None
    
    @staticmethod
    def profissional_alterar_senha(id, senha):
        obj = Service.profissional_listar_id(id)

        if obj != None:
            Service.profissional_atualizar(
                id,
                obj.get_nome(),
                obj.get_email(),
                obj.get_especialidade(),
                senha
            )