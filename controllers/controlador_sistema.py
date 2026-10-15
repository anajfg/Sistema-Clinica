from controllers.controlador_atendimento import ControladorAtendimento
from controllers.controlador_clinica import ControladorClinica
from controllers.controlador_pagamento import ControladorPagamento
from controllers.controlador_paciente import ControladorPaciente
from controllers.controlador_procedimento import ControladorProcedimento
from controllers.controlador_profissional import ControladorProfissional
from controllers.controlador_relatorio import ControladorRelatorio
from controllers.controlador_tipo_atendimento import ControladorTipoAtendimento
from views.tela_sistema import TelaSistema


class ControladorSistema:
    def __init__(self):
        self.__tela = TelaSistema()
        self.__paciente = ControladorPaciente()
        self.__profissional = ControladorProfissional()
        self.__clinica = ControladorClinica(self.__profissional)
        self.__tipo = ControladorTipoAtendimento()
        self.__atendimento = ControladorAtendimento(
            self.__clinica, self.__paciente, self.__profissional, self.__tipo)
        self.__procedimento = ControladorProcedimento(
            self.__atendimento, self.__profissional)
        self.__pagamento = ControladorPagamento(self.__atendimento)
        self.__relatorio = ControladorRelatorio(self.__clinica, self.__atendimento)

        # Os cadastros são criados antes do atendimento, então recebem a
        # referência depois (evita dependência circular entre os controladores).
        self.__paciente.vincula_atendimento(self.__atendimento)
        self.__clinica.vincula_atendimento(self.__atendimento)
        self.__tipo.vincula_atendimento(self.__atendimento)
        self.__profissional.vincula_controladores(self.__atendimento, self.__clinica)

    def inicia(self):
        telas = {1: self.__paciente, 2: self.__profissional, 3: self.__clinica,
                 4: self.__tipo, 5: self.__atendimento, 6: self.__procedimento,
                 7: self.__pagamento, 8: self.__relatorio}
        while True:
            opcao = self.__tela.tela_opcoes()
            if opcao == 0:
                self.__tela.mostra_mensagem("Sistema encerrado.")
                return
            telas[opcao].abre_tela()