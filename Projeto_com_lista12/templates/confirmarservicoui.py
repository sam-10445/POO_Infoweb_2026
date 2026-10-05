import streamlit as st
import time
from service import Service

class ConfirmarServicoUI:
    def main():
        st.header("Confirmar Serviço")

        # Aqui aparecem somente os serviços que:
        # 1. pertencem ao profissional logado;
        # 2. já possuem cliente;
        # 3. ainda não foram confirmados.
        horarios = Service.horario_listar_agendados(
            st.session_state["usuario_id"]
        )

        if len(horarios) == 0:
            st.write("Nenhum serviço para confirmar")

        else:
            horario = st.selectbox(
                "Informe o horário",
                horarios
            )

            cliente = Service.cliente_listar_id(
                horario.get_id_cliente()
            )

            if cliente != None:
                st.selectbox(
                    "Cliente",
                    [cliente]
                )

            if st.button("Confirmar"):

                # Mantém todos os dados do horário e altera
                # somente o valor de confirmado para True.
                Service.horario_atualizar(
                    horario.get_id(),
                    horario.get_data(),
                    True,
                    horario.get_id_cliente(),
                    horario.get_id_servico(),
                    horario.get_id_profissional()
                )

                st.success("Serviço confirmado com sucesso")

                time.sleep(2)

                st.rerun()