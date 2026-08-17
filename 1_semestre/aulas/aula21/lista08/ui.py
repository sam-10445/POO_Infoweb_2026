from service import Service

class UI:

    @staticmethod
    def menu():
        print("1 - Inserir Cliente")
        print("2 - Listar Clientes")
        print("3 - Atualizar Cliente")
        print("4 - Excluir Cliente")
        print("----------------------")
        print("5 - Inserir Serviço")
        print("6 - Listar Serviços")
        print("7 - Atualizar Serviço")
        print("8 - Excluir Serviço")
        print("----------------------")
        print("9 - Fim")
        return int(input("Informe uma opção: "))

    @staticmethod
    def main():
        op = 0
        while op != 9:
            op = UI.menu()

            if op == 1: UI.cliente_inserir()
            elif op == 2: UI.cliente_listar()
            elif op == 3: UI.cliente_atualizar()
            elif op == 4: UI.cliente_excluir()
            elif op == 5: UI.servico_inserir()
            elif op == 6: UI.servico_listar()
            elif op == 7: UI.servico_atualizar()
            elif op == 8: UI.servico_excluir()

    @staticmethod
    def cliente_inserir():
        id = int(input("Informe o id: "))
        nome = input("Informe o nome: ")
        email = input("Informe o e-mail: ")
        fone = input("Informe o telefone: ")
        Service.cliente_inserir(id, nome, email, fone)

    @staticmethod
    def cliente_listar():
        for obj in Service.cliente_listar(): print(obj)

    @staticmethod
    def cliente_atualizar():
        for obj in Service.cliente_listar(): print(obj)

        id = int(input("Informe o id do cliente: "))
        nome = input("Novo nome: ")
        email = input("Novo e-mail: ")
        fone = input("Novo telefone: ")

        Service.cliente_atualizar(id, nome, email, fone)

    @staticmethod
    def cliente_excluir():
        for obj in Service.cliente_listar(): print(obj)

        id = int(input("Informe o id do cliente: "))
        Service.cliente_excluir(id)

    @staticmethod
    def servico_inserir():
        id = int(input("Informe o id: "))
        descricao = input("Informe a descrição: ")
        valor = float(input("Informe o valor: "))
        Service.servico_inserir(id, descricao, valor)

    @staticmethod
    def servico_listar():
        for obj in Service.servico_listar(): print(obj)

    @staticmethod
    def servico_atualizar():
        for obj in Service.servico_listar(): print(obj)

        id = int(input("Informe o id do serviço: "))
        descricao = input("Nova descrição: ")
        valor = float(input("Novo valor: "))

        Service.servico_atualizar(id, descricao, valor)

    @staticmethod
    def servico_excluir():
        for obj in Service.servico_listar(): print(obj)

        id = int(input("Informe o id do serviço: "))
        Service.servico_excluir(id)

UI.main()
