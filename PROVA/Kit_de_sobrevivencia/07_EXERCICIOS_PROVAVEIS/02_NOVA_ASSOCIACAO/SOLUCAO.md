# SOLUÇÃO — NOVA ASSOCIAÇÃO

# 1. horario.py

## No __init__:

self.set_id_profissional(0)

## Getter:

def get_id_profissional(self):
    return self.__id_profissional

## Setter:

def set_id_profissional(self, id_profissional):
    self.__id_profissional = id_profissional

## No to_json():

"id_profissional": self.__id_profissional

## No from_json():

horario.set_id_profissional(dic["id_profissional"])

# 2. Service

## Alterar inserir:

@staticmethod
def horario_inserir(data, confirmado, id_cliente, id_servico, id_profissional:
    c = Horario(0, data)

    c.set_confirmado(confirmado)
    c.set_id_cliente(id_cliente)
    c.set_id_servico(id_servico)
    c.set_id_profissional(id_profissional)

    HorarioDAO().inserir(c)

## Alterar atualizar:

@staticmethod
def horario_atualizar(id, data, confirmado, id_cliente, id_servico, id_profissional):

    c = Horario(id, data)

    c.set_confirmado(confirmado)
    c.set_id_cliente(id_cliente)
    c.set_id_servico(id_servico)
    c.set_id_profissional(id_profissional)

    HorarioDAO().atualizar(c)
# 3. UI

## Buscar profissionais:

profissionais = Service.profissional_listar()

## Selectbox:

profissional = st.selectbox(
    "Informe o profissional",
    profissionais,
    index=None
)

## Pegar ID:

id_profissional = None

if profissional != None:
    id_profissional = profissional.get_id()

## Enviar:

Service.horario_inserir(
    datetime.strptime(data, "%d/%m/%Y %H:%M"),
    confirmado,
    id_cliente,
    id_servico,
    id_profissional
)
# 4. Listagem

## Buscar:

profissional = Service.profissional_listar_id(
    obj.get_id_profissional()
)

## Transformar em nome:

if profissional != None:
    profissional = profissional.get_nome()

## Adicionar ao dicionário:

"profissional": profissional