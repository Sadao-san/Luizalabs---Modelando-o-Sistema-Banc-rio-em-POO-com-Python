from abc import ABC, abstractmethod
from typing import TypedDict, TYPE_CHECKING

if TYPE_CHECKING:
    from classes.conta.conta import Conta


class RegistroTransacao(TypedDict):
    tipo: str
    valor: float
    data: str


class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self) -> float: pass

    @abstractmethod
    def registrar(self, conta: Conta) -> None: pass
