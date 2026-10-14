from exception.sistema_exception import SistemaException


class CpfDuplicadoException(SistemaException):
    def __init__(self, mensagem: str = "Já existe um cadastro com este CPF."):
        super().__init__(mensagem)