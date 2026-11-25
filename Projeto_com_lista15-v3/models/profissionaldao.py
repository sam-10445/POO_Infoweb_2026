from models.profissional import Profissional
from models.dao import DAO

class ProfissionalDAO(DAO):
    def __init__(self):
        super().__init__()
        self.execute("CREATE TABLE IF NOT EXISTS profissional (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, email TEXT, especialidade TEXT, senha TEXT)")

    def inserir(self, obj):
        cursor = self.execute("INSERT INTO profissional (nome, email, especialidade, senha) VALUES (?, ?, ?, ?)",
                              (obj.get_nome(), obj.get_email(), obj.get_especialidade(), obj.get_senha()))
        obj.set_id(cursor.lastrowid)

    def listar(self):
        cursor = self.execute("SELECT id, nome, email, especialidade, senha FROM profissional")
        return [Profissional(*linha) for linha in cursor.fetchall()]

    def listar_id(self, id):
        cursor = self.execute("SELECT id, nome, email, especialidade, senha FROM profissional WHERE id = ?", (id,))
        linha = cursor.fetchone()
        if linha:
            return Profissional(*linha)
        return None

    def atualizar(self, obj):
        self.execute("UPDATE profissional SET nome = ?, email = ?, especialidade = ?, senha = ? WHERE id = ?",
                     (obj.get_nome(), obj.get_email(), obj.get_especialidade(), obj.get_senha(), obj.get_id()))

    def excluir(self, id):
        self.execute("DELETE FROM profissional WHERE id = ?", (id,))
