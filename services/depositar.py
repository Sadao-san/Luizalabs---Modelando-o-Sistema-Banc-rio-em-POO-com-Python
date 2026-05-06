from classes.cliente.cliente import Cliente
from classes.transacao.deposito import Deposito
from services.filtrar_clientes import filtrar_clientes
from services.recuperar_conta_cliente import recuperar_conta_cliente


def depositar(clientes: list[Cliente]) -> None:
    cpf = input("Informe o CPF do titular da conta: ")
    cliente = filtrar_clientes(cpf, clientes)

    if not cliente:
        print("Cliente não encontrado!")
        return

    valor = float(input("Informe o valor do depósito: "))
    transacao = Deposito(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)
