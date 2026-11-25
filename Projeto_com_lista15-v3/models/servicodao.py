from models.servico import Servico
from models.dao import DAO

class ServicoDAO(DAO):
    def __init__(self):
        super().__init__()
        self.execute("CREATE TABLE IF NOT EXISTS servico (id INTEGER PRIMARY KEY AUTOINCREMENT, descricao TEXT, valor REAL)")

    def inserir(self, obj):
        cursor = self.execute("INSERT INTO servico (descricao, valor) VALUES (?, ?)",
                              (obj.get_descricao(), obj.get_valor()))
        obj.set_id(cursor.lastrowid)

    def listar(self):
        cursor = self.execute("SELECT id, descricao, valor FROM servico")
        return [Servico(*linha) for linha in cursor.fetchall()]

    def listar_id(self, id):
        cursor = self.execute("SELECT id, descricao, valor FROM servico WHERE id = ?", (id,))
        linha = cursor.fetchone()
        if linha:
            return Servico(*linha)
        return None

    def atualizar(self, obj):
        self.execute("UPDATE servico SET descricao = ?, valor = ? WHERE id = ?",
                     (obj.get_descricao(), obj.get_valor(), obj.get_id()))

    def excluir(self, id):
        self.execute("DELETE FROM servico WHERE id = ?", (id,))
