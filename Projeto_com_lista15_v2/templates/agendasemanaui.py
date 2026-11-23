import streamlit as st
import pandas as pd
from service import Service

class AgendaSemanaUI:
    def main():
        st.header("Agenda da Semana")
        horarios = Service.horario_agenda_semana()
        if len(horarios) == 0:
            st.write("Nenhum horário agendado para os próximos sete dias")
        else:
            dados = []
            for horario in horarios:
                cliente = Service.cliente_listar_id(horario.get_id_cliente())
                servico = Service.servico_listar_id(horario.get_id_servico())
                profissional = Service.profissional_listar_id(horario.get_id_profissional())
                dados.append({
                    "id": horario.get_id(),
                    "data": horario.get_data().strftime("%d/%m/%Y"),
                    "hora": horario.get_data().strftime("%H:%M"),
                    "cliente": cliente.get_nome() if cliente else "",
                    "serviço": servico.get_descricao() if servico else "",
                    "profissional": profissional.get_nome() if profissional else ""
                })
            df = pd.DataFrame(dados)
            st.dataframe(df, hide_index=True)
