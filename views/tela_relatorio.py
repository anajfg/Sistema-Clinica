from views.tela_abstrata import TelaAbstrata


class TelaRelatorio(TelaAbstrata):
    def tela_opcoes(self) -> int:
        print("\n----- RELATÓRIOS -----")
        print("1 - Clínicas com maior número de atendimentos")
        print("2 - Atendimentos mais caros e mais baratos")
        print("3 - Procedimentos mais realizados")
        print("4 - Procedimentos mais caros e mais baratos")
        print("0 - Voltar")
        return self.le_inteiro("Escolha a opção: ", [0, 1, 2, 3, 4])

    def mostra_clinicas_por_atendimentos(self, ranking: list):
        print("\n== Clínicas com maior número de atendimentos ==")
        for posicao, (clinica, quantidade) in enumerate(ranking, start=1):
            print(f"{posicao}º - {clinica.nome} ({clinica.cidade}): "
                  f"{quantidade} atendimento(s)")

    def __linha_atendimento(self, atendimento) -> str:
        return (f"Código {atendimento.codigo} | {atendimento.clinica.nome} | "
                f"Paciente: {atendimento.paciente.nome} | "
                f"{atendimento.data.strftime('%d/%m/%Y')} | "
                f"R$ {atendimento.valor:.2f}")

    def mostra_atendimentos_extremos(self, mais_caros: list, mais_baratos: list):
        print("\n== Atendimento(s) mais caro(s) ==")
        for atendimento in mais_caros:
            print(self.__linha_atendimento(atendimento))
        print("\n== Atendimento(s) mais barato(s) ==")
        for atendimento in mais_baratos:
            print(self.__linha_atendimento(atendimento))

    def mostra_procedimentos_populares(self, ranking: list):
        print("\n== Procedimentos mais realizados ==")
        for posicao, (descricao, quantidade) in enumerate(ranking, start=1):
            print(f"{posicao}º - {descricao}: {quantidade} vez(es)")

    def __linha_procedimento(self, atendimento, procedimento) -> str:
        return (f"{procedimento.descricao} | Atendimento {atendimento.codigo} | "
                f"Responsável: {procedimento.profissional.nome} | "
                f"R$ {procedimento.custo:.2f}")

    def mostra_procedimentos_extremos(self, mais_caros: list, mais_baratos: list):
        print("\n== Procedimento(s) mais caro(s) ==")
        for atendimento, procedimento in mais_caros:
            print(self.__linha_procedimento(atendimento, procedimento))
        print("\n== Procedimento(s) mais barato(s) ==")
        for atendimento, procedimento in mais_baratos:
            print(self.__linha_procedimento(atendimento, procedimento))