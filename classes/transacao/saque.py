from classes.conta.conta import Conta
from classes.transacao.transacao import Transacao

class Saque(Transacao):
    def __init__(self, valor: float) -> None:
        self._valor = valor
    
    @property
    def valor(self) -> float:
        return self._valor

    def registrar(self, conta: Conta) -> None:
        sucesso_transacao = conta.sacar(self._valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)
