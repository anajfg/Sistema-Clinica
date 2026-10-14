from exception.sistema_exception import SistemaException


class OpcaoInvalidaException(SistemaException):
    def __init__(self, mensagem: str = "Opção inválida."):
        super().__init__(mensagem)