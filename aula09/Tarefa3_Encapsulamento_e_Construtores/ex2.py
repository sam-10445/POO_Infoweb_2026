class Pais:
    def __init__(self, nome, populacao, area):
        self.set_nome(nome)
        self.set_populacao(populacao)
        self.set_area(area)

    # Getters e Setters com validação
    def get_nome(self):
        return self._nome

    def set_nome(self, nome):
        if nome and isinstance(nome, str):
            self._nome = nome
        else:
            raise ValueError("Nome inválido.")

    def get_populacao(self):
        return self._populacao

    def set_populacao(self, populacao):
        if populacao > 0:
            self._populacao = populacao
        else:
            raise ValueError("População deve ser maior que zero.")

    def get_area(self):
        return self._area

    def set_area(self, area):
        if area > 0:
            self._area = area
        else:
            raise ValueError("Área deve ser maior que zero.")

    # Método densidade
    def densidade(self):
        return self._populacao / self._area

    # Representação do objeto
    def __str__(self):
        return (f"\nPaís: {self._nome}\n"
                f"População: {self._populacao}\n"
                f"Área: {self._area} km²")


class PaisUI:

    @staticmethod
    def menu():
        print("\n1 - Calcular")
        print("2 - Fim")
        return int(input("Escolha uma opção: "))

    @staticmethod
    def calculo():
        nome = input("Digite o nome do país: ")
        populacao = int(input("Digite a população: "))
        area = float(input("Digite a área (km²): "))

        pais = Pais(nome, populacao, area)

        print("\nDados do país:")
        print(pais)

        print(f"Densidade demográfica: {pais.densidade():.2f} hab/km²")

    @staticmethod
    def main():
        while True:
            opcao = PaisUI.menu()

            if opcao == 1:
                PaisUI.calculo()
            elif opcao == 2:
                print("Encerrando programa...")
                break
            else:
                print("Opção inválida.")

PaisUI.main()