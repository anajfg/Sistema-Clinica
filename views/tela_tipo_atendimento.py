from views.tela_abstrata import TelaAbstrata


class TelaTipoAtendimento(TelaAbstrata):
    def tela_opcoes(self) -> int:
        print("\n----- TIPOS DE ATENDIMENTO -----")
        print("1 - Incluir")
        print("2 - Alterar")
        print("3 - Listar")
        print("4 - Excluir")
        print("0 - Voltar")
        return self.le_inteiro("Escolha a opção: ", [0, 1, 2, 3, 4])

    def pega_codigo(self) -> int:
        return self.le_inteiro("Código do tipo de atendimento: ")

    def pega_descricao(self) -> str:
        return self.le_texto("Descrição (ex.: consulta, exame, retorno): ")

    def mostra_tipo(self, tipo):
        print(f"Código: {tipo.codigo} | Descrição: {tipo.descricao}")