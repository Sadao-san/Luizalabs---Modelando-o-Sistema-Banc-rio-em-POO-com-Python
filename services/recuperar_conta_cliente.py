from classes.cliente.cliente import Cliente
from classes.conta.conta import Conta


def recuperar_conta_cliente(cliente: Cliente) -> Conta | None:
    if not cliente.contas:
        print("Cliente não possui conta!")
        return
    
    # FIXME: Refatorar para exibir as contas
    return cliente.contas[0]