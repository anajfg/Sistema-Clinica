from exception.sistema_exception import SistemaException


class PacienteMenorDeIdadeException(SistemaException):
    def __init__(self, mensagem: str = "O paciente precisa ter mais de 18 anos completos."):
        super().__init__(mensagem)