class TipoAtendimento:
    def __init__(self, codigo: int, descricao: str):
        self.__codigo = codigo
        self.__descricao = descricao

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo: int):
        self.__codigo = codigo

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao: str):
        self.__descricao = descricao