# SERVICE

O Service faz a ligação entre a UI e o DAO.

---

# PADRÃO DE INSERIR

@staticmethod
def nomedaclasse_inserir(atributo1, atributo2):

    obj = NomeDaClasse(
        0,
        atributo1,
        atributo2
    )

    NomeDaClasseDAO().inserir(obj)

## PADRÃO DE LISTAR
@staticmethod
def nomedaclasse_listar():

    return NomeDaClasseDAO().listar()

## PADRÃO DE BUSCAR POR ID
@staticmethod
def nomedaclasse_listar_id(id):

    return NomeDaClasseDAO().listar_id(id)

## PADRÃO DE ATUALIZAR
@staticmethod
def nomedaclasse_atualizar(id, atributo1, atributo2):

    obj = NomeDaClasse(
        id,
        atributo1,
        atributo2
    )

    NomeDaClasseDAO().atualizar(obj)

## PADRÃO DE EXCLUIR
@staticmethod
def nomedaclasse_excluir(id):

    NomeDaClasseDAO().excluir(id)

