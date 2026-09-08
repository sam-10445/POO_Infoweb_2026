import streamlit as st
import pandas as pd
from service import Service
import time
from datetime import datetime

class ManterAtendimentoUI:
    def main():
        st.header("Cadastro de Atendimentos")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterAtendimentoUI.listar()
        with tab2: ManterAtendimentoUI.inserir()
        with tab3: ManterAtendimentoUI.atualizar()
        with tab4: ManterAtendimentoUI.excluir()

    def listar():
        atendimentos = Service.atendimento_listar()
        if len(atendimentos) == 0: st.write("Nenhum atendimento cadastrado")
        else:
            dic = []
            for obj in atendimentos:
                horario = Service.horario_listar_id(obj.get_id_horario()) #pega o id do horário
                if horario != None: horario = horario.get_nome()
                dic.append({"id" : obj.get_id(), "data" : obj.get_data(),
                "queixa" : obj.get_queixa_principal(), "historico" : obj.get_historico_saude(), 
                "avaliacao" : obj.get_avaliacao(), "prescricao" : obj.get_prescricao(), 
                "horario" : horario})

            df = pd.DataFrame(dic)
            st.dataframe(df)

    def inserir():
        horarios = Service.horario_listar()
        data = st.text_input("Informe a data e horário do serviço", datetime.now().strftime("%d/%m/%Y %H:%M"))
        horario = st.selectbox("Informe o horario", horarios, index = None)
        if st.button("Inserir"):
            id_horario = None
            if horario != None: id_horario = horario.get_id()
            Service.atendimento_inserir(datetime.strptime(data, "%d/%m/%Y %H:%M"), id_horario)
            st.success("Atendimento inserido com sucesso")
            time.sleep(2)
            st.rerun()

    def atualizar():
        atendimentos = Service.atendimento_listar()
        if len(atendimentos) == 0: st.write("Nenhum atendimento cadastrado")
        else:
            horarios = Service.horario_listar()
            op = st.selectbox("Atualização de Atendimentos", atendimentos)
            data = st.text_input("Informe a nova data e horário do serviço", op.get_data().strftime("%d/%m/%Y %H:%M"))
            id_horario = None if op.get_id_horario() in [0, None] else op.get_id_horario()
            horario = st.selectbox("Informe o novo horário", horarios, next((i for i, c in enumerate(horarios) if c.get_id() == id_horario), None))
            if st.button("Atualizar"):
                id_horario = None
                if horario != None: id_horario = horario.get_id()
                Service.atendimento_atualizar(op.get_id(), datetime.strptime(data, "%d/%m/%Y %H:%M"), id_horario)
                st.success("Atendimento atualizado com sucesso")
                time.sleep(2)
                st.rerun()

    def excluir():
        atendimentos = Service.atendimento_listar()
        if len(atendimentos) == 0: st.write("Nenhum atendimento cadastrado")
        else:
            op = st.selectbox("Exclusão de Horários", atendimentos)
            if st.button("Excluir"):
                Service.atendimento_excluir(op.get_id())
                st.success("Atendimento excluído com sucesso")
                time.sleep(2)
                st.rerun()