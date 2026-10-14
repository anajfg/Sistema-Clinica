from exception.objeto_nao_encontrado_exception import ObjetoNaoEncontradoException
from exception.sistema_exception import SistemaException
from exception.valor_invalido_exception import ValorInvalidoException
from models.clinica import Clinica
from views.tela_clinica import TelaClinica


class ControladorClinica:
    def __init__(self, controlador_profissional):
        self.__clinicas = []
        self.__controlador_profissional = controlador_profissional
        self.__tela = TelaClinica()

    @property
    def clinicas(self):
        return self.__clinicas

    def buscar_por_nome(self, nome: str) -> Clinica:
        for clinica in self.__clinicas:
            if clinica.nome.lower() == nome.lower():
                return clinica
        raise ObjetoNaoEncontradoException("Clínica não encontrada.")

    def __valida_horario(self, abertura, fechamento):
        if abertura >= fechamento:
            raise ValorInvalidoException(
                "O horário de abertura deve ser anterior ao de fechamento.")

    def incluir(self):
        nome = self.__tela.pega_nome()
        if any(c.nome.lower() == nome.lower() for c in self.__clinicas):
            raise ValorInvalidoException("Já existe uma clínica com este nome.")
        dados = self.__tela.pega_dados_clinica()
        self.__valida_horario(dados["hora_abertura"], dados["hora_fechamento"])
        clinica = Clinica(nome, dados["cidade"], dados["descricao"],
                          dados["hora_abertura"], dados["hora_fechamento"])
        self.__clinicas.append(clinica)
        self.__tela.mostra_mensagem("Clínica incluída com sucesso.")

    def alterar(self):
        clinica = self.buscar_por_nome(self.__tela.pega_nome())
        dados = self.__tela.pega_dados_clinica()
        self.__valida_horario(dados["hora_abertura"], dados["hora_fechamento"])
        clinica.cidade = dados["cidade"]
        clinica.descricao = dados["descricao"]
        clinica.hora_abertura = dados["hora_abertura"]
        clinica.hora_fechamento = dados["hora_fechamento"]
        self.__tela.mostra_mensagem("Clínica alterada com sucesso.")

    def listar(self):
        if not self.__clinicas:
            self.__tela.mostra_mensagem("Nenhuma clínica cadastrada.")
            return
        for clinica in self.__clinicas:
            self.__tela.mostra_clinica(clinica)

    def excluir(self):
        clinica = self.buscar_por_nome(self.__tela.pega_nome())
        self.__clinicas.remove(clinica)
        self.__tela.mostra_mensagem("Clínica excluída com sucesso.")

    def vincular_profissional(self):
        clinica = self.buscar_por_nome(self.__tela.pega_nome())
        profissional = self.__controlador_profissional.buscar_por_cpf(
            self.__tela.pega_cpf_profissional())
        clinica.adicionar_profissional(profissional)
        self.__tela.mostra_mensagem("Profissional vinculado à clínica.")

    def desvincular_profissional(self):
        clinica = self.buscar_por_nome(self.__tela.pega_nome())
        profissional = self.__controlador_profissional.buscar_por_cpf(
            self.__tela.pega_cpf_profissional())
        clinica.remover_profissional(profissional)
        self.__tela.mostra_mensagem("Profissional desvinculado da clínica.")

    def abre_tela(self):
        opcoes = {1: self.incluir, 2: self.alterar, 3: self.listar,
                  4: self.excluir, 5: self.vincular_profissional,
                  6: self.desvincular_profissional}
        while True:
            opcao = self.__tela.tela_opcoes()
            if opcao == 0:
                return
            try:
                opcoes[opcao]()
            except SistemaException as e:
                self.__tela.mostra_mensagem(str(e))