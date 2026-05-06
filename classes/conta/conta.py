from __future__ import annotations
from typing import TYPE_CHECKING

from classes.historico.historico import Historico

if TYPE_CHECKING:
    from classes.cliente.cliente import Cliente


class Conta:
    def __init__(self, numero: int, cliente: Cliente) -> None:
        self._saldo = 0.0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()
    
    @classmethod
    def nova_conta(cls, numero: int, cliente: Cliente) -> Conta:
        return cls(numero, cliente)

    @property
    def saldo(self) -> float:
        return self._saldo
    
    @property
    def numero(self) -> int:
        return self._numero

    @property
    def agencia(self) -> str:
        return self._agencia
    
    @property
    def cliente(self) -> Cliente:
        return self._cliente

    @property
    def historico(self) -> Historico:
        return self._historico

    def sacar(self, valor: float) -> bool:
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

    def depositar(self, valor: float) -> bool:
        if valor > 0:
            self._saldo += valor
            print("Depósito realizado com sucesso!")
            return True
        
        else: 
            print("Operação falhou! O valor informado é inválido.")
        
        return False
