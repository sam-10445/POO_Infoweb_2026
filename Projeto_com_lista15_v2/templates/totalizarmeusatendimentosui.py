import streamlit as st
import pandas as pd
from datetime import date
from service import Service

class TotalizarMeusAtendimentosUI:
    def main():
        st.header("Totalizar Meus Atendimentos")
        data_inicio = st.date_input("Data inicial", date.today(), key="data_inicio_meus_atendimentos")
        data_fim = st.date_input("Data final", date.today(), key="data_fim_meus_atendimentos")
        if data_inicio > data_fim:
            st.error("A data inicial deve ser anterior à data final")
        else:
            totais = Service.atendimento_totalizar_meus_servicos(st.session_state["usuario_id"], data_inicio, data_fim)
            if len(totais) == 0:
                st.write("Nenhum atendimento realizado nesse período")
            else:
                dados = [{"Serviço": descricao, "Quantidade": total} for descricao, total in totais.items()]
                df = pd.DataFrame(dados).sort_values("Serviço")
                st.dataframe(df, hide_index=True)
                st.subheader("Gráfico de serviços realizados")
                st.bar_chart(df.set_index("Serviço"))
