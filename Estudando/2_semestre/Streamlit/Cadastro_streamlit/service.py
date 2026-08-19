# OPERAÇÕES

import streamlit as st
from cliente import Cliente


# Lista de clientes
if 'clientes' not in st.session_state:
    st.session_state.clientes = []


def inserir():

    st.subheader('Inserir Cliente')

    id = st.text_input('ID: ', key='id_inserir')
    nome = st.text_input('Nome: ', key='nome_inserir')
    email = st.text_input('E-mail: ', key='email_inserir')
    fone = st.text_input('Telefone: ', key='fone_inserir')

    if st.button('Cadastrar', key='cadastrar'):

        try:
            x = Cliente(id, nome, email, fone)

            for cliente in st.session_state.clientes:
                if cliente.get_id() == id:
                    st.error('Já existe um cliente com esse ID.')
                    return

            st.session_state.clientes.append(x)

            st.success('Cliente cadastrado com sucesso!')

        except ValueError as erro:
            st.error(str(erro))


def listar():

    st.subheader('Lista de Clientes')

    if len(st.session_state.clientes) == 0:

        st.write('Não há clientes cadastrados')

    else:

        for x in st.session_state.clientes:
            st.write(x)


def atualizar():

    st.subheader('Atualizar Cliente')

    id = st.text_input(
        'ID do Cliente a ser atualizado: ',
        key='id_atualizar'
    )

    novo_nome = st.text_input(
        'Novo nome: ',
        key='nome_atualizar'
    )

    novo_email = st.text_input(
        'Novo e-mail: ',
        key='email_atualizar'
    )

    novo_fone = st.text_input(
        'Novo Telefone: ',
        key='fone_atualizar'
    )

    if st.button('Atualizar', key='botao_atualizar'):

        for x in st.session_state.clientes:

            if x.get_id() == id:

                try:
                    x.set_nome(novo_nome)
                    x.set_email(novo_email)
                    x.set_fone(novo_fone)

                    st.success('Cliente atualizado com sucesso!')

                except ValueError as erro:
                    st.error(str(erro))

                return

        st.error('Cliente não encontrado.')


def excluir():

    st.subheader('Excluir Cliente')

    id = st.text_input(
        'ID do Cliente a ser excluído: ',
        key='id_excluir'
    )

    if st.button('Excluir', key='botao_excluir'):

        for x in st.session_state.clientes:

            if x.get_id() == id:

                st.session_state.clientes.remove(x)

                st.success('Cliente excluído com sucesso!')

                return

        st.error('Cliente não encontrado.')
