import streamlit as st
import pandas as pd
from service import Service

class ListarHorariosNaoConfirmadosHojeUI:
    def main():
        st.header("Horários Não Confirmados Hoje")
        horarios = Service.listar_horarios_nao_confirmados_hoje()
        if len(horarios) == 0: st.write("Nenhum horário não confirmado encontrado")
        else:
            dic = []
            for obj in horarios:
                cliente = Service.cliente_listar_id(obj.get_id_cliente())
                servico = Service.servico_listar_id(obj.get_id_servico())
                profissional = Service.profissional_listar_id(obj.get_id_profissional())

                if cliente != None: cliente = cliente.get_nome()
                if servico != None: servico = servico.get_descricao()
                if profissional != None: profissional = profissional.get_nome()

                dic.append({"id" : obj.get_id(), "data" : obj.get_confirmado(),
                "confirmado" : obj.get_confirmado(), "cliente" : cliente,
                "serviço" : servico, "profissional" : profissional})
            df = pd.DataFrame(dic) 
            st.dataframe(df)
