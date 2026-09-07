# SOLUÇÃO — NOVO CADASTRO

## ARQUIVOS NECESSÁRIOS

Criar:

Projeto/models/profissional.py
Projeto/models/profissionaldao.py
Projeto/templates/manterprofissionalui.py

Alterar:

Projeto/service.py
Projeto/index.py

---

# 1. profissional.py

```python
class Profissional:

    def __init__(self, id, nome, email, fone):
        self.set_id(id)
        self.set_nome(nome)
        self.set_email(email)
        self.set_fone(fone)

    def set_id(self, id):
        if id < 0:
            raise ValueError("Id deve ser positivo")
        self.__id = id

    def set_nome(self, nome):
        if nome == "":
            raise ValueError("Nome deve ser informado")
        self.__nome = nome

    def set_email(self, email):
        if email == "":
            raise ValueError("E-mail deve ser informado")
        self.__email = email

    def set_fone(self, fone):
        if fone == "":
            raise ValueError("Fone deve ser informado")
        self.__fone = fone

    def get_id(self):
        return self.__id

    def get_nome(self):
        return self.__nome

    def get_email(self):
        return self.__email

    def get_fone(self):
        return self.__fone

    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__email} - {self.__fone}"

    def to_json(self):
        return {
            "id": self.__id,
            "nome": self.__nome,
            "email": self.__email,
            "fone": self.__fone
        }

    @staticmethod
    def from_json(dic):
        return Profissional(
            dic["id"],
            dic["nome"],
            dic["email"],
            dic["fone"]
        )

```
## 2. Profissionaldao.py
``` python
from models.profissional import Profissional
import json


class ProfissionalDAO:

    def __init__(self):
        self.__arquivo = "profissionais.json"
        self.__objetos = []
        self.__abrir()

    def inserir(self, obj):
        id = 0

        if len(self.__objetos) > 0:
            for aux in self.__objetos:
                if aux.get_id() > id:
                    id = aux.get_id()

        obj.set_id(id + 1)
        self.__objetos.append(obj)
        self.__salvar()

    def listar(self):
        return self.__objetos

    def listar_id(self, id):
        for obj in self.__objetos:
            if obj.get_id() == id:
                return obj
        return None

    def atualizar(self, obj):
        aux = self.listar_id(obj.get_id())

        if aux != None:
            self.__objetos.remove(aux)
            self.__objetos.append(obj)
            self.__salvar()

    def excluir(self, id):
        aux = self.listar_id(id)

        if aux != None:
            self.__objetos.remove(aux)
            self.__salvar()

    def __abrir(self):
        try:
            arquivo = open(self.__arquivo, mode="r")
            list_dic = json.load(arquivo)
            arquivo.close()

            for dic in list_dic:
                obj = Profissional.from_json(dic)
                self.__objetos.append(obj)

        except FileNotFoundError:
            pass

    def __salvar(self):
        arquivo = open(self.__arquivo, mode="w")

        json.dump(
            self.__objetos,
            arquivo,
            default=Profissional.to_json,
            indent=2
        )

        arquivo.close()
```

## 3. Service
```python
from models.profissional import Profissional
from models.profissionaldao import ProfissionalDAO

@staticmethod
def profissional_inserir(nome, email, fone):
    obj = Profissional(0, nome, email, fone)
    ProfissionalDAO().inserir(obj)

@staticmethod
def profissional_listar():
    return ProfissionalDAO().listar()

@staticmethod
def profissional_listar_id(id):
    return ProfissionalDAO().listar_id(id)

@staticmethod
def profissional_atualizar(id, nome, email, fone):
    obj = Profissional(id, nome, email, fone)
    ProfissionalDAO().atualizar(obj)

@staticmethod
def profissional_excluir(id):
    ProfissionalDAO().excluir(id)

```

## 4. manterprofissionalui.py
```python
import streamlit as st
import pandas as pd
import time
from service import Service


class ManterProfissionalUI:

    def main():

        st.header("Cadastro de Profissionais")

        tab1, tab2, tab3, tab4 = st.tabs(
            ["Listar", "Inserir", "Atualizar", "Excluir"]
        )

        with tab1:
            ManterProfissionalUI.listar()

        with tab2:
            ManterProfissionalUI.inserir()

        with tab3:
            ManterProfissionalUI.atualizar()

        with tab4:
            ManterProfissionalUI.excluir()

    def listar():

        profissionais = Service.profissional_listar()

        if len(profissionais) == 0:
            st.write("Nenhum profissional cadastrado")

        else:
            lista = []

            for obj in profissionais:
                lista.append(obj.to_json())

            df = pd.DataFrame(lista)
            st.dataframe(df)

    def inserir():

        nome = st.text_input("Informe o nome")
        email = st.text_input("Informe o e-mail")
        fone = st.text_input("Informe o fone")

        if st.button("Inserir"):

            Service.profissional_inserir(
                nome,
                email,
                fone
            )

            st.success("Profissional inserido com sucesso")

            time.sleep(2)
            st.rerun()

    def atualizar():

        profissionais = Service.profissional_listar()

        if len(profissionais) == 0:
            st.write("Nenhum profissional cadastrado")

        else:

            op = st.selectbox(
                "Atualização de Profissionais",
                profissionais
            )

            nome = st.text_input(
                "Novo nome",
                op.get_nome()
            )

            email = st.text_input(
                "Novo e-mail",
                op.get_email()
            )

            fone = st.text_input(
                "Novo fone",
                op.get_fone()
            )

            if st.button("Atualizar"):

                Service.profissional_atualizar(
                    op.get_id(),
                    nome,
                    email,
                    fone
                )

                st.success("Profissional atualizado com sucesso")

                time.sleep(2)
                st.rerun()

    def excluir():

        profissionais = Service.profissional_listar()

        if len(profissionais) == 0:
            st.write("Nenhum profissional cadastrado")

        else:

            op = st.selectbox(
                "Exclusão de Profissionais",
                profissionais
            )

            if st.button("Excluir"):

                Service.profissional_excluir(
                    op.get_id()
                )

                st.success("Profissional excluído com sucesso")

                time.sleep(2)
                st.rerun()
```