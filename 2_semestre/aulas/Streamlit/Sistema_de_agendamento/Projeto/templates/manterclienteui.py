import streamlit as st
import pandas as pd #dataframe
import time
from service import Service

class ManterClienteUI:

    def main():
        st.header("Cadastro de Clientes")

        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir","Atualizar", "Excluir"])
        #st.tabs cria uma aba
        with tab1: ManterClienteUI.listar()
        with tab2: ManterClienteUI.inserir()
        with tab3: ManterClienteUI.atualizar()
        with tab4: ManterClienteUI.excluir()

    def listar():
        clientes = Service.cliente_listar()
        if len(clientes) == 0: st.write("Nenhum cliente cadastrado")
        else:
            list_dic = []
            for obj in clientes: list_dic.append(obj.to_json())
            df = pd.DataFrame(list_dic) #passa para o "panda" uma lista de dicionários
            st.dataframe(df) #mostra na forma de tabela o DataFrame

    def inserir():
        #perguntar as informações
        nome = st.text_input("Informe o nome")
        email = st.text_input("Informe o e-mail")
        fone = st.text_input("Informe o fone")

        if st.button("Inserir"):
            #depois de apertar o botão de envio
            Service.cliente_inserir(nome, email, fone) #a classe Service (onde estão as operações) é quem roda as operações, aí vc só passa as informações
            st.success("Cliente inserido com sucesso") #mensagem de sucesso
            time.sleep(2) #mensagem de sucesso fica por 2s
            st.rerun() #o streamlit é atualizado (roda de novo)

    def atualizar():
        clientes = Service.cliente_listar()

        if len(clientes) == 0: st.write("Nenhum cliente cadastrado")

        else:
            op = st.selectbox("Atualização de Clientes", clientes)
            nome = st.text_input("Novo nome", op.get_nome()) #op é o cliente selcionado
            email = st.text_input("Novo e-mail", op.get_email())
            fone = st.text_input("Novo fone", op.get_fone())
            if st.button("Atualizar"):
                id = op.get_id()
                Service.cliente_atualizar(id, nome, email, fone)
                st.success("Cliente atualizado com sucesso") #mostra a mensagem de sucessor
                time.sleep(2) #mensagem de sucesso fica por 2s
                st.rerun() #o streamlit é atualizado (roda de novo)

    def excluir():
        clientes = Service.cliente_listar()
        if len(clientes) == 0: st.write("Nenhum cliente cadastrado")

        else:
            op = st.selectbox("Exclusão de Clientes", clientes)
            if st.button("Excluir"): 
                id = op.get_id()
                Service.cliente_excluir(id)
                st.success("Cliente excluído com sucesso")