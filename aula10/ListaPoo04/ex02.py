class Contato: 
    def __init__(self, id, nome, email, fone):
        self.set_id(id)
        self.set_nome(nome)
        self.set_email(email)
        self.set_fone(fone)

    def set_id(self, id):
        if id < 0: raise ValueError('Id deve ser positivo')
        self.__id = id

    def set_nome(self, nome):
        if nome == "": raise ValueError('Nome não pode ser vazio')
        self.__nome = nome

    def set_email(self, email): 
        self.__email = email

    def set_fone(self, fone): 
        self.__fone = fone

    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_email(self): return self.__email
    def get_fone(self): return self.__fone

    def __str__(self): 
        return f"{self.__id} - {self.__nome} - {self.__email} - {self.__fone}"


class ContatoUI:
    contatos = []

    @staticmethod
    def main():
        op = 0
        while op != 6:
            op = ContatoUI.menu()
            if op == 1: ContatoUI.inserir()
            elif op == 2: ContatoUI.listar()
            elif op == 3: ContatoUI.atualizar()
            elif op == 4: ContatoUI.excluir()
            elif op == 5: ContatoUI.pesquisar()
        print("Fim do programa.")

    @staticmethod #quando você não precisa acessar nenhuma variável
    def menu():
        print('-'*30)
        print('\n1- Inserir')
        print('2- Listar')
        print('3- Atualizar')
        print('4- Excluir')
        print('5- Pesquisar')
        print('6- Fim')
        return int(input('Informe uma opção: '))

    @classmethod #quando você precisa acessar uma variavel solta (contatos)
    def inserir(cls):
        id = int(input('Informe o id do contato: '))
        nome = input('Informe o nome: ')
        email = input('Informe o e-mail: ')
        fone = input('Informe o telefone: ')
        x = Contato(id, nome, email, fone)
        cls.contatos.append(x)

    @classmethod #quando você precisa acessar uma variavel solta (contatos)
    def listar(cls):
        if len(cls.contatos) == 0:
            print('Nenhum contato inserido')
        else:
            for x in cls.contatos:
                print(x)

    @classmethod #quando você precisa acessar uma variavel solta (contatos)
    def atualizar(cls):
        if len(cls.contatos) == 0:
            print('Lista vazia')
            return

        y = int(input('Informe o ID do contato: '))
        for i in range(len(cls.contatos)):
            if cls.contatos[i].get_id() == y:
                print('Encontrado!')
                cls.contatos[i].set_nome(input('Novo nome: '))
                cls.contatos[i].set_email(input('Novo e-mail: '))
                cls.contatos[i].set_fone(input('Novo telefone: '))
                return

        print('Não encontrado')

    @classmethod #quando você precisa acessar uma variavel solta (contatos)
    def excluir(cls):
        if len(cls.contatos) == 0:
            print('Lista vazia')
            return

        y = int(input('Informe o ID do contato para excluir: '))
        for i in range(len(cls.contatos)):
            if cls.contatos[i].get_id() == y:
                cls.contatos.pop(i)
                print('Contato removido!')
                return

        print('Não encontrado')

    @classmethod #quando você precisa acessar uma variavel solta (contatos)
    def pesquisar(cls):
        if len(cls.contatos) == 0:
            print('Lista vazia')
            return

        inicio = input('Digite o início do nome: ').lower()
        encontrou = False

        for x in cls.contatos:
            if x.get_nome().lower().startswith(inicio):
                print(x)
                encontrou = True

        if not encontrou:
            print('Nenhum contato encontrado')

ContatoUI.main()