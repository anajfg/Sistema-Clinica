class SistemaException(Exception):
    def __init__(self, mensagem: str = "Erro no sistema."):
        super().__init__(mensagem)