import streamlit as st
import pandas as pd
from datetime import date
from service import Service

class TotalizarAtendimentosProfissionaisUI:
    def main():
        st.header("Totalizar Atendimentos dos Profissionais")
        data_inicio = st.date_input("Data inicial", date.today(), key="data_inicio_profissionais")
        data_fim = st.date_input("Data final", date.today(), key="data_fim_profissionais")
        if data_inicio > data_fim:
            st.error("A data inicial deve ser anterior à data final")
        else:
            totais = Service.atendimento_totalizar_profissionais(data_inicio, data_fim)
            if len(totais) == 0:
                st.write("Nenhum atendimento realizado nesse período")
            else:
                dados = [{"Profissional": nome, "Total de atendimentos": total} for nome, total in totais.items()]
                df = pd.DataFrame(dados).sort_values("Profissional")
                st.dataframe(df, hide_index=True)
                st.subheader("Gráfico de atendimentos")
                st.bar_chart(df.set_index("Profissional"))
