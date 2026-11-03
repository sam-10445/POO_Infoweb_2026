from datetime import datetime
from service import Service


class UI:
    @staticmethod
    def main():
        op = 0
        while op != 9:
            op = UI.menu()
            if op == 1: UI.cliente_inserir()
            if op == 2: UI.cliente_listar()
            if op == 3: UI.cliente_atualizar()
            if op == 4: UI.cliente_excluir()
            if op == 5: UI.servico_inserir()
            if op == 6: UI.servico_listar()
            if op == 7: UI.servico_atualizar()
            if op == 8: UI.servico_excluir()
            if op == 9: UI.horario_inserir()
            if op == 10: UI.horario_listar()
            if op == 11: UI.horario_atualizar()
            if op == 12: UI.horario_excluir()
            if op == 13: UI.profissional_inserir()
            if op == 14: UI.profissional_listar()
            if op == 15: UI.profissional_atualizar()
            if op == 16: UI.profissional_excluir()

    @staticmethod
    def menu():
        print("\n========== SISTEMA DE AGENDAMENTOS ==========")
        print("Clientes      1-Inserir  2-Listar  3-Atualizar  4-Excluir")
        print("Serviços      5-Inserir  6-Listar  7-Atualizar  8-Excluir")
        print("Horários      9-Inserir 10-Listar 11-Atualizar 12-Excluir")
        print("Profissionais 13-Inserir 14-Listar 15-Atualizar 16-Excluir")
        print("17-Sair")
        return int(input("Escolha uma opção: "))

    @staticmethod
    def ler_texto(rotulo, atual=None):
        valor = input(f"{rotulo}: ").strip()
        return valor if valor else (atual if atual is not None else "")

    @staticmethod
    def ler_inteiro(rotulo, atual=None):
        valor = input(f"{rotulo}: ").strip()
        if not valor and atual is not None:
            return atual
        return int(valor)

    @staticmethod
    def ler_id_opcional(rotulo, atual=None):
        valor = input(f"{rotulo} (Enter=manter, 0=nenhum): ").strip()
        if not valor:
            return atual
        id = int(valor)
        if id < 0:
            raise ValueError("O ID não pode ser negativo")
        return None if id == 0 else id

    @staticmethod
    def ler_data(rotulo, atual=None):
        valor = input(f"{rotulo} (dd/mm/aaaa HH:MM): ").strip()
        if not valor and atual is not None:
            return atual
        return datetime.strptime(valor, "%d/%m/%Y %H:%M")

    @staticmethod
    def ler_confirmacao(rotulo, atual=False):
        valor = input(f"{rotulo} (s/n, Enter mantém): ").strip().lower()
        if valor == "":
            return atual
        if valor in ("s", "sim"):
            return True
        if valor in ("n", "nao", "não"):
            return False
        raise ValueError("Responda s ou n")

    # CLIENTES
    @staticmethod
    def cliente_inserir():
        nome = UI.ler_texto("Nome")
        email = UI.ler_texto("E-mail")
        fone = UI.ler_texto("Telefone")
        senha = UI.ler_texto("Senha")
        Service.cliente_inserir(nome, email, fone, senha)
        print("Cliente cadastrado com sucesso.")

    @staticmethod
    def cliente_listar():
        clientes = Service.cliente_listar()
        if not clientes:
            print("Nenhum cliente cadastrado.")
        for cliente in clientes:
            print(cliente)

    @staticmethod
    def cliente_atualizar():
        UI.cliente_listar()
        id = UI.ler_inteiro("ID do cliente")
        cliente = Service.cliente_listar_id(id)
        if cliente is None:
            print("Cliente não encontrado.")
            return
        nome = UI.ler_texto("Nome (Enter mantém)", cliente.get_nome())
        email = UI.ler_texto("E-mail (Enter mantém)", cliente.get_email())
        fone = UI.ler_texto("Telefone (Enter mantém)", cliente.get_fone())
        senha = UI.ler_texto("Nova senha (Enter mantém)", cliente.get_senha())
        Service.cliente_atualizar(id, nome, email, fone, senha)
        print("Cliente atualizado com sucesso.")

    @staticmethod
    def cliente_excluir():
        UI.cliente_listar()
        id = UI.ler_inteiro("ID do cliente")
        if Service.cliente_listar_id(id) is None:
            print("Cliente não encontrado.")
            return
        Service.cliente_excluir(id)
        print("Cliente excluído com sucesso.")

    
    @staticmethod
    def servico_inserir():
        descricao = UI.ler_texto("Descrição")
        valor = float(input("Valor: "))
        duracao = UI.ler_inteiro("Duração em minutos")
        Service.servico_inserir(descricao, valor, duracao)
        print("Serviço cadastrado com sucesso.")

    @staticmethod
    def servico_listar():
        servicos = Service.servico_listar()
        if not servicos:
            print("Nenhum serviço cadastrado.")
        for servico in servicos:
            print(servico)

    @staticmethod
    def servico_atualizar():
        UI.servico_listar()
        id = UI.ler_inteiro("ID do serviço")
        servico = Service.servico_listar_id(id)
        if servico is None:
            print("Serviço não encontrado.")
            return
        descricao = UI.ler_texto("Descrição (Enter mantém)", servico.get_descricao())
        valor_texto = input("Valor (Enter mantém): ").strip()
        valor = float(valor_texto) if valor_texto else servico.get_valor()
        duracao = UI.ler_inteiro("Duração em minutos (Enter mantém)", servico.get_duracao())
        Service.servico_atualizar(id, descricao, valor, duracao)
        print("Serviço atualizado com sucesso.")

    @staticmethod
    def servico_excluir():
        UI.servico_listar()
        id = UI.ler_inteiro("ID do serviço")
        if Service.servico_listar_id(id) is None:
            print("Serviço não encontrado.")
            return
        Service.servico_excluir(id)
        print("Serviço excluído com sucesso.")


    @staticmethod
    def horario_listar():
        horarios = Service.horario_listar()
        if not horarios:
            print("Nenhum horário cadastrado.")
        for h in horarios:
            print(
                f"ID {h.get_id()} | {h.get_data():%d/%m/%Y %H:%M} | "
                f"Profissional: {h.get_id_profissional()} | "
                f"Cliente: {h.get_id_cliente()} | "
                f"Serviço: {h.get_id_servico()} | "
                f"Confirmado: {h.get_confirmado()}"
            )

    @staticmethod
    def horario_inserir():
        UI.profissional_listar()
        id_profissional = UI.ler_inteiro("ID do profissional")
        data = UI.ler_data("Data e hora")
        UI.cliente_listar()
        id_cliente = UI.ler_id_opcional("ID do cliente")
        UI.servico_listar()
        id_servico = UI.ler_id_opcional("ID do serviço")
        confirmado = UI.ler_confirmacao("Confirmado")
        if id_cliente is not None and id_servico is None:
            raise ValueError("Para um agendamento, informe também o serviço")
        Service.horario_inserir(data, confirmado, id_cliente, id_servico, id_profissional)
        print("Horário cadastrado com sucesso.")

    @staticmethod
    def horario_atualizar():
        UI.horario_listar()
        id = UI.ler_inteiro("ID do horário")
        horario = Service.horario_listar_id(id)
        if horario is None:
            print("Horário não encontrado.")
            return
        data = UI.ler_data("Data e hora (Enter mantém)", horario.get_data())
        id_profissional = UI.ler_inteiro(
            "ID do profissional (Enter mantém)", horario.get_id_profissional()
        )
        id_cliente = UI.ler_id_opcional("ID do cliente", horario.get_id_cliente())
        id_servico = UI.ler_id_opcional("ID do serviço", horario.get_id_servico())
        confirmado = UI.ler_confirmacao("Confirmado", horario.get_confirmado())
        if id_cliente is not None and id_cliente != 0 and id_servico in (None, 0):
            raise ValueError("Para um agendamento, informe também o serviço")
        Service.horario_atualizar(id, data, confirmado, id_cliente, id_servico, id_profissional)
        print("Horário atualizado com sucesso.")

    @staticmethod
    def horario_excluir():
        UI.horario_listar()
        id = UI.ler_inteiro("ID do horário")
        if Service.horario_listar_id(id) is None:
            print("Horário não encontrado.")
            return
        Service.horario_excluir(id)
        print("Horário excluído com sucesso.")

    
    @staticmethod
    def profissional_inserir():
        nome = UI.ler_texto("Nome")
        email = UI.ler_texto("E-mail")
        especialidade = UI.ler_texto("Especialidade")
        senha = UI.ler_texto("Senha")
        Service.profissional_inserir(nome, email, especialidade, senha)
        print("Profissional cadastrado com sucesso.")

    @staticmethod
    def profissional_listar():
        profissionais = Service.profissional_listar()
        if not profissionais:
            print("Nenhum profissional cadastrado.")
        for profissional in profissionais:
            print(profissional)

    @staticmethod
    def profissional_atualizar():
        UI.profissional_listar()
        id = UI.ler_inteiro("ID do profissional")
        profissional = Service.profissional_listar_id(id)
        if profissional is None:
            print("Profissional não encontrado.")
            return
        nome = UI.ler_texto("Nome (Enter mantém)", profissional.get_nome())
        email = UI.ler_texto("E-mail (Enter mantém)", profissional.get_email())
        especialidade = UI.ler_texto("Especialidade (Enter mantém)", profissional.get_especialidade())
        senha = UI.ler_texto("Nova senha (Enter mantém)", profissional.get_senha())
        Service.profissional_atualizar(id, nome, email, especialidade, senha)
        print("Profissional atualizado com sucesso.")

    @staticmethod
    def profissional_excluir():
        UI.profissional_listar()
        id = UI.ler_inteiro("ID do profissional")
        if Service.profissional_listar_id(id) is None:
            print("Profissional não encontrado.")
            return
        Service.profissional_excluir(id)
        print("Profissional excluído com sucesso.")


UI.main()
