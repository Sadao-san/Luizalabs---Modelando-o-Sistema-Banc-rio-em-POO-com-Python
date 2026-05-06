from classes.cliente.cliente import Cliente
from classes.conta.conta import Conta
from services.depositar import depositar
from services.sacar import sacar
from ui.exibir_extrato import exibir_extrato
from services.criar_cliente import criar_cliente
from services.criar_conta import criar_conta
from ui.menu import menu
from ui.listar_contas import listar_contas


def main():
    clientes: list[Cliente] = []
    contas: list[Conta] = []

    while True:
        opcao = menu()

        if opcao == "d":
            depositar(clientes)

        elif opcao == "s":
            sacar(clientes)

        elif opcao == "e":
            exibir_extrato(clientes)

        elif opcao == "nu":
            criar_cliente(clientes)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    main()
