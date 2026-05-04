from __future__ import annotations
from abc import ABC, abstractmethod
from datetime import datetime
from typing import TypedDict
import textwrap


class RegistroTransacao(TypedDict):
    tipo: str
    valor: float
    data: str


class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self)-> float: pass

    @abstractmethod
    def registrar(self, conta: Conta)-> None: pass


class Saque(Transacao):
    def __init__(self, valor: float)-> None:
        self._valor = valor
    
    @property
    def valor(self)-> float:
        return self._valor

    def registrar(self, conta: Conta):
        sucesso_transacao = conta.sacar(self._valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


class Deposito(Transacao):
    def __init__(self, valor: float)-> None:
        self._valor = valor
    
    @property
    def valor(self)-> float:
        return self._valor

    def registrar(self, conta: Conta):
        sucesso_transacao = conta.depositar(self._valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


class Historico:
    def __init__(self)-> None:
        self._transacoes: list[RegistroTransacao] = []
    
    @property
    def transacoes(self) -> list[RegistroTransacao]:
        return self._transacoes
    
    def adicionar_transacao(self, transacao: Transacao) -> None:
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
            }
        )


class Cliente:
    def __init__(self, endereco: str)-> None:
        self.endereco = endereco
        self.contas: list[Conta] = []
    
    @property
    @abstractmethod
    def nome(self) -> str: pass

    @property
    @abstractmethod
    def cpf(self) -> str: pass

    def adicionar_conta(self, conta: Conta)-> None:
        self.contas.append(conta)
    
    def realizar_transacao(self, conta: Conta, transacao: Transacao)-> None:
        transacao.registrar(conta)


class PessoaFisica(Cliente):
    def __init__(self, nome: str, data_nascimento: str, cpf: str, endereco: str):
        super().__init__(endereco)
        self._nome = nome
        self.data_nascimento = data_nascimento
        self._cpf = cpf

    @property
    def nome(self) -> str:
        return self._nome
    
    @property
    def cpf(self) -> str:
        return self._cpf


class Conta:
    def __init__(self, numero: int, cliente: Cliente)-> None:
        self._saldo = 0.0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()
    
    @classmethod
    def nova_conta(cls, numero: int, cliente: Cliente)-> Conta:
        return cls(numero, cliente)

    @property
    def saldo(self)-> float:
        return self._saldo
    
    @property
    def numero(self)-> int:
        return self._numero

    @property
    def agencia(self)-> str:
        return self._agencia
    
    @property
    def cliente(self)-> Cliente:
        return self._cliente

    @property
    def historico(self)-> Historico:
        return self._historico

    def sacar(self, valor: float)-> bool:
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
    
        elif valor > 0:
            self._saldo -= valor
            print("Saque realizado com sucesso!")
            return True
        
        else:
            print("Operação falhou! O valor informado é inválido.")
        
        return False

    def depositar(self, valor: float)-> bool:
        if valor > 0:
            self._saldo += valor
            print("Depósito realizado com sucesso!")
            return True
        
        else: 
            print("Operação falhou! O valor informado é inválido.")
        
        return False


class ContaCorrente(Conta):
    def __init__(self, numero: int, cliente: Cliente, limite: float = 500, limite_saques = 3)-> None:
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques
    
    def sacar(self, valor: float)-> bool:
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes
            if transacao["tipo"] == Saque.__name__]
            )
        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques >= self.limite_saques

        if excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
        
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")
        
        else:
            return super().sacar(valor)
        
        return False
    
    def __str__(self):
        return f"""
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """


def menu()-> str:
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))


def filtrar_clientes(cpf: str, clientes: list[Cliente])-> Cliente | None:
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None


def recuperar_conta_cliente(cliente: Cliente)-> Conta | None:
    if not cliente.contas:
        print("Cliente não possui conta!")
        return
    
    # FIXME: Refatorar para exibir as contas
    return cliente.contas[0]


def depositar(clientes: list[Cliente])-> None:
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


def sacar(clientes: list[Cliente])-> None:
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


def exibir_extrato(clientes):
    cpf = input("Informe o CPF do titular da conta: ")
    cliente = filtrar_clientes(cpf, clientes)

    if not cliente:
        print("Cliente não encontrado!")
        return

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    print("\n================ EXTRATO =================")
    transacoes = conta.historico.transacoes

    extrato = ""
    if not transacoes:
        extrato = "Não foram realizadas movimentações."

    else:
        for transacao in transacoes:
            extrato += f"\n{transacao['tipo']}:\n\tR$ {transacao['valor']:.2f}"

    print(extrato)
    print(f"\nSaldo:\n\tR$ {conta.saldo:.2f}")
    print("==========================================")


def criar_cliente(clientes: list[Cliente])-> None:
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


def criar_conta(numero_conta: int, clientes: list[Cliente], contas: list[Conta])-> None:
    cpf = input("Informe o CPF do titular da conta: ")
    cliente = filtrar_clientes(cpf, clientes)

    if not cliente:
        print("Cliente não encontrado!")
        return

    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
    contas.append(conta)
    print("Conta criada com sucesso!")


def listar_contas(contas: list[Conta])-> None:
    if not contas:
        print("Nenhuma conta cadastrada.")
        return
    for conta in contas:
        print("=" * 100)
        print(textwrap.dedent(str(conta)))


def main():
    clientes = []
    contas = []

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