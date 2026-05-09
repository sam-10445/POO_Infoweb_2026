class Playlist:
    def __init__(self, id, nome, descricao):
        self.set_id(id)
        self.set_nome(nome)
        self.set_descricao(descricao)

    #gets
    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_descricao(self): return self.__descricao

    #sets
    def set_id(self, id):
        if id <= 0: raise ValueError("O ID deve ser maior que zero.")
        self.__id = id

    def set_nome(self, nome):
        if nome == "": raise ValueError("O nome não pode ser vazio.")
        self.__nome = nome

    def set_descricao(self, descricao):
        if descricao == "": raise ValueError("A descrição não pode ser vazia.")
        self.__descricao = descricao

    #ToString
    def __str__(self):
        return f"ID: {self.__id} | Nome: {self.__nome} | Descrição: {self.__descricao}"

class Musica:
    def __init__(self, id, titulo, artista, album):
        self.set_id(id)
        self.set_titulo(titulo)
        self.set_artista(artista)
        self.set_album(album)

    #gets
    def get_id(self): return self.__id
    def get_titulo(self): return self.__titulo
    def get_artista(self): return self.__artista
    def get_album(self): return self.__album

    #sets
    def set_id(self, id):
        if id <= 0: raise ValueError("O ID deve ser maior que zero.")
        self.__id = id

    def set_titulo(self, titulo):
        if titulo == "": raise ValueError("O título não pode ser vazio.")
        self.__titulo = titulo

    def set_artista(self, artista):
        if artista == "":
            raise ValueError("O artista não pode ser vazio.")

        self.__artista = artista

    def set_album(self, album):
        if album == "": raise ValueError("O álbum não pode ser vazio.")
        self.__album = album

    #ToString
    def __str__(self):
        return f"ID: {self.__id} | Título: {self.__titulo} | Artista: {self.__artista} | Álbum: {self.__album}"

class PlaylistItem:
    def __init__(self, id, id_playlist, id_musica, sequencia):
        self.set_id(id)
        self.set_id_playlist(id_playlist)
        self.set_id_musica(id_musica)
        self.set_sequencia(sequencia)

    #gets
    def get_id(self): return self.__id
    def get_id_playlist(self): return self.__id_playlist
    def get_id_musica(self): return self.__id_musica
    def get_sequencia(self): return self.__sequencia

    #sets
    def set_id(self, id):
        if id <= 0: raise ValueError("O ID deve ser maior que zero.")
        self.__id = id

    def set_id_playlist(self, id_playlist):
        if id_playlist <= 0: raise ValueError("O ID da playlist deve ser maior que zero.")
        self.__id_playlist = id_playlist

    def set_id_musica(self, id_musica):
        if id_musica <= 0: raise ValueError("O ID da música deve ser maior que zero.")
        self.__id_musica = id_musica

    def set_sequencia(self, sequencia):
        if sequencia <= 0: raise ValueError("A sequência deve ser maior que zero.")
        self.__sequencia = sequencia

    #ToString
    def __str__(self):
        return f"ID: {self.__id} | Playlist: {self.__id_playlist} | Música: {self.__id_musica} | Sequência: {self.__sequencia}"

#INTERFACE COM O USUÁRIO
class UI:
    #criar as listas
    playlists = []
    musicas = []
    itens = []

    def inserir_playlist(self):
        id = int(input("ID da playlist: "))
        nome = input("Nome da playlist: ")
        descricao = input("Descrição: ")

        playlist = Playlist(id, nome, descricao)
        self.playlists.append(playlist)

        print("Playlist cadastrada!\n")

    def listar_playlists(self):
        if len(self.playlists) == 0:
            print("Nenhuma playlist cadastrada.\n")
        else:
            for playlist in self.playlists:
                print(playlist)

    def inserir_musica(self):
        id = int(input("ID da música: "))
        titulo = input("Título: ")
        artista = input("Artista: ")
        album = input("Álbum: ")

        musica = Musica(id, titulo, artista, album)
        self.musicas.append(musica)

        print("Música cadastrada!\n")


    def listar_musicas(self):
        if len(self.musicas) == 0:
            print("Nenhuma música cadastrada.\n")
        else:
            for musica in self.musicas:
                print(musica)
            print()

    def inserir_item(self):
        id = int(input("ID do item: "))
        id_playlist = int(input("ID da playlist: "))
        id_musica = int(input("ID da música: "))
        sequencia = int(input("Sequência da música: "))

        item = PlaylistItem(id, id_playlist, id_musica, sequencia)
        self.itens.append(item)

        print("Item cadastrado!\n")

    def listar_itens(self):
        if len(self.itens) == 0:
            print("Nenhum item cadastrado.\n")
        else:
            for item in self.itens:
                print(item)

    #menu
    def main(self):
        opcao = 100000

        while opcao != 0:
            print("1 - Inserir playlist")
            print("2 - Listar playlists")
            print("3 - Inserir música")
            print("4 - Listar músicas")
            print("5 - Inserir item da playlist")
            print("6 - Listar itens")
            print("0 - Sair")
            opcao = int(input("Informe uma opção: "))

            if opcao == 1: self.inserir_playlist()
            if opcao == 2: self.listar_playlists()
            if opcao == 3: self.inserir_musica()
            if opcao == 4: self.listar_musicas()
            if opcao == 5: self.inserir_item()
            if opcao == 6: self.listar_itens()
            if opcao == 0: print("Tchau! :P")

ui = UI()
ui.main()