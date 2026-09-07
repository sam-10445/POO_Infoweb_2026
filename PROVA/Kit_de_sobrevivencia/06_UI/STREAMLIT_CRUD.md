# STREAMLIT — CRUD

## CABEÇALHO
st.header("Cadastro de Nome")

## ABAS
tab1, tab2, tab3, tab4 = st.tabs(
    ["Listar", "Inserir", "Atualizar", "Excluir"]
)

## CAMPO DE TEXTO
nome = st.text_input("Informe o nome")

## NÚMERO
valor = st.text_input("Informe o valor")
float(valor)

## BOTÃO
if st.button("Inserir"):
    ...

## SELECTBOX
op = st.selectbox(
    "Selecione",
    objetos
)

## Pega o ID
id = op.get_id()

## CHECKBOX
confirmado = st.checkbox("Confirmado")

## DATA
from datetime import datetime

data = st.text_input(
    "Informe a data",
    datetime.now().strftime("%d/%m/%Y %H:%M")
)

**Converter:**
datetime.strptime(
    data,
    "%d/%m/%Y %H:%M"
)

## MENSAGEM
st.success("Operação realizada com sucesso")

## ATUALIZAR A PÁGINA
import time

time.sleep(2)
st.rerun()
