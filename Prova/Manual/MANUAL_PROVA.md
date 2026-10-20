# KIT DE SOBREVIVÊNCIA — PROVA DE POO
## Versão prática para o projeto de Agendamento

> Este material foi montado a partir do código do repositório enviado e da Tarefa 11.
> A ideia NÃO é explicar a arquitetura do projeto. É fornecer modelos para copiar, colar e adaptar durante o estudo/prova.

---

# 1. TABELA: O QUE O ENUNCIADO ESTÁ PEDINDO?

| Se o enunciado disser... | Normalmente alterar/criar |
|---|---|
| "crie uma nova entidade/classe" | `models/novaentidade.py` + `models/novaentidadedao.py` + `service.py` + UI |
| "cadastre..." | Model + DAO + Service + UI de inserir |
| "liste..." | Service + UI de listar |
| "consulte pelo id" | `listar_id()` no DAO + método no Service |
| "atualize..." | Model + DAO já existente + Service + UI |
| "exclua..." | DAO + Service + UI |
| "relacione X com Y" | novo `id_x`/`id_y` + busca `Service.x_listar_id(...)` |
| "mostre o nome em vez do id" | UI: buscar objeto relacionado pelo ID |
| "filtre por..." | Service com lista `r = []` + `if` |
| "ordene por..." | Service com `r.sort(key = lambda...)` |
| "filtre e ordene" | primeiro `if`, depois `sort` |
| "somente os do usuário logado" | filtro usando `st.session_state["usuario_id"]` |
| "somente os do profissional logado" | filtro usando `st.session_state["usuario_id"]` |
| "somente disponíveis" | filtro por data + situação + IDs |
| "registre atendimento" | provável nova classe `Atendimento` + DAO + Service + UI |
| "registre pagamento" | provável nova classe `Pagamento` + DAO + Service + UI |
| "serviços realizados no atendimento" | provável relação `AtendimentoServico` ou lista/IDs de serviços |
| "totalizar valor" | buscar serviços e somar `get_valor()` |
| "visualizar atendimentos" | Service de filtragem + UI |
| "buscar por nome/descrição" | filtro com `.casefold()` |
| "entre duas datas" | filtro comparando `get_data()` com duas datas |
| "maior/menor valor" | `sort(key = lambda obj : obj.get_valor())` |
| "mais recente/mais antigo" | ordenar por data |
| "confirmados/não confirmados" | filtro por `get_confirmado()` |

---

# 2. MODELO PRONTO — CLASSE SEM ID DE OUTRA CLASSE

Use quando a nova classe NÃO guardar o ID de outra entidade.

## `models/novaentidade.py`

```python
class NovaEntidade:
    def __init__(self, id, campo1, campo2, campo3):
        self.set_id(id)
        self.set_campo1(campo1)
        self.set_campo2(campo2)
        self.set_campo3(campo3)

    def set_id(self, id):
        if id < 0: raise ValueError("Id deve ser positivo")
        self.__id = id

    def set_campo1(self, campo1):
        if campo1 == "": raise ValueError("Campo1 deve ser informado")
        self.__campo1 = campo1

    def set_campo2(self, campo2):
        self.__campo2 = campo2

    def set_campo3(self, campo3):
        self.__campo3 = campo3

    def get_id(self): return self.__id
    def get_campo1(self): return self.__campo1
    def get_campo2(self): return self.__campo2
    def get_campo3(self): return self.__campo3

    def __str__(self):
        return f"{self.__id} - {self.__campo1} - {self.__campo2} - {self.__campo3}"

    def to_json(self):
        return {
            "id": self.__id,
            "campo1": self.__campo1,
            "campo2": self.__campo2,
            "campo3": self.__campo3
        }

    def to_dict(self):
        return {
            "id": self.__id,
            "campo1": self.__campo1,
            "campo2": self.__campo2,
            "campo3": self.__campo3
        }

    @staticmethod
    def from_json(dic):
        return NovaEntidade(
            dic["id"],
            dic["campo1"],
            dic["campo2"],
            dic["campo3"]
        )
```

## `models/novaentidadedao.py`

```python
from models.novaentidade import NovaEntidade
import json

class NovaEntidadeDAO:
    def __init__(self):
        self.__arquivo = "novaentidade.json"
        self.__objetos = []
        self.__abrir()

    def inserir(self, obj):
        id = 0
        if len(self.__objetos) > 0:
            for aux in self.__objetos:
                if aux.get_id() > id: id = aux.get_id()
        obj.set_id(id + 1)
        self.__objetos.append(obj)
        self.__salvar()

    def listar(self):
        return self.__objetos

    def listar_id(self, id):
        for obj in self.__objetos:
            if obj.get_id() == id: return obj
        return None

    def atualizar(self, obj):
        aux = self.listar_id(obj.get_id())
        if aux != None:
            self.__objetos.remove(aux)
            self.__objetos.append(obj)
            self.__salvar()

    def excluir(self, id):
        aux = self.listar_id(id)
        if aux != None:
            self.__objetos.remove(aux)
            self.__salvar()

    def __abrir(self):
        try:
            arquivo = open(self.__arquivo, mode = "r")
            list_dic = json.load(arquivo)
            arquivo.close()
            self.__objetos = []
            for dic in list_dic:
                obj = NovaEntidade.from_json(dic)
                self.__objetos.append(obj)
        except FileNotFoundError:
            pass

    def __salvar(self):
        arquivo = open(self.__arquivo, mode = "w")
        json.dump(
            self.__objetos,
            arquivo,
            default = NovaEntidade.to_json,
            indent = 2
        )
        arquivo.close()
```

## `service.py` — bloco para acrescentar

```python
from models.novaentidade import NovaEntidade
from models.novaentidadedao import NovaEntidadeDAO

class Service:
    # ...

    @staticmethod
    def novaentidade_inserir(campo1, campo2, campo3):
        obj = NovaEntidade(0, campo1, campo2, campo3)
        NovaEntidadeDAO().inserir(obj)

    @staticmethod
    def novaentidade_listar():
        r = NovaEntidadeDAO().listar()
        r.sort(key = lambda obj : obj.get_campo1().casefold())
        return r

    @staticmethod
    def novaentidade_listar_id(id):
        return NovaEntidadeDAO().listar_id(id)

    @staticmethod
    def novaentidade_atualizar(id, campo1, campo2, campo3):
        obj = NovaEntidade(id, campo1, campo2, campo3)
        NovaEntidadeDAO().atualizar(obj)

    @staticmethod
    def novaentidade_excluir(id):
        NovaEntidadeDAO().excluir(id)
```

---

# 3. MODELO PRONTO — CLASSE QUE GUARDA ID DE OUTRA CLASSE

Use quando o enunciado disser algo como:

- "um atendimento pertence a um horário";
- "um pagamento pertence a um atendimento";
- "X está associado a Y".

## `models/novaentidade.py`

```python
class NovaEntidade:
    def __init__(self, id, campo1, id_outra):
        self.set_id(id)
        self.set_campo1(campo1)
        self.set_id_outra(id_outra)

    def set_id(self, id):
        if id < 0: raise ValueError("Id deve ser positivo")
        self.__id = id

    def set_campo1(self, campo1):
        if campo1 == "": raise ValueError("Campo deve ser informado")
        self.__campo1 = campo1

    def set_id_outra(self, id_outra):
        self.__id_outra = id_outra

    def get_id(self): return self.__id
    def get_campo1(self): return self.__campo1
    def get_id_outra(self): return self.__id_outra

    def __str__(self):
        return f"{self.__id} - {self.__campo1}"

    def to_json(self):
        return {
            "id": self.__id,
            "campo1": self.__campo1,
            "id_outra": self.__id_outra
        }

    @staticmethod
    def from_json(dic):
        obj = NovaEntidade(
            dic["id"],
            dic["campo1"],
            dic["id_outra"]
        )
        return obj
```

## DAO

```python
from models.novaentidade import NovaEntidade
import json

class NovaEntidadeDAO:
    def __init__(self):
        self.__arquivo = "novaentidade.json"
        self.__objetos = []
        self.__abrir()

    def inserir(self, obj):
        id = 0
        if len(self.__objetos) > 0:
            for aux in self.__objetos:
                if aux.get_id() > id: id = aux.get_id()
        obj.set_id(id + 1)
        self.__objetos.append(obj)
        self.__salvar()

    def listar(self):
        return self.__objetos

    def listar_id(self, id):
        for obj in self.__objetos:
            if obj.get_id() == id: return obj
        return None

    def atualizar(self, obj):
        aux = self.listar_id(obj.get_id())
        if aux != None:
            self.__objetos.remove(aux)
            self.__objetos.append(obj)
            self.__salvar()

    def excluir(self, id):
        aux = self.listar_id(id)
        if aux != None:
            self.__objetos.remove(aux)
            self.__salvar()

    def __abrir(self):
        try:
            arquivo = open(self.__arquivo, mode = "r")
            list_dic = json.load(arquivo)
            arquivo.close()
            self.__objetos = []
            for dic in list_dic:
                obj = NovaEntidade.from_json(dic)
                self.__objetos.append(obj)
        except FileNotFoundError:
            pass

    def __salvar(self):
        arquivo = open(self.__arquivo, mode = "w")
        json.dump(
            self.__objetos,
            arquivo,
            default = NovaEntidade.to_json,
            indent = 2
        )
        arquivo.close()
```

## Service

```python
from models.novaentidade import NovaEntidade
from models.novaentidadedao import NovaEntidadeDAO

class Service:

    @staticmethod
    def novaentidade_inserir(campo1, id_outra):
        obj = NovaEntidade(0, campo1, id_outra)
        NovaEntidadeDAO().inserir(obj)

    @staticmethod
    def novaentidade_listar():
        r = NovaEntidadeDAO().listar()
        r.sort(key = lambda obj : obj.get_campo1().casefold())
        return r

    @staticmethod
    def novaentidade_listar_id(id):
        return NovaEntidadeDAO().listar_id(id)

    @staticmethod
    def novaentidade_atualizar(id, campo1, id_outra):
        obj = NovaEntidade(id, campo1, id_outra)
        NovaEntidadeDAO().atualizar(obj)

    @staticmethod
    def novaentidade_excluir(id):
        NovaEntidadeDAO().excluir(id)
```

---

# 4. UI PRONTA — CRUD DE UMA NOVA CLASSE

Troque os nomes e campos.

## `templates/manternovaentidadeui.py`

```python
import streamlit as st
import pandas as pd
import time
from service import Service

class ManterNovaEntidadeUI:
    def main():
        st.header("Cadastro de Nova Entidade")
        tab1, tab2, tab3, tab4 = st.tabs(
            ["Listar", "Inserir", "Atualizar", "Excluir"]
        )

        with tab1: ManterNovaEntidadeUI.listar()
        with tab2: ManterNovaEntidadeUI.inserir()
        with tab3: ManterNovaEntidadeUI.atualizar()
        with tab4: ManterNovaEntidadeUI.excluir()

    def listar():
        objetos = Service.novaentidade_listar()

        if len(objetos) == 0:
            st.write("Nenhum registro cadastrado")
        else:
            list_dic = []

            for obj in objetos:
                list_dic.append(obj.to_dict())

            df = pd.DataFrame(list_dic)
            st.dataframe(df)

    def inserir():
        campo1 = st.text_input("Informe o campo 1")
        campo2 = st.text_input("Informe o campo 2")
        campo3 = st.text_input("Informe o campo 3")

        if st.button("Inserir"):
            Service.novaentidade_inserir(
                campo1,
                campo2,
                campo3
            )
            st.success("Registro inserido com sucesso")
            time.sleep(2)
            st.rerun()

    def atualizar():
        objetos = Service.novaentidade_listar()

        if len(objetos) == 0:
            st.write("Nenhum registro cadastrado")
        else:
            op = st.selectbox(
                "Atualização",
                objetos
            )

            campo1 = st.text_input(
                "Informe o novo campo 1",
                op.get_campo1()
            )

            campo2 = st.text_input(
                "Informe o novo campo 2",
                op.get_campo2()
            )

            campo3 = st.text_input(
                "Informe o novo campo 3",
                op.get_campo3()
            )

            if st.button("Atualizar"):
                Service.novaentidade_atualizar(
                    op.get_id(),
                    campo1,
                    campo2,
                    campo3
                )

                st.success("Registro atualizado com sucesso")
                time.sleep(2)
                st.rerun()

    def excluir():
        objetos = Service.novaentidade_listar()

        if len(objetos) == 0:
            st.write("Nenhum registro cadastrado")
        else:
            op = st.selectbox(
                "Exclusão",
                objetos
            )

            if st.button("Excluir"):
                Service.novaentidade_excluir(op.get_id())
                st.success("Registro excluído com sucesso")
                time.sleep(2)
                st.rerun()
```

---

# 5. UI PRONTA — CLASSE COM ID DE OUTRA CLASSE

Esse é o modelo mais importante para novas funcionalidades do sistema.

```python
import streamlit as st
import pandas as pd
import time
from service import Service

class ManterNovaEntidadeUI:
    def main():
        st.header("Cadastro de Nova Entidade")
        tab1, tab2, tab3, tab4 = st.tabs(
            ["Listar", "Inserir", "Atualizar", "Excluir"]
        )

        with tab1: ManterNovaEntidadeUI.listar()
        with tab2: ManterNovaEntidadeUI.inserir()
        with tab3: ManterNovaEntidadeUI.atualizar()
        with tab4: ManterNovaEntidadeUI.excluir()

    def listar():
        objetos = Service.novaentidade_listar()

        if len(objetos) == 0:
            st.write("Nenhum registro cadastrado")
        else:
            dic = []

            for obj in objetos:
                outra = Service.outra_listar_id(
                    obj.get_id_outra()
                )

                if outra != None:
                    outra = outra.get_nome()

                dic.append({
                    "id": obj.get_id(),
                    "campo1": obj.get_campo1(),
                    "outra": outra
                })

            df = pd.DataFrame(dic)
            st.dataframe(df)

    def inserir():
        objetos = Service.outra_listar()

        campo1 = st.text_input("Informe o campo 1")
        outra = st.selectbox(
            "Informe a outra entidade",
            objetos,
            index = None
        )

        if st.button("Inserir"):
            id_outra = None

            if outra != None:
                id_outra = outra.get_id()

            Service.novaentidade_inserir(
                campo1,
                id_outra
            )

            st.success("Registro inserido com sucesso")
            time.sleep(2)
            st.rerun()

    def atualizar():
        objetos = Service.novaentidade_listar()

        if len(objetos) == 0:
            st.write("Nenhum registro cadastrado")
        else:
            outras = Service.outra_listar()
            op = st.selectbox("Atualização", objetos)

            campo1 = st.text_input(
                "Informe o novo campo 1",
                op.get_campo1()
            )

            id_outra = None if op.get_id_outra() in [0, None] else op.get_id_outra()

            outra = st.selectbox(
                "Informe a nova associação",
                outras,
                next(
                    (
                        i for i, x in enumerate(outras)
                        if x.get_id() == id_outra
                    ),
                    None
                )
            )

            if st.button("Atualizar"):
                id_outra = None

                if outra != None:
                    id_outra = outra.get_id()

                Service.novaentidade_atualizar(
                    op.get_id(),
                    campo1,
                    id_outra
                )

                st.success("Registro atualizado com sucesso")
                time.sleep(2)
                st.rerun()

    def excluir():
        objetos = Service.novaentidade_listar()

        if len(objetos) == 0:
            st.write("Nenhum registro cadastrado")
        else:
            op = st.selectbox("Exclusão", objetos)

            if st.button("Excluir"):
                Service.novaentidade_excluir(op.get_id())
                st.success("Registro excluído com sucesso")
                time.sleep(2)
                st.rerun()
```

---

# 6. FILTRAGEM — CASOS PRONTOS

## Caso 1 — somente clientes com determinado nome

Serve para procurar clientes pelo nome.

```python
@staticmethod
def cliente_listar_nome(nome):
    r = []

    for c in Service.cliente_listar():
        if nome.casefold() in c.get_nome().casefold():
            r.append(c)

    return r
```

---

## Caso 2 — somente serviços com determinada descrição

```python
@staticmethod
def servico_listar_descricao(descricao):
    r = []

    for s in Service.servico_listar():
        if descricao.casefold() in s.get_descricao().casefold():
            r.append(s)

    return r
```

---

## Caso 3 — somente horários de um profissional

Já usado no projeto:

```python
@staticmethod
def horario_listar_profissional(id_profissional):
    r = []

    for h in Service.horario_listar():
        if h.get_id_profissional() == id_profissional:
            r.append(h)

    r.sort(key = lambda h : h.get_data())

    return r
```

---

## Caso 4 — somente horários de um cliente

```python
@staticmethod
def horario_listar_cliente(id_cliente):
    r = []

    for h in Service.horario_listar():
        if h.get_id_cliente() == id_cliente:
            r.append(h)

    r.sort(key = lambda h : h.get_data())

    return r
```

---

## Caso 5 — somente horários disponíveis

```python
@staticmethod
def horario_listar_disponiveis(id_profissional):
    r = []

    agora = datetime.now(
        ZoneInfo("America/Sao_Paulo")
    ).replace(tzinfo=None)

    for h in Service.horario_listar():
        if h.get_data() >= agora \
        and h.get_confirmado() == False \
        and h.get_id_cliente() in [None, 0] \
        and h.get_id_profissional() == id_profissional:
            r.append(h)

    r.sort(key = lambda h : h.get_data())

    return r
```

---

## Caso 6 — somente horários confirmados

```python
@staticmethod
def horario_listar_confirmados():
    r = []

    for h in Service.horario_listar():
        if h.get_confirmado() == True:
            r.append(h)

    r.sort(key = lambda h : h.get_data())

    return r
```

---

## Caso 7 — somente horários NÃO confirmados

```python
@staticmethod
def horario_listar_nao_confirmados():
    r = []

    for h in Service.horario_listar():
        if h.get_confirmado() == False:
            r.append(h)

    r.sort(key = lambda h : h.get_data())

    return r
```

---

## Caso 8 — horários agendados de um profissional

```python
@staticmethod
def horario_listar_agendados(id_profissional):
    r = []

    for h in Service.horario_listar():
        if h.get_id_profissional() == id_profissional \
        and h.get_id_cliente() not in [None, 0] \
        and h.get_confirmado() == False:
            r.append(h)

    r.sort(key = lambda h : h.get_data())

    return r
```

---

## Caso 9 — clientes cujo e-mail contém texto

```python
@staticmethod
def cliente_listar_email(email):
    r = []

    for c in Service.cliente_listar():
        if email.casefold() in c.get_email().casefold():
            r.append(c)

    return r
```

---

## Caso 10 — serviços acima de determinado valor

```python
@staticmethod
def servico_listar_valor_maior(valor):
    r = []

    for s in Service.servico_listar():
        if s.get_valor() > valor:
            r.append(s)

    return r
```

---

## Caso 11 — serviços abaixo de determinado valor

```python
@staticmethod
def servico_listar_valor_menor(valor):
    r = []

    for s in Service.servico_listar():
        if s.get_valor() < valor:
            r.append(s)

    return r
```

---

## Caso 12 — profissionais de determinada especialidade

```python
@staticmethod
def profissional_listar_especialidade(especialidade):
    r = []

    for p in Service.profissional_listar():
        if especialidade.casefold() in p.get_especialidade().casefold():
            r.append(p)

    return r
```

---

## Caso 13 — combinar dois filtros

Exemplo: serviços acima de R$ 100 que tenham determinada palavra.

```python
@staticmethod
def servico_filtrar(descricao, valor):
    r = []

    for s in Service.servico_listar():
        if descricao.casefold() in s.get_descricao().casefold() \
        and s.get_valor() > valor:
            r.append(s)

    return r
```

---

## Caso 14 — filtrar pelo usuário logado

```python
@staticmethod
def horario_listar_usuario_logado(id_cliente):
    r = []

    for h in Service.horario_listar():
        if h.get_id_cliente() == id_cliente:
            r.append(h)

    r.sort(key = lambda h : h.get_data())

    return r
```

---

# 7. ORDENAÇÃO — CASOS PRONTOS

## Caso 1 — nome A → Z

```python
r.sort(key = lambda obj : obj.get_nome().casefold())
```

## Caso 2 — nome Z → A

```python
r.sort(
    key = lambda obj : obj.get_nome().casefold(),
    reverse = True
)
```

## Caso 3 — serviço pela descrição A → Z

```python
r.sort(key = lambda obj : obj.get_descricao().casefold())
```

## Caso 4 — serviço pelo valor menor → maior

```python
r.sort(key = lambda obj : obj.get_valor())
```

## Caso 5 — serviço pelo valor maior → menor

```python
r.sort(
    key = lambda obj : obj.get_valor(),
    reverse = True
)
```

## Caso 6 — horário mais antigo → mais recente

```python
r.sort(key = lambda obj : obj.get_data())
```

## Caso 7 — horário mais recente → mais antigo

```python
r.sort(
    key = lambda obj : obj.get_data(),
    reverse = True
)
```

## Caso 8 — ID menor → maior

```python
r.sort(key = lambda obj : obj.get_id())
```

## Caso 9 — ID maior → menor

```python
r.sort(
    key = lambda obj : obj.get_id(),
    reverse = True
)
```

## Caso 10 — filtrar + ordenar

```python
@staticmethod
def servico_filtrar_ordenar(valor):
    r = []

    for s in Service.servico_listar():
        if s.get_valor() >= valor:
            r.append(s)

    r.sort(key = lambda s : s.get_valor())

    return r
```

---

# 8. FILTRO POR INTERVALO DE DATAS

Se a prova pedir "horários entre duas datas":

```python
@staticmethod
def horario_listar_periodo(data_inicio, data_fim):
    r = []

    for h in Service.horario_listar():
        if h.get_data() >= data_inicio \
        and h.get_data() <= data_fim:
            r.append(h)

    r.sort(key = lambda h : h.get_data())

    return r
```

Na UI:

```python
data_inicio = st.text_input(
    "Data inicial",
    "01/01/2026 00:00"
)

data_fim = st.text_input(
    "Data final",
    "31/12/2026 23:59"
)

if st.button("Filtrar"):
    horarios = Service.horario_listar_periodo(
        datetime.strptime(data_inicio, "%d/%m/%Y %H:%M"),
        datetime.strptime(data_fim, "%d/%m/%Y %H:%M")
    )

    dic = []

    for obj in horarios:
        dic.append({
            "id": obj.get_id(),
            "data": obj.get_data(),
            "confirmado": obj.get_confirmado()
        })

    df = pd.DataFrame(dic)
    st.dataframe(df)
```

---

# 9. SIMULAÇÃO 1 — REGISTRAR ATENDIMENTO

## Por que é uma aposta forte?

A Tarefa 11 pede explicitamente o registro de atendimento, com data, queixa principal, histórico, avaliação e prescrição. Ela também diz que o profissional deve registrar os serviços realizados para totalizar o valor. 

A forma mais compatível com o código atual é criar `Atendimento` ligado a um `Horario`.

---

## `models/atendimento.py`

```python
from datetime import datetime

class Atendimento:
    def __init__(
        self,
        id,
        data,
        queixa_principal,
        historico_saude,
        avaliacao,
        prescricao,
        id_horario
    ):
        self.set_id(id)
        self.set_data(data)
        self.set_queixa_principal(queixa_principal)
        self.set_historico_saude(historico_saude)
        self.set_avaliacao(avaliacao)
        self.set_prescricao(prescricao)
        self.set_id_horario(id_horario)

    def set_id(self, id):
        if id < 0: raise ValueError("Id deve ser positivo")
        self.__id = id

    def set_data(self, data):
        self.__data = data

    def set_queixa_principal(self, queixa_principal):
        self.__queixa_principal = queixa_principal

    def set_historico_saude(self, historico_saude):
        self.__historico_saude = historico_saude

    def set_avaliacao(self, avaliacao):
        self.__avaliacao = avaliacao

    def set_prescricao(self, prescricao):
        self.__prescricao = prescricao

    def set_id_horario(self, id_horario):
        self.__id_horario = id_horario

    def get_id(self): return self.__id
    def get_data(self): return self.__data
    def get_queixa_principal(self): return self.__queixa_principal
    def get_historico_saude(self): return self.__historico_saude
    def get_avaliacao(self): return self.__avaliacao
    def get_prescricao(self): return self.__prescricao
    def get_id_horario(self): return self.__id_horario

    def __str__(self):
        return f"{self.__id} - {self.__data.strftime('%d/%m/%Y %H:%M')}"

    def to_json(self):
        return {
            "id": self.__id,
            "data": self.__data.strftime("%d/%m/%Y %H:%M"),
            "queixa_principal": self.__queixa_principal,
            "historico_saude": self.__historico_saude,
            "avaliacao": self.__avaliacao,
            "prescricao": self.__prescricao,
            "id_horario": self.__id_horario
        }

    @staticmethod
    def from_json(dic):
        return Atendimento(
            dic["id"],
            datetime.strptime(dic["data"], "%d/%m/%Y %H:%M"),
            dic["queixa_principal"],
            dic["historico_saude"],
            dic["avaliacao"],
            dic["prescricao"],
            dic["id_horario"]
        )
```

## `models/atendimentodao.py`

```python
from models.atendimento import Atendimento
import json

class AtendimentoDAO:
    def __init__(self):
        self.__arquivo = "atendimentos.json"
        self.__objetos = []
        self.__abrir()

    def inserir(self, obj):
        id = 0

        if len(self.__objetos) > 0:
            for aux in self.__objetos:
                if aux.get_id() > id:
                    id = aux.get_id()

        obj.set_id(id + 1)
        self.__objetos.append(obj)
        self.__salvar()

    def listar(self):
        return self.__objetos

    def listar_id(self, id):
        for obj in self.__objetos:
            if obj.get_id() == id:
                return obj
        return None

    def atualizar(self, obj):
        aux = self.listar_id(obj.get_id())

        if aux != None:
            self.__objetos.remove(aux)
            self.__objetos.append(obj)
            self.__salvar()

    def excluir(self, id):
        aux = self.listar_id(id)

        if aux != None:
            self.__objetos.remove(aux)
            self.__salvar()

    def __abrir(self):
        try:
            arquivo = open(self.__arquivo, mode = "r")
            list_dic = json.load(arquivo)
            arquivo.close()

            self.__objetos = []

            for dic in list_dic:
                obj = Atendimento.from_json(dic)
                self.__objetos.append(obj)

        except FileNotFoundError:
            pass

    def __salvar(self):
        arquivo = open(self.__arquivo, mode = "w")

        json.dump(
            self.__objetos,
            arquivo,
            default = Atendimento.to_json,
            indent = 2
        )

        arquivo.close()
```

## `service.py` — acrescentar

```python
from models.atendimento import Atendimento
from models.atendimentodao import AtendimentoDAO
```

```python
@staticmethod
def atendimento_inserir(
    data,
    queixa_principal,
    historico_saude,
    avaliacao,
    prescricao,
    id_horario
):
    obj = Atendimento(
        0,
        data,
        queixa_principal,
        historico_saude,
        avaliacao,
        prescricao,
        id_horario
    )

    AtendimentoDAO().inserir(obj)

@staticmethod
def atendimento_listar():
    r = AtendimentoDAO().listar()
    r.sort(key = lambda obj : obj.get_data())
    return r

@staticmethod
def atendimento_listar_id(id):
    return AtendimentoDAO().listar_id(id)

@staticmethod
def atendimento_atualizar(
    id,
    data,
    queixa_principal,
    historico_saude,
    avaliacao,
    prescricao,
    id_horario
):
    obj = Atendimento(
        id,
        data,
        queixa_principal,
        historico_saude,
        avaliacao,
        prescricao,
        id_horario
    )

    AtendimentoDAO().atualizar(obj)

@staticmethod
def atendimento_excluir(id):
    AtendimentoDAO().excluir(id)

@staticmethod
def atendimento_listar_cliente(id_cliente):
    r = []

    for a in Service.atendimento_listar():
        horario = Service.horario_listar_id(
            a.get_id_horario()
        )

        if horario != None \
        and horario.get_id_cliente() == id_cliente:
            r.append(a)

    r.sort(key = lambda a : a.get_data())

    return r

@staticmethod
def atendimento_listar_profissional(id_profissional):
    r = []

    for a in Service.atendimento_listar():
        horario = Service.horario_listar_id(
            a.get_id_horario()
        )

        if horario != None \
        and horario.get_id_profissional() == id_profissional:
            r.append(a)

    r.sort(key = lambda a : a.get_data())

    return r
```

## UI de registro — modelo

```python
import streamlit as st
import time
from datetime import datetime
from service import Service

class RegistrarAtendimentoUI:
    def main():
        st.header("Registrar Atendimento")

        horarios = Service.horario_listar_agendados(
            st.session_state["usuario_id"]
        )

        if len(horarios) == 0:
            st.write("Nenhum serviço para atendimento")

        else:
            horario = st.selectbox(
                "Informe o horário",
                horarios
            )

            data = st.text_input(
                "Informe a data do atendimento",
                horario.get_data().strftime("%d/%m/%Y %H:%M")
            )

            queixa_principal = st.text_area(
                "Informe a queixa principal"
            )

            historico_saude = st.text_area(
                "Informe o histórico de saúde"
            )

            avaliacao = st.text_area(
                "Informe a avaliação"
            )

            prescricao = st.text_area(
                "Informe a prescrição"
            )

            if st.button("Registrar"):
                Service.atendimento_inserir(
                    datetime.strptime(
                        data,
                        "%d/%m/%Y %H:%M"
                    ),
                    queixa_principal,
                    historico_saude,
                    avaliacao,
                    prescricao,
                    horario.get_id()
                )

                st.success(
                    "Atendimento registrado com sucesso"
                )

                time.sleep(2)
                st.rerun()
```

---

# 10. SIMULAÇÃO 2 — PAGAMENTO DO ATENDIMENTO

A Tarefa 11 também pede que o cliente visualize atendimentos e efetue o pagamento, podendo ser criada outra entidade para registrar pagamentos.

## `models/pagamento.py`

```python
from datetime import datetime

class Pagamento:
    def __init__(self, id, data, valor, forma, id_atendimento):
        self.set_id(id)
        self.set_data(data)
        self.set_valor(valor)
        self.set_forma(forma)
        self.set_id_atendimento(id_atendimento)

    def set_id(self, id):
        if id < 0: raise ValueError("Id deve ser positivo")
        self.__id = id

    def set_data(self, data):
        self.__data = data

    def set_valor(self, valor):
        if valor < 0: raise ValueError("Valor deve ser positivo")
        self.__valor = valor

    def set_forma(self, forma):
        self.__forma = forma

    def set_id_atendimento(self, id_atendimento):
        self.__id_atendimento = id_atendimento

    def get_id(self): return self.__id
    def get_data(self): return self.__data
    def get_valor(self): return self.__valor
    def get_forma(self): return self.__forma
    def get_id_atendimento(self): return self.__id_atendimento

    def __str__(self):
        return f"{self.__id} - {self.__data.strftime('%d/%m/%Y %H:%M')} - {self.__valor}"

    def to_json(self):
        return {
            "id": self.__id,
            "data": self.__data.strftime("%d/%m/%Y %H:%M"),
            "valor": self.__valor,
            "forma": self.__forma,
            "id_atendimento": self.__id_atendimento
        }

    @staticmethod
    def from_json(dic):
        return Pagamento(
            dic["id"],
            datetime.strptime(
                dic["data"],
                "%d/%m/%Y %H:%M"
            ),
            dic["valor"],
            dic["forma"],
            dic["id_atendimento"]
        )
```

## `models/pagamentodao.py`

```python
from models.pagamento import Pagamento
import json

class PagamentoDAO:
    def __init__(self):
        self.__arquivo = "pagamentos.json"
        self.__objetos = []
        self.__abrir()

    def inserir(self, obj):
        id = 0

        if len(self.__objetos) > 0:
            for aux in self.__objetos:
                if aux.get_id() > id:
                    id = aux.get_id()

        obj.set_id(id + 1)
        self.__objetos.append(obj)
        self.__salvar()

    def listar(self):
        return self.__objetos

    def listar_id(self, id):
        for obj in self.__objetos:
            if obj.get_id() == id:
                return obj
        return None

    def atualizar(self, obj):
        aux = self.listar_id(obj.get_id())

        if aux != None:
            self.__objetos.remove(aux)
            self.__objetos.append(obj)
            self.__salvar()

    def excluir(self, id):
        aux = self.listar_id(id)

        if aux != None:
            self.__objetos.remove(aux)
            self.__salvar()

    def __abrir(self):
        try:
            arquivo = open(self.__arquivo, mode = "r")
            list_dic = json.load(arquivo)
            arquivo.close()

            self.__objetos = []

            for dic in list_dic:
                obj = Pagamento.from_json(dic)
                self.__objetos.append(obj)

        except FileNotFoundError:
            pass

    def __salvar(self):
        arquivo = open(self.__arquivo, mode = "w")

        json.dump(
            self.__objetos,
            arquivo,
            default = Pagamento.to_json,
            indent = 2
        )

        arquivo.close()
```

## `service.py` — acrescentar

```python
from models.pagamento import Pagamento
from models.pagamentodao import PagamentoDAO
```

```python
@staticmethod
def pagamento_inserir(data, valor, forma, id_atendimento):
    obj = Pagamento(
        0,
        data,
        valor,
        forma,
        id_atendimento
    )

    PagamentoDAO().inserir(obj)

@staticmethod
def pagamento_listar():
    r = PagamentoDAO().listar()
    r.sort(key = lambda obj : obj.get_data())
    return r

@staticmethod
def pagamento_listar_id(id):
    return PagamentoDAO().listar_id(id)

@staticmethod
def pagamento_atualizar(
    id,
    data,
    valor,
    forma,
    id_atendimento
):
    obj = Pagamento(
        id,
        data,
        valor,
        forma,
        id_atendimento
    )

    PagamentoDAO().atualizar(obj)

@staticmethod
def pagamento_excluir(id):
    PagamentoDAO().excluir(id)

@staticmethod
def pagamento_listar_atendimento(id_atendimento):
    r = []

    for p in Service.pagamento_listar():
        if p.get_id_atendimento() == id_atendimento:
            r.append(p)

    return r
```

## UI de pagamento

```python
import streamlit as st
import time
from datetime import datetime
from service import Service

class PagarAtendimentoUI:
    def main():
        st.header("Pagar Atendimento")

        atendimentos = Service.atendimento_listar_cliente(
            st.session_state["usuario_id"]
        )

        if len(atendimentos) == 0:
            st.write("Nenhum atendimento realizado")

        else:
            atendimentos_sem_pagamento = []

            for a in atendimentos:
                pagamentos = Service.pagamento_listar_atendimento(
                    a.get_id()
                )

                if len(pagamentos) == 0:
                    atendimentos_sem_pagamento.append(a)

            if len(atendimentos_sem_pagamento) == 0:
                st.write("Nenhum atendimento pendente de pagamento")

            else:
                atendimento = st.selectbox(
                    "Informe o atendimento",
                    atendimentos_sem_pagamento
                )

                valor = st.number_input(
                    "Valor",
                    min_value = 0.0,
                    value = 0.0
                )

                forma = st.selectbox(
                    "Forma de pagamento",
                    ["Dinheiro", "Pix", "Cartão"]
                )

                if st.button("Pagar"):
                    Service.pagamento_inserir(
                        datetime.now(),
                        valor,
                        forma,
                        atendimento.get_id()
                    )

                    st.success(
                        "Pagamento realizado com sucesso"
                    )

                    time.sleep(2)
                    st.rerun()
```

---

# 11. SIMULAÇÃO 3 — SERVIÇOS REALIZADOS NO ATENDIMENTO

Esta é uma das partes mais prováveis de gerar uma implementação adicional porque a Tarefa 11 fala explicitamente em vários serviços realizados em um atendimento.

Uma forma simples e compatível com o padrão do projeto é criar uma classe de ligação:

`AtendimentoServico`

Ela guarda:

- `id`;
- `id_atendimento`;
- `id_servico`.

Assim, um atendimento pode possuir vários serviços.

## `models/atendimentoservico.py`

```python
class AtendimentoServico:
    def __init__(self, id, id_atendimento, id_servico):
        self.set_id(id)
        self.set_id_atendimento(id_atendimento)
        self.set_id_servico(id_servico)

    def set_id(self, id):
        if id < 0: raise ValueError("Id deve ser positivo")
        self.__id = id

    def set_id_atendimento(self, id_atendimento):
        self.__id_atendimento = id_atendimento

    def set_id_servico(self, id_servico):
        self.__id_servico = id_servico

    def get_id(self): return self.__id
    def get_id_atendimento(self): return self.__id_atendimento
    def get_id_servico(self): return self.__id_servico

    def __str__(self):
        return f"{self.__id} - {self.__id_atendimento} - {self.__id_servico}"

    def to_json(self):
        return {
            "id": self.__id,
            "id_atendimento": self.__id_atendimento,
            "id_servico": self.__id_servico
        }

    @staticmethod
    def from_json(dic):
        return AtendimentoServico(
            dic["id"],
            dic["id_atendimento"],
            dic["id_servico"]
        )
```

## `models/atendimentoservicodao.py`

```python
from models.atendimentoservico import AtendimentoServico
import json

class AtendimentoServicoDAO:
    def __init__(self):
        self.__arquivo = "atendimentoservicos.json"
        self.__objetos = []
        self.__abrir()

    def inserir(self, obj):
        id = 0

        if len(self.__objetos) > 0:
            for aux in self.__objetos:
                if aux.get_id() > id:
                    id = aux.get_id()

        obj.set_id(id + 1)
        self.__objetos.append(obj)
        self.__salvar()

    def listar(self):
        return self.__objetos

    def listar_id(self, id):
        for obj in self.__objetos:
            if obj.get_id() == id:
                return obj
        return None

    def atualizar(self, obj):
        aux = self.listar_id(obj.get_id())

        if aux != None:
            self.__objetos.remove(aux)
            self.__objetos.append(obj)
            self.__salvar()

    def excluir(self, id):
        aux = self.listar_id(id)

        if aux != None:
            self.__objetos.remove(aux)
            self.__salvar()

    def __abrir(self):
        try:
            arquivo = open(self.__arquivo, mode = "r")
            list_dic = json.load(arquivo)
            arquivo.close()

            self.__objetos = []

            for dic in list_dic:
                obj = AtendimentoServico.from_json(dic)
                self.__objetos.append(obj)

        except FileNotFoundError:
            pass

    def __salvar(self):
        arquivo = open(self.__arquivo, mode = "w")

        json.dump(
            self.__objetos,
            arquivo,
            default = AtendimentoServico.to_json,
            indent = 2
        )

        arquivo.close()
```

## Service

```python
from models.atendimentoservico import AtendimentoServico
from models.atendimentoservicodao import AtendimentoServicoDAO
```

```python
@staticmethod
def atendimento_servico_inserir(id_atendimento, id_servico):
    obj = AtendimentoServico(
        0,
        id_atendimento,
        id_servico
    )

    AtendimentoServicoDAO().inserir(obj)

@staticmethod
def atendimento_servico_listar():
    return AtendimentoServicoDAO().listar()

@staticmethod
def atendimento_servico_listar_id(id):
    return AtendimentoServicoDAO().listar_id(id)

@staticmethod
def atendimento_servico_excluir(id):
    AtendimentoServicoDAO().excluir(id)

@staticmethod
def atendimento_servico_listar_atendimento(id_atendimento):
    r = []

    for x in Service.atendimento_servico_listar():
        if x.get_id_atendimento() == id_atendimento:
            r.append(x)

    return r

@staticmethod
def atendimento_calcular_total(id_atendimento):
    total = 0

    for x in Service.atendimento_servico_listar_atendimento(
        id_atendimento
    ):
        servico = Service.servico_listar_id(
            x.get_id_servico()
        )

        if servico != None:
            total += servico.get_valor()

    return total
```

---

# 12. SIMULAÇÃO 4 — LISTAR ATENDIMENTOS DO CLIENTE COM SERVIÇOS E TOTAL

```python
import streamlit as st
import pandas as pd
from service import Service

class MeusAtendimentosUI:
    def main():
        st.header("Meus Atendimentos")

        atendimentos = Service.atendimento_listar_cliente(
            st.session_state["usuario_id"]
        )

        if len(atendimentos) == 0:
            st.write("Nenhum atendimento realizado")

        else:
            dic = []

            for a in atendimentos:
                horario = Service.horario_listar_id(
                    a.get_id_horario()
                )

                profissional = None

                if horario != None:
                    profissional = Service.profissional_listar_id(
                        horario.get_id_profissional()
                    )

                if profissional != None:
                    profissional = profissional.get_nome()

                total = Service.atendimento_calcular_total(
                    a.get_id()
                )

                dic.append({
                    "id": a.get_id(),
                    "data": a.get_data(),
                    "profissional": profissional,
                    "queixa": a.get_queixa_principal(),
                    "avaliação": a.get_avaliacao(),
                    "total": total
                })

            df = pd.DataFrame(dic)
            st.dataframe(df)
```

---

# 13. SIMULAÇÃO 5 — ORDENAR ATENDIMENTOS PELO VALOR TOTAL

```python
@staticmethod
def atendimento_listar_por_valor():
    r = Service.atendimento_listar()

    r.sort(
        key = lambda a :
            Service.atendimento_calcular_total(a.get_id())
    )

    return r
```

Do maior para o menor:

```python
r.sort(
    key = lambda a :
        Service.atendimento_calcular_total(a.get_id()),
    reverse = True
)
```

---

# 14. SIMULAÇÃO 6 — MOSTRAR SOMENTE ATENDIMENTOS PAGOS

```python
@staticmethod
def atendimento_listar_pagos():
    r = []

    for a in Service.atendimento_listar():
        pagamentos = Service.pagamento_listar_atendimento(
            a.get_id()
        )

        if len(pagamentos) > 0:
            r.append(a)

    return r
```

---

# 15. SIMULAÇÃO 7 — MOSTRAR SOMENTE ATENDIMENTOS NÃO PAGOS

```python
@staticmethod
def atendimento_listar_nao_pagos():
    r = []

    for a in Service.atendimento_listar():
        pagamentos = Service.pagamento_listar_atendimento(
            a.get_id()
        )

        if len(pagamentos) == 0:
            r.append(a)

    return r
```

---

# 16. SIMULAÇÃO 8 — CANCELAR AGENDAMENTO

Se o enunciado pedir "cancelar", normalmente não precisa criar uma entidade nova.

Modelo simples:

```python
@staticmethod
def horario_cancelar(id):
    obj = Service.horario_listar_id(id)

    if obj != None:
        Service.horario_atualizar(
            obj.get_id(),
            obj.get_data(),
            False,
            None,
            None,
            obj.get_id_profissional()
        )
```

UI:

```python
import streamlit as st
import time
from service import Service

class CancelarAgendamentoUI:
    def main():
        st.header("Cancelar Agendamento")

        horarios = Service.horario_listar_cliente(
            st.session_state["usuario_id"]
        )

        if len(horarios) == 0:
            st.write("Nenhum agendamento")

        else:
            horario = st.selectbox(
                "Informe o agendamento",
                horarios
            )

            if st.button("Cancelar"):
                Service.horario_cancelar(
                    horario.get_id()
                )

                st.success(
                    "Agendamento cancelado com sucesso"
                )

                time.sleep(2)
                st.rerun()
```

---

# 17. SIMULAÇÃO 9 — BUSCAR CLIENTE POR NOME NA UI

Service:

```python
@staticmethod
def cliente_listar_nome(nome):
    r = []

    for c in Service.cliente_listar():
        if nome.casefold() in c.get_nome().casefold():
            r.append(c)

    return r
```

UI:

```python
nome = st.text_input("Digite o nome")

clientes = Service.cliente_listar_nome(nome)

list_dic = []

for c in clientes:
    list_dic.append(c.to_dict())

df = pd.DataFrame(list_dic)

st.dataframe(df)
```

---

# 18. SIMULAÇÃO 10 — BUSCAR SERVIÇO POR DESCRIÇÃO E ORDENAR PELO VALOR

```python
@staticmethod
def servico_buscar(descricao):
    r = []

    for s in Service.servico_listar():
        if descricao.casefold() in s.get_descricao().casefold():
            r.append(s)

    r.sort(key = lambda s : s.get_valor())

    return r
```

---

# 19. SIMULAÇÃO 11 — FILTRAR HORÁRIOS POR PROFISSIONAL + CONFIRMAÇÃO

```python
@staticmethod
def horario_filtrar_profissional_confirmado(
    id_profissional,
    confirmado
):
    r = []

    for h in Service.horario_listar():
        if h.get_id_profissional() == id_profissional \
        and h.get_confirmado() == confirmado:
            r.append(h)

    r.sort(key = lambda h : h.get_data())

    return r
```

---

# 20. SIMULAÇÃO 12 — FILTRAR POR PROFISSIONAL + CLIENTE

```python
@staticmethod
def horario_filtrar(
    id_profissional,
    id_cliente
):
    r = []

    for h in Service.horario_listar():
        if h.get_id_profissional() == id_profissional \
        and h.get_id_cliente() == id_cliente:
            r.append(h)

    r.sort(key = lambda h : h.get_data())

    return r
```

---

# 21. SIMULAÇÃO 13 — FILTRAR ATENDIMENTOS POR PERÍODO

```python
@staticmethod
def atendimento_listar_periodo(data_inicio, data_fim):
    r = []

    for a in Service.atendimento_listar():
        if a.get_data() >= data_inicio \
        and a.get_data() <= data_fim:
            r.append(a)

    r.sort(key = lambda a : a.get_data())

    return r
```

---

# 22. SIMULAÇÃO 14 — TOTAL DOS SERVIÇOS DE UM CLIENTE

```python
@staticmethod
def cliente_calcular_total(id_cliente):
    total = 0

    atendimentos = Service.atendimento_listar_cliente(
        id_cliente
    )

    for a in atendimentos:
        total += Service.atendimento_calcular_total(
            a.get_id()
        )

    return total
```

---

# 23. SIMULAÇÃO 15 — LISTAR SERVIÇOS MAIS CAROS PRIMEIRO

```python
@staticmethod
def servico_listar_maior_valor():
    r = Service.servico_listar()

    r.sort(
        key = lambda s : s.get_valor(),
        reverse = True
    )

    return r
```

---

# 24. SIMULAÇÃO 16 — LISTAR PROFISSIONAIS POR ESPECIALIDADE E NOME

```python
@staticmethod
def profissional_filtrar_especialidade(
    especialidade
):
    r = []

    for p in Service.profissional_listar():
        if especialidade.casefold() in \
        p.get_especialidade().casefold():
            r.append(p)

    r.sort(
        key = lambda p : p.get_nome().casefold()
    )

    return r
```

---

# 25. SIMULAÇÃO 17 — CRIAR UMA ENTIDADE DE PAGAMENTO SEM ASSOCIAÇÃO

Se o enunciado disser que o pagamento não precisa guardar ID de atendimento, use o modelo simples:

```python
class Pagamento:
    def __init__(self, id, data, valor, forma):
        self.set_id(id)
        self.set_data(data)
        self.set_valor(valor)
        self.set_forma(forma)

    def set_id(self, id):
        if id < 0: raise ValueError("Id deve ser positivo")
        self.__id = id

    def set_data(self, data):
        self.__data = data

    def set_valor(self, valor):
        if valor < 0: raise ValueError("Valor deve ser positivo")
        self.__valor = valor

    def set_forma(self, forma):
        self.__forma = forma

    def get_id(self): return self.__id
    def get_data(self): return self.__data
    def get_valor(self): return self.__valor
    def get_forma(self): return self.__forma

    def __str__(self):
        return f"{self.__id} - {self.__data} - {self.__valor} - {self.__forma}"

    def to_json(self):
        return {
            "id": self.__id,
            "data": self.__data.strftime("%d/%m/%Y %H:%M"),
            "valor": self.__valor,
            "forma": self.__forma
        }

    @staticmethod
    def from_json(dic):
        return Pagamento(
            dic["id"],
            datetime.strptime(
                dic["data"],
                "%d/%m/%Y %H:%M"
            ),
            dic["valor"],
            dic["forma"]
        )
```

---

# 26. CHECKLIST — NOVA CLASSE

- [ ] Criar `models/nome.py`
- [ ] Criar `models/nomedao.py`
- [ ] Criar o JSON, se necessário
- [ ] Importar Model no `service.py`
- [ ] Importar DAO no `service.py`
- [ ] Criar `inserir`
- [ ] Criar `listar`
- [ ] Criar `listar_id`
- [ ] Criar `atualizar`
- [ ] Criar `excluir`
- [ ] Criar UI
- [ ] Importar UI no `index.py`
- [ ] Colocar opção no menu correto

---

# 27. CHECKLIST — NOVA ASSOCIAÇÃO

- [ ] Criar `id_outra` no Model
- [ ] Criar `set_id_outra`
- [ ] Criar `get_id_outra`
- [ ] Colocar `id_outra` no `to_json`
- [ ] Recuperar `id_outra` no `from_json`
- [ ] Passar `id_outra` no Service
- [ ] Na UI, buscar a outra entidade com `Service.outra_listar_id(...)`
- [ ] Na inserção, pegar `outra.get_id()`
- [ ] Na atualização, selecionar a associação atual

---

# 28. CHECKLIST — FILTRAGEM / ORDENAÇÃO

- [ ] Criar `r = []`
- [ ] Percorrer a lista
- [ ] Colocar a condição no `if`
- [ ] `r.append(obj)`
- [ ] Ordenar se o enunciado pedir
- [ ] `return r`
- [ ] Se for texto, considerar `.casefold()`
- [ ] Se for data, comparar objetos `datetime`
- [ ] Se for número, usar `>`, `<`, `>=` ou `<=`
- [ ] Se houver duas condições, usar `and`
- [ ] Se houver alternativas, usar `or`

---

# 29. CHECKLIST — NOVA TELA

- [ ] `import streamlit as st`
- [ ] `import pandas as pd` se houver tabela
- [ ] `import time` se usar `sleep`
- [ ] `from service import Service`
- [ ] criar classe `NomeUI`
- [ ] criar `main()`
- [ ] criar campos
- [ ] chamar Service
- [ ] mostrar `st.success`
- [ ] usar `st.rerun()` quando necessário
- [ ] importar no `index.py`
- [ ] colocar no menu correto

---

# 30. CHECKLIST — SE A PROVA PEDIR "REGISTRAR ATENDIMENTO"

- [ ] `models/atendimento.py`
- [ ] `models/atendimentodao.py`
- [ ] importar os dois no Service
- [ ] criar inserir/listar/listar_id/atualizar/excluir
- [ ] guardar `id_horario`
- [ ] criar UI de registro
- [ ] buscar os horários do profissional logado
- [ ] registrar data
- [ ] registrar queixa
- [ ] registrar histórico
- [ ] registrar avaliação
- [ ] registrar prescrição
- [ ] salvar o `id_horario`

---

# 31. CHECKLIST — SE PEDIR "PAGAR ATENDIMENTO"

- [ ] `models/pagamento.py`
- [ ] `models/pagamentodao.py`
- [ ] importar no Service
- [ ] criar CRUD
- [ ] guardar `id_atendimento`
- [ ] listar atendimentos do cliente logado
- [ ] descobrir quais já têm pagamento
- [ ] mostrar somente os pendentes
- [ ] registrar data
- [ ] registrar valor
- [ ] registrar forma
- [ ] salvar pagamento

---

# 32. CHECKLIST — SE PEDIR "SERVIÇOS REALIZADOS"

- [ ] criar `AtendimentoServico`
- [ ] guardar `id_atendimento`
- [ ] guardar `id_servico`
- [ ] criar DAO
- [ ] criar Service
- [ ] criar filtro por `id_atendimento`
- [ ] buscar cada serviço com `Service.servico_listar_id()`
- [ ] somar `servico.get_valor()`
- [ ] mostrar total na UI

---

# 33. CHECKLIST — ANTES DE CONSIDERAR TERMINADO

- [ ] O nome do arquivo bate com o import?
- [ ] O nome da classe bate com o arquivo?
- [ ] Todos os métodos usados na UI existem no Service?
- [ ] Todos os métodos usados no Service existem no DAO?
- [ ] O DAO importa a classe correta?
- [ ] O `from_json()` tem todos os campos?
- [ ] O `to_json()` tem todos os campos?
- [ ] O construtor recebe os mesmos campos usados no Service?
- [ ] Os `get_...()` usados na UI existem?
- [ ] Os `set_...()` usados existem?
- [ ] Se houver associação, o ID está sendo salvo?
- [ ] A nova UI foi importada no `index.py`?
- [ ] A nova opção foi colocada no menu?
- [ ] A lista vazia está tratada?
- [ ] Depois de inserir/atualizar/excluir há `st.rerun()`?
- [ ] O filtro está realmente retornando apenas o que o enunciado pediu?
- [ ] A ordenação está aplicada à lista certa?

---

# 34. TABELA DE DECISÃO RÁPIDA

| Pedido da prova | Código que provavelmente será necessário |
|---|---|
| "Cadastrar X" | Model + DAO + Service + UI |
| "Listar X" | Service + UI |
| "Buscar X por ID" | DAO `listar_id` + Service |
| "Buscar X por nome" | Service com `if nome...` |
| "Ordenar X por nome" | `sort(key = lambda...)` |
| "Ordenar X por valor" | `sort(key = lambda...)` |
| "Ordenar do maior para menor" | `reverse = True` |
| "Filtrar X por condição" | `r = []` + `for` + `if` |
| "Filtrar por duas condições" | `if condicao1 and condicao2` |
| "Filtrar por qualquer uma" | `if condicao1 or condicao2` |
| "Mostrar nome relacionado" | `Service.x_listar_id(obj.get_id_x())` |
| "Somente usuário logado" | `st.session_state["usuario_id"]` |
| "Nova relação entre duas classes" | guardar IDs |
| "Vários serviços em um atendimento" | classe de ligação `AtendimentoServico` |
| "Totalizar serviços" | somar `get_valor()` |
| "Pagamento" | classe `Pagamento` + `id_atendimento` |
| "Cancelar" | alterar estado/dados do horário |
| "Entre datas" | comparar `get_data()` com início/fim |

---

# 35. APOSTAS PARA A PROVA

Estas são **simulações/inferências**, não afirmações sobre o que o professor necessariamente cobrará.

### Aposta 1 — Atendimento
**Alta prioridade.**

Motivo: aparece explicitamente na Tarefa 11.

Arquivos prováveis:
- `models/atendimento.py`
- `models/atendimentodao.py`
- `service.py`
- `templates/registraratendimentoui.py`
- `index.py`

### Aposta 2 — Pagamento
**Alta prioridade.**

Motivo: aparece explicitamente na Tarefa 11.

Arquivos prováveis:
- `models/pagamento.py`
- `models/pagamentodao.py`
- `service.py`
- `templates/pagaratendimentoui.py`
- `index.py`

### Aposta 3 — Filtrar/ordenar uma entidade já existente
**Alta prioridade.**

Exemplos:
- clientes por nome;
- serviços por valor;
- horários por profissional;
- atendimentos por data;
- atendimentos por cliente.

### Aposta 4 — Associação entre entidades
**Alta prioridade.**

Exemplos:
- atendimento → horário;
- pagamento → atendimento;
- atendimento → serviço.

### Aposta 5 — Totalização
**Média/alta prioridade.**

Exemplo:

```python
total = 0

for x in Service.atendimento_servico_listar_atendimento(
    id_atendimento
):
    servico = Service.servico_listar_id(
        x.get_id_servico()
    )

    if servico != None:
        total += servico.get_valor()
```

### Aposta 6 — Tela específica para usuário logado
**Média/alta prioridade.**

Padrão já existente no projeto:

```python
st.session_state["usuario_id"]
```

### Aposta 7 — Status/situação
**Média prioridade.**

Exemplos:
- confirmado/não confirmado;
- pago/não pago;
- disponível/agendado;
- ativo/inativo.

### Aposta 8 — Relatório/listagem combinada
**Média prioridade.**

Exemplo:
mostrar atendimento + cliente + profissional + serviço + valor.

Padrão:

```python
horario = Service.horario_listar_id(
    atendimento.get_id_horario()
)
```

depois:

```python
cliente = Service.cliente_listar_id(
    horario.get_id_cliente()
)
```

e:

```python
profissional = Service.profissional_listar_id(
    horario.get_id_profissional()
)
```

---

# 36. MODELO DE TABELA PARA UMA LISTAGEM COM ASSOCIAÇÕES

```python
dic = []

for obj in objetos:

    outra = Service.outra_listar_id(
        obj.get_id_outra()
    )

    if outra != None:
        outra = outra.get_nome()

    dic.append({
        "id": obj.get_id(),
        "campo": obj.get_campo(),
        "outra": outra
    })

df = pd.DataFrame(dic)

st.dataframe(df)
```

---

# 37. MODELO DE FILTRO + ASSOCIAÇÃO

Quando o filtro depende de outra classe:

```python
@staticmethod
def novaentidade_listar_por_profissional(id_profissional):
    r = []

    for obj in Service.novaentidade_listar():

        horario = Service.horario_listar_id(
            obj.get_id_horario()
        )

        if horario != None \
        and horario.get_id_profissional() == id_profissional:
            r.append(obj)

    r.sort(key = lambda obj : obj.get_data())

    return r
```

---

# 38. MODELO DE SELECTBOX PARA UMA ASSOCIAÇÃO

```python
objetos = Service.outra_listar()

outra = st.selectbox(
    "Informe a associação",
    objetos,
    index = None
)

if st.button("Inserir"):

    id_outra = None

    if outra != None:
        id_outra = outra.get_id()

    Service.novaentidade_inserir(
        campo,
        id_outra
    )
```

---

# 39. MODELO DE SELECTBOX PARA ATUALIZAR ASSOCIAÇÃO

```python
id_outra = None

if op.get_id_outra() not in [0, None]:
    id_outra = op.get_id_outra()

outra = st.selectbox(
    "Informe a associação",
    objetos,
    next(
        (
            i for i, x in enumerate(objetos)
            if x.get_id() == id_outra
        ),
        None
    )
)
```

---

# 40. MODELO DE LISTAGEM COM NOME NO LUGAR DO ID

```python
for obj in objetos:

    cliente = Service.cliente_listar_id(
        obj.get_id_cliente()
    )

    if cliente != None:
        cliente = cliente.get_nome()

    dic.append({
        "id": obj.get_id(),
        "cliente": cliente
    })
```

---

# 41. MODELO DE LISTAGEM COM TOTAL

```python
dic = []

for obj in objetos:

    total = Service.atendimento_calcular_total(
        obj.get_id()
    )

    dic.append({
        "id": obj.get_id(),
        "data": obj.get_data(),
        "total": total
    })

df = pd.DataFrame(dic)
st.dataframe(df)
```

---

# 42. ARQUIVOS QUE MAIS VALE A PENA TER COMO REFERÊNCIA DURANTE O ESTUDO

| Arquivo atual | Serve como modelo para |
|---|---|
| `models/cliente.py` | entidade simples |
| `models/clientedao.py` | DAO CRUD |
| `models/horario.py` | entidade com vários IDs |
| `models/horariodao.py` | DAO de entidade relacionada |
| `service.py` | filtragem + ordenação + associações |
| `templates/manterhorarioui.py` | UI com várias associações |
| `templates/minhaagendaui.py` | filtro pelo profissional logado |
| `templates/meusservicosui.py` | filtro pelo cliente logado |
| `templates/confirmarservicoui.py` | operação específica em cima de horário |
| `index.py` | adicionar nova tela ao menu |

---

# 43. RESUMO DE MODELOS PARA COPIAR

### Entidade simples

```text
models/novaentidade.py
models/novaentidadedao.py
service.py
templates/manternovaentidadeui.py
index.py
```

### Entidade com associação

```text
models/novaentidade.py
models/novaentidadedao.py
service.py
templates/manternovaentidadeui.py
index.py
```

### Filtro

```python
r = []

for obj in Service.alguma_lista():
    if CONDIÇÃO:
        r.append(obj)

r.sort(key = lambda obj : CAMPO)

return r
```

### Ordenação

```python
r.sort(key = lambda obj : obj.get_campo())
```

### Ordem inversa

```python
r.sort(
    key = lambda obj : obj.get_campo(),
    reverse = True
)
```

### Associação

```python
outra = Service.outra_listar_id(
    obj.get_id_outra()
)
```

### ID da associação

```python
if outra != None:
    id_outra = outra.get_id()
```

### Usuário logado

```python
st.session_state["usuario_id"]
```

---

# 44. OBSERVAÇÃO SOBRE AS SIMULAÇÕES

Os blocos de `Atendimento`, `Pagamento` e `AtendimentoServico` são **modelos de estudo/inferência para possíveis extensões da prova**, construídos seguindo os padrões que aparecem no projeto enviado.

Eles não devem ser tratados como se fossem código oficialmente fornecido pelo professor. Se o enunciado da prova usar nomes, atributos ou regras diferentes, adapte os campos mantendo o mesmo padrão do modelo.


---

# 90. SIMULAÇÕES EXTRAS

Foi criado um arquivo separado `SIMULACOES_EXTRAS.md` com mais possibilidades de implementação, incluindo:
- cancelar;
- reagendar;
- filtros por data;
- filtros combinados;
- relatórios;
- contagens;
- ranking;
- faturamento;
- verificação de disponibilidade;
- prevenção de duplicidade;
- histórico;
- novas associações;
- novas entidades;
- avaliações;
- notificações;
- endereços;
- situações;
- vários cenários completos de possível enunciado.
