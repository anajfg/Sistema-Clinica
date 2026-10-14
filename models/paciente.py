from datetime import date

from models.pessoa import Pessoa


class Paciente(Pessoa):
    def __init__(self, nome: str, celular: str, cpf: str, data_nascimento: date):
        super().__init__(nome, celular, cpf)
        self.__data_nascimento = data_nascimento

    @property
    def data_nascimento(self):
        return self.__data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, data_nascimento: date):
        self.__data_nascimento = data_nascimento

    def resumo(self) -> str:
        return f"{self.nome} | CPF: {self.cpf} | Nascimento: {self.data_nascimento.strftime('%d/%m/%Y')}"