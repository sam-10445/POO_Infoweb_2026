import streamlit as st
from datetime import datetime

from paciente import Paciente #chamar a classe

class PacienteUI:
    def main():
        st.header('Dados do Paciente')

        nome = st.text_input('Nome: ')
        cpf = st.text_input('CPF: ')
        fone = st.text_input('Telefone: ')
        nasc = st.text_input('Data de nascimento: ') 
        # a data de nascimento será registrada como string, mas vamos converter depois para fazer o cálculo como data

        if st.button('Idade'):
            nasc = datetime.strptime(nasc, '%d/%m/%Y') #lembre-se de converter o texto para datetime
            x = Paciente(nome, cpf, fone, nasc)
            st.write(f"Idade: {x.idade()}")