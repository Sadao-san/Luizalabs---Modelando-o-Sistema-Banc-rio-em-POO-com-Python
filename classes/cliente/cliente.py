from __future__ import annotations
from abc import abstractmethod
from typing import TYPE_CHECKING

from classes.transacao.transacao import Transacao

if TYPE_CHECKING:
    from classes.conta.conta import Conta


class Cliente:
    def __init__(self, endereco: str) -> None:
        self.endereco = endereco
        self.contas: list[Conta] = []
    
    @property
    @abstractmethod
    def nome(self) -> str: pass

    @property
    @abstractmethod
    def cpf(self) -> str: pass

    def adicionar_conta(self, conta: Conta) -> None:
        self.contas.append(conta)
    
    def realizar_transacao(self, conta: Conta, transacao: Transacao) -> None:
        transacao.registrar(conta)
