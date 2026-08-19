#INTERFACE COM O USUÁRIO

import streamlit as st
from datetime import datetime

from cliente import Cliente #chamar a classe

class ClienteUI:
    def main():
        st.header('Cadastro de Clientes')

        st.write('''
[1] - Inserir 
[2] - Listar 
[3] - Atualizar
[4] - Excluir
[0] - SAIR
''')
        op = st.text_input('Opção: ')

        if st.button('OK'):
            if op == 1: 
            if op == 2:
            if op == 3:
            if op == 4: 