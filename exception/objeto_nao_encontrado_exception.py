from exception.sistema_exception import SistemaException


class ObjetoNaoEncontradoException(SistemaException):
    def __init__(self, mensagem: str = "Registro não encontrado."):
        super().__init__(mensagem)