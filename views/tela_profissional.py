from views.tela_abstrata import TelaAbstrata


class TelaProfissional(TelaAbstrata):
    def tela_opcoes(self) -> int:
        print("\n----- PROFISSIONAIS DE SAÚDE -----")
        print("1 - Incluir")
        print("2 - Alterar")
        print("3 - Listar")
        print("4 - Excluir")
        print("0 - Voltar")
        return self.le_inteiro("Escolha a opção: ", [0, 1, 2, 3, 4])

    def pega_cpf(self) -> str:
        return self.le_cpf("CPF do profissional: ")

    def pega_dados_profissional(self) -> dict:
        return {
            "nome": self.le_texto("Nome: "),
            "celular": self.le_texto("Celular: "),
            "especialidade": self.le_texto("Especialidade: "),
            "registro_profissional": self.le_texto("Registro profissional: "),
        }

    def mostra_profissional(self, profissional):
        print(f"Nome: {profissional.nome} | CPF: {profissional.cpf} | "
              f"Celular: {profissional.celular} | "
              f"Especialidade: {profissional.especialidade} | "
              f"Registro: {profissional.registro_profissional}")