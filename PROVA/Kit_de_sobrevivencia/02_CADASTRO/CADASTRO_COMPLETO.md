# CADASTRO COMPLETO

Quando o professor pedir para criar um novo cadastro, normalmente será necessário criar:

1. Classe
2. DAO
3. Métodos no Service
4. UI
5. Opção no Index

---

# ORDEM PARA FAZER

## 1. Classe

Criar:

`Projeto/models/nome.py`

Use:

`01_MODELOS_BASE/MODELO_CLASSE.py`

---

## 2. DAO

Criar:

`Projeto/models/nomedao.py`

Use:

`01_MODELOS_BASE/MODELO_DAO.py`

---

## 3. Service

Alterar:

`Projeto/service.py`

Use:

`01_MODELOS_BASE/MODELO_SERVICE.py`

---

## 4. UI

Criar:

`Projeto/templates/manternomeui.py`

Use:

`01_MODELOS_BASE/MODELO_UI.py`

---

## 5. Index

Alterar:

`Projeto/index.py`

Use:

`01_MODELOS_BASE/MODELO_INDEX.py`

---

# PADRÃO

Classe:

NomeDaClasse

DAO:

NomeDaClasseDAO

Service:

nomedaclasse_inserir()
nomedaclasse_listar()
nomedaclasse_listar_id()
nomedaclasse_atualizar()
nomedaclasse_excluir()

UI:

ManterNomeDaClasseUI

---

# EXEMPLO

Se o professor disser:

"Crie o cadastro de profissionais."

Você fará:

Profissional
↓
ProfissionalDAO
↓
Service
↓
ManterProfissionalUI
↓
IndexUI