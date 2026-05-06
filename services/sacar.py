from classes.cliente.cliente import Cliente
from classes.transacao.saque import Saque
from services.filtrar_clientes import filtrar_clientes
from services.recuperar_conta_cliente import recuperar_conta_cliente


def sacar(clientes: list[Cliente]) -> None:
    cpf = input("Informe o CPF do titular da conta: ")
    cliente = filtrar_clientes(cpf, clientes)

    if not cliente:
        print("Cliente não encontrado!")
        return

    valor = float(input("Informe o valor do saque: "))
    transacao = Saque(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)
