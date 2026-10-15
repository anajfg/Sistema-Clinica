from exception.objeto_nao_encontrado_exception import ObjetoNaoEncontradoException
from exception.pagamento_apos_data_exception import PagamentoAposDataException
from exception.sistema_exception import SistemaException
from exception.valor_invalido_exception import ValorInvalidoException
from models.pagamento import Pagamento
from views.tela_pagamento import TelaPagamento


class ControladorPagamento:
    def __init__(self, controlador_atendimento):
        self.__controlador_atendimento = controlador_atendimento
        self.__proximo_codigo = 1
        self.__tela = TelaPagamento()

    def __buscar(self, codigo: int):
        for atendimento in self.__controlador_atendimento.atendimentos:
            for pagamento in atendimento.pagamentos:
                if pagamento.codigo == codigo:
                    return atendimento, pagamento
        raise ObjetoNaoEncontradoException("Pagamento não encontrado.")

    def __valida(self, atendimento, data, valor_pago, limite):
        if data > atendimento.data:
            raise PagamentoAposDataException()
        if round(valor_pago, 2) > round(limite, 2):
            raise ValorInvalidoException(
                f"O valor excede o restante do atendimento (R$ {limite:.2f}).")

    def incluir(self):
        atendimento = self.__controlador_atendimento.buscar_por_codigo(
            self.__tela.pega_codigo_atendimento())
        dados = self.__tela.pega_dados_pagamento()
        self.__valida(atendimento, dados["data"], dados["valor_pago"],
                      atendimento.calcular_valor_restante())
        pagamento = Pagamento(self.__proximo_codigo, dados["data"],
                              dados["valor_pago"], dados["modalidade"],
                              dados["cpf_pagador"], dados["numero_cartao"],
                              dados["bandeira"])
        atendimento.adicionar_pagamento(pagamento)
        self.__tela.mostra_mensagem(
            f"Pagamento registrado. Código: {self.__proximo_codigo} | "
            f"Restante: R$ {atendimento.calcular_valor_restante():.2f}")
        self.__proximo_codigo += 1

    def alterar(self):
        atendimento, pagamento = self.__buscar(self.__tela.pega_codigo())
        dados = self.__tela.pega_dados_alteracao()
        limite = atendimento.calcular_valor_restante() + pagamento.valor_pago
        self.__valida(atendimento, dados["data"], dados["valor_pago"], limite)
        pagamento.data = dados["data"]
        pagamento.valor_pago = dados["valor_pago"]
        self.__tela.mostra_mensagem("Pagamento alterado com sucesso.")

    def listar(self):
        encontrou = False
        for atendimento in self.__controlador_atendimento.atendimentos:
            for pagamento in atendimento.pagamentos:
                self.__tela.mostra_pagamento(atendimento, pagamento)
                encontrou = True
        if not encontrou:
            self.__tela.mostra_mensagem("Nenhum pagamento registrado.")

    def excluir(self):
        atendimento, pagamento = self.__buscar(self.__tela.pega_codigo())
        atendimento.remover_pagamento(pagamento)
        self.__tela.mostra_mensagem("Pagamento excluído com sucesso.")

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