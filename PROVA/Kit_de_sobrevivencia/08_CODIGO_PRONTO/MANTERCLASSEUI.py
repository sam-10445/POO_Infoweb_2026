import streamlit as st

from service import Service


class ManterClasseUI:

    @staticmethod
    def main():

        st.title("Cadastro de Classe")

        tab1, tab2, tab3, tab4 = st.tabs(
            ["Listar", "Inserir", "Atualizar", "Excluir"]
        )

        # LISTAR

        with tab1:

            st.subheader("Lista de registros")

            lista = Service.classe_listar()

            for obj in lista:

                st.write(obj)

                # ASSOCIAÇÃO:
                # Se a classe possuir ID de outra classe,
                # você pode buscar o objeto relacionado pelo ID.
                #
                # Exemplo:
                #
                # cliente = Service.cliente_listar_id(
                #     obj.get_id_cliente()
                # )
                #
                # if cliente != None:
                #     st.write("Cliente:", cliente.get_nome())
                #
                # Essas linhas SÓ são necessárias se houver
                # associação entre classes.


        # INSERIR

        with tab2:

            st.subheader("Inserir")

            descricao = st.text_input("Descrição")

            valor = st.number_input(
                "Valor",
                min_value=0.0
            )

            # ASSOCIAÇÃO:
            # Se a classe precisar receber o ID de outra classe,
            # coloque aqui um selectbox para escolher o objeto.
            #
            # Exemplo:
            #
            # clientes = Service.cliente_listar()
            #
            # cliente = st.selectbox(
            #     "Cliente",
            #     clientes,
            #     format_func=lambda x: x.get_nome()
            # )
            #
            # id_cliente = cliente.get_id()
            #
            # O "id_cliente" será enviado para o Service.

            if st.button("Inserir"):

                try:

                    Service.classe_inserir(
                        descricao,
                        valor
                    )

                    st.success("Registro inserido com sucesso!")

                except ValueError as erro:

                    st.error(erro)

        # ATUALIZAR

        with tab3:

            st.subheader("Atualizar")

            id = st.number_input(
                "ID",
                min_value=1,
                step=1
            )

            descricao = st.text_input(
                "Nova descrição"
            )

            valor = st.number_input(
                "Novo valor",
                min_value=0.0
            )

            # ASSOCIAÇÃO:
            # Caso a classe possua uma associação, coloque aqui
            # novamente a escolha da outra classe.
            #
            # Exemplo:
            #
            # clientes = Service.cliente_listar()
            #
            # cliente = st.selectbox(
            #     "Cliente",
            #     clientes,
            #     format_func=lambda x: x.get_nome()
            # )
            #
            # id_cliente = cliente.get_id()
            #

            if st.button("Atualizar"):

                try:

                    Service.classe_atualizar(
                        id,
                        descricao,
                        valor
                    )

                    st.success("Registro atualizado com sucesso!")

                except ValueError as erro:

                    st.error(erro)

        # EXCLUIR

        with tab4:

            st.subheader("Excluir")

            id = st.number_input(
                "ID do registro",
                min_value=1,
                step=1
            )

            if st.button("Excluir"):

                Service.classe_excluir(id)

                st.success("Registro excluído com sucesso!")