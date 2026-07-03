from service import Service


class UI:

    @staticmethod
    def main():
        op = 0

        while op != 9:

            op = UI.menu()

            if op == 1:
                UI.cliente_inserir()

            if op == 2:
                UI.cliente_listar()

            if op == 3:
                UI.cliente_atualizar()

            if op == 4:
                UI.cliente_excluir()

            if op == 5:
                UI.servico_inserir()

            if op == 6:
                UI.servico_listar()

            if op == 7:
                UI.servico_atualizar()

            if op == 8:
                UI.servico_excluir()

    @staticmethod
    def menu():
        print()
        print("1 - Inserir Cliente")
        print("2 - Listar Clientes")
        print("3 - Atualizar Cliente")
        print("4 - Excluir Cliente")
        print("5 - Inserir Serviço")
        print("6 - Listar Serviços")
        print("7 - Atualizar Serviço")
        print("8 - Excluir Serviço")
        print("9 - Fim")
        print()

        return int(input("Informe uma opção: "))

    # ==========================
    # CLIENTES
    # ==========================

    @staticmethod
    def cliente_inserir():

        id = int(input("Informe o id: "))
        nome = input("Informe o nome: ")
        email = input("Informe o e-mail: ")
        fone = input("Informe o telefone: ")

        Service.cliente_inserir(id, nome, email, fone)

    @staticmethod
    def cliente_listar():

        for obj in Service.cliente_listar():
            print(obj)

    @staticmethod
    def cliente_atualizar():

        for obj in Service.cliente_listar():
            print(obj)

        id = int(input("Informe o id do cliente: "))
        nome = input("Informe o novo nome: ")
        email = input("Informe o novo e-mail: ")
        fone = input("Informe o novo telefone: ")

        Service.cliente_atualizar(id, nome, email, fone)

    @staticmethod
    def cliente_excluir():

        for obj in Service.cliente_listar():
            print(obj)

        id = int(input("Informe o id do cliente: "))

        Service.cliente_excluir(id)

    # ==========================
    # SERVIÇOS
    # ==========================

    @staticmethod
    def servico_inserir():

        id = int(input("Informe o id: "))
        descricao = input("Informe a descrição: ")
        valor = float(input("Informe o valor: "))

        Service.servico_inserir(id, descricao, valor)

    @staticmethod
    def servico_listar():

        for obj in Service.servico_listar():
            print(obj)

    @staticmethod
    def servico_atualizar():

        for obj in Service.servico_listar():
            print(obj)

        id = int(input("Informe o id do serviço: "))
        descricao = input("Informe a nova descrição: ")
        valor = float(input("Informe o novo valor: "))

        Service.servico_atualizar(id, descricao, valor)

    @staticmethod
    def servico_excluir():

        for obj in Service.servico_listar():
            print(obj)

        id = int(input("Informe o id do serviço: "))

        Service.servico_excluir(id)


UI.main()