import streamlit as st
from service import Service
import time
import base64

class PerfilClienteUI:
    def main():
        st.header("Meus Dados")
        op = Service.cliente_listar_id(st.session_state["usuario_id"])
        nome = st.text_input("Informe o novo nome", op.get_nome())
        email = st.text_input("Informe o novo e-mail", op.get_email())
        fone = st.text_input("Informe o novo fone", op.get_fone())
        senha = st.text_input("Informe a nova senha", op.get_senha(), type="password")
        if op.get_foto(): st.image(base64.b64decode(op.get_foto()), width=150)
        foto = st.file_uploader("Alterar foto do perfil", type=["png", "jpg", "jpeg"])
        if st.button("Atualizar"):
            id = op.get_id()
            imagem = base64.b64encode(foto.getvalue()).decode("utf-8") if foto else op.get_foto()
            Service.cliente_atualizar(id, nome, email, fone, senha, imagem)
            st.success("Cliente atualizado com sucesso")
            time.sleep(2)
            st.rerun()
                        