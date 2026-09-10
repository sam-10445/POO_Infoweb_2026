import streamlit as st
import pandas as pd
import time
from service import Service

class ManterDepartamentoUI:
    def main():
        st.header("Cadastro de Departamentos")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterDepartamentoUI.listar()
        with tab2: ManterDepartamentoUI.inserir()
        with tab3: ManterDepartamentoUI.atualizar()
        with tab4: ManterDepartamentoUI.excluir()

    def listar():
        departamentos = Service.departamento_listar()
        if len(departamentos) == 0: st.write("Nenhum departamento cadastrado")
        else:
            list_dic = []
            for obj in departamentos: list_dic.append(obj.to_json())
            df = pd.DataFrame(list_dic)
            st.dataframe(df)

    def inserir():
        nome = st.text_input("Informe o nome")
        diretor = st.text_input("Informe o diretor")
        fone = st.text_input("Informe o fone")
        if st.button("Inserir"):
            Service.departamento_inserir(nome, diretor, fone)
            st.success("departamento inserido com sucesso")
            time.sleep(2)
            st.rerun()

    def atualizar():
        departamentos = Service.departamento_listar()
        if len(departamentos) == 0: st.write("Nenhum departamento cadastrado")
        else:
            op = st.selectbox("Atualização de Departamentos", departamentos)
            nome = st.text_input("Novo nome", op.get_nome())
            diretor = st.text_input("Novo diretor", op.get_diretor())
            fone = st.text_input("Novo fone", op.get_fone())
            if st.button("Atualizar"):
                id = op.get_id()
                Service.departamento_atualizar(id, nome, diretor, fone)
                st.success("Departamento atualizado com sucesso")
                time.sleep(2)
                st.rerun() 

    def excluir():
        departamentos = Service.departamento_listar()
        if len(departamentos) == 0: st.write("Nenhum departamento cadastrado")
        else:
            op = st.selectbox("Exclusão de departamentos", departamentos)
            if st.button("Excluir"):
                id = op.get_id()
                Service.departamento_excluir(id)
                st.success("departamento excluído com sucesso")
                time.sleep(2)
                st.rerun()                  