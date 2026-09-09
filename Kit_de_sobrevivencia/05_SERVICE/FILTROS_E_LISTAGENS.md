# FILTROS E LISTAGENS

## LISTAR TODOS
objetos = Service.nomedaclasse_listar()

for obj in objetos:
    print(obj)

## BUSCAR POR ID
obj = Service.nomedaclasse_listar_id(id)

## FILTRAR UMA LISTA
objetos = Service.nomedaclasse_listar()

resultado = []

for obj in objetos:

    if obj.get_atributo() == valor:
        resultado.append(obj)

## BUSCAR OBJETO RELACIONADO
cliente = Service.cliente_listar_id(
    horario.get_id_cliente()
)

**Depois:**
if cliente != None: nome = cliente.get_nome()
