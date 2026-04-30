import random

class Bingo:
    def __init__(self):
        self.__bolas = 0
        self.__sorteados = []

    def iniciar(self, bolas):
        self.__bolas = bolas
        self.__sorteados = []

    def sortear(self):
        if len(self.__sorteados) == self.__bolas:
            return -1

        n = random.randint(1, self.__bolas)

        while n in self.__sorteados:
            n = random.randint(1, self.__bolas)

        self.__sorteados.append(n)
        return n

    def sorteados(self):
        return self.__sorteados


class BingoUI:
    jogo = None

    @staticmethod
    def main():
        op = 0
        while op != 4:
            op = BingoUI.menu()
            if op == 1: BingoUI.iniciar_jogo()
            elif op == 2: BingoUI.sortear()
            elif op == 3: BingoUI.mostrar_sorteados()
        print("Fim.")

    @staticmethod
    def menu():
        print('\n1- Iniciar jogo')
        print('2- Sortear número')
        print('3- Ver sorteados')
        print('4- Sair')
        return int(input('Opção: '))

    @staticmethod
    def iniciar_jogo():
        n = int(input('Quantidade de bolas: '))
        BingoUI.jogo = Bingo()
        BingoUI.jogo.iniciar(n)
        print("Jogo iniciado!")

    @staticmethod
    def sortear():
        if BingoUI.jogo is None:
            print("Inicie o jogo primeiro")
            return

        n = BingoUI.jogo.sortear()
        if n == -1:
            print("Todas as bolas já foram sorteadas")
        else:
            print("Número sorteado:", n)

    @staticmethod
    def mostrar_sorteados():
        if BingoUI.jogo is None:
            print("Inicie o jogo primeiro")
        else:
            print("Sorteados:", BingoUI.jogo.sorteados())

BingoUI.main()