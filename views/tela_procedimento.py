from views.tela_abstrata import TelaAbstrata


class TelaProcedimento(TelaAbstrata):
    def tela_opcoes(self) -> int:
        print("\n----- PROCEDIMENTOS -----")
        print("1 - Incluir")
        print("2 - Alterar")
        print("3 - Listar")
        print("4 - Excluir")
        print("0 - Voltar")
        return self.le_inteiro("Escolha a opção: ", [0, 1, 2, 3, 4])

    def pega_codigo_atendimento(self) -> int:
        return self.le_inteiro("Código do atendimento: ")

    def pega_codigo(self) -> int:
        return self.le_inteiro("Código do procedimento: ")

    def pega_dados_procedimento(self) -> dict:
        return {
            "descricao": self.le_texto("Descrição: "),
            "custo": self.le_decimal_positivo("Custo: "),
            "cpf_profissional": self.le_cpf("CPF do profissional responsável: "),
        }

    def mostra_procedimento(self, atendimento, procedimento):
        print(f"Código: {procedimento.codigo} | Atendimento: {atendimento.codigo} | "
              f"Descrição: {procedimento.descricao} | "
              f"Custo: R$ {procedimento.custo:.2f} | "
              f"Responsável: {procedimento.profissional.nome}")