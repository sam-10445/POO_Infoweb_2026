# Estudo 18/08/2026 - Tentando fazer o cadastro de um cliente com Streamlit
# ! FRACASSO ! - NÃO CONSEGUIR FAZER O PROGRAMA RODAR (Usei o Chat GPT)

# Coisas que aprendir:
# Quando se chega a comandos de entrada usando Streamlit, o Streamlit roda o código todo de novo
# Não dá pra usar @classmethod, sem NO MESMO ARQUIVO ter uma classe
# Não dá pra criar uma lista de clientes normalmente como antes usando o Streamlit, você tem que usar:
#  if 'clientes' not in st.session_state:
#      st.session_state.clientes = [] (???????)

#EXECUÇÃO DO PROGRAMA
import streamlit as st
from clienteUI import ClienteUI #Chamar a UI 

ClienteUI.main()