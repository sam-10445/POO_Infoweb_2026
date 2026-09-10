import streamlit as st
import pandas as pd
import time
from service import Service

class ManterServicoUI:
    def main():
        st.header("Cadastro de Serviços")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterServicoUI.listar()
        with tab2: ManterServicoUI.inserir()
        with tab3: ManterServicoUI.atualizar()
        with tab4: ManterServicoUI.excluir()

    def listar():
        servicos = Service.servico_listar()
        if len(servicos) == 0: st.write("Nenhum serviço cadastrado")
        else:
            dic = []
            for obj in servicos: 
                departamento = Service.departamento_listar_id(obj.get_id_departamento())
                if departamento != None: departamento = departamento.get_nome()
                dic.append({"id" : obj.get_id(), "descricao" : obj.get_descricao(),
                "valor" : obj.get_valor()})
            df = pd.DataFrame(dic)
            st.dataframe(df)

    def inserir():
        descr = st.text_input("Informe a descrição")
        valor = st.text_input("Informe o valor")
        departamentos = Service.departamento_listar()
        departamento = st.selectbox("Informe o departamento", departamentos, index = None)
        if st.button("Inserir"):
            id_departamento = None
            if departamento != None: id_departamento = departamento.get_id()
            Service.servico_inserir(descr, float(valor), id_departamento)
            st.success("Serviço inserido com sucesso")
            time.sleep(2)
            st.rerun()

    def atualizar():
        servicos = Service.servico_listar()
        if len(servicos) == 0: st.write("Nenhum serviço cadastrado")
        else:
            departamentos = Service.departamento_listar()
            op = st.selectbox("Atualização de Serviços", servicos)
            descr = st.text_input("Informe a nova descrição", op.get_descricao())
            valor = st.text_input("Informe o novo valor", str(op.get_valor()))
            id_departamento = None if op.get_id_departamento() in [0, None] else op.get_id_departamento()
            departamento = st.selectbox("Informe o novo departamento", departamentos, next((i for i, c in enumerate(departamentos) if c.get_id() == id_departamento), None))
            if st.button("Atualizar"):
                id = op.get_id()
                id_departamento = None
                if departamento != None: id_departamento = departamento.get_id()
                Service.servico_atualizar(id, descr, float(valor), id_departamento)
                st.success("Serviço atualizado com sucesso")
                time.sleep(2)
                st.rerun()
                
    def excluir():
        servicos = Service.servico_listar()
        if len(servicos) == 0: st.write("Nenhum serviço cadastrado")
        else:
            op = st.selectbox("Exclusão de Serviços", servicos)
            if st.button("Excluir"):
                id = op.get_id()
                Service.servico_excluir(id)
                st.success("Serviço excluído com sucesso")
                time.sleep(2)
                st.rerun()