# ADICIONAR ATRIBUTO

Quando o professor mandar adicionar um atributo em uma classe existente:

## NÃO ALTERE SOMENTE O __init__.

Procure todos estes lugares:

1. __init__
2. setter
3. getter
4. __str__
5. to_json
6. from_json
7. Service
8. UI

---

# EXEMPLO

Adicionar:

`especialidade`

em Profissional.

## __init__

`self.set_especialidade(especialidade)`

## setter
def set_especialidade(self, especialidade):
    self.__especialidade = especialidade

## getter
def get_especialidade(self):
    return self.__especialidade

## to_json
"especialidade": self.__especialidade

## from_json
dic["especialidade"]

## Service
Adicionar o parâmetro nos métodos de inserir e atualizar.

## UI
Adicionar o campo de entrada correspondente.

