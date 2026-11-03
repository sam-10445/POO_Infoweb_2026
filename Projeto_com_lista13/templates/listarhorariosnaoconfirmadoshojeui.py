import streamlit as st
import pandas as pd
from service import Service


class ListarHorariosNaoConfirmadosHojeUI:
    def main():
        st.header("Horários Não Confirmados de Hoje")

        horarios = Service.horario_listar_nao_confirmados_hoje()

        if len(horarios) == 0:
            st.info("Não há horários agendados por clientes aguardando confirmação hoje.")
            return

        dados = []

        for obj in horarios:
            cliente = Service.cliente_listar_id(obj.get_id_cliente())
            servico = Service.servico_listar_id(obj.get_id_servico())
            profissional = Service.profissional_listar_id(
                obj.get_id_profissional()
            )

            dados.append({
                "id": obj.get_id(),
                "data e hora": obj.get_data().strftime("%d/%m/%Y %H:%M"),
                "cliente": cliente.get_nome() if cliente is not None else "Não encontrado",
                "serviço": servico.get_descricao() if servico is not None else "Não encontrado",
                "profissional": profissional.get_nome() if profissional is not None else "Não encontrado"
            })

        st.dataframe(pd.DataFrame(dados))
