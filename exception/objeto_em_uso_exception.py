from exception.sistema_exception import SistemaException


class ObjetoEmUsoException(SistemaException):
    def __init__(self, mensagem: str = "Não é possível excluir: o registro está em uso."):
        super().__init__(mensagem)