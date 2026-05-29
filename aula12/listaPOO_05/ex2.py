# ATIVIDADE DO BOLETO (USO DE VARIÁVEIS E FUNÇÃO Enum)
from enum import Enum
from datetime import datetime

class Pagamento(Enum):
    EM_ABERTO = 1
    PAGO_PARCIAL = 2
    PAGO = 3

class Boleto:
    def __init__(self, cod, emissao, venc, valor):
        self.set_cod_barras(cod)
        self.set_data_emissao(emissao)
        self.set_data_vencimento(venc)
        self.set_valor_boleto(valor)
        # atributos com valor inicial definido:
        self.__data_pagamento = None
        self.__valor_pago = 0
        self.__situacao_pagamento = Pagamento.EM_ABERTO

    def set_cod_barras(self, cod):
        # supondo que o boleto deve ter 10 digitos
        if len(cod) != 10: raise ValueError("Deve ter 10 digitos")
        self.__cod_barras = cod
    def set_data_emissoa(self, emissao):
        if emissao > datetime.now(): raise ValueError('A data não pode está no futuro')
        self.__data_emissao = emissao
    def set_data_vencimento(self, venc):
        if venc < datetime.now(): raise ValueError('A data precisa está no futuro')
        self.__data_vencimento = venc
    def set_valor_boleto(self, valor):
        if valor < 0: raise ValueError('Valor não pode ser negativo.')
        self.__valor_boleto = valor
    # NÃO FAZ SET PRAS VARIÁVEIS JÁ DEFINIDAS

    def pagar(self, valor_pago):
        if valor_pago < 0: raise ValueError('O valor pago não pode ser negativo')
        if self.__situacao_pagamento != Pagamento.EM_ABERTO: raise ValueError('Não pode pagar de novo um boleto já pago')
        self.__valor_pago = valor_pago
        self.__data_pagamento = datetime.now()
        if self.__valor_pago == self.__valor_boleto: self.__situacao_pagamento = Pagamento.PAGO
        else: self.__situacao_pagamento = Pagamento.PAGO_PARCIAL

    def get_cod_barra(self): return self.__cod_barras
    def get_data_emissao(self): return self.__data_emissao
    def get_data_vencimento(self): return self.__data_vencimento
    def get_data_pagamento(self): return self.__data_pagamento
    def get_valor_boleto(self): return self.__valor_boleto
    def get_valor_pago(self): return self.__valor_pago
    def get_situacao_pagamento(self): return self.__situacao_pagamento
    # no diagrama get_situacao_pagamento está como situacao
    def situacao(self): return self.__situacao_pagamento

    def __str__(self):
        s = f"Boleto: {self.__cod_barras} | Emissão: {self.__data_emissao.strftime('%d/%m/%Y')}"
        s += f"Vencimento: {self.__data_vencimento.strftime('%d/%m/%Y')}"
        s += f"Valor Boleto R${self.__valor_boleto:.2f}"
        s += f"Valor Pago R${self.__valor_pago:.2f}"
        s += f"Pagamento: {self.__data_pagamento}"
        s += f"{self.__situacao_pagamento}"
        return s