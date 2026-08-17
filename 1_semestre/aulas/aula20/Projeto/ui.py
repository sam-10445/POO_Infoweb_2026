from service import Service
class UI:
    @staticmethod
    def menu():
        print("1 - Inserir Cliente")
        print("2 - Listar Clientes")
        print("3 - Atualizar Cliente")
        print("4 - Excluir Cliente")
        print("5 - Pesquisar Cliente por Nome")
        print("6 - Inserir Serviço")
        print("7 - Listar Serviços")
        print("8 - Atualizar Serviço")
        print("9 - Excluir Serviço")
        print("10 - Pesquisar Serviço por Descrição")
        print("11 - Fim")
        return int(input("Informe uma opção: "))

    @staticmethod
    def main():
        op = 0
        while op != 11:
            op = UI.menu()
            if op == 1: UI.cliente_inserir()
            if op == 2: UI.cliente_listar()
            if op == 3: UI.cliente_atualizar()
            if op == 4: UI.cliente_excluir()
            if op == 5: UI.cliente_listar_nome()
            if op == 6: UI.servico_inserir()
            if op == 7: UI.servico_listar()
            if op == 8: UI.servico_atualizar()
            if op == 9: UI.servico_excluir()
            if op == 10: UI.servico_listar_descricao()

    @staticmethod
    def cliente_inserir():
        nome = input("Informe o nome: ")
        email = input("Informe o e-mail: ")
        fone = input("Informe o telefone: ")
        Service.cliente_inserir(nome, email, fone)

    @staticmethod
    def cliente_listar():
        for x in Service.cliente_listar():
            print(x)

    @staticmethod
    def cliente_listar_nome():
        nome = input("Informe o início do nome: ")
        for x in Service.cliente_listar_nome(nome):
            print(x)

    @staticmethod
    def cliente_atualizar():
        for x in Service.cliente_listar():
            print(x)

        id = int(input("Informe o id do cliente: "))
        nome = input("Informe o novo nome: ")
        email = input("Informe o novo e-mail: ")
        fone = input("Informe o novo telefone: ")
        Service.cliente_atualizar(id, nome, email, fone)

    @staticmethod
    def cliente_excluir():
        for x in Service.cliente_listar():
            print(x)
        id = int(input("Informe o id do cliente: "))
        Service.cliente_excluir(id)

    @staticmethod
    def servico_inserir():
        descricao = input("Informe a descrição: ")
        valor = float(input("Informe o valor: "))
        Service.servico_inserir(descricao, valor)

    @staticmethod
    def servico_listar():
        for x in Service.servico_listar():
            print(x)

    @staticmethod
    def servico_listar_descricao():
        descricao = input("Informe o início da descrição: ")
        for x in Service.servico_listar_descricao(descricao):
            print(x)

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
        for x in Service.servico_listar():
            print(x)
        id = int(input("Informe o id do serviço: "))
        Service.servico_excluir(id)

UI.main()