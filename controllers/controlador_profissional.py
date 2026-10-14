from exception.cpf_duplicado_exception import CpfDuplicadoException
from exception.objeto_nao_encontrado_exception import ObjetoNaoEncontradoException
from exception.sistema_exception import SistemaException
from models.profissional_saude import ProfissionalSaude
from views.tela_profissional import TelaProfissional


class ControladorProfissional:
    def __init__(self):
        self.__profissionais = []
        self.__tela = TelaProfissional()

    @property
    def profissionais(self):
        return self.__profissionais

    def buscar_por_cpf(self, cpf: str) -> ProfissionalSaude:
        for profissional in self.__profissionais:
            if profissional.cpf == cpf:
                return profissional
        raise ObjetoNaoEncontradoException("Profissional não encontrado.")

    def incluir(self):
        cpf = self.__tela.pega_cpf()
        if any(p.cpf == cpf for p in self.__profissionais):
            raise CpfDuplicadoException()
        dados = self.__tela.pega_dados_profissional()
        profissional = ProfissionalSaude(dados["nome"], dados["celular"], cpf,
                                         dados["especialidade"],
                                         dados["registro_profissional"])
        self.__profissionais.append(profissional)
        self.__tela.mostra_mensagem("Profissional incluído com sucesso.")

    def alterar(self):
        profissional = self.buscar_por_cpf(self.__tela.pega_cpf())
        dados = self.__tela.pega_dados_profissional()
        profissional.nome = dados["nome"]
        profissional.celular = dados["celular"]
        profissional.especialidade = dados["especialidade"]
        profissional.registro_profissional = dados["registro_profissional"]
        self.__tela.mostra_mensagem("Profissional alterado com sucesso.")

    def listar(self):
        if not self.__profissionais:
            self.__tela.mostra_mensagem("Nenhum profissional cadastrado.")
            return
        for profissional in self.__profissionais:
            self.__tela.mostra_profissional(profissional)

    def excluir(self):
        profissional = self.buscar_por_cpf(self.__tela.pega_cpf())
        self.__profissionais.remove(profissional)
        self.__tela.mostra_mensagem("Profissional excluído com sucesso.")

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