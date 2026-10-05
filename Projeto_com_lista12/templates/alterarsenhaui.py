import streamlit as st
import time
from service import Service

class AlterarSenhaUI:
    def main():
        st.header("Alterar Senha")

        nova_senha = st.text_input(
            "Informe a nova senha",
            type="password"
        )

        confirmar_senha = st.text_input(
            "Confirme a nova senha",
            type="password"
        )

        if st.button("Alterar Senha"):

            if nova_senha == "":
                st.error("Informe a nova senha")

            elif nova_senha != confirmar_senha:
                st.error("As senhas não conferem")

            else:
                # Somente a senha é alterada.
                # O e-mail do admin permanece o mesmo.
                Service.cliente_alterar_senha(
                    st.session_state["usuario_id"],
                    nova_senha
                )

                st.success("Senha alterada com sucesso")

                time.sleep(2)

                st.rerun()