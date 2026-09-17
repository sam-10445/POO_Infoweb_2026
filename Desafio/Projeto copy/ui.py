'''from service import Service

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

    @staticmethod
    def menu():
        print("Clientes ----------------------------------")
        print("1-Inserir, 2-Listar, 3-Atualizar, 4-Excluir")
        print("Serviços ----------------------------------")
        print("5-Inserir, 6-Listar, 7-Atualizar, 8-Excluir")
        print("Outras opções -----------------------------")
        print("9-Fim")
        return int(input("Informe uma opção: "))

    @staticmethod
    def cliente_inserir():
        # id = int(input("Informe o id: "))
        nome = input("Informe o nome: ")
        email = input("Informe o e-mail: ")
        fone = input("Informe o telefone: ")
        Service.cliente_inserir(nome, email, fone)

    @staticmethod
    def cliente_listar():
        for obj in Service.cliente_listar(): print(obj)

    @staticmethod
    def cliente_atualizar():
        for obj in Service.cliente_listar(): print(obj)
        id = int(input("Informe o id do cliente a ser atualizado: "))
        nome = input("Informe o novo nome: ")
        email = input("Informe o novo e-mail: ")
        fone = input("Informe o novo telefone: ")
        Service.cliente_atualizar(id, nome, email, fone)

    @staticmethod
    def cliente_excluir():
        for obj in Service.cliente_listar(): print(obj)
        id = int(input("Informe o id do cliente a ser excluído: "))
        Service.cliente_excluir(id)

    @staticmethod
    def servico_inserir():
        #id = int(input("Informe o id: "))
        descricao = input("Informe a descrição: ")
        valor = float(input("Informe o valor: "))
        Service.servico_inserir(descricao, valor)

    @staticmethod
    def servico_listar():
        for obj in Service.servico_listar(): print(obj)

    @staticmethod
    def servico_atualizar():
        for obj in Service().servico_listar(): print(obj)
        id = int(input("Informe o id do serviço a ser atualizado: "))
        descricao = input("Informe a nova descrição: ")
        valor = float(input("Informe o novo valor: "))
        Service.servico_atualizar(id, descricao, valor)

    @staticmethod
    def servico_excluir():
        for obj in Service().servico_listar(): print(obj)
        id = int(input("Informe o id do serviço a ser excluído: "))
        Service.servico_excluir(id)

UI.main()'''
from service import Service
from datetime import datetime
 
class UI: 
    @staticmethod 
    def main(): 
        op = 0 
        while op != 21: 
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
            if op == 17: UI.atendimento_inserir()
            if op == 18: UI.atendimento_listar()
            if op == 19: UI.atendimento_atualizar()
            if op == 20: UI.atendimento_excluir()
 
    @staticmethod 
    def menu(): 
        print("Clientes ----------------------------------") 
        print("1-Inserir, 2-Listar, 3-Atualizar, 4-Excluir") 
        print("Serviços ----------------------------------") 
        print("5-Inserir, 6-Listar, 7-Atualizar, 8-Excluir")
        print("Horários ----------------------------------")
        print("9-Inserir, 10-Listar, 11-Atualizar, 12-Excluir")
        print("Profissionais -----------------------------")
        print("13-Inserir, 14-Listar, 15-Atualizar, 16-Excluir")
        print("Atendimentos ------------------------------")
        print("17-Inserir, 18-Listar, 19-Atualizar, 20-Excluir")
        print("Outras opções -----------------------------") 
        print("21-Fim") 
        return int(input("Informe uma opção: ")) 
 
    @staticmethod 
    def cliente_inserir(): 
        # id = int(input("Informe o id: ")) 
        nome = input("Informe o nome: ") 
        email = input("Informe o e-mail: ") 
        fone = input("Informe o telefone: ") 
        Service.cliente_inserir(nome, email, fone) 
 
    @staticmethod 
    def cliente_listar(): 
        for obj in Service.cliente_listar(): print(obj) 
 
    @staticmethod 
    def cliente_atualizar(): 
        for obj in Service.cliente_listar(): print(obj) 
        id = int(input("Informe o id do cliente a ser atualizado: ")) 
        nome = input("Informe o novo nome: ") 
        email = input("Informe o novo e-mail: ") 
        fone = input("Informe o novo telefone: ") 
        Service.cliente_atualizar(id, nome, email, fone) 
 
    @staticmethod 
    def cliente_excluir(): 
        for obj in Service.cliente_listar(): print(obj) 
        id = int(input("Informe o id do cliente a ser excluído: ")) 
        Service.cliente_excluir(id) 
 
    @staticmethod 
    def servico_inserir(): 
        #id = int(input("Informe o id: ")) 
        descricao = input("Informe a descrição: ") 
        valor = float(input("Informe o valor: ")) 
        Service.servico_inserir(descricao, valor) 
 
    @staticmethod 
    def servico_listar(): 
        for obj in Service.servico_listar(): print(obj) 
 
    @staticmethod 
    def servico_atualizar(): 
        for obj in Service().servico_listar(): print(obj) 
        id = int(input("Informe o id do serviço a ser atualizado: ")) 
        descricao = input("Informe a nova descrição: ") 
        valor = float(input("Informe o novo valor: ")) 
        Service.servico_atualizar(id, descricao, valor) 
 
    @staticmethod 
    def servico_excluir(): 
        for obj in Service().servico_listar(): print(obj) 
 
        id = int(input("Informe o id do serviço a ser excluído: ")) 
        Service.servico_excluir(id)

    @staticmethod
    def horario_inserir():
        data = input("Informe a data e horário: ")
        data = datetime.strptime(data, "%d/%m/%Y %H:%M")
        confirmado = input("Informe se está confirmado (True/False): ") == "True"
        id_cliente = int(input("Informe o id do cliente: "))
        id_servico = int(input("Informe o id do serviço: "))
        Service.horario_inserir(data, confirmado, id_cliente, id_servico)

    @staticmethod
    def horario_listar():
        for obj in Service.horario_listar(): print(obj)

    @staticmethod
    def horario_atualizar():
        for obj in Service.horario_listar(): print(obj)
        id = int(input("Informe o id do horário a ser atualizado: "))
        data = input("Informe a nova data e horário: ")
        data = datetime.strptime(data, "%d/%m/%Y %H:%M")
        confirmado = input("Informe se está confirmado (True/False): ") == "True"
        id_cliente = int(input("Informe o novo id do cliente: "))
        id_servico = int(input("Informe o novo id do serviço: "))
        Service.horario_atualizar(id, data, confirmado, id_cliente, id_servico)

    @staticmethod
    def horario_excluir():
        for obj in Service.horario_listar(): print(obj)
        id = int(input("Informe o id do horário a ser excluído: "))
        Service.horario_excluir(id)

    @staticmethod
    def profissional_inserir():
        nome = input("Informe o nome: ")
        email = input("Informe o e-mail: ")
        especialidade = input("Informe a especialidade: ")
        Service.profissional_inserir(nome, email, especialidade)

    @staticmethod
    def profissional_listar():
        for obj in Service.profissional_listar(): print(obj)

    @staticmethod
    def profissional_atualizar():
        for obj in Service.profissional_listar(): print(obj)
        id = int(input("Informe o id do profissional a ser atualizado: "))
        nome = input("Informe o novo nome: ")
        email = input("Informe o novo e-mail: ")
        especialidade = input("Informe a nova especialidade: ")
        Service.profissional_atualizar(id, nome, email, especialidade)

    @staticmethod
    def profissional_excluir():
        for obj in Service.profissional_listar(): print(obj)
        id = int(input("Informe o id do profissional a ser excluído: "))
        Service.profissional_excluir(id)

    @staticmethod
    def atendimento_inserir():
        data = input("Informe a data e horário do atendimento: ")
        data = datetime.strptime(data, "%d/%m/%Y %H:%M")
        queixa_principal = input("Informe a queixa principal: ")
        historico_saude = input("Informe o histórico de saúde: ")
        avaliacao = input("Informe a avaliação: ")
        prescricao = input("Informe a prescrição: ")
        id_horario = int(input("Informe o id do horário: "))
        Service.atendimento_inserir(data, queixa_principal, historico_saude, avaliacao, prescricao, id_horario)

    @staticmethod
    def atendimento_listar():
        for obj in Service.atendimento_listar(): print(obj)

    @staticmethod
    def atendimento_atualizar():
        for obj in Service.atendimento_listar(): print(obj)
        id = int(input("Informe o id do atendimento a ser atualizado: "))
        data = input("Informe a nova data e horário do atendimento: ")
        data = datetime.strptime(data, "%d/%m/%Y %H:%M")
        queixa_principal = input("Informe a nova queixa principal: ")
        historico_saude = input("Informe o novo histórico de saúde: ")
        avaliacao = input("Informe a nova avaliação: ")
        prescricao = input("Informe a nova prescrição: ")
        id_horario = int(input("Informe o novo id do horário: "))
        Service.atendimento_atualizar(id, data, queixa_principal, historico_saude, avaliacao, prescricao, id_horario)

    @staticmethod
    def atendimento_excluir():
        for obj in Service.atendimento_listar(): print(obj)
        id = int(input("Informe o id do atendimento a ser excluído: "))
        Service.atendimento_excluir(id)
 
UI.main()