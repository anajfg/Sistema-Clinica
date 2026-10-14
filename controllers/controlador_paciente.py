from exception.cpf_duplicado_exception import CpfDuplicadoException
from exception.objeto_nao_encontrado_exception import ObjetoNaoEncontradoException
from exception.sistema_exception import SistemaException
from models.paciente import Paciente
from views.tela_paciente import TelaPaciente


class ControladorPaciente:
    def __init__(self):
        self.__pacientes = []
        self.__tela = TelaPaciente()

    @property
    def pacientes(self):
        return self.__pacientes

    def buscar_por_cpf(self, cpf: str) -> Paciente:
        for paciente in self.__pacientes:
            if paciente.cpf == cpf:
                return paciente
        raise ObjetoNaoEncontradoException("Paciente não encontrado.")

    def incluir(self):
        cpf = self.__tela.pega_cpf()
        if any(p.cpf == cpf for p in self.__pacientes):
            raise CpfDuplicadoException()
        dados = self.__tela.pega_dados_paciente()
        paciente = Paciente(dados["nome"], dados["celular"], cpf,
                            dados["data_nascimento"])
        self.__pacientes.append(paciente)
        self.__tela.mostra_mensagem("Paciente incluído com sucesso.")

    def alterar(self):
        paciente = self.buscar_por_cpf(self.__tela.pega_cpf())
        dados = self.__tela.pega_dados_paciente()
        paciente.nome = dados["nome"]
        paciente.celular = dados["celular"]
        paciente.data_nascimento = dados["data_nascimento"]
        self.__tela.mostra_mensagem("Paciente alterado com sucesso.")

    def listar(self):
        if not self.__pacientes:
            self.__tela.mostra_mensagem("Nenhum paciente cadastrado.")
            return
        for paciente in self.__pacientes:
            self.__tela.mostra_paciente(paciente)

    def excluir(self):
        paciente = self.buscar_por_cpf(self.__tela.pega_cpf())
        self.__pacientes.remove(paciente)
        self.__tela.mostra_mensagem("Paciente excluído com sucesso.")

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