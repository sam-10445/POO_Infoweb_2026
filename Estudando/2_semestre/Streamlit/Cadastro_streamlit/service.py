# OPERAÇÕES
# OB: tem que fazer um while também em algum lugar para ficar fazendo o loop

import streamlit as st
from cliente import Cliente #chamar a classe

__clientes = []

def inserir(cls):
    id = st.text_input('ID: ')
    nome = st.text_input('Nome: ')
    email = st.text_input('E-mail: ')
    nasc = st.text_input('Data de nascimento: ')
    x = Cliente(id, nome, email, nasc)
    cls.clientes.append(x)

def listar(cls):
    if len(cls.__clientes) == 0:
        st.write('Não há clientes cadastrados')
    else:
        for x in cls.__clientes: st.write(x)
