import streamlit as st
import pandas as pd
from service import Service


class ListarAgendaClienteUI:
    def main():
        st.header("Listar Agenda do Cliente")

        clientes = Service.cliente_listar()

        if len(clientes) == 0:
            st.info("Nenhum cliente cadastrado.")
            return

        cliente = st.selectbox(
            "Selecione o cliente",
            clientes,
            format_func=lambda c: f"{c.get_nome()} (ID {c.get_id()})"
        )

        horarios = Service.horario_listar_cliente(cliente.get_id())

        if len(horarios) == 0:
            st.info(f"Nenhum horário cadastrado para {cliente.get_nome()}.")
            return

        dados = []

        for obj in horarios:
            profissional = Service.profissional_listar_id(
                obj.get_id_profissional()
            )
            servico = Service.servico_listar_id(obj.get_id_servico())

            dados.append({
                "id": obj.get_id(),
                "data e hora": obj.get_data().strftime("%d/%m/%Y %H:%M"),
                "profissional": profissional.get_nome() if profissional is not None else "Não encontrado",
                "serviço": servico.get_descricao() if servico is not None else "Não encontrado"
            })

        # Service.horario_listar_cliente já ordena pela data crescente.
        st.dataframe(pd.DataFrame(dados))
