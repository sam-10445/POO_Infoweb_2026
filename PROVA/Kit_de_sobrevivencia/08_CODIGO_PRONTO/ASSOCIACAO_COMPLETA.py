# ============================================================
# ASSOCIAÇÃO COMPLETA
# ============================================================
#
# EXEMPLO:
#
# Horario possui id_cliente
# Horario possui id_servico
# Horario possui id_profissional
#
# ============================================================


# ============================================================
# 1. ATRIBUTO NO CONSTRUTOR
# ============================================================

self.set_id_profissional(0)


# ============================================================
# 2. GETTER
# ============================================================

def get_id_profissional(self):

    return self.__id_profissional


# ============================================================
# 3. SETTER
# ============================================================

def set_id_profissional(self, id_profissional):

    self.__id_profissional = id_profissional


# ============================================================
# 4. TO_JSON
# ============================================================

def to_json(self):

    dic = {
        "id": self.__id,
        "data": self.__data.strftime(
            "%d/%m/%Y %H:%M"
        ),
        "confirmado": self.__confirmado,
        "id_cliente": self.__id_cliente,
        "id_servico": self.__id_servico,
        "id_profissional": self.__id_profissional
    }

    return dic


# ============================================================
# 5. FROM_JSON
# ============================================================

@staticmethod
def from_json(dic):

    horario = Horario(
        dic["id"],
        datetime.strptime(
            dic["data"],
            "%d/%m/%Y %H:%M"
        )
    )

    horario.set_confirmado(
        dic["confirmado"]
    )

    horario.set_id_cliente(
        dic["id_cliente"]
    )

    horario.set_id_servico(
        dic["id_servico"]
    )

    horario.set_id_profissional(
        dic["id_profissional"]
    )

    return horario


# ============================================================
# 6. SERVICE — INSERIR
# ============================================================

@staticmethod
def horario_inserir(
    data,
    confirmado,
    id_cliente,
    id_servico,
    id_profissional
):

    c = Horario(0, data)

    c.set_confirmado(confirmado)
    c.set_id_cliente(id_cliente)
    c.set_id_servico(id_servico)
    c.set_id_profissional(id_profissional)

    HorarioDAO().inserir(c)


# ============================================================
# 7. SERVICE — ATUALIZAR
# ============================================================

@staticmethod
def horario_atualizar(
    id,
    data,
    confirmado,
    id_cliente,
    id_servico,
    id_profissional
):

    c = Horario(id, data)

    c.set_confirmado(confirmado)
    c.set_id_cliente(id_cliente)
    c.set_id_servico(id_servico)
    c.set_id_profissional(id_profissional)

    HorarioDAO().atualizar(c)


# ============================================================
# 8. UI — BUSCAR PROFISSIONAIS
# ============================================================

profissionais = Service.profissional_listar()


# ============================================================
# 9. UI — SELECTBOX
# ============================================================

profissional = st.selectbox(
    "Informe o profissional",
    profissionais,
    index=None
)


# ============================================================
# 10. UI — PEGAR ID
# ============================================================

id_profissional = None

if profissional != None:

    id_profissional = profissional.get_id()


# ============================================================
# 11. UI — MOSTRAR NOME NA LISTAGEM
# ============================================================

profissional = Service.profissional_listar_id(
    obj.get_id_profissional()
)

if profissional != None:

    profissional = profissional.get_nome()


# ============================================================
# 12. ADICIONAR AO DICIONÁRIO DA TABELA
# ============================================================

dic.append({
    "id": obj.get_id(),
    "data": obj.get_data(),
    "confirmado": obj.get_confirmado(),
    "cliente": cliente,
    "serviço": servico,
    "profissional": profissional
})