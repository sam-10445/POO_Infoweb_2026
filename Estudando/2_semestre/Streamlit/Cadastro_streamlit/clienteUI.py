import streamlit as st
import service

class ClienteUI:

    @staticmethod
    def main():
        st.header('Cadastro de Clientes')

        if 'opcao' not in st.session_state:
            st.session_state.opcao = None

        st.write('[1] - Inserir')
        st.write('[2] - Listar')
        st.write('[3] - Atualizar')
        st.write('[4] - Excluir')
        st.write('[0] - SAIR')

        resp = st.text_input('Opção:', key='opcao_menu')

        if st.button('OK', key='ok'):

            if resp in ['0', '1', '2', '3', '4']:
                st.session_state.opcao = resp
                st.rerun()
            else:
                st.warning('Opção inválida.')

        if st.session_state.opcao == '1':service.inserir()
        elif st.session_state.opcao == '2':service.listar()
        elif st.session_state.opcao == '3':service.atualizar()
        elif st.session_state.opcao == '4':service.excluir()
        elif st.session_state.opcao == '0':st.write('Saindo...')
