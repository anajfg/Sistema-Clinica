from exception.sistema_exception import SistemaException


class ValorInvalidoException(SistemaException):
    def __init__(self, mensagem: str = "Valor inválido."):
        super().__init__(mensagem)