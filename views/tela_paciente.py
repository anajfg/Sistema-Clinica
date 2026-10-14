from views.tela_abstrata import TelaAbstrata


class TelaPaciente(TelaAbstrata):
    def tela_opcoes(self) -> int:
        print("\n----- PACIENTES -----")
        print("1 - Incluir")
        print("2 - Alterar")
        print("3 - Listar")
        print("4 - Excluir")
        print("0 - Voltar")
        return self.le_inteiro("Escolha a opção: ", [0, 1, 2, 3, 4])

    def pega_cpf(self) -> str:
        return self.le_cpf("CPF do paciente: ")

    def pega_dados_paciente(self) -> dict:
        return {
            "nome": self.le_texto("Nome: "),
            "celular": self.le_texto("Celular: "),
            "data_nascimento": self.le_data("Data de nascimento (dd/mm/aaaa): "),
        }

    def mostra_paciente(self, paciente):
        print(f"Nome: {paciente.nome} | CPF: {paciente.cpf} | "
              f"Celular: {paciente.celular} | "
              f"Nascimento: {paciente.data_nascimento.strftime('%d/%m/%Y')}")