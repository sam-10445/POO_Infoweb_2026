# SOLUÇÃO — LISTAGEM ESPECIAL

## Service

Adicionar:

```python
@staticmethod
def horario_listar_confirmados():

    horarios = HorarioDAO().listar()

    resultado = []

    for horario in horarios:

        if horario.get_confirmado():
            resultado.append(horario)

    return resultado
```
## UI

### Criar um método:

def listar_confirmados():

    horarios = Service.horario_listar_confirmados()

    if len(horarios) == 0:

        st.write("Nenhum horário confirmado")

    else:

        lista = []

        for obj in horarios:

            lista.append(obj.to_json())

        df = pd.DataFrame(lista)

        st.dataframe(df)

Depois chamar esse método na interface.


---

