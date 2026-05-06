from classes.cliente.cliente import Cliente
from classes.conta.conta import Conta
from classes.conta.conta_corrente import ContaCorrente
from services.filtrar_clientes import filtrar_clientes


def criar_conta(numero_conta: int, clientes: list[Cliente], contas: list[Conta])-> None:
    cpf = input("Informe o CPF do titular da conta: ")
    cliente = filtrar_clientes(cpf, clientes)

    if not cliente:
        print("Cliente não encontrado!")
        return

    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
    contas.append(conta)
    cliente.adicionar_conta(conta)
    print("Conta criada com sucesso!")
