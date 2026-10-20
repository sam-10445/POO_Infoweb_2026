# SIMULAÇÕES EXTRAS — POSSÍVEIS IMPLEMENTAÇÕES DA PROVA

> Estas são previsões/simulações. Elas não são garantias do que cairá.
> Foram escolhidas olhando para os recursos que o projeto atual já possui: Cliente, Serviço, Horário, Profissional, login por tipo, confirmação de serviço, agenda do profissional, serviços do cliente, filtragem e ordenação.

---

# 1. CANCELAR UM SERVIÇO AGENDADO

## Possibilidade do enunciado

> "Permitir que o cliente cancele um serviço agendado."

Como o projeto já usa `Horario` para representar o agendamento, não é necessário criar uma classe nova.

### Service — acrescentar

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

### UI completa

```python
import streamlit as st
import time
from service import Service

class CancelarServicoUI:
    def main():
        st.header("Cancelar Serviço")

        horarios = Service.horario_listar_cliente(
            st.session_state["usuario_id"]
        )

        horarios = [
            h for h in horarios
            if h.get_data() >= datetime.now()
        ]

        if len(horarios) == 0:
            st.write("Nenhum serviço agendado")

        else:
            horario = st.selectbox(
                "Informe o serviço",
                horarios
            )

            if st.button("Cancelar"):
                Service.horario_cancelar(
                    horario.get_id()
                )

                st.success(
                    "Serviço cancelado com sucesso"
                )

                time.sleep(2)
                st.rerun()
```

> Se o enunciado exigir "cancelado" como situação permanente, o código atual não possui um campo específico para isso. Nesse caso, será necessário acrescentar um campo de situação em `Horario`.

---

# 2. REAGENDAR SERVIÇO

## Possibilidade

> "Permitir que o cliente altere a data/horário de um serviço."

### Service

```python
@staticmethod
def horario_reagendar(id, data):
    obj = Service.horario_listar_id(id)

    if obj != None:
        Service.horario_atualizar(
            obj.get_id(),
            data,
            False,
            obj.get_id_cliente(),
            obj.get_id_servico(),
            obj.get_id_profissional()
        )
```

### UI completa

```python
import streamlit as st
import time
from datetime import datetime
from service import Service

class ReagendarServicoUI:
    def main():
        st.header("Reagendar Serviço")

        horarios = Service.horario_listar_cliente(
            st.session_state["usuario_id"]
        )

        if len(horarios) == 0:
            st.write("Nenhum serviço agendado")

        else:
            horario = st.selectbox(
                "Informe o serviço",
                horarios
            )

            data = st.text_input(
                "Nova data e horário",
                horario.get_data().strftime(
                    "%d/%m/%Y %H:%M"
                )
            )

            if st.button("Reagendar"):
                try:
                    nova_data = datetime.strptime(
                        data,
                        "%d/%m/%Y %H:%M"
                    )

                    Service.horario_reagendar(
                        horario.get_id(),
                        nova_data
                    )

                    st.success(
                        "Serviço reagendado com sucesso"
                    )

                    time.sleep(2)
                    st.rerun()

                except ValueError:
                    st.error(
                        "Informe a data no formato dd/mm/aaaa HH:MM"
                    )
```

---

# 3. MOSTRAR SOMENTE SERVIÇOS FUTUROS DO CLIENTE

## Possibilidade

> "O cliente deve visualizar seus próximos serviços."

### Service

```python
@staticmethod
def horario_listar_proximos(id_cliente):
    r = []

    agora = datetime.now(
        ZoneInfo("America/Sao_Paulo")
    ).replace(tzinfo=None)

    for h in Service.horario_listar_cliente(id_cliente):
        if h.get_data() >= agora:
            r.append(h)

    r.sort(key = lambda h : h.get_data())

    return r
```

### UI

```python
import streamlit as st
import pandas as pd
from service import Service

class ProximosServicosUI:
    def main():
        st.header("Próximos Serviços")

        horarios = Service.horario_listar_proximos(
            st.session_state["usuario_id"]
        )

        if len(horarios) == 0:
            st.write("Nenhum próximo serviço")

        else:
            dic = []

            for h in horarios:
                profissional = Service.profissional_listar_id(
                    h.get_id_profissional()
                )

                servico = Service.servico_listar_id(
                    h.get_id_servico()
                )

                if profissional != None:
                    profissional = profissional.get_nome()

                if servico != None:
                    servico = servico.get_descricao()

                dic.append({
                    "data": h.get_data(),
                    "serviço": servico,
                    "profissional": profissional,
                    "confirmado": h.get_confirmado()
                })

            st.dataframe(pd.DataFrame(dic))
```

---

# 4. MOSTRAR SOMENTE SERVIÇOS DE HOJE

## Possibilidade

> "O profissional deve visualizar os atendimentos/serviços de hoje."

### Service

```python
@staticmethod
def horario_listar_hoje(id_profissional):
    r = []

    hoje = datetime.now(
        ZoneInfo("America/Sao_Paulo")
    ).date()

    for h in Service.horario_listar_profissional(
        id_profissional
    ):
        if h.get_data().date() == hoje:
            r.append(h)

    r.sort(key = lambda h : h.get_data())

    return r
```

---

# 5. FILTRAR HORÁRIOS POR SERVIÇO

## Possibilidade

> "Mostrar somente os horários de determinado serviço."

### Service

```python
@staticmethod
def horario_listar_servico(id_servico):
    r = []

    for h in Service.horario_listar():
        if h.get_id_servico() == id_servico:
            r.append(h)

    r.sort(key = lambda h : h.get_data())

    return r
```

---

# 6. FILTRAR POR PROFISSIONAL E SERVIÇO

## Possibilidade

> "Mostrar os horários de um profissional para determinado serviço."

### Service

```python
@staticmethod
def horario_filtrar_profissional_servico(
    id_profissional,
    id_servico
):
    r = []

    for h in Service.horario_listar():
        if h.get_id_profissional() == id_profissional \
        and h.get_id_servico() == id_servico:
            r.append(h)

    r.sort(key = lambda h : h.get_data())

    return r
```

---

# 7. FILTRAR POR PROFISSIONAL + SERVIÇO + DISPONIBILIDADE

## Possibilidade

> "Exibir apenas horários disponíveis para determinado profissional e serviço."

```python
@staticmethod
def horario_filtrar_disponiveis(
    id_profissional,
    id_servico
):
    r = []

    agora = datetime.now(
        ZoneInfo("America/Sao_Paulo")
    ).replace(tzinfo=None)

    for h in Service.horario_listar():
        if h.get_data() >= agora \
        and h.get_id_profissional() == id_profissional \
        and h.get_id_servico() == id_servico \
        and h.get_confirmado() == False \
        and h.get_id_cliente() in [None, 0]:
            r.append(h)

    r.sort(key = lambda h : h.get_data())

    return r
```

---

# 8. LISTAR SERVIÇOS CONFIRMADOS DO CLIENTE

## Possibilidade

> "O cliente deve visualizar somente seus serviços confirmados."

```python
@staticmethod
def horario_listar_confirmados_cliente(id_cliente):
    r = []

    for h in Service.horario_listar_cliente(id_cliente):
        if h.get_confirmado() == True:
            r.append(h)

    r.sort(key = lambda h : h.get_data())

    return r
```

---

# 9. LISTAR SERVIÇOS AINDA NÃO CONFIRMADOS

## Possibilidade

> "O cliente deve visualizar os serviços aguardando confirmação."

```python
@staticmethod
def horario_listar_pendentes_cliente(id_cliente):
    r = []

    for h in Service.horario_listar_cliente(id_cliente):
        if h.get_confirmado() == False:
            r.append(h)

    r.sort(key = lambda h : h.get_data())

    return r
```

---

# 10. CONTAR QUANTOS SERVIÇOS UM PROFISSIONAL TEM

## Possibilidade

> "Mostrar a quantidade de serviços agendados para cada profissional."

### Service

```python
@staticmethod
def profissional_quantidade_servicos(id_profissional):
    quantidade = 0

    for h in Service.horario_listar_profissional(
        id_profissional
    ):
        if h.get_id_cliente() not in [None, 0]:
            quantidade += 1

    return quantidade
```

### Listagem de todos os profissionais

```python
@staticmethod
def profissional_listar_quantidade_servicos():
    r = Service.profissional_listar()

    r.sort(
        key = lambda p :
            Service.profissional_quantidade_servicos(
                p.get_id()
            ),
        reverse = True
    )

    return r
```

---

# 11. PROFISSIONAIS COM MAIS SERVIÇOS AGENDADOS

## Possibilidade

> "Ordenar os profissionais pela quantidade de serviços."

```python
@staticmethod
def profissional_listar_mais_agendados():
    r = []

    for p in Service.profissional_listar():
        quantidade = Service.profissional_quantidade_servicos(
            p.get_id()
        )

        r.append((p, quantidade))

    r.sort(
        key = lambda item : item[1],
        reverse = True
    )

    return r
```

### UI

```python
import streamlit as st
import pandas as pd
from service import Service

class RankingProfissionaisUI:
    def main():
        st.header("Profissionais por quantidade de serviços")

        lista = Service.profissional_listar_mais_agendados()

        dic = []

        for profissional, quantidade in lista:
            dic.append({
                "profissional": profissional.get_nome(),
                "especialidade": profissional.get_especialidade(),
                "serviços": quantidade
            })

        st.dataframe(pd.DataFrame(dic))
```

---

# 12. SERVIÇOS MAIS AGENDADOS

## Possibilidade

> "Mostrar quais serviços são mais procurados."

### Service

```python
@staticmethod
def servico_quantidade_agendamentos(id_servico):
    quantidade = 0

    for h in Service.horario_listar():
        if h.get_id_servico() == id_servico \
        and h.get_id_cliente() not in [None, 0]:
            quantidade += 1

    return quantidade

@staticmethod
def servico_listar_mais_agendados():
    r = []

    for s in Service.servico_listar():
        quantidade = Service.servico_quantidade_agendamentos(
            s.get_id()
        )

        r.append((s, quantidade))

    r.sort(
        key = lambda item : item[1],
        reverse = True
    )

    return r
```

---

# 13. FILTRAR SERVIÇOS POR FAIXA DE PREÇO

## Possibilidade

> "Listar serviços com valor entre R$ X e R$ Y."

```python
@staticmethod
def servico_listar_faixa(valor_min, valor_max):
    r = []

    for s in Service.servico_listar():
        if s.get_valor() >= valor_min \
        and s.get_valor() <= valor_max:
            r.append(s)

    r.sort(key = lambda s : s.get_valor())

    return r
```

---

# 14. FILTRAR CLIENTES POR NOME E E-MAIL

## Possibilidade

> "Pesquisar clientes por nome ou e-mail."

```python
@staticmethod
def cliente_buscar(texto):
    r = []

    for c in Service.cliente_listar():
        if texto.casefold() in c.get_nome().casefold() \
        or texto.casefold() in c.get_email().casefold():
            r.append(c)

    return r
```

---

# 15. FILTRAR PROFISSIONAIS POR NOME OU ESPECIALIDADE

## Possibilidade

> "Pesquisar profissionais."

```python
@staticmethod
def profissional_buscar(texto):
    r = []

    for p in Service.profissional_listar():
        if texto.casefold() in p.get_nome().casefold() \
        or texto.casefold() in p.get_especialidade().casefold():
            r.append(p)

    return r
```

---

# 16. ORDENAR PROFISSIONAIS POR ESPECIALIDADE

```python
@staticmethod
def profissional_listar_por_especialidade():
    r = Service.profissional_listar()

    r.sort(
        key = lambda p :
            p.get_especialidade().casefold()
    )

    return r
```

Do contrário:

```python
r.sort(
    key = lambda p :
        p.get_especialidade().casefold(),
    reverse = True
)
```

---

# 17. ORDENAR CLIENTES PELO NÚMERO DE SERVIÇOS

## Possibilidade

> "Mostrar os clientes com mais serviços agendados."

```python
@staticmethod
def cliente_quantidade_servicos(id_cliente):
    quantidade = 0

    for h in Service.horario_listar_cliente(id_cliente):
        quantidade += 1

    return quantidade

@staticmethod
def cliente_listar_mais_agendados():
    r = []

    for c in Service.cliente_listar():
        quantidade = Service.cliente_quantidade_servicos(
            c.get_id()
        )

        r.append((c, quantidade))

    r.sort(
        key = lambda item : item[1],
        reverse = True
    )

    return r
```

---

# 18. VERIFICAR SE UM HORÁRIO ESTÁ DISPONÍVEL

## Possibilidade

> "Verificar se o horário informado já está ocupado."

```python
@staticmethod
def horario_disponivel(
    data,
    id_profissional
):
    for h in Service.horario_listar():
        if h.get_data() == data \
        and h.get_id_profissional() == id_profissional \
        and h.get_id_cliente() in [None, 0]:
            return True

    return False
```

---

# 19. IMPEDIR DUPLICIDADE DE HORÁRIO

## Possibilidade

> "Não permitir dois agendamentos para o mesmo horário."

```python
@staticmethod
def horario_pode_agendar(
    data,
    id_profissional
):
    for h in Service.horario_listar():
        if h.get_data() == data \
        and h.get_id_profissional() == id_profissional \
        and h.get_id_cliente() not in [None, 0]:
            return False

    return True
```

Uso na UI:

```python
if Service.horario_pode_agendar(
    horario.get_data(),
    profissional.get_id()
):
    Service.horario_atualizar(
        horario.get_id(),
        horario.get_data(),
        False,
        st.session_state["usuario_id"],
        servico.get_id(),
        profissional.get_id()
    )

    st.success("Horário agendado com sucesso")

else:
    st.error("Esse horário já está ocupado")
```

---

# 20. VERIFICAR SE CLIENTE JÁ TEM SERVIÇO NO MESMO HORÁRIO

## Possibilidade

> "O cliente não pode marcar dois serviços no mesmo horário."

```python
@staticmethod
def cliente_pode_agendar(
    id_cliente,
    data
):
    for h in Service.horario_listar_cliente(
        id_cliente
    ):
        if h.get_data() == data:
            return False

    return True
```

---

# 21. MOSTRAR HISTÓRICO DO CLIENTE

## Possibilidade

> "Mostrar todos os serviços já realizados pelo cliente."

Como o projeto atual não possui uma situação "realizado", a versão possível usando apenas os campos atuais seria baseada em datas passadas:

```python
@staticmethod
def cliente_historico(id_cliente):
    r = []

    agora = datetime.now(
        ZoneInfo("America/Sao_Paulo")
    ).replace(tzinfo=None)

    for h in Service.horario_listar_cliente(
        id_cliente
    ):
        if h.get_data() < agora:
            r.append(h)

    r.sort(
        key = lambda h : h.get_data(),
        reverse = True
    )

    return r
```

---

# 22. MOSTRAR AGENDA DO PROFISSIONAL POR PERÍODO

## Possibilidade

> "O profissional escolhe uma data e visualiza sua agenda."

```python
@staticmethod
def horario_listar_profissional_data(
    id_profissional,
    data
):
    r = []

    for h in Service.horario_listar_profissional(
        id_profissional
    ):
        if h.get_data().date() == data:
            r.append(h)

    r.sort(key = lambda h : h.get_data())

    return r
```

UI:

```python
import streamlit as st
import pandas as pd
from datetime import datetime
from service import Service

class AgendaPorDataUI:
    def main():
        st.header("Minha Agenda por Data")

        data = st.date_input(
            "Informe a data"
        )

        horarios = Service.horario_listar_profissional_data(
            st.session_state["usuario_id"],
            data
        )

        dic = []

        for h in horarios:
            cliente = Service.cliente_listar_id(
                h.get_id_cliente()
            )

            servico = Service.servico_listar_id(
                h.get_id_servico()
            )

            if cliente != None:
                cliente = cliente.get_nome()

            if servico != None:
                servico = servico.get_descricao()

            dic.append({
                "data": h.get_data(),
                "cliente": cliente,
                "serviço": servico,
                "confirmado": h.get_confirmado()
            })

        st.dataframe(pd.DataFrame(dic))
```

---

# 23. LISTAR HORÁRIOS DE UMA SEMANA

## Possibilidade

> "Mostrar a agenda da semana."

```python
from datetime import timedelta

@staticmethod
def horario_listar_semana(
    id_profissional,
    data_inicio
):
    r = []

    data_fim = data_inicio + timedelta(days=7)

    for h in Service.horario_listar_profissional(
        id_profissional
    ):
        if h.get_data().date() >= data_inicio \
        and h.get_data().date() < data_fim:
            r.append(h)

    r.sort(key = lambda h : h.get_data())

    return r
```

---

# 24. FILTRAR SERVIÇOS PELO CLIENTE E CONFIRMAÇÃO

```python
@staticmethod
def horario_filtrar_cliente_confirmado(
    id_cliente,
    confirmado
):
    r = []

    for h in Service.horario_listar_cliente(
        id_cliente
    ):
        if h.get_confirmado() == confirmado:
            r.append(h)

    r.sort(key = lambda h : h.get_data())

    return r
```

---

# 25. MOSTRAR SOMENTE SERVIÇOS COM CLIENTE

## Possibilidade

> "Listar os horários já agendados."

```python
@staticmethod
def horario_listar_com_cliente():
    r = []

    for h in Service.horario_listar():
        if h.get_id_cliente() not in [None, 0]:
            r.append(h)

    r.sort(key = lambda h : h.get_data())

    return r
```

---

# 26. MOSTRAR SOMENTE HORÁRIOS LIVRES

```python
@staticmethod
def horario_listar_livres():
    r = []

    for h in Service.horario_listar():
        if h.get_id_cliente() in [None, 0]:
            r.append(h)

    r.sort(key = lambda h : h.get_data())

    return r
```

---

# 27. TOTAL DE SERVIÇOS AGENDADOS POR PROFISSIONAL

```python
@staticmethod
def profissional_total_servicos(id_profissional):
    total = 0

    for h in Service.horario_listar_profissional(
        id_profissional
    ):
        servico = Service.servico_listar_id(
            h.get_id_servico()
        )

        if servico != None:
            total += servico.get_valor()

    return total
```

---

# 28. FATURAMENTO TOTAL POR PROFISSIONAL

## Possibilidade

> "Mostrar o valor total dos serviços agendados para cada profissional."

```python
@staticmethod
def profissional_listar_faturamento():
    r = []

    for p in Service.profissional_listar():
        total = Service.profissional_total_servicos(
            p.get_id()
        )

        r.append((p, total))

    r.sort(
        key = lambda item : item[1],
        reverse = True
    )

    return r
```

---

# 29. FATURAMENTO TOTAL DE TODOS OS SERVIÇOS

```python
@staticmethod
def servico_calcular_faturamento():
    total = 0

    for h in Service.horario_listar():
        servico = Service.servico_listar_id(
            h.get_id_servico()
        )

        if servico != None \
        and h.get_id_cliente() not in [None, 0]:
            total += servico.get_valor()

    return total
```

---

# 30. LISTAR SERVIÇOS POR VALOR E DESCRIÇÃO

## Possibilidade

> "Ordenar por valor e, em caso de empate, por descrição."

```python
@staticmethod
def servico_listar_ordenado():
    r = Service.servico_listar()

    r.sort(
        key = lambda s : (
            s.get_valor(),
            s.get_descricao().casefold()
        )
    )

    return r
```

---

# 31. LISTAR HORÁRIOS POR PROFISSIONAL E DATA

```python
@staticmethod
def horario_listar_ordenado():
    r = Service.horario_listar()

    r.sort(
        key = lambda h : (
            h.get_id_profissional(),
            h.get_data()
        )
    )

    return r
```

---

# 32. RELATÓRIO GERAL DE HORÁRIOS

## Possibilidade

> "Mostrar uma relação de horários com cliente, profissional e serviço."

```python
import streamlit as st
import pandas as pd
from service import Service

class RelatorioHorariosUI:
    def main():
        st.header("Relatório de Horários")

        horarios = Service.horario_listar()

        dic = []

        for h in horarios:

            cliente = Service.cliente_listar_id(
                h.get_id_cliente()
            )

            profissional = Service.profissional_listar_id(
                h.get_id_profissional()
            )

            servico = Service.servico_listar_id(
                h.get_id_servico()
            )

            dic.append({
                "data": h.get_data(),
                "cliente":
                    cliente.get_nome()
                    if cliente != None else None,
                "profissional":
                    profissional.get_nome()
                    if profissional != None else None,
                "serviço":
                    servico.get_descricao()
                    if servico != None else None,
                "valor":
                    servico.get_valor()
                    if servico != None else 0,
                "confirmado": h.get_confirmado()
            })

        st.dataframe(pd.DataFrame(dic))
```

---

# 33. RELATÓRIO SOMENTE DE HORÁRIOS CONFIRMADOS

```python
@staticmethod
def horario_listar_confirmados():
    r = []

    for h in Service.horario_listar():
        if h.get_confirmado():
            r.append(h)

    r.sort(key = lambda h : h.get_data())

    return r
```

---

# 34. RELATÓRIO SOMENTE DE HORÁRIOS PENDENTES

```python
@staticmethod
def horario_listar_pendentes():
    r = []

    for h in Service.horario_listar():
        if not h.get_confirmado() \
        and h.get_id_cliente() not in [None, 0]:
            r.append(h)

    r.sort(key = lambda h : h.get_data())

    return r
```

---

# 35. PESQUISA DE SERVIÇO POR TEXTO + FAIXA DE PREÇO

```python
@staticmethod
def servico_buscar_completo(
    texto,
    valor_min,
    valor_max
):
    r = []

    for s in Service.servico_listar():
        if texto.casefold() in s.get_descricao().casefold() \
        and s.get_valor() >= valor_min \
        and s.get_valor() <= valor_max:
            r.append(s)

    r.sort(
        key = lambda s : s.get_valor()
    )

    return r
```

---

# 36. PESQUISA DE HORÁRIOS POR TEXTO DO CLIENTE

## Possibilidade

> "Pesquisar horários pelo nome do cliente."

```python
@staticmethod
def horario_buscar_cliente(nome):
    r = []

    for h in Service.horario_listar():
        cliente = Service.cliente_listar_id(
            h.get_id_cliente()
        )

        if cliente != None \
        and nome.casefold() in cliente.get_nome().casefold():
            r.append(h)

    r.sort(key = lambda h : h.get_data())

    return r
```

---

# 37. FILTRAR POR MÊS

## Possibilidade

> "Mostrar os serviços de determinado mês."

```python
@staticmethod
def horario_listar_mes(
    ano,
    mes
):
    r = []

    for h in Service.horario_listar():
        if h.get_data().year == ano \
        and h.get_data().month == mes:
            r.append(h)

    r.sort(key = lambda h : h.get_data())

    return r
```

---

# 38. FILTRAR POR ANO

```python
@staticmethod
def horario_listar_ano(ano):
    r = []

    for h in Service.horario_listar():
        if h.get_data().year == ano:
            r.append(h)

    r.sort(key = lambda h : h.get_data())

    return r
```

---

# 39. CRIAR UMA NOVA SITUAÇÃO NO HORÁRIO

## Possibilidade

> "O horário deve ter situação: disponível, agendado, confirmado, cancelado ou realizado."

Aqui o código atual não possui esse campo. Se isso aparecer, é uma alteração de Model + DAO/JSON + Service + UI.

### `Horario` — novo campo

```python
def __init__(
    self,
    id,
    data,
    situacao
):
    self.set_id(id)
    self.set_data(data)
    self.set_situacao(situacao)
    self.set_id_cliente(0)
    self.set_id_servico(0)
    self.set_id_profissional(0)

def set_situacao(self, situacao):
    self.__situacao = situacao

def get_situacao(self):
    return self.__situacao
```

### JSON

```python
"data": self.__data.strftime("%d/%m/%Y %H:%M"),
"situacao": self.__situacao,
"id_cliente": self.__id_cliente,
"id_servico": self.__id_servico,
"id_profissional": self.__id_profissional
```

### Filtro

```python
@staticmethod
def horario_listar_situacao(situacao):
    r = []

    for h in Service.horario_listar():
        if h.get_situacao() == situacao:
            r.append(h)

    r.sort(key = lambda h : h.get_data())

    return r
```

---

# 40. NOVA CLASSE — AVALIAÇÃO DO SERVIÇO

## Possibilidade

> "Depois do atendimento, o cliente pode avaliar o serviço."

Esta é uma possibilidade de nova entidade independente.

### `models/avaliacao.py`

```python
class Avaliacao:
    def __init__(
        self,
        id,
        nota,
        comentario,
        id_cliente,
        id_profissional,
        id_servico
    ):
        self.set_id(id)
        self.set_nota(nota)
        self.set_comentario(comentario)
        self.set_id_cliente(id_cliente)
        self.set_id_profissional(id_profissional)
        self.set_id_servico(id_servico)

    def set_id(self, id):
        if id < 0:
            raise ValueError("Id deve ser positivo")
        self.__id = id

    def set_nota(self, nota):
        if nota < 0 or nota > 5:
            raise ValueError("Nota deve estar entre 0 e 5")
        self.__nota = nota

    def set_comentario(self, comentario):
        self.__comentario = comentario

    def set_id_cliente(self, id_cliente):
        self.__id_cliente = id_cliente

    def set_id_profissional(self, id_profissional):
        self.__id_profissional = id_profissional

    def set_id_servico(self, id_servico):
        self.__id_servico = id_servico

    def get_id(self): return self.__id
    def get_nota(self): return self.__nota
    def get_comentario(self): return self.__comentario
    def get_id_cliente(self): return self.__id_cliente
    def get_id_profissional(self): return self.__id_profissional
    def get_id_servico(self): return self.__id_servico

    def __str__(self):
        return f"{self.__id} - {self.__nota} - {self.__comentario}"

    def to_json(self):
        return {
            "id": self.__id,
            "nota": self.__nota,
            "comentario": self.__comentario,
            "id_cliente": self.__id_cliente,
            "id_profissional": self.__id_profissional,
            "id_servico": self.__id_servico
        }

    @staticmethod
    def from_json(dic):
        return Avaliacao(
            dic["id"],
            dic["nota"],
            dic["comentario"],
            dic["id_cliente"],
            dic["id_profissional"],
            dic["id_servico"]
        )
```

---

# 41. NOVA CLASSE — CUPOM/DESCONTO

## Possibilidade

> "Permitir desconto no pagamento."

Se o professor pedir uma entidade nova, o modelo pode ser:

```python
class Desconto:
    def __init__(
        self,
        id,
        codigo,
        percentual
    ):
        self.set_id(id)
        self.set_codigo(codigo)
        self.set_percentual(percentual)

    def set_id(self, id):
        self.__id = id

    def set_codigo(self, codigo):
        self.__codigo = codigo

    def set_percentual(self, percentual):
        if percentual < 0 or percentual > 100:
            raise ValueError(
                "Percentual deve estar entre 0 e 100"
            )
        self.__percentual = percentual

    def get_id(self): return self.__id
    def get_codigo(self): return self.__codigo
    def get_percentual(self): return self.__percentual

    def __str__(self):
        return f"{self.__codigo} - {self.__percentual}%"

    def to_json(self):
        return {
            "id": self.__id,
            "codigo": self.__codigo,
            "percentual": self.__percentual
        }

    @staticmethod
    def from_json(dic):
        return Desconto(
            dic["id"],
            dic["codigo"],
            dic["percentual"]
        )
```

---

# 42. NOVA CLASSE — NOTIFICAÇÃO

## Possibilidade

> "Registrar notificações para clientes/profissionais."

```python
class Notificacao:
    def __init__(
        self,
        id,
        mensagem,
        data,
        lida,
        id_cliente
    ):
        self.set_id(id)
        self.set_mensagem(mensagem)
        self.set_data(data)
        self.set_lida(lida)
        self.set_id_cliente(id_cliente)

    def set_id(self, id):
        self.__id = id

    def set_mensagem(self, mensagem):
        self.__mensagem = mensagem

    def set_data(self, data):
        self.__data = data

    def set_lida(self, lida):
        self.__lida = lida

    def set_id_cliente(self, id_cliente):
        self.__id_cliente = id_cliente

    def get_id(self): return self.__id
    def get_mensagem(self): return self.__mensagem
    def get_data(self): return self.__data
    def get_lida(self): return self.__lida
    def get_id_cliente(self): return self.__id_cliente

    def __str__(self):
        return f"{self.__id} - {self.__mensagem}"

    def to_json(self):
        return {
            "id": self.__id,
            "mensagem": self.__mensagem,
            "data": self.__data.strftime("%d/%m/%Y %H:%M"),
            "lida": self.__lida,
            "id_cliente": self.__id_cliente
        }

    @staticmethod
    def from_json(dic):
        return Notificacao(
            dic["id"],
            dic["mensagem"],
            datetime.strptime(
                dic["data"],
                "%d/%m/%Y %H:%M"
            ),
            dic["lida"],
            dic["id_cliente"]
        )
```

---

# 43. NOVA CLASSE — ENDEREÇO DO CLIENTE

## Possibilidade

> "Cadastrar endereço do cliente."

Como o endereço pertence a um cliente, use associação:

```python
class Endereco:
    def __init__(
        self,
        id,
        rua,
        numero,
        cidade,
        id_cliente
    ):
        self.set_id(id)
        self.set_rua(rua)
        self.set_numero(numero)
        self.set_cidade(cidade)
        self.set_id_cliente(id_cliente)

    def set_id(self, id):
        self.__id = id

    def set_rua(self, rua):
        self.__rua = rua

    def set_numero(self, numero):
        self.__numero = numero

    def set_cidade(self, cidade):
        self.__cidade = cidade

    def set_id_cliente(self, id_cliente):
        self.__id_cliente = id_cliente

    def get_id(self): return self.__id
    def get_rua(self): return self.__rua
    def get_numero(self): return self.__numero
    def get_cidade(self): return self.__cidade
    def get_id_cliente(self): return self.__id_cliente

    def __str__(self):
        return f"{self.__rua}, {self.__numero} - {self.__cidade}"

    def to_json(self):
        return {
            "id": self.__id,
            "rua": self.__rua,
            "numero": self.__numero,
            "cidade": self.__cidade,
            "id_cliente": self.__id_cliente
        }

    @staticmethod
    def from_json(dic):
        return Endereco(
            dic["id"],
            dic["rua"],
            dic["numero"],
            dic["cidade"],
            dic["id_cliente"]
        )
```

---

# 44. NOVA CLASSE — SERVIÇO + PROFISSIONAL

## Possibilidade

> "Definir quais profissionais realizam determinado serviço."

A associação seria:

```text
ProfissionalServico
    id
    id_profissional
    id_servico
```

### Model

```python
class ProfissionalServico:
    def __init__(
        self,
        id,
        id_profissional,
        id_servico
    ):
        self.set_id(id)
        self.set_id_profissional(id_profissional)
        self.set_id_servico(id_servico)

    def set_id(self, id):
        self.__id = id

    def set_id_profissional(self, id_profissional):
        self.__id_profissional = id_profissional

    def set_id_servico(self, id_servico):
        self.__id_servico = id_servico

    def get_id(self): return self.__id
    def get_id_profissional(self):
        return self.__id_profissional
    def get_id_servico(self):
        return self.__id_servico

    def to_json(self):
        return {
            "id": self.__id,
            "id_profissional": self.__id_profissional,
            "id_servico": self.__id_servico
        }

    @staticmethod
    def from_json(dic):
        return ProfissionalServico(
            dic["id"],
            dic["id_profissional"],
            dic["id_servico"]
        )
```

---

# 45. FILTRAR PROFISSIONAIS QUE REALIZAM DETERMINADO SERVIÇO

Se existir `ProfissionalServico`:

```python
@staticmethod
def profissional_listar_servico(id_servico):
    r = []

    for ps in Service.profissional_servico_listar():
        if ps.get_id_servico() == id_servico:

            profissional = Service.profissional_listar_id(
                ps.get_id_profissional()
            )

            if profissional != None:
                r.append(profissional)

    r.sort(
        key = lambda p : p.get_nome().casefold()
    )

    return r
```

---

# 46. VALOR TOTAL DE UM AGENDAMENTO

Mesmo sem criar Atendimento:

```python
@staticmethod
def horario_get_valor(id_horario):
    horario = Service.horario_listar_id(
        id_horario
    )

    if horario == None:
        return 0

    servico = Service.servico_listar_id(
        horario.get_id_servico()
    )

    if servico == None:
        return 0

    return servico.get_valor()
```

---

# 47. ORDENAR HORÁRIOS PELO VALOR DO SERVIÇO

```python
@staticmethod
def horario_listar_por_valor():
    r = Service.horario_listar()

    r.sort(
        key = lambda h :
            Service.horario_get_valor(h.get_id())
    )

    return r
```

Maior primeiro:

```python
r.sort(
    key = lambda h :
        Service.horario_get_valor(h.get_id()),
    reverse = True
)
```

---

# 48. RELATÓRIO DE SERVIÇOS POR PROFISSIONAL

```python
import streamlit as st
import pandas as pd
from service import Service

class RelatorioProfissionalUI:
    def main():
        st.header("Serviços por Profissional")

        profissionais = Service.profissional_listar()

        profissional = st.selectbox(
            "Informe o profissional",
            profissionais,
            index = None
        )

        if profissional != None:

            horarios = Service.horario_listar_profissional(
                profissional.get_id()
            )

            dic = []

            for h in horarios:
                cliente = Service.cliente_listar_id(
                    h.get_id_cliente()
                )

                servico = Service.servico_listar_id(
                    h.get_id_servico()
                )

                dic.append({
                    "data": h.get_data(),
                    "cliente":
                        cliente.get_nome()
                        if cliente != None else None,
                    "serviço":
                        servico.get_descricao()
                        if servico != None else None,
                    "valor":
                        servico.get_valor()
                        if servico != None else 0,
                    "confirmado": h.get_confirmado()
                })

            st.dataframe(pd.DataFrame(dic))
```

---

# 49. RELATÓRIO DE SERVIÇOS POR CLIENTE

```python
import streamlit as st
import pandas as pd
from service import Service

class RelatorioClienteUI:
    def main():
        st.header("Serviços por Cliente")

        clientes = Service.cliente_listar()

        cliente = st.selectbox(
            "Informe o cliente",
            clientes,
            index = None
        )

        if cliente != None:

            horarios = Service.horario_listar_cliente(
                cliente.get_id()
            )

            dic = []

            for h in horarios:
                profissional = Service.profissional_listar_id(
                    h.get_id_profissional()
                )

                servico = Service.servico_listar_id(
                    h.get_id_servico()
                )

                dic.append({
                    "data": h.get_data(),
                    "profissional":
                        profissional.get_nome()
                        if profissional != None else None,
                    "serviço":
                        servico.get_descricao()
                        if servico != None else None,
                    "valor":
                        servico.get_valor()
                        if servico != None else 0,
                    "confirmado": h.get_confirmado()
                })

            st.dataframe(pd.DataFrame(dic))
```

---

# 50. CHECKLIST EXTRA — SE O ENUNCIADO PEDIR UMA ALTERAÇÃO EM HORÁRIO

- [ ] Ver se dá para resolver usando `Horario`
- [ ] Se for só mudar data: `horario_atualizar`
- [ ] Se for só confirmar: `horario_atualizar`
- [ ] Se for cancelar: decidir se basta liberar o horário ou se precisa de nova situação
- [ ] Se for filtrar: criar método `horario_listar_...`
- [ ] Se for ordenar: adicionar `sort`
- [ ] Se for "disponível": verificar data + cliente + confirmação
- [ ] Se for "meus": usar `usuario_id`
- [ ] Se envolver cliente: `cliente_listar_id`
- [ ] Se envolver serviço: `servico_listar_id`
- [ ] Se envolver profissional: `profissional_listar_id`

---

# 51. CHECKLIST EXTRA — SE O ENUNCIADO PEDIR UMA NOVA ENTIDADE

- [ ] Model
- [ ] DAO
- [ ] JSON
- [ ] imports no `service.py`
- [ ] inserir
- [ ] listar
- [ ] listar_id
- [ ] atualizar
- [ ] excluir
- [ ] UI
- [ ] import no `index.py`
- [ ] menu
- [ ] se tiver associação, guardar somente o ID
- [ ] `to_json`
- [ ] `from_json`
- [ ] `__str__`

---

# 52. CHECKLIST EXTRA — SE O ENUNCIADO PEDIR UM RELATÓRIO

- [ ] Identificar qual lista é a principal
- [ ] Percorrer a lista
- [ ] Buscar associações com `Service.x_listar_id(...)`
- [ ] Montar `dic = []`
- [ ] `dic.append({...})`
- [ ] `pd.DataFrame(dic)`
- [ ] `st.dataframe(df)`
- [ ] Se houver filtro, fazer antes da montagem da tabela
- [ ] Se houver ordenação, fazer antes da montagem da tabela

---

# 53. CHECKLIST EXTRA — SE O ENUNCIADO PEDIR "SOMENTE..."

Procure imediatamente por um filtro.

Exemplos:

| Enunciado | Condição |
|---|---|
| somente confirmados | `== True` |
| somente não confirmados | `== False` |
| somente livres | `id_cliente in [None, 0]` |
| somente agendados | `id_cliente not in [None, 0]` |
| somente de um cliente | `id_cliente == X` |
| somente de um profissional | `id_profissional == X` |
| somente de um serviço | `id_servico == X` |
| somente futuros | `data >= agora` |
| somente passados | `data < agora` |
| somente acima de X | `valor > X` |
| somente abaixo de X | `valor < X` |
| entre X e Y | `valor >= X and valor <= Y` |

---

# 54. CHECKLIST EXTRA — SE O ENUNCIADO PEDIR "POR..."

| Pedido | Código |
|---|---|
| por nome | `get_nome()` |
| por descrição | `get_descricao()` |
| por valor | `get_valor()` |
| por data | `get_data()` |
| por cliente | `get_id_cliente()` |
| por serviço | `get_id_servico()` |
| por profissional | `get_id_profissional()` |
| por confirmação | `get_confirmado()` |
| por especialidade | `get_especialidade()` |

---

# 55. POSSIBILIDADES QUE EU CONSIDERARIA MAIS IMPORTANTES

Depois de olhar novamente para o código atual, eu priorizaria estas:

| Prioridade | Implementação | Por quê |
|---|---|---|
| 🔴 Muito alta | Filtrar/ordenar Horários | O projeto já tem muitos dados para filtrar |
| 🔴 Muito alta | Atendimento | Está diretamente na Tarefa 11 |
| 🔴 Muito alta | Pagamento | Está diretamente na Tarefa 11 |
| 🔴 Muito alta | Serviços do Atendimento | A Tarefa 11 pede vários serviços + total |
| 🟠 Alta | Relatório combinado | O projeto já faz várias associações nas UIs |
| 🟠 Alta | Filtrar por cliente/profissional/serviço | Já existe exatamente esse padrão no Service |
| 🟠 Alta | Filtro por data/período | Horário já usa `datetime` |
| 🟠 Alta | Cancelar/reagendar | São operações naturais sobre `Horario` |
| 🟡 Média | Ranking/quantidade | Extensão típica de filtragem/ordenação |
| 🟡 Média | Avaliação | Nova entidade plausível |
| 🟡 Média | Situação do horário | Plausível, mas exigiria alterar a classe existente |
| 🟡 Média | Profissional-Serviço | Associação plausível |
| 🟡 Média | Endereço | Nova entidade plausível |
| 🟡 Média | Notificação | Nova entidade plausível |
| 🟡 Baixa | Desconto/cupom | Possível, mas menos ligado ao código atual |

---

# 56. PADRÃO PARA QUALQUER FILTRO NOVO

Se aparecer uma filtragem que não está aqui, o modelo é:

```python
@staticmethod
def alguma_lista_filtro(valor):
    r = []

    for obj in Service.alguma_lista():

        if CONDIÇÃO_COM_VALOR:
            r.append(obj)

    r.sort(
        key = lambda obj : CAMPO_DA_ORDENAÇÃO
    )

    return r
```

---

# 57. PADRÃO PARA QUALQUER RELATÓRIO NOVO

```python
objetos = Service.alguma_lista()

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

# 58. PADRÃO PARA QUALQUER NOVA OPERAÇÃO

Se a prova disser:

> "Permitir que X faça Y"

e X/Y já existem no projeto, tente primeiro localizar um método existente que atualize o objeto.

Exemplo:

```python
obj = Service.horario_listar_id(id)
```

Depois:

```python
Service.horario_atualizar(
    obj.get_id(),
    obj.get_data(),
    novo_confirmado,
    obj.get_id_cliente(),
    obj.get_id_servico(),
    obj.get_id_profissional()
)
```

Isso evita criar uma entidade nova quando a operação é apenas uma alteração em um objeto existente.

---

# 59. ATENÇÃO: CAMPOS QUE O PROJETO ATUAL JÁ POSSUI EM HORÁRIO

```text
id
data
confirmado
id_cliente
id_servico
id_profissional
```

Portanto, muitos pedidos podem ser resolvidos apenas com:

```python
Service.horario_listar()
```

+

```python
if ...
```

+

```python
Service.horario_atualizar(...)
```

antes de criar uma nova classe.

---

# 60. MAIS UMA SIMULAÇÃO — PROFISSIONAL CONFIRMA E CLIENTE VÊ APENAS CONFIRMADOS

### Service

```python
@staticmethod
def horario_listar_confirmados_cliente(id_cliente):
    r = []

    for h in Service.horario_listar_cliente(
        id_cliente
    ):
        if h.get_confirmado():
            r.append(h)

    r.sort(key = lambda h : h.get_data())

    return r
```

### UI

```python
import streamlit as st
import pandas as pd
from service import Service

class ServicosConfirmadosUI:
    def main():
        st.header("Serviços Confirmados")

        horarios = Service.horario_listar_confirmados_cliente(
            st.session_state["usuario_id"]
        )

        dic = []

        for h in horarios:
            profissional = Service.profissional_listar_id(
                h.get_id_profissional()
            )

            servico = Service.servico_listar_id(
                h.get_id_servico()
            )

            dic.append({
                "data": h.get_data(),
                "profissional":
                    profissional.get_nome()
                    if profissional != None else None,
                "serviço":
                    servico.get_descricao()
                    if servico != None else None
            })

        st.dataframe(pd.DataFrame(dic))
```

---

# 61. MAIS UMA SIMULAÇÃO — PROFISSIONAL VÊ APENAS PENDENTES

```python
@staticmethod
def horario_listar_pendentes_profissional(
    id_profissional
):
    r = []

    for h in Service.horario_listar_profissional(
        id_profissional
    ):
        if h.get_id_cliente() not in [None, 0] \
        and h.get_confirmado() == False:
            r.append(h)

    r.sort(key = lambda h : h.get_data())

    return r
```

---

# 62. MAIS UMA SIMULAÇÃO — BUSCA COM VÁRIOS CAMPOS

```python
@staticmethod
def cliente_buscar_completo(texto):
    r = []

    texto = texto.casefold()

    for c in Service.cliente_listar():

        if texto in c.get_nome().casefold() \
        or texto in c.get_email().casefold() \
        or texto in c.get_fone().casefold():
            r.append(c)

    r.sort(
        key = lambda c : c.get_nome().casefold()
    )

    return r
```

---

# 63. MAIS UMA SIMULAÇÃO — ORDENAR POR DOIS CAMPOS

```python
@staticmethod
def profissional_listar_ordenado():
    r = Service.profissional_listar()

    r.sort(
        key = lambda p : (
            p.get_especialidade().casefold(),
            p.get_nome().casefold()
        )
    )

    return r
```

---

# 64. MAIS UMA SIMULAÇÃO — FILTRO + ORDENAR DO MAIOR PARA O MENOR

```python
@staticmethod
def servico_listar_caros(valor):
    r = []

    for s in Service.servico_listar():
        if s.get_valor() >= valor:
            r.append(s)

    r.sort(
        key = lambda s : s.get_valor(),
        reverse = True
    )

    return r
```

---

# 65. MAIS UMA SIMULAÇÃO — VERIFICAR SE CLIENTE POSSUI SERVIÇOS

```python
@staticmethod
def cliente_tem_servicos(id_cliente):
    horarios = Service.horario_listar_cliente(
        id_cliente
    )

    return len(horarios) > 0
```

Uso:

```python
if Service.cliente_tem_servicos(
    cliente.get_id()
):
    st.write("Cliente possui serviços")
else:
    st.write("Cliente não possui serviços")
```

---

# 66. MAIS UMA SIMULAÇÃO — VERIFICAR SE PROFISSIONAL POSSUI AGENDA

```python
@staticmethod
def profissional_tem_horarios(id_profissional):
    horarios = Service.horario_listar_profissional(
        id_profissional
    )

    return len(horarios) > 0
```

---

# 67. MAIS UMA SIMULAÇÃO — PRIMEIRO HORÁRIO DISPONÍVEL

```python
@staticmethod
def horario_primeiro_disponivel(id_profissional):
    horarios = Service.horario_listar_disponiveis(
        id_profissional
    )

    if len(horarios) > 0:
        return horarios[0]

    return None
```

---

# 68. MAIS UMA SIMULAÇÃO — QUANTIDADE DE HORÁRIOS LIVRES

```python
@staticmethod
def profissional_quantidade_horarios_livres(
    id_profissional
):
    quantidade = 0

    for h in Service.horario_listar_profissional(
        id_profissional
    ):
        if h.get_id_cliente() in [None, 0]:
            quantidade += 1

    return quantidade
```

---

# 69. MAIS UMA SIMULAÇÃO — QUANTIDADE DE HORÁRIOS CONFIRMADOS

```python
@staticmethod
def profissional_quantidade_confirmados(
    id_profissional
):
    quantidade = 0

    for h in Service.horario_listar_profissional(
        id_profissional
    ):
        if h.get_confirmado():
            quantidade += 1

    return quantidade
```

---

# 70. POSSÍVEL PROVA COMPLETA — CENÁRIO A

> "Implemente no Sistema de Agendamento uma funcionalidade para o cliente consultar seus serviços futuros, podendo filtrar por profissional e ordenar pela data."

### Service

```python
@staticmethod
def horario_listar_cliente_profissional_futuros(
    id_cliente,
    id_profissional
):
    r = []

    agora = datetime.now(
        ZoneInfo("America/Sao_Paulo")
    ).replace(tzinfo=None)

    for h in Service.horario_listar_cliente(
        id_cliente
    ):
        if h.get_id_profissional() == id_profissional \
        and h.get_data() >= agora:
            r.append(h)

    r.sort(key = lambda h : h.get_data())

    return r
```

---

# 71. POSSÍVEL PROVA COMPLETA — CENÁRIO B

> "Permita que o profissional consulte os serviços não confirmados da sua agenda, ordenados pela data."

### Service

```python
@staticmethod
def horario_listar_nao_confirmados_profissional(
    id_profissional
):
    r = []

    for h in Service.horario_listar_profissional(
        id_profissional
    ):
        if h.get_confirmado() == False \
        and h.get_id_cliente() not in [None, 0]:
            r.append(h)

    r.sort(key = lambda h : h.get_data())

    return r
```

---

# 72. POSSÍVEL PROVA COMPLETA — CENÁRIO C

> "Crie uma tela que permita ao administrador visualizar os serviços ordenados pelo valor, do maior para o menor."

```python
import streamlit as st
import pandas as pd
from service import Service

class RelatorioServicosUI:
    def main():
        st.header("Serviços por Valor")

        servicos = Service.servico_listar()

        servicos.sort(
            key = lambda s : s.get_valor(),
            reverse = True
        )

        dic = []

        for s in servicos:
            dic.append({
                "id": s.get_id(),
                "descrição": s.get_descricao(),
                "valor": s.get_valor()
            })

        st.dataframe(
            pd.DataFrame(dic)
        )
```

---

# 73. POSSÍVEL PROVA COMPLETA — CENÁRIO D

> "Crie uma tela para o profissional visualizar os clientes que possuem serviços agendados para ele."

```python
import streamlit as st
import pandas as pd
from service import Service

class ClientesAgendaUI:
    def main():
        st.header("Clientes da Agenda")

        horarios = Service.horario_listar_profissional(
            st.session_state["usuario_id"]
        )

        dic = []
        ids_clientes = []

        for h in horarios:
            if h.get_id_cliente() not in [None, 0] \
            and h.get_id_cliente() not in ids_clientes:

                cliente = Service.cliente_listar_id(
                    h.get_id_cliente()
                )

                if cliente != None:
                    ids_clientes.append(
                        cliente.get_id()
                    )

                    dic.append({
                        "id": cliente.get_id(),
                        "nome": cliente.get_nome(),
                        "email": cliente.get_email(),
                        "fone": cliente.get_fone()
                    })

        dic.sort(
            key = lambda c : c["nome"].casefold()
        )

        st.dataframe(pd.DataFrame(dic))
```

---

# 74. POSSÍVEL PROVA COMPLETA — CENÁRIO E

> "Mostre os horários disponíveis de um profissional em determinada data."

```python
@staticmethod
def horario_listar_disponiveis_data(
    id_profissional,
    data
):
    r = []

    agora = datetime.now(
        ZoneInfo("America/Sao_Paulo")
    ).replace(tzinfo=None)

    for h in Service.horario_listar_profissional(
        id_profissional
    ):
        if h.get_data().date() == data \
        and h.get_data() >= agora \
        and h.get_id_cliente() in [None, 0] \
        and h.get_confirmado() == False:
            r.append(h)

    r.sort(key = lambda h : h.get_data())

    return r
```

---

# 75. POSSÍVEL PROVA COMPLETA — CENÁRIO F

> "Permita que o administrador filtre os serviços por valor e ordene alfabeticamente."

```python
@staticmethod
def servico_filtrar_valor_ordenar_nome(
    valor
):
    r = []

    for s in Service.servico_listar():
        if s.get_valor() >= valor:
            r.append(s)

    r.sort(
        key = lambda s :
            s.get_descricao().casefold()
    )

    return r
```

---

# 76. POSSÍVEL PROVA COMPLETA — CENÁRIO G

> "Mostre a quantidade de serviços agendados para cada cliente."

```python
@staticmethod
def cliente_listar_com_quantidade():
    r = []

    for c in Service.cliente_listar():

        quantidade = len(
            Service.horario_listar_cliente(
                c.get_id()
            )
        )

        r.append({
            "cliente": c.get_nome(),
            "quantidade": quantidade
        })

    r.sort(
        key = lambda c : c["quantidade"],
        reverse = True
    )

    return r
```

UI:

```python
import streamlit as st
import pandas as pd
from service import Service

class QuantidadeServicosClienteUI:
    def main():
        st.header("Quantidade de Serviços por Cliente")

        dados = Service.cliente_listar_com_quantidade()

        st.dataframe(
            pd.DataFrame(dados)
        )
```

---

# 77. POSSÍVEL PROVA COMPLETA — CENÁRIO H

> "Mostre o total financeiro dos serviços agendados de cada cliente."

```python
@staticmethod
def cliente_listar_total():
    r = []

    for c in Service.cliente_listar():

        total = 0

        for h in Service.horario_listar_cliente(
            c.get_id()
        ):
            servico = Service.servico_listar_id(
                h.get_id_servico()
            )

            if servico != None:
                total += servico.get_valor()

        r.append({
            "cliente": c.get_nome(),
            "total": total
        })

    r.sort(
        key = lambda c : c["total"],
        reverse = True
    )

    return r
```

---

# 78. POSSÍVEL PROVA COMPLETA — CENÁRIO I

> "Permita que o cliente escolha um profissional e visualize somente os horários disponíveis para ele."

### UI completa

```python
import streamlit as st
from service import Service

class HorariosDisponiveisUI:
    def main():
        st.header("Horários Disponíveis")

        profissionais = Service.profissional_listar()

        if len(profissionais) == 0:
            st.write("Nenhum profissional cadastrado")

        else:
            profissional = st.selectbox(
                "Informe o profissional",
                profissionais
            )

            horarios = Service.horario_listar_disponiveis(
                profissional.get_id()
            )

            if len(horarios) == 0:
                st.write("Nenhum horário disponível")

            else:
                for h in horarios:
                    st.write(
                        h.get_data().strftime(
                            "%d/%m/%Y %H:%M"
                        )
                    )
```

---

# 79. POSSÍVEL PROVA COMPLETA — CENÁRIO J

> "O profissional deve visualizar seus serviços e o valor de cada um."

```python
import streamlit as st
import pandas as pd
from service import Service

class MinhaAgendaValoresUI:
    def main():
        st.header("Minha Agenda")

        horarios = Service.horario_listar_profissional(
            st.session_state["usuario_id"]
        )

        dic = []

        for h in horarios:

            cliente = Service.cliente_listar_id(
                h.get_id_cliente()
            )

            servico = Service.servico_listar_id(
                h.get_id_servico()
            )

            dic.append({
                "data": h.get_data(),
                "cliente":
                    cliente.get_nome()
                    if cliente != None else None,
                "serviço":
                    servico.get_descricao()
                    if servico != None else None,
                "valor":
                    servico.get_valor()
                    if servico != None else 0,
                "confirmado": h.get_confirmado()
            })

        st.dataframe(pd.DataFrame(dic))
```

---

# 80. CONCLUSÃO DAS SIMULAÇÕES

As possibilidades extras acima se dividem em três grupos:

### Grupo A — muito compatível com o código atual

- filtrar;
- ordenar;
- buscar;
- combinar filtros;
- filtrar por cliente;
- filtrar por profissional;
- filtrar por serviço;
- filtrar por confirmação;
- filtrar por data;
- relatórios;
- contagens;
- totais;
- cancelar;
- reagendar.

### Grupo B — diretamente ligado à Tarefa 11

- Atendimento;
- AtendimentoServico;
- Pagamento;
- total do atendimento;
- histórico;
- atendimentos do cliente;
- serviços realizados.

### Grupo C — novas entidades que podem aparecer

- Avaliação;
- Desconto;
- Notificação;
- Endereço;
- ProfissionalServico;
- Situação do Horário.

As do Grupo C exigem adaptação ao enunciado. Não há indicação no material fornecido de que alguma delas será cobrada.
