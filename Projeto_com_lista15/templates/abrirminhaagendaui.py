import streamlit as st
from service import Service
from datetime import datetime
import time

class AbrirMinhaAgendaUI:
    def main():
        st.header("Abrir Minha Agenda")
        data = st.text_input("Informe a data no formato dd/mm/aaaa", datetime.now().strftime("%d/%m/%Y"))
        hora_inicio = st.text_input("Informe o horário inicial no formato HH:MM")
        hora_fim = st.text_input("Informe o horário final no formato HH:MM")
        intervalo = st.text_input("Informe o intervalo entre os horários (min)")
        if st.button("Abrir Agenda"):
            Service.horario_abrir_agenda(data, hora_inicio, hora_fim, int(intervalo), st.session_state["usuario_id"])
            st.success("Horários cadastrados com sucesso")
            time.sleep(2)
            st.rerun()
