import streamlit as st
import pandas as pd
import time
import base64
from service import Service

class ManterProfissionalUI:
    def main():
        st.header("Cadastro de Profissionais")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterProfissionalUI.listar()
        with tab2: ManterProfissionalUI.inserir()
        with tab3: ManterProfissionalUI.atualizar()
        with tab4: ManterProfissionalUI.excluir()

    def listar():
        profissionais = Service.profissional_listar()
        if len(profissionais) == 0: st.write("Nenhum profissional cadastrado")
        else:
            list_dic = []
            for obj in profissionais: list_dic.append(obj.to_dict())
            df = pd.DataFrame(list_dic)
            st.dataframe(df)

    def inserir():
        nome = st.text_input("Informe o nome")
        email = st.text_input("Informe o e-mail")
        especialidade = st.text_input("Informe a especialidade")
        senha = st.text_input("Informe a senha", type="password")
        foto = st.file_uploader("Foto do profissional", type=["png", "jpg", "jpeg"])
        if st.button("Inserir"):
            imagem = base64.b64encode(foto.getvalue()).decode("utf-8") if foto else None
            Service.profissional_inserir(nome, email, especialidade, senha, imagem)
            st.success("Profissional inserido com sucesso")
            time.sleep(2)
            st.rerun()

    def atualizar():
        profissionais = Service.profissional_listar()
        if len(profissionais) == 0: st.write("Nenhum profissional cadastrado")
        else:
            op = st.selectbox("Atualização de Profissionais", profissionais)
            nome = st.text_input("Informe o novo nome", op.get_nome())
            email = st.text_input("Informe o novo email", op.get_email())
            especialidade = st.text_input("Informe a nova especialidade", op.get_especialidade())
            senha = st.text_input("Nova senha", op.get_senha(), type="password")
            if op.get_foto(): st.image(base64.b64decode(op.get_foto()), width=150)
            foto = st.file_uploader("Nova foto do profissional", type=["png", "jpg", "jpeg"])

            if st.button("Atualizar"):
                id = op.get_id()
                imagem = base64.b64encode(foto.getvalue()).decode("utf-8") if foto else op.get_foto()
                Service.profissional_atualizar(id, nome, email, especialidade, senha, imagem)
                st.success("Profissional atualizado com sucesso")
                time.sleep(2)
                st.rerun()

    def excluir():
        profissionais = Service.profissional_listar()
        if len(profissionais) == 0: st.write("Nenhum profissional cadastrado")
        else:
            op = st.selectbox("Exclusão de Profissionais", profissionais)
            if st.button("Excluir"):
                id = op.get_id()
                Service.profissional_excluir(id)
                st.success("Profissional excluído com sucesso")
                time.sleep(2)
                st.rerun()