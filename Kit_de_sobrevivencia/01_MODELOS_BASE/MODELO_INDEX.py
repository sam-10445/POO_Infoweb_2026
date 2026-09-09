# ============================================================
# MODELO PARA ALTERAR O INDEX
# ============================================================
#
# Quando criar uma nova UI:
#
# 1. Faça o import no começo.
# 2. Coloque o nome no selectbox.
# 3. Crie o if correspondente.
# ============================================================

from templates.manternomedaclasseui import ManterNomeDaClasseUI

import streamlit as st


class IndexUI:

    def main():

        op = st.sidebar.selectbox(
            "Menu",
            [
                "Clientes",
                "Serviços",
                "Horários",
                "NomeDaClasse"
            ]
        )

        if op == "Clientes":
            ManterClienteUI.main()

        if op == "Serviços":
            ManterServicoUI.main()

        if op == "Horários":
            ManterHorarioUI.main()

        # NOVA OPÇÃO
        if op == "NomeDaClasse":
            ManterNomeDaClasseUI.main()


IndexUI.main()