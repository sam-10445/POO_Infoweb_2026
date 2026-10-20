from Prova.Projeto_com_lista12.templates.manterclienteui import ManterClienteUI
from Prova.Projeto_com_lista12.templates.manterservicoui import ManterServicoUI
from Prova.Projeto_com_lista12.templates.manterhorarioui import ManterHorarioUI
from Prova.Projeto_com_lista12.templates.manterprofissionalui import ManterProfissionalUI
from Prova.Projeto_com_lista12.templates.abrircontaui import AbrirContaUI
from Prova.Projeto_com_lista12.templates.loginui import LoginUI
from Prova.Projeto_com_lista12.templates.perfilclienteui import PerfilClienteUI
from Prova.Projeto_com_lista12.templates.perfilprofissionalui import PerfilProfissionalUI
from Prova.Projeto_com_lista12.templates.agendarservicoui import AgendarServicoUI
from Prova.Projeto_com_lista12.templates.abrirminhaagendaui import AbrirMinhaAgendaUI
from Prova.Projeto_com_lista12.templates.minhaagendaui import MinhaAgendaUI
from Prova.Projeto_com_lista12.templates.meusservicosui import MeusServicosUI
from Prova.Projeto_com_lista12.templates.confirmarservicoui import ConfirmarServicoUI
from Prova.Projeto_com_lista12.templates.alterarsenhaui import AlterarSenhaUI
from Prova.Projeto_com_lista12.service import Service
import streamlit as st

class IndexUI:

    def menu_visitante():
        op = st.sidebar.selectbox(
            "Menu",
            ["Entrar no Sistema", "Abrir Conta"]
        )

        if op == "Entrar no Sistema":
            LoginUI.main()

        if op == "Abrir Conta":
            AbrirContaUI.main()

    def menu_cliente():
        op = st.sidebar.selectbox(
            "Menu",
            ["Meus Dados", "Agendar Serviço", "Meus Serviços"]
        )

        if op == "Meus Dados":
            PerfilClienteUI.main()

        if op == "Agendar Serviço":
            AgendarServicoUI.main()

        if op == "Meus Serviços":
            MeusServicosUI.main()

    def menu_profissional():
        op = st.sidebar.selectbox(
            "Menu",
            [
                "Meus Dados",
                "Abrir Minha Agenda",
                "Minha Agenda",
                "Confirmar Serviço"
            ]
        )

        if op == "Meus Dados":
            PerfilProfissionalUI.main()

        if op == "Abrir Minha Agenda":
            AbrirMinhaAgendaUI.main()

        if op == "Minha Agenda":
            MinhaAgendaUI.main()

        if op == "Confirmar Serviço":
            ConfirmarServicoUI.main()

    def menu_admin():
        op = st.sidebar.selectbox(
            "Menu",
            [
                "Clientes",
                "Serviços",
                "Horários",
                "Profissionais",
                "Alterar Senha"
            ]
        )

        if op == "Clientes":
            ManterClienteUI.main()

        if op == "Serviços":
            ManterServicoUI.main()

        if op == "Horários":
            ManterHorarioUI.main()

        if op == "Profissionais":
            ManterProfissionalUI.main()

        if op == "Alterar Senha":
            AlterarSenhaUI.main()

    def sair_do_sistema():
        if st.sidebar.button("Sair"):
            del st.session_state["usuario_id"]
            del st.session_state["usuario_nome"]
            del st.session_state["usuario_tipo"]

            st.rerun()

    def sidebar():
        if "usuario_id" not in st.session_state:
            IndexUI.menu_visitante()

        else:
            admin = st.session_state["usuario_nome"] == "admin"

            st.sidebar.write(
                "Bem-vindo(a), " +
                st.session_state["usuario_nome"]
            )

            if admin:
                IndexUI.menu_admin()

            else:
                if st.session_state["usuario_tipo"] == "cliente":
                    IndexUI.menu_cliente()

                else:
                    IndexUI.menu_profissional()

            IndexUI.sair_do_sistema()

    def main():
        # Verifica se existe o usuário admin.
        Service.cliente_criar_admin()

        # Monta o menu lateral.
        IndexUI.sidebar()


IndexUI.main()