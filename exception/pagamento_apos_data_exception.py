from exception.sistema_exception import SistemaException


class PagamentoAposDataException(SistemaException):
    def __init__(self, mensagem: str = "O pagamento deve ser feito até a data do atendimento."):
        super().__init__(mensagem)