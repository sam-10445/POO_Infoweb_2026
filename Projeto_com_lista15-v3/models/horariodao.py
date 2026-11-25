from models.horario import Horario
from models.dao import DAO
from datetime import datetime

class HorarioDAO(DAO):
    def __init__(self):
        super().__init__()
        self.execute("CREATE TABLE IF NOT EXISTS horario (id INTEGER PRIMARY KEY AUTOINCREMENT, data TEXT, confirmado INTEGER, id_cliente INTEGER, id_servico INTEGER, id_profissional INTEGER)")

    def inserir(self, obj):
        cursor = self.execute("INSERT INTO horario (data, confirmado, id_cliente, id_servico, id_profissional) VALUES (?, ?, ?, ?, ?)",
                              (obj.get_data().strftime("%d/%m/%Y %H:%M"), int(obj.get_confirmado()),
                               obj.get_id_cliente(), obj.get_id_servico(), obj.get_id_profissional()))
        obj.set_id(cursor.lastrowid)

    def listar(self):
        cursor = self.execute("SELECT id, data, confirmado, id_cliente, id_servico, id_profissional FROM horario")
        objetos = []
        for linha in cursor.fetchall():
            obj = Horario(linha[0], datetime.strptime(linha[1], "%d/%m/%Y %H:%M"))
            obj.set_confirmado(bool(linha[2]))
            obj.set_id_cliente(linha[3])
            obj.set_id_servico(linha[4])
            obj.set_id_profissional(linha[5])
            objetos.append(obj)
        return objetos

    def listar_id(self, id):
        cursor = self.execute("SELECT id, data, confirmado, id_cliente, id_servico, id_profissional FROM horario WHERE id = ?", (id,))
        linha = cursor.fetchone()
        if linha:
            obj = Horario(linha[0], datetime.strptime(linha[1], "%d/%m/%Y %H:%M"))
            obj.set_confirmado(bool(linha[2]))
            obj.set_id_cliente(linha[3])
            obj.set_id_servico(linha[4])
            obj.set_id_profissional(linha[5])
            return obj
        return None

    def atualizar(self, obj):
        self.execute("UPDATE horario SET data = ?, confirmado = ?, id_cliente = ?, id_servico = ?, id_profissional = ? WHERE id = ?",
                     (obj.get_data().strftime("%d/%m/%Y %H:%M"), int(obj.get_confirmado()),
                      obj.get_id_cliente(), obj.get_id_servico(), obj.get_id_profissional(), obj.get_id()))

    def excluir(self, id):
        self.execute("DELETE FROM horario WHERE id = ?", (id,))
