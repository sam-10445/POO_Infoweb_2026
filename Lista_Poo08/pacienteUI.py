import streamlit as st
from paciente import Paciente
from datetime import date, datetime

class PacienteUI:
    def main():
        st.header('dados do Paciente')
        nome = st.text_input('Nome: ')
        cpf = st.text_input('CPF: ')
        fone = st.text_input('Fone: ')
        nasc = st.text_input('Nascimento: ')
        if st.button('Idade'):
            x = Paciente(nome, cpf, fone, nasc)
            st.write(f"Idade: {x.idade()}")