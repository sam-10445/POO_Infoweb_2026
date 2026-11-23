import streamlit as st
from service import Service
import time
import base64

class AbrirContaUI:
    def main():
        st.header("Abrir Conta no Sistema")
        nome = st.text_input("Informe o nome")
        email = st.text_input("Informe o e-mail")
        fone = st.text_input("Informe o fone")
        senha = st.text_input("Informe a senha", type="password")
        foto = st.file_uploader("Foto do perfil", type=["png", "jpg", "jpeg"])
        if st.button("Inserir"):
            imagem = base64.b64encode(foto.getvalue()).decode("utf-8") if foto else None
            Service.cliente_inserir(nome, email, fone, senha, imagem)
            st.success("Conta criada com sucesso")
            time.sleep(2)
            st.rerun()
            