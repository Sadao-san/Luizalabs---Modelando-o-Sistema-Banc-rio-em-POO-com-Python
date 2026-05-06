from classes.cliente.cliente import Cliente


class PessoaFisica(Cliente):
    def __init__(self, nome: str, data_nascimento: str, cpf: str, endereco: str) -> None:
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
