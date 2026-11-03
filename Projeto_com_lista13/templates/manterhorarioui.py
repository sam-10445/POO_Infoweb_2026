import streamlit as st
import pandas as pd
from service import Service
import time
from datetime import datetime

class ManterHorarioUI:
    def main():
        st.header("Cadastro de Horários")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterHorarioUI.listar()
        with tab2: ManterHorarioUI.inserir()
        with tab3: ManterHorarioUI.atualizar()
        with tab4: ManterHorarioUI.excluir()

    def listar():
        horarios = Service.horario_listar()
        if len(horarios) == 0: st.write("Nenhum horário cadastrado")
        else:
            dic = []
            for obj in horarios:
                cliente = Service.cliente_listar_id(obj.get_id_cliente()) if obj.get_id_cliente() not in [None, 0] else None
                servico = Service.servico_listar_id(obj.get_id_servico()) if obj.get_id_servico() not in [None, 0] else None
                profissional = Service.profissional_listar_id(obj.get_id_profissional()) if obj.get_id_profissional() not in [None, 0] else None
                if cliente is not None: cliente = cliente.get_nome()
                if servico is not None: servico = servico.get_descricao()
                if profissional is not None: profissional = profissional.get_nome()
                dic.append({"id": obj.get_id(), "data": obj.get_data(), "confirmado": obj.get_confirmado(), "cliente": cliente, "serviço": servico, "profissional": profissional})
            df = pd.DataFrame(dic)
            st.dataframe(df)

    def inserir():
        clientes = Service.cliente_listar()
        servicos = Service.servico_listar()
        profissionais = Service.profissional_listar()
        data = st.text_input("Informe a data e horário do serviço", datetime.now().strftime("%d/%m/%Y %H:%M"))
        confirmado = st.checkbox("Confirmado")
        cliente = st.selectbox("Informe o cliente", clientes, index=None)
        servico = st.selectbox("Informe o serviço", servicos, index=None)
        profissional = st.selectbox("Informe o profissional", profissionais, index=None)
        if st.button("Inserir"):
            try:
                id_cliente = cliente.get_id() if cliente is not None else None
                id_servico = servico.get_id() if servico is not None else None
                id_profissional = profissional.get_id() if profissional is not None else None
                Service.horario_inserir(datetime.strptime(data, "%d/%m/%Y %H:%M"), confirmado, id_cliente, id_servico, id_profissional)
                st.success("Horário inserido com sucesso")
                time.sleep(2)
                st.rerun()
            except ValueError as erro:
                st.error(str(erro))

    def atualizar():
        horarios = Service.horario_listar()
        if len(horarios) == 0: st.write("Nenhum horário cadastrado")
        else:
            clientes = Service.cliente_listar()
            servicos = Service.servico_listar()
            profissionais = Service.profissional_listar()
            op = st.selectbox("Atualização de Horários", horarios)
            data = st.text_input("Informe a nova data e horário do serviço", op.get_data().strftime("%d/%m/%Y %H:%M"))
            confirmado = st.checkbox("Nova confirmação", op.get_confirmado())
            id_cliente_atual = None if op.get_id_cliente() in [0, None] else op.get_id_cliente()
            id_servico_atual = None if op.get_id_servico() in [0, None] else op.get_id_servico()
            id_profissional_atual = None if op.get_id_profissional() in [0, None] else op.get_id_profissional()
            indice_cliente = next((i for i, c in enumerate(clientes) if c.get_id() == id_cliente_atual), None)
            indice_servico = next((i for i, s in enumerate(servicos) if s.get_id() == id_servico_atual), None)
            indice_profissional = next((i for i, p in enumerate(profissionais) if p.get_id() == id_profissional_atual), None)
            cliente = st.selectbox("Informe o novo cliente", clientes, index=indice_cliente)
            servico = st.selectbox("Informe o novo serviço", servicos, index=indice_servico)
            profissional = st.selectbox("Informe o novo profissional", profissionais, index=indice_profissional)
            if st.button("Atualizar"):
                try:
                    id_cliente = cliente.get_id() if cliente is not None else None
                    id_servico = servico.get_id() if servico is not None else None
                    id_profissional = profissional.get_id() if profissional is not None else None
                    Service.horario_atualizar(op.get_id(), datetime.strptime(data, "%d/%m/%Y %H:%M"), confirmado, id_cliente, id_servico, id_profissional)
                    st.success("Horário atualizado com sucesso")
                    time.sleep(2)
                    st.rerun()
                except ValueError as erro:
                    st.error(str(erro))

    def excluir():
        horarios = Service.horario_listar()
        if len(horarios) == 0: st.write("Nenhum horário cadastrado")
        else:
            op = st.selectbox("Exclusão de Horários", horarios)
            if st.button("Excluir"):
                try:
                    Service.horario_excluir(op.get_id())
                    st.success("Horário excluído com sucesso")
                    time.sleep(2)
                    st.rerun()
                except ValueError as erro:
                    st.error(str(erro))
