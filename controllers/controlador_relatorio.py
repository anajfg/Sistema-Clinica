from exception.objeto_nao_encontrado_exception import ObjetoNaoEncontradoException
from exception.sistema_exception import SistemaException
from views.tela_relatorio import TelaRelatorio


class ControladorRelatorio:
    def __init__(self, controlador_clinica, controlador_atendimento):
        self.__controlador_clinica = controlador_clinica
        self.__controlador_atendimento = controlador_atendimento
        self.__tela = TelaRelatorio()

    def __atendimentos(self) -> list:
        atendimentos = self.__controlador_atendimento.atendimentos
        if not atendimentos:
            raise ObjetoNaoEncontradoException("Nenhum atendimento registrado.")
        return atendimentos

    def __procedimentos(self) -> list:
        pares = [(atendimento, procedimento)
                 for atendimento in self.__controlador_atendimento.atendimentos
                 for procedimento in atendimento.procedimentos]
        if not pares:
            raise ObjetoNaoEncontradoException("Nenhum procedimento registrado.")
        return pares

    def clinicas_com_mais_atendimentos(self):
        atendimentos = self.__atendimentos()
        ranking = []
        for clinica in self.__controlador_clinica.clinicas:
            quantidade = sum(1 for a in atendimentos if a.clinica is clinica)
            if quantidade > 0:
                ranking.append((clinica, quantidade))
        ranking.sort(key=lambda item: (-item[1], item[0].nome))
        self.__tela.mostra_clinicas_por_atendimentos(ranking)

    def atendimentos_mais_caros_e_baratos(self):
        atendimentos = self.__atendimentos()
        maior = max(a.valor for a in atendimentos)
        menor = min(a.valor for a in atendimentos)
        mais_caros = [a for a in atendimentos if a.valor == maior]
        mais_baratos = [a for a in atendimentos if a.valor == menor]
        self.__tela.mostra_atendimentos_extremos(mais_caros, mais_baratos)

    def procedimentos_mais_realizados(self):
        contagem = {}
        for _, procedimento in self.__procedimentos():
            chave = " ".join(procedimento.descricao.lower().split())
            if chave in contagem:
                contagem[chave][1] += 1
            else:
                contagem[chave] = [procedimento.descricao.strip(), 1]
        ranking = sorted(contagem.values(), key=lambda item: (-item[1], item[0]))
        self.__tela.mostra_procedimentos_populares(ranking)

    def procedimentos_mais_caros_e_baratos(self):
        pares = self.__procedimentos()
        maior = max(p.custo for _, p in pares)
        menor = min(p.custo for _, p in pares)
        mais_caros = [(a, p) for a, p in pares if p.custo == maior]
        mais_baratos = [(a, p) for a, p in pares if p.custo == menor]
        self.__tela.mostra_procedimentos_extremos(mais_caros, mais_baratos)

    def abre_tela(self):
        opcoes = {1: self.clinicas_com_mais_atendimentos,
                  2: self.atendimentos_mais_caros_e_baratos,
                  3: self.procedimentos_mais_realizados,
                  4: self.procedimentos_mais_caros_e_baratos}
        while True:
            opcao = self.__tela.tela_opcoes()
            if opcao == 0:
                return
            try:
                opcoes[opcao]()
            except SistemaException as e:
                self.__tela.mostra_mensagem(str(e))