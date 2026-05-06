from classes.cliente.cliente import Cliente


def filtrar_clientes(cpf: str, clientes: list[Cliente]) -> Cliente | None:
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None
