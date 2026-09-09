# ============================================================
# MODELO DE UI
# ============================================================
#
# Modelo baseado nas interfaces do Projeto.
#
# USE quando precisar criar uma nova página de cadastro.
# ============================================================

import streamlit as st
import pandas as pd
import time
from service import Service


class ManterNomeDaClasseUI:

    def main():

        st.header("Cadastro de NomeDaClasse")

        tab1, tab2, tab3, tab4 = st.tabs(
            ["Listar", "Inserir", "Atualizar", "Excluir"]
        )

        with tab1:
            ManterNomeDaClasseUI.listar()

        with tab2:
            ManterNomeDaClasseUI.inserir()

        with tab3:
            ManterNomeDaClasseUI.atualizar()

        with tab4:
            ManterNomeDaClasseUI.excluir()

    # ========================================================
    # LISTAR
    # ========================================================

    def listar():

        objetos = Service.nomedaclasse_listar()

        if len(objetos) == 0:

            st.write("Nenhum objeto cadastrado")

        else:

            lista = []

            for obj in objetos:

                lista.append(obj.to_json())

            df = pd.DataFrame(lista)

            st.dataframe(df)

    # ========================================================
    # INSERIR
    # ========================================================

    def inserir():

        atributo1 = st.text_input("Informe o atributo 1")

        atributo2 = st.text_input("Informe o atributo 2")

        atributo3 = st.text_input("Informe o atributo 3")

        if st.button("Inserir"):

            Service.nomedaclasse_inserir(
                atributo1,
                atributo2,
                atributo3
            )

            st.success("Objeto inserido com sucesso")

            time.sleep(2)

            st.rerun()

    # ========================================================
    # ATUALIZAR
    # ========================================================

    def atualizar():

        objetos = Service.nomedaclasse_listar()

        if len(objetos) == 0:

            st.write("Nenhum objeto cadastrado")

        else:

            op = st.selectbox(
                "Atualização",
                objetos
            )

            atributo1 = st.text_input(
                "Novo atributo 1",
                op.get_atributo1()
            )

            atributo2 = st.text_input(
                "Novo atributo 2",
                op.get_atributo2()
            )

            atributo3 = st.text_input(
                "Novo atributo 3",
                op.get_atributo3()
            )

            if st.button("Atualizar"):

                id = op.get_id()

                Service.nomedaclasse_atualizar(
                    id,
                    atributo1,
                    atributo2,
                    atributo3
                )

                st.success("Objeto atualizado com sucesso")

                time.sleep(2)

                st.rerun()

    # ========================================================
    # EXCLUIR
    # ========================================================

    def excluir():

        objetos = Service.nomedaclasse_listar()

        if len(objetos) == 0:

            st.write("Nenhum objeto cadastrado")

        else:

            op = st.selectbox(
                "Exclusão",
                objetos
            )

            if st.button("Excluir"):

                Service.nomedaclasse_excluir(
                    op.get_id()
                )

                st.success("Objeto excluído com sucesso")

                time.sleep(2)

                st.rerun()