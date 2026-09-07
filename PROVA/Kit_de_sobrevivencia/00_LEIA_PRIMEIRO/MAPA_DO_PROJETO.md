# MAPA DO PROJETO

Este arquivo mostra onde cada parte do sistema está localizada.

---

# MODELS

## Cliente

`Projeto/models/cliente.py`

Representa a classe Cliente.

Atributos:

- id
- nome
- email
- fone

---

## ClienteDAO

`Projeto/models/clientedao.py`

Responsável pelo armazenamento e operações do Cliente.

Possui:

- inserir
- listar
- listar_id
- atualizar
- excluir

---

## Serviço

`Projeto/models/servico.py`

Representa a classe Servico.

Atributos:

- id
- descricao
- valor

---

## ServicoDAO

`Projeto/models/servicodao.py`

Responsável pelo armazenamento e operações do Servico.

Possui:

- inserir
- listar
- listar_id
- atualizar
- excluir

---

## Horário

`Projeto/models/horario.py`

Representa a classe Horario.

Atributos:

- id
- data
- confirmado
- id_cliente
- id_servico

---

## HorarioDAO

`Projeto/models/horariodao.py`

Responsável pelo armazenamento e operações do Horario.

Possui:

- inserir
- listar
- listar_id
- atualizar
- excluir

---

# SERVICE

Arquivo:

`Projeto/service.py`

Faz a ligação entre as classes da aplicação e os respectivos DAOs.

Possui métodos para:

- inserir
- listar
- buscar por ID
- atualizar
- excluir

de Cliente, Servico e Horario.

---

# INTERFACES

As interfaces estão em:

`Projeto/templates/`

## Cliente

`manterclienteui.py`

Possui:

- Listar
- Inserir
- Atualizar
- Excluir

## Serviço

`manterservicoui.py`

Possui:

- Listar
- Inserir
- Atualizar
- Excluir

## Horário

`manterhorarioui.py`

Possui:

- Listar
- Inserir
- Atualizar
- Excluir

---

# MENU PRINCIPAL

Arquivo:

`Projeto/index.py`

É responsável pelo menu lateral do sistema.

Atualmente possui:

- Clientes
- Serviços
- Horários

---

# ARQUIVOS JSON

Os dados são armazenados em:

`Projeto/clientes.json`

`Projeto/servicos.json`

`Projeto/horarios.json`

---

# MAPA RÁPIDO

Se precisar alterar...

| Preciso fazer | Arquivo/pasta |
|---|---|
| Nova classe | `models/` |
| Novo DAO | `models/` |
| Cadastro completo | `models/` + `service.py` + `templates/` + `index.py` |
| Novo atributo | Classe + DAO/JSON + Service + UI |
| Associação | Classes relacionadas + Service + UI |
| Nova página | `templates/` + `index.py` |
| Nova listagem | `service.py` + UI |
| Inserir | Classe + DAO + Service + UI |
| Atualizar | Classe + DAO + Service + UI |
| Excluir | DAO + Service + UI |