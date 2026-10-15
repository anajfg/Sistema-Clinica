from exception.objeto_em_uso_exception import ObjetoEmUsoException
from exception.objeto_nao_encontrado_exception import ObjetoNaoEncontradoException
from exception.sistema_exception import SistemaException
from models.tipo_atendimento import TipoAtendimento
from views.tela_tipo_atendimento import TelaTipoAtendimento


class ControladorTipoAtendimento:
    def __init__(self):
        self.__tipos = []
        self.__proximo_codigo = 1
        self.__controlador_atendimento = None
        self.__tela = TelaTipoAtendimento()

    def vincula_atendimento(self, controlador_atendimento):
        self.__controlador_atendimento = controlador_atendimento

    @property
    def tipos(self):
        return self.__tipos

    def buscar_por_codigo(self, codigo: int) -> TipoAtendimento:
        for tipo in self.__tipos:
            if tipo.codigo == codigo:
                return tipo
        raise ObjetoNaoEncontradoException("Tipo de atendimento não encontrado.")

    def incluir(self):
        descricao = self.__tela.pega_descricao()
        tipo = TipoAtendimento(self.__proximo_codigo, descricao)
        self.__tipos.append(tipo)
        self.__tela.mostra_mensagem(
            f"Tipo incluído com sucesso. Código: {self.__proximo_codigo}")
        self.__proximo_codigo += 1

    def alterar(self):
        tipo = self.buscar_por_codigo(self.__tela.pega_codigo())
        tipo.descricao = self.__tela.pega_descricao()
        self.__tela.mostra_mensagem("Tipo alterado com sucesso.")

    def listar(self):
        if not self.__tipos:
            self.__tela.mostra_mensagem("Nenhum tipo de atendimento cadastrado.")
            return
        for tipo in self.__tipos:
            self.__tela.mostra_tipo(tipo)

    def excluir(self):
        tipo = self.buscar_por_codigo(self.__tela.pega_codigo())
        if self.__controlador_atendimento.tipo_possui_atendimento(tipo):
            raise ObjetoEmUsoException(
                "Não é possível excluir: o tipo está em uso em atendimentos.")
        self.__tipos.remove(tipo)
        self.__tela.mostra_mensagem("Tipo excluído com sucesso.")

    def abre_tela(self):
        opcoes = {1: self.incluir, 2: self.alterar, 3: self.listar, 4: self.excluir}
        while True:
            opcao = self.__tela.tela_opcoes()
            if opcao == 0:
                return
            try:
                opcoes[opcao]()
            except SistemaException as e:
                self.__tela.mostra_mensagem(str(e))