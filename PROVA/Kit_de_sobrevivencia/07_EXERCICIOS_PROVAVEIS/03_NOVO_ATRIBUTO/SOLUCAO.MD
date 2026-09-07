# SOLUÇÃO — NOVO ATRIBUTO

## profissional.py

### __init__

```python
def __init__(self, id, nome, email, fone, especialidade):
    self.set_id(id)
    self.set_nome(nome)
    self.set_email(email)
    self.set_fone(fone)
    self.set_especialidade(especialidade)

```

### setter
def set_especialidade(self, especialidade):
    if especialidade == "":
        raise ValueError("Especialidade deve ser informada")
    self.__especialidade = especialidade

### getter
def get_especialidade(self):
    return self.__especialidade

### to_json

#### Adicionar:

"especialidade": self.__especialidade
from_json

#### Alterar para:

return Profissional(
    dic["id"],
    dic["nome"],
    dic["email"],
    dic["fone"],
    dic["especialidade"]
)

## Service

### Inserir:

def profissional_inserir(nome, email, fone, especialidade):

    obj = Profissional(
        0,
        nome,
        email,
        fone,
        especialidade
    )

    ProfissionalDAO().inserir(obj)

### Atualizar:

def profissional_atualizar(
    id,
    nome,
    email,
    fone,
    especialidade
):

    obj = Profissional(
        id,
        nome,
        email,
        fone,
        especialidade
    )

    ProfissionalDAO().atualizar(obj)
## UI

### Campo:

especialidade = st.text_input(
    "Informe a especialidade"
)

### Na atualização:

especialidade = st.text_input(
    "Nova especialidade",
    op.get_especialidade()
)

Enviar o novo atributo para o Service.