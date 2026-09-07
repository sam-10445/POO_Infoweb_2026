# ASSOCIAÇÃO ENTRE CLASSES

## MODELO DO PROJETO

O Horario já possui associações com:

- Cliente
- Servico

Ele guarda:

- id_cliente
- id_servico

---

# SE O PROFESSOR PEDIR UMA NOVA ASSOCIAÇÃO

Exemplo:

Adicionar Profissional ao Horario.

---

## 1. Alterar a classe

Arquivo:

`Projeto/models/horario.py`

Adicionar:

`self.set_id_profissional(0)`

## 2. Criar getter
def get_id_profissional(self):
    return self.__id_profissional

## 3. Criar setter
def set_id_profissional(self, id_profissional):
    self.__id_profissional = id_profissional

## 4. Alterar o to_json()
Adicionar: "id_profissional": self.__id_profissional

## 5. Alterar o from_json()
Adicionar: horario.set_id_profissional(dic["id_profissional"])

## 6. Alterar Service
Adicionar o parâmetro "id_profissional" no inserir e atualizar

## 7. Alterar UI
**Buscar os profissionais:** profissionais = Service.profissional_listar()
**Criar o selectbox:**
profissional = st.selectbox(
    "Informe o profissional",
    profissionais,
    index=None
)
**Pegar o id:** 
id_profissional = None

if profissional != None:
    id_profissional = profissional.get_id()
