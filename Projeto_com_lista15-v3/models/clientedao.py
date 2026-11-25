from models.cliente import Cliente
from models.dao import DAO

class ClienteDAO(DAO):
    def __init__(self):
        super().__init__()
        self.execute("CREATE TABLE IF NOT EXISTS cliente (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, email TEXT, fone TEXT, senha TEXT)")

    def inserir(self, obj):
        cursor = self.execute("INSERT INTO cliente (nome, email, fone, senha) VALUES (?, ?, ?, ?)",
                              (obj.get_nome(), obj.get_email(), obj.get_fone(), obj.get_senha()))
        obj.set_id(cursor.lastrowid)

    def listar(self):
        cursor = self.execute("SELECT id, nome, email, fone, senha FROM cliente")
        return [Cliente(*linha) for linha in cursor.fetchall()]

    def listar_id(self, id):
        cursor = self.execute("SELECT id, nome, email, fone, senha FROM cliente WHERE id = ?", (id,))
        linha = cursor.fetchone()
        if linha:
            return Cliente(*linha)
        return None

    def atualizar(self, obj):
        self.execute("UPDATE cliente SET nome = ?, email = ?, fone = ?, senha = ? WHERE id = ?",
                     (obj.get_nome(), obj.get_email(), obj.get_fone(), obj.get_senha(), obj.get_id()))

    def excluir(self, id):
        self.execute("DELETE FROM cliente WHERE id = ?", (id,))
