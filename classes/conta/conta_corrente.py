from classes.cliente.cliente import Cliente
from classes.conta.conta import Conta
from classes.transacao.saque import Saque


class ContaCorrente(Conta):
    def __init__(self, numero: int, cliente: Cliente, limite: float = 500, limite_saques = 3) -> None:
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques
    
    def sacar(self, valor: float) -> bool:
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
    
    def __str__(self) -> str:
        return f"""
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """
