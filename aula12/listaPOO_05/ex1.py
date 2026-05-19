class Paciente: 
    #init
    def __init__(self, nome, cpf, fone, nasc):
        self.set_nome(nome)
        self.set_cpf(cpf)
        self.set_fone(fone)
        self.set_nasc(nasc)
    #set
    def set_nome(self, nome):
        if len(nome) == 0: raise ValueError()
        self.__nome = nome
    def set_cpf(self, cpf):
        if len(cpf) < 12: raise ValueError()
        self.__cpf = cpf
    def set_fone(self, fone):
        if len(fone) == 0: raise ValueError()
        self.__fone = fone
    def set_nasc(self, nasc):
        if nasc == '': raise ValueError()
        self.__nasc = nasc
    #get
    def get_nome(self): return self.__nome
    def get_cpf(self): return self.__cpf
    def get_fone(self): return self.__fone
    def get_nasc(self): return self.__nasc
    #ToString
    def __str__(self):
        return f"Nome: {self.__nome} | Cpf: {self.__cpf} | Telefone: {self.__fone} | Data de Nascimento: {self.__nasc}"
    
class PacienteUI:
    #listas
    pacientes = []
    #main (op, while, op = UI.menu())
    def main():
        op = -1
        while op != 0:
            op = PacienteUI.menu()
            if op == 1: PacienteUI.inserir()
    #menu
    def menu():
        print(...)
        return int(input('Escolha: '))
PacienteUI.main()