import streamlit as st
from service import Service
import time

class ListarAgendaClienteUI:
    def main():
        st.header("Agendar Serviço")
        clits = Service.cliente_listar()
        if len(clits) == 0: st.write("Nenhum cliente cadastrado")
        else:
            cliente = st.selectbox("Informe o profissional", clits)
            clientes = Service.listar_agenda_cliente_ui(cliente.get_id())
            if len(clientes) == 0: st.write("Nenhum cliente disponível")
            else:
                cliente = st.selectbox("Informe o horário", clientes)

