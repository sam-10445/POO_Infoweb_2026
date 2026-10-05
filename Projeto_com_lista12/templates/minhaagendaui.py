import streamlit as st
import pandas as pd
from service import Service

class MinhaAgendaUI:
    def main():
        st.header("Minha Agenda")

        # Busca somente os horários do profissional que está logado.
        horarios = Service.horario_listar_profissional(
            st.session_state["usuario_id"]
        )

        if len(horarios) == 0:
            st.write("Nenhum horário cadastrado")

        else:
            dic = []

            for obj in horarios:
                cliente = Service.cliente_listar_id(
                    obj.get_id_cliente()
                )

                servico = Service.servico_listar_id(
                    obj.get_id_servico()
                )

                if cliente != None:
                    cliente = cliente.get_nome()

                if servico != None:
                    servico = servico.get_descricao()

                dic.append({
                    "id": obj.get_id(),
                    "data": obj.get_data(),
                    "confirmado": obj.get_confirmado(),
                    "cliente": cliente,
                    "serviço": servico
                })

            df = pd.DataFrame(dic)

            st.dataframe(df)