# COLA RÁPIDA — PROVA POO

## Tabela: o que mexer?

| Pedido | Mexer em |
|---|---|
| Nova classe | Model + DAO + Service + UI |
| Nova associação | Model com `id_...` + DAO + Service + UI |
| Filtrar | Service |
| Ordenar | Service |
| Nova tela | `templates/` + `index.py` |
| Mostrar nome relacionado | `Service.x_listar_id(...)` |
| Usuário logado | `st.session_state["usuario_id"]` |
| Totalizar | buscar serviços + somar `get_valor()` |

---

## FILTRAR

### Nome
```python
r = []
for obj in Service.cliente_listar():
    if texto.casefold() in obj.get_nome().casefold():
        r.append(obj)
return r
```

### Número maior
```python
r = []
for obj in Service.servico_listar():
    if obj.get_valor() > valor:
        r.append(obj)
return r
```

### Duas condições
```python
if condicao1 and condicao2:
    r.append(obj)
```

### Ou
```python
if condicao1 or condicao2:
    r.append(obj)
```

### Pelo usuário logado
```python
if obj.get_id_cliente() == id_cliente:
    r.append(obj)
```

---

## ORDENAR

```python
r.sort(key = lambda obj : obj.get_nome().casefold())
```

```python
r.sort(key = lambda obj : obj.get_valor())
```

```python
r.sort(
    key = lambda obj : obj.get_valor(),
    reverse = True
)
```

```python
r.sort(key = lambda obj : obj.get_data())
```

---

## ASSOCIAÇÃO

### Guardar ID
```python
self.set_id_outra(id_outra)
```

### Buscar objeto
```python
outra = Service.outra_listar_id(
    obj.get_id_outra()
)
```

### Pegar ID
```python
if outra != None:
    id_outra = outra.get_id()
```

---

## UI COM ASSOCIAÇÃO

```python
objetos = Service.outra_listar()

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
        campo,
        id_outra
    )
```

---

## NOVA CLASSE

### Model
```text
models/novaentidade.py
```

### DAO
```text
models/novaentidadedao.py
```

### Service
```text
service.py
```

### UI
```text
templates/manternovaentidadeui.py
```

### Menu
```text
index.py
```

---

## CHECKLIST

- [ ] Model
- [ ] DAO
- [ ] JSON
- [ ] imports no Service
- [ ] inserir
- [ ] listar
- [ ] listar_id
- [ ] atualizar
- [ ] excluir
- [ ] UI
- [ ] import no index
- [ ] opção no menu
- [ ] associação/IDs
- [ ] filtro
- [ ] ordenação
- [ ] `st.rerun()`

---

# APOSTAS MAIS IMPORTANTES

### 1. Atendimento
`Atendimento` + `AtendimentoDAO` + Service + UI.

### 2. Pagamento
`Pagamento` + `PagamentoDAO` + Service + UI.

### 3. Serviços do atendimento
`AtendimentoServico` com:
```python
id_atendimento
id_servico
```

### 4. Total
```python
total = 0

for x in Service.atendimento_servico_listar_atendimento(id_atendimento):
    servico = Service.servico_listar_id(x.get_id_servico())

    if servico != None:
        total += servico.get_valor()
```

### 5. Atendimento do cliente
```python
horario = Service.horario_listar_id(
    atendimento.get_id_horario()
)

if horario != None \
and horario.get_id_cliente() == id_cliente:
    r.append(atendimento)
```

### 6. Atendimento do profissional
```python
horario = Service.horario_listar_id(
    atendimento.get_id_horario()
)

if horario != None \
and horario.get_id_profissional() == id_profissional:
    r.append(atendimento)
```

---

# Tarefa 11

A Tarefa 11 pede:
- registrar atendimento;
- dados do atendimento;
- serviços realizados;
- totalizar valor;
- cliente visualizar atendimentos;
- cliente efetuar pagamento.

Por isso, essas três partes são as simulações prioritárias:
1. `Atendimento`
2. `AtendimentoServico`
3. `Pagamento`


---

# SIMULAÇÕES EXTRAS

### Cancelar
```python
obj = Service.horario_listar_id(id)

Service.horario_atualizar(
    obj.get_id(),
    obj.get_data(),
    False,
    None,
    None,
    obj.get_id_profissional()
)
```

### Reagendar
```python
Service.horario_atualizar(
    obj.get_id(),
    nova_data,
    False,
    obj.get_id_cliente(),
    obj.get_id_servico(),
    obj.get_id_profissional()
)
```

### Por serviço
```python
if h.get_id_servico() == id_servico:
    r.append(h)
```

### Por profissional + serviço
```python
if h.get_id_profissional() == id_profissional \
and h.get_id_servico() == id_servico:
    r.append(h)
```

### Por período
```python
if h.get_data() >= inicio \
and h.get_data() <= fim:
    r.append(h)
```

### Hoje
```python
if h.get_data().date() == hoje:
    r.append(h)
```

### Mês
```python
if h.get_data().year == ano \
and h.get_data().month == mes:
    r.append(h)
```

### Cliente + confirmação
```python
if h.get_confirmado() == confirmado:
    r.append(h)
```

### Horário livre
```python
if h.get_id_cliente() in [None, 0]:
    r.append(h)
```

### Horário agendado
```python
if h.get_id_cliente() not in [None, 0]:
    r.append(h)
```

### Valor do horário
```python
servico = Service.servico_listar_id(
    h.get_id_servico()
)

valor = servico.get_valor()
```

### Relatório
```python
dic = []

for h in horarios:
    dic.append({
        "data": h.get_data(),
        "campo": valor
    })

st.dataframe(pd.DataFrame(dic))
```

### Ordenar por dois campos
```python
r.sort(
    key = lambda obj : (
        obj.get_campo1(),
        obj.get_campo2()
    )
)
```

### Maior primeiro
```python
r.sort(
    key = lambda obj : obj.get_valor(),
    reverse = True
)
```

### Verificar se existe
```python
if len(lista) > 0:
```

### Primeiro resultado
```python
if len(lista) > 0:
    obj = lista[0]
```

### Quantidade
```python
len(lista)
```

### Total
```python
total = 0

for obj in lista:
    total += obj.get_valor()
```

### Associação
```python
outra = Service.outra_listar_id(
    obj.get_id_outra()
)
```
