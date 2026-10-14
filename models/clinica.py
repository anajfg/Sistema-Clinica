from datetime import time

from models.profissional_saude import ProfissionalSaude


class Clinica:
    def __init__(self, nome: str, cidade: str, descricao: str,
                 hora_abertura: time, hora_fechamento: time):
        self.__nome = nome
        self.__cidade = cidade
        self.__descricao = descricao
        self.__hora_abertura = hora_abertura
        self.__hora_fechamento = hora_fechamento
        self.__profissionais = []

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def cidade(self):
        return self.__cidade

    @cidade.setter
    def cidade(self, cidade: str):
        self.__cidade = cidade

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao: str):
        self.__descricao = descricao

    @property
    def hora_abertura(self):
        return self.__hora_abertura

    @hora_abertura.setter
    def hora_abertura(self, hora_abertura: time):
        self.__hora_abertura = hora_abertura

    @property
    def hora_fechamento(self):
        return self.__hora_fechamento

    @hora_fechamento.setter
    def hora_fechamento(self, hora_fechamento: time):
        self.__hora_fechamento = hora_fechamento

    @property
    def profissionais(self):
        return self.__profissionais

    def adicionar_profissional(self, profissional: ProfissionalSaude):
        if profissional not in self.__profissionais:
            self.__profissionais.append(profissional)

    def remover_profissional(self, profissional: ProfissionalSaude):
        if profissional in self.__profissionais:
            self.__profissionais.remove(profissional)