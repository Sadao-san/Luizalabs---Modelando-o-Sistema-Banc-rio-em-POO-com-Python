from classes.cliente.cliente import Cliente
from classes.cliente.pessoa_fisica import PessoaFisica
from services.filtrar_clientes import filtrar_clientes


def criar_cliente(clientes: list[Cliente]) -> None:
    cpf = input("Informe o CPF (somente número): ")
    cliente = filtrar_clientes(cpf, clientes)

    if cliente:
        print("Já existe um cliente com esse CPF!")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)

    clientes.append(cliente)

    print("Cliente criado com sucesso!")
