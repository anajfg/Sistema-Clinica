from exception.objeto_nao_encontrado_exception import ObjetoNaoEncontradoException
from exception.sistema_exception import SistemaException
from models.procedimento import Procedimento
from views.tela_procedimento import TelaProcedimento


class ControladorProcedimento:
    def __init__(self, controlador_atendimento, controlador_profissional):
        self.__controlador_atendimento = controlador_atendimento
        self.__controlador_profissional = controlador_profissional
        self.__proximo_codigo = 1
        self.__tela = TelaProcedimento()

    def __buscar(self, codigo: int):
        for atendimento in self.__controlador_atendimento.atendimentos:
            for procedimento in atendimento.procedimentos:
                if procedimento.codigo == codigo:
                    return atendimento, procedimento
        raise ObjetoNaoEncontradoException("Procedimento não encontrado.")

    def incluir(self):
        atendimento = self.__controlador_atendimento.buscar_por_codigo(
            self.__tela.pega_codigo_atendimento())
        dados = self.__tela.pega_dados_procedimento()
        profissional = self.__controlador_profissional.buscar_por_cpf(
            dados["cpf_profissional"])
        procedimento = Procedimento(self.__proximo_codigo, dados["descricao"],
                                    dados["custo"], profissional)
        atendimento.adicionar_procedimento(procedimento)
        self.__tela.mostra_mensagem(
            f"Procedimento incluído com sucesso. Código: {self.__proximo_codigo}")
        self.__proximo_codigo += 1

    def alterar(self):
        _, procedimento = self.__buscar(self.__tela.pega_codigo())
        dados = self.__tela.pega_dados_procedimento()
        profissional = self.__controlador_profissional.buscar_por_cpf(
            dados["cpf_profissional"])
        procedimento.descricao = dados["descricao"]
        procedimento.custo = dados["custo"]
        procedimento.profissional = profissional
        self.__tela.mostra_mensagem("Procedimento alterado com sucesso.")

    def listar(self):
        encontrou = False
        for atendimento in self.__controlador_atendimento.atendimentos:
            for procedimento in atendimento.procedimentos:
                self.__tela.mostra_procedimento(atendimento, procedimento)
                encontrou = True
        if not encontrou:
            self.__tela.mostra_mensagem("Nenhum procedimento registrado.")

    def excluir(self):
        atendimento, procedimento = self.__buscar(self.__tela.pega_codigo())
        atendimento.remover_procedimento(procedimento)
        self.__tela.mostra_mensagem("Procedimento excluído com sucesso.")

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