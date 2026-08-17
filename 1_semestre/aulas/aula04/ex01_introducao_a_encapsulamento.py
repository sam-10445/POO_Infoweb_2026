#Entidades
class Aluno:
    #FUNÇÕES PRA PEGA OS DADOS (DADOS ENCAPSULADOS)
    def __init__(self):
        self.__nome = '' #atributo escondido (encapculado) do programa principal (__)
        self.__matricula = '' #atributo encapsulado
    
    #FUNÇÃO PRA LER O NOME 
    def set_nome(self, valor): 
        #função que ler o nome
        if len(valor) < 3: raise ValueError("Nome deve ter pelo menos 3 letras")
        #else: (opcional pq quando dá erro ele já para)
        self.__nome = valor
    
    #FUNÇÃO PRA RETORNAR O NOME
    def get_nome(self):
        return self.__nome
    
    #FUNÇÃO PRA LER A MATRÍCULA
    def set_matricula(self, valor): 
        #função que ler a matricula
        if len(valor) < 5: raise ValueError('Nome deve ter pelo menos 5 caracteres')
        self.__matricula = valor
    
    #FUNÇÃO PRA RETORNAR O NOME
    def get_matricula(self):
        return self.__matricula
    
    #FUNÇÃO PRA CALCULAR O ANO DE INGRESSO
    def ano_ingresso(self):
        return self.__matricula[:4]

#Programa principal
class UI: #(interfase do usuario em inglês)
    def main():
        x = Aluno()
        x.set_nome(input('Nome: ')) #ler o nome (set)
        x.set_matricula(input('Matrícula: ')) #ler a matricula (set)
        print(f'Aluno(a) {x.get_nome()}, de matricula {x.get_matricula()}') #retornar o nome e matricula (get)
        print(f'entrou no IF em {x.ano_ingresso()}') #retornar a função que foi calculada (normal)

UI.main()