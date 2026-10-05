import streamlit as st
import pandas as pd
from service import Service

class MeusServicosUI:
    def main():
        st.header("Meus Serviços")

        # Busca somente os horários pertencentes ao cliente logado.
        horarios = Service.horario_listar_cliente(
            st.session_state["usuario_id"]
        )

        if len(horarios) == 0:
            st.write("Nenhum serviço agendado")

        else:
            dic = []

            for obj in horarios:
                profissional = Service.profissional_listar_id(
                    obj.get_id_profissional()
                )

                servico = Service.servico_listar_id(
                    obj.get_id_servico()
                )

                if profissional != None:
                    profissional = profissional.get_nome()

                if servico != None:
                    servico = servico.get_descricao()

                dic.append({
                    "id": obj.get_id(),
                    "data": obj.get_data(),
                    "confirmado": obj.get_confirmado(),
                    "serviço": servico,
                    "profissional": profissional
                })

            df = pd.DataFrame(dic)

            st.dataframe(df)