from models.atendimento import Atendimento
from models.dao import DAO
from datetime import datetime

class AtendimentoDAO(DAO):
    def __init__(self):
        super().__init__()
        self.execute("CREATE TABLE IF NOT EXISTS atendimento (id INTEGER PRIMARY KEY AUTOINCREMENT, data TEXT, queixa_principal TEXT, historico_saude TEXT, avaliacao TEXT, prescricao TEXT, id_horario INTEGER)")

    def inserir(self, obj):
        cursor = self.execute("INSERT INTO atendimento (data, queixa_principal, historico_saude, avaliacao, prescricao, id_horario) VALUES (?, ?, ?, ?, ?, ?)",
                              (obj.get_data().strftime("%d/%m/%Y %H:%M"), obj.get_queixa_principal(),
                               obj.get_historico_saude(), obj.get_avaliacao(), obj.get_prescricao(), obj.get_id_horario()))
        obj.set_id(cursor.lastrowid)

    def listar(self):
        cursor = self.execute("SELECT id, data, queixa_principal, historico_saude, avaliacao, prescricao, id_horario FROM atendimento")
        objetos = []
        for linha in cursor.fetchall():
            objetos.append(Atendimento(linha[0], datetime.strptime(linha[1], "%d/%m/%Y %H:%M"),
                                       linha[2], linha[3], linha[4], linha[5], linha[6]))
        return objetos

    def listar_id(self, id):
        cursor = self.execute("SELECT id, data, queixa_principal, historico_saude, avaliacao, prescricao, id_horario FROM atendimento WHERE id = ?", (id,))
        linha = cursor.fetchone()
        if linha:
            return Atendimento(linha[0], datetime.strptime(linha[1], "%d/%m/%Y %H:%M"),
                               linha[2], linha[3], linha[4], linha[5], linha[6])
        return None

    def atualizar(self, obj):
        self.execute("UPDATE atendimento SET data = ?, queixa_principal = ?, historico_saude = ?, avaliacao = ?, prescricao = ?, id_horario = ? WHERE id = ?",
                     (obj.get_data().strftime("%d/%m/%Y %H:%M"), obj.get_queixa_principal(),
                      obj.get_historico_saude(), obj.get_avaliacao(), obj.get_prescricao(),
                      obj.get_id_horario(), obj.get_id()))

    def excluir(self, id):
        self.execute("DELETE FROM atendimento WHERE id = ?", (id,))
