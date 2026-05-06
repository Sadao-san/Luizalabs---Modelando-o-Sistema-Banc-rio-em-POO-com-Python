from datetime import datetime

from classes.transacao.transacao import Transacao, RegistroTransacao


class Historico:
    def __init__(self) -> None:
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