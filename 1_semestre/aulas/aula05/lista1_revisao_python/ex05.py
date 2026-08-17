class País:
    #dados
    def __init__(self):
        self.nome = ''
        self.popu = 0
        self.area = 0
    #calculos
    def densidade(self):
        return self.popu / self.area

x = País()
x.nome = input('Digite o nome do país: ')
x.popu = int(input('Digite sua população: '))
x.area = int(input('Digite a área em km²: '))
print(f'A densidade demográfica do {x.nome} é de {x.densidade():.2f}')
