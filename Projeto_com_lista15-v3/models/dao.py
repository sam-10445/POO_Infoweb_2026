from abc import ABC, abstractmethod
import sqlite3

class DAO(ABC):
    def __init__(self):
        self.nome_bd = "agendamento.db"
        self.conn = None
        self.abrir()

    def abrir(self):
        self.conn = sqlite3.connect(self.nome_bd)

    def fechar(self):
        if self.conn:
            self.conn.close()
            self.conn = None

    def execute(self, sql, parametros=()):
        cursor = self.conn.cursor()
        cursor.execute(sql, parametros)
        self.conn.commit()
        return cursor

    @abstractmethod
    def inserir(self, obj):
        pass

    @abstractmethod
    def listar(self):
        pass

    @abstractmethod
    def listar_id(self, id):
        pass

    @abstractmethod
    def atualizar(self, obj):
        pass

    @abstractmethod
    def excluir(self, id):
        pass
