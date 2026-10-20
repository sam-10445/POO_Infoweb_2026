import streamlit as st
import time
from service import Service

class PagarAtendimentoUI:
    def main():
        st.header("Pagar Atendimento")

        atendimentos = Service.atendimento_listar_nao_pagos(
            st.session_state["usuario_id"]
        )

        if len(atendimentos) == 0:
            st.write("Nenhum atendimento pendente de pagamento")
            return

        atendimento = st.selectbox("Informe o atendimento", atendimentos)

        st.write("Data:", atendimento.get_data().strftime("%d/%m/%Y %H:%M"))
        st.write(f"Total: R$ {atendimento.get_total():.2f}")

        if st.button("Pagar Atendimento"):
            Service.atendimento_pagar(atendimento.get_id())
            st.success("Atendimento pago com sucesso")
            time.sleep(2)
            st.rerun()
