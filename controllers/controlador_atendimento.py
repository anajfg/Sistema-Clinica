from exception.fora_do_horario_clinica_exception import ForaDoHorarioClinicaException
from exception.objeto_nao_encontrado_exception import ObjetoNaoEncontradoException
from exception.paciente_menor_de_idade_exception import PacienteMenorDeIdadeException
from exception.sistema_exception import SistemaException
from exception.valor_invalido_exception import ValorInvalidoException
from models.atendimento import Atendimento
from views.tela_atendimento import TelaAtendimento


class ControladorAtendimento:
    def __init__(self, controlador_clinica, controlador_paciente,
                 controlador_profissional, controlador_tipo_atendimento):
        self.__controlador_clinica = controlador_clinica
        self.__controlador_paciente = controlador_paciente
        self.__controlador_profissional = controlador_profissional
        self.__controlador_tipo = controlador_tipo_atendimento
        self.__atendimentos = []
        self.__proximo_codigo = 1
        self.__tela = TelaAtendimento()

    @property
    def atendimentos(self):
        return self.__atendimentos

    def paciente_possui_atendimento(self, paciente) -> bool:
        return any(a.paciente is paciente for a in self.__atendimentos)

    def clinica_possui_atendimento(self, clinica) -> bool:
        return any(a.clinica is clinica for a in self.__atendimentos)

    def tipo_possui_atendimento(self, tipo) -> bool:
        return any(a.tipo_atendimento is tipo for a in self.__atendimentos)

    def profissional_possui_vinculo(self, profissional) -> bool:
        for atendimento in self.__atendimentos:
            if atendimento.profissional is profissional:
                return True
            if any(p.profissional is profissional for p in atendimento.procedimentos):
                return True
        return False

    def buscar_por_codigo(self, codigo: int) -> Atendimento:
        for atendimento in self.__atendimentos:
            if atendimento.codigo == codigo:
                return atendimento
        raise ObjetoNaoEncontradoException("Atendimento não encontrado.")

    def __valida_maioridade(self, paciente, data_atendimento):
        nasc = paciente.data_nascimento
        idade = (data_atendimento.year - nasc.year
                 - ((data_atendimento.month, data_atendimento.day) < (nasc.month, nasc.day)))
        if idade < 18:
            raise PacienteMenorDeIdadeException()

    def __valida_horario(self, clinica, hora_inicio, hora_fim):
        if hora_inicio >= hora_fim:
            raise ValorInvalidoException("A hora de início deve ser anterior à hora de fim.")
        if hora_inicio < clinica.hora_abertura or hora_fim > clinica.hora_fechamento:
            raise ForaDoHorarioClinicaException()

    def incluir(self):
        dados = self.__tela.pega_dados_atendimento()
        clinica = self.__controlador_clinica.buscar_por_nome(dados["nome_clinica"])
        paciente = self.__controlador_paciente.buscar_por_cpf(dados["cpf_paciente"])
        profissional = self.__controlador_profissional.buscar_por_cpf(dados["cpf_profissional"])
        tipo = self.__controlador_tipo.buscar_por_codigo(dados["codigo_tipo"])
        self.__valida_maioridade(paciente, dados["data"])
        self.__valida_horario(clinica, dados["hora_inicio"], dados["hora_fim"])
        atendimento = Atendimento(self.__proximo_codigo, clinica, paciente,
                                  profissional, tipo, dados["data"],
                                  dados["hora_inicio"], dados["hora_fim"],
                                  dados["valor"])
        self.__atendimentos.append(atendimento)
        self.__tela.mostra_mensagem(
            f"Atendimento incluído com sucesso. Código: {self.__proximo_codigo}")
        self.__proximo_codigo += 1

    def alterar(self):
        atendimento = self.buscar_por_codigo(self.__tela.pega_codigo())
        dados = self.__tela.pega_dados_alteracao()
        self.__valida_maioridade(atendimento.paciente, dados["data"])
        self.__valida_horario(atendimento.clinica, dados["hora_inicio"], dados["hora_fim"])
        total_pago = sum(p.valor_pago for p in atendimento.pagamentos)
        if round(dados["valor"], 2) < round(total_pago, 2):
            raise ValorInvalidoException("O novo valor não pode ser menor que o total já pago.")
        if any(p.data > dados["data"] for p in atendimento.pagamentos):
            raise ValorInvalidoException("Existem pagamentos posteriores à nova data.")
        atendimento.data = dados["data"]
        atendimento.hora_inicio = dados["hora_inicio"]
        atendimento.hora_fim = dados["hora_fim"]
        atendimento.valor = dados["valor"]
        self.__tela.mostra_mensagem("Atendimento alterado com sucesso.")

    def listar(self):
        if not self.__atendimentos:
            self.__tela.mostra_mensagem("Nenhum atendimento cadastrado.")
            return
        for atendimento in self.__atendimentos:
            self.__tela.mostra_atendimento(atendimento)

    def excluir(self):
        atendimento = self.buscar_por_codigo(self.__tela.pega_codigo())
        self.__atendimentos.remove(atendimento)
        self.__tela.mostra_mensagem(
            "Atendimento excluído (seus procedimentos e pagamentos foram removidos junto).")

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