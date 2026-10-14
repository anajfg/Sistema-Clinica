from exception.sistema_exception import SistemaException


class ForaDoHorarioClinicaException(SistemaException):
    def __init__(self, mensagem: str = "Atendimento fora do horário de funcionamento da clínica."):
        super().__init__(mensagem)