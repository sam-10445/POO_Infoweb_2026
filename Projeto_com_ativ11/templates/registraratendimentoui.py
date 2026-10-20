import streamlit as st
import pandas as pd
import time
from datetime import datetime
from service import Service

class RegistrarAtendimentoUI:
    def main():
        st.header("Registrar Atendimento")

        profissional_id = st.session_state["usuario_id"]
        horarios = []

        for horario in Service.horario_listar():
            if horario.get_id_profissional() == profissional_id \
            and horario.get_id_cliente() not in [None, 0] \
            and horario.get_confirmado() == True \
            and Service.atendimento_ja_registrado(horario.get_id()) == False:
                horarios.append(horario)

        horarios.sort(key = lambda obj : obj.get_data())

        if len(horarios) == 0:
            st.write("Nenhum atendimento disponível para registrar")
            return

        horario = st.selectbox("Informe o horário", horarios)
        cliente = Service.cliente_listar_id(horario.get_id_cliente())

        if cliente != None:
            st.write("Cliente:", cliente.get_nome())

        data = st.text_input(
            "Informe a data do atendimento",
            horario.get_data().strftime("%d/%m/%Y %H:%M")
        )
        queixa = st.text_area("Queixa principal")
        historico = st.text_area("Histórico de saúde")
        avaliacao = st.text_area("Avaliação clínica")
        prescricao = st.text_area("Prescrição de exames e medicamentos")

        servicos = Service.servico_listar()
        if len(servicos) == 0:
            st.write("Nenhum serviço cadastrado")
            return

        if "atendimento_itens" not in st.session_state:
            st.session_state["atendimento_itens"] = []

        servico = st.selectbox("Serviço realizado", servicos)
        qtd = st.number_input("Quantidade", min_value=1, value=1, step=1)

        if st.button("Adicionar serviço"):
            st.session_state["atendimento_itens"].append({
                "id_servico": servico.get_id(),
                "qtd": int(qtd)
            })
            st.rerun()

        itens = st.session_state["atendimento_itens"]

        if len(itens) > 0:
            dados = []
            total = 0

            for item in itens:
                s = Service.servico_listar_id(item["id_servico"])
                subtotal = item["qtd"] * s.get_valor()
                total += subtotal
                dados.append({
                    "serviço": s.get_descricao(),
                    "quantidade": item["qtd"],
                    "valor": s.get_valor(),
                    "subtotal": subtotal
                })

            st.dataframe(pd.DataFrame(dados))
            st.write(f"Total: R$ {total:.2f}")

        if st.button("Registrar Atendimento"):
            if len(itens) == 0:
                st.error("Adicione pelo menos um serviço realizado")
            else:
                try:
                    data_obj = datetime.strptime(data, "%d/%m/%Y %H:%M")
                    Service.atendimento_inserir(
                        data_obj, queixa, historico, avaliacao,
                        prescricao, horario.get_id(), itens
                    )
                    st.session_state["atendimento_itens"] = []
                    st.success("Atendimento registrado com sucesso")
                    time.sleep(2)
                    st.rerun()
                except ValueError:
                    st.error("Informe a data no formato dd/mm/aaaa HH:MM")
