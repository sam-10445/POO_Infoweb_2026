from datetime import datetime
class Paciente: 
    #init
    def __init__(self, id,  nome, cpf, fone, nasc):
        self.set_id(id)
        self.set_nome(nome)
        self.set_cpf(cpf)
        self.set_fone(fone)
        self.set_nasc(nasc)
    #set
    def set_id(self, id):
        if id < 0: raise ValueError('Id deve ser positivo.')
        self.__id = id
    def set_nome(self, nome):
        if len(nome) == 0: raise ValueError('Nome não pode ser vazio.')
        self.__nome = nome
    def set_cpf(self, cpf):
        if len(cpf) < 12: raise ValueError('O CPF deve conter, pelo menos, 12 caracteres.')
        self.__cpf = cpf
    def set_fone(self, fone):
        if len(fone) == 0: raise ValueError('O Telefone não pode ser vazio.')
        self.__fone = fone
    # validar data de nascimento
    def set_nasc(self, nasc):
        if nasc > datetime.now(): raise ValueError('Data não pode ser no futuro.')
        self.__nasc = nasc

    #get
    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_cpf(self): return self.__cpf
    def get_fone(self): return self.__fone
    def get_nasc(self): return self.__nasc

    #ToString (contrario do init)
    def __str__(self):
        return f"ID: {self.__id} | Nome: {self.__nome} | Cpf: {self.__cpf} | Telefone: {self.__fone} | " + \
            f"Data de Nascimento: {self.__nasc.strftime("%d/%m/%Y")}"
            # formatar a data para aparecer no formato nacional

    def calc_idade(self):
        tempo = datetime.now() - self.__nasc  # dias, horas, minutos, ... timedelta
        anos = tempo.days // 365
        meses = tempo.days % 365 // 30 #maior valor possível: 364 (antes de dividir por 30)
        return f"{anos} ano(s) e {meses} mes(es)"
    
#TESTAR 
#OB: SÓ DEIXE ATIVO A CLASS PACIENTE PARA TESTAR SEM O UI
#x = Paciente(1, "Eduardo", "09876655544433", "8490014458", datetime(1990, 10, 5))
#print(x)
#print(x.calc_idade())

    
class PacienteUI:
    #listas
    __pacientes = []

    #main (op, while, op = UI.menu())
    @staticmethod
    def main():
        op = -1
        while op != 0:
            op = PacienteUI.menu()
            if op == 1: PacienteUI.inserir()
            if op == 2: PacienteUI.listar()
            if op == 3: PacienteUI.excluir()
            if op == 4: PacienteUI.atualizar()
            if op == 5: Paciente.pesquisar()
            if op == 6: PacienteUI.anive()
        print('Programa encerrado...')

    #menu
    @staticmethod
    def menu():
        print('1 - Inserir')
        print('2 - Listar')
        print('3 - Atualizar')
        print('4 - Excluir')
        print('5 - Pesquisar')
        print('6 - Aniversariantes')
        print(' 0 - Sair')
        return int(input('Escolha: '))
    
    @classmethod
    def inserir(cls):
        id = int(input('ID: '))
        nome = input('Nome:')
        cpf = input('CPF: ')
        fone = input('Telefone: ')
        # pedi data
        data = datetime.strptime(input('Data de Nascimento (dd/mm/aaaa): '), "%d/%m/%Y")

        x = Paciente(id, nome, cpf, fone, data)
        cls.__pacientes.append(x)

    @classmethod
    def listar(cls):
        if len(cls.__pacientes) == 0:
            print('Nenhum paciente cadastrado.')
        else:
            for x in cls.__pacientes: print(x, x.calc_idade())

    @classmethod
    def atualizar(cls):
        id = int(input('ID do paciente: '))
        for x in cls.__pacientes:
            if x.get_id() == id:
                nome = input('Novo Nome:')
                cpf = input('Novo CPF: ')
                fone = input('Novo Telefone: ')
                # pedi data
                data = datetime.strptime(input('Nova Data de Nascimento (dd/mm/aaaa): '), "%d/%m/%Y")
            
            x.set_nome(nome)
            x.set_cpf(cpf)
            x.set_fone(fone)
            x.set_data(data)

    @classmethod
    def excluir(cls):
        id = int(input('ID do paciente: '))
        for x in cls.__pacientes:
            if x.get_id() == id:
                cls.__pacientes.remove(x)

    @classmethod
    def pesquisar(cls):
        s = input('As iniciais do paciente: ')
        for x in cls.__pacientes:
            if x.get_nome().startwith(s): print(x)

    @classmethod
    def anive(cls):
        m = int(input('O mês para listar os aniversariantes: '))
        for x in cls.__pacientes:
            if x.get_data().month == m: print(x)

PacienteUI.main()