import streamlit as st
import pandas as pd #dataframe
import time
from service import Service

class ManterServicoUI:

    def main():
        st.header("Cadastro de Serviços")

        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir","Atualizar", "Excluir"])
        #st.tabs cria uma aba
        with tab1: ManterServicoUI.listar()
        with tab2: ManterServicoUI.inserir()
        with tab3: ManterServicoUI.atualizar()
        with tab4: ManterServicoUI.excluir()

    def listar():
        servicos = Service.servico_listar()
        if len(servicos) == 0: st.write("Nenhum serviço cadastrado")
        else:
            list_dic = []
            for obj in servicos: list_dic.append(obj.to_json())
            df = pd.DataFrame(list_dic) #passa para o "panda" uma lista de dicionários
            st.dataframe(df) #mostra na forma de tabela o DataFrame

    def inserir():
        #perguntar as informações
        nome = st.text_input("Informe o nome")
        email = st.text_input("Informe o e-mail")
        fone = st.text_input("Informe o fone")

        if st.button("Inserir"):
            #depois de apertar o botão de envio
            Service.servico_inserir(nome, email, fone) #a classe Service (onde estão as operações) é quem roda as operações, aí vc só passa as informações
            st.success("Serviço inserido com sucesso") #mensagem de sucesso
            time.sleep(2) #mensagem de sucesso fica por 2s
            st.rerun() #o streamlit é atualizado (roda de novo)

    def atualizar():
        servicos = Service.servico_listar()

        if len(servicos) == 0: st.write("Nenhum serviço cadastrado")

        else:
            op = st.selectbox("Atualização de Serviços", servicos)
            nome = st.text_input("Novo nome", op.get_nome()) #op é o serviço selecionado
            email = st.text_input("Novo e-mail", op.get_email())
            fone = st.text_input("Novo fone", op.get_fone())
            if st.button("Atualizar"):
                id = op.get_id()
                Service.servico_atualizar(id, nome, email, fone)
                st.success("Serviço atualizado com sucesso") #mostra a mensagem de sucessor
                time.sleep(2) #mensagem de sucesso fica por 2s
                st.rerun() #o streamlit é atualizado (roda de novo)

    def excluir():
        servicos = Service.servico_listar()
        if len(servicos) == 0: st.write("Nenhum serviço cadastrado")

        else:
            op = st.selectbox("Exclusão de Serviços", servicos)
            if st.button("Excluir"): 
                id = op.get_id()
                Service.servico_excluir(id)
                st.success("Serviço excluído com sucesso")