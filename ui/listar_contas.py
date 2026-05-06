import textwrap

from classes.conta.conta import Conta


def listar_contas(contas: list[Conta]) -> None:
    if not contas:
        print("Nenhuma conta cadastrada.")
        return
    for conta in contas:
        print("=" * 100)
        print(textwrap.dedent(str(conta)))