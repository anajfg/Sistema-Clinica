from datetime import date, time

from models.clinica import Clinica
from models.paciente import Paciente
from models.pagamento import Pagamento
from models.procedimento import Procedimento
from models.profissional_saude import ProfissionalSaude
from models.tipo_atendimento import TipoAtendimento


class Atendimento:
    def __init__(self, codigo: int, clinica: Clinica, paciente: Paciente,
                 profissional: ProfissionalSaude, tipo_atendimento: TipoAtendimento,
                 data: date, hora_inicio: time, hora_fim: time, valor: float):
        self.__codigo = codigo
        self.__clinica = clinica
        self.__paciente = paciente
        self.__profissional = profissional
        self.__tipo_atendimento = tipo_atendimento
        self.__data = data
        self.__hora_inicio = hora_inicio
        self.__hora_fim = hora_fim
        self.__valor = valor
        self.__procedimentos = []
        self.__pagamentos = []

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo: int):
        self.__codigo = codigo

    @property
    def clinica(self):
        return self.__clinica

    @clinica.setter
    def clinica(self, clinica: Clinica):
        self.__clinica = clinica

    @property
    def paciente(self):
        return self.__paciente

    @paciente.setter
    def paciente(self, paciente: Paciente):
        self.__paciente = paciente

    @property
    def profissional(self):
        return self.__profissional

    @profissional.setter
    def profissional(self, profissional: ProfissionalSaude):
        self.__profissional = profissional

    @property
    def tipo_atendimento(self):
        return self.__tipo_atendimento

    @tipo_atendimento.setter
    def tipo_atendimento(self, tipo_atendimento: TipoAtendimento):
        self.__tipo_atendimento = tipo_atendimento

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data: date):
        self.__data = data

    @property
    def hora_inicio(self):
        return self.__hora_inicio

    @hora_inicio.setter
    def hora_inicio(self, hora_inicio: time):
        self.__hora_inicio = hora_inicio

    @property
    def hora_fim(self):
        return self.__hora_fim

    @hora_fim.setter
    def hora_fim(self, hora_fim: time):
        self.__hora_fim = hora_fim

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, valor: float):
        self.__valor = valor

    @property
    def procedimentos(self):
        return self.__procedimentos

    @property
    def pagamentos(self):
        return self.__pagamentos

    def adicionar_procedimento(self, procedimento: Procedimento):
        self.__procedimentos.append(procedimento)

    def remover_procedimento(self, procedimento: Procedimento):
        if procedimento in self.__procedimentos:
            self.__procedimentos.remove(procedimento)

    def adicionar_pagamento(self, pagamento: Pagamento):
        self.__pagamentos.append(pagamento)

    def remover_pagamento(self, pagamento: Pagamento):
        if pagamento in self.__pagamentos:
            self.__pagamentos.remove(pagamento)

    def calcular_valor_restante(self) -> float:
        total_pago = sum(p.valor_pago for p in self.__pagamentos)
        return self.__valor - total_pago