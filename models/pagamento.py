from datetime import date


class Pagamento:
    def __init__(self, codigo: int, data: date, valor_pago: float, modalidade: str,
                 cpf_pagador: str = None, numero_cartao: str = None,
                 bandeira: str = None):
        self.__codigo = codigo
        self.__data = data
        self.__valor_pago = valor_pago
        self.__modalidade = modalidade
        self.__cpf_pagador = cpf_pagador
        self.__numero_cartao = numero_cartao
        self.__bandeira = bandeira

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo: int):
        self.__codigo = codigo

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data: date):
        self.__data = data

    @property
    def valor_pago(self):
        return self.__valor_pago

    @valor_pago.setter
    def valor_pago(self, valor_pago: float):
        self.__valor_pago = valor_pago

    @property
    def modalidade(self):
        return self.__modalidade

    @modalidade.setter
    def modalidade(self, modalidade: str):
        self.__modalidade = modalidade

    @property
    def cpf_pagador(self):
        return self.__cpf_pagador

    @cpf_pagador.setter
    def cpf_pagador(self, cpf_pagador: str):
        self.__cpf_pagador = cpf_pagador

    @property
    def numero_cartao(self):
        return self.__numero_cartao

    @numero_cartao.setter
    def numero_cartao(self, numero_cartao: str):
        self.__numero_cartao = numero_cartao

    @property
    def bandeira(self):
        return self.__bandeira

    @bandeira.setter
    def bandeira(self, bandeira: str):
        self.__bandeira = bandeira