from views.tela_abstrata import TelaAbstrata


class TelaClinica(TelaAbstrata):
    def tela_opcoes(self) -> int:
        print("\n----- CLÍNICAS -----")
        print("1 - Incluir")
        print("2 - Alterar")
        print("3 - Listar")
        print("4 - Excluir")
        print("5 - Vincular profissional")
        print("6 - Desvincular profissional")
        print("0 - Voltar")
        return self.le_inteiro("Escolha a opção: ", [0, 1, 2, 3, 4, 5, 6])

    def pega_nome(self) -> str:
        return self.le_texto("Nome da clínica: ")

    def pega_cpf_profissional(self) -> str:
        return self.le_cpf("CPF do profissional: ")

    def pega_dados_clinica(self) -> dict:
        return {
            "cidade": self.le_texto("Cidade: "),
            "descricao": self.le_texto("Descrição: "),
            "hora_abertura": self.le_hora("Horário de abertura (hh:mm): "),
            "hora_fechamento": self.le_hora("Horário de fechamento (hh:mm): "),
        }

    def mostra_clinica(self, clinica):
        nomes = ", ".join(p.nome for p in clinica.profissionais) or "nenhum"
        print(f"Nome: {clinica.nome} | Cidade: {clinica.cidade} | "
              f"Descrição: {clinica.descricao} | "
              f"Funcionamento: {clinica.hora_abertura.strftime('%H:%M')} "
              f"às {clinica.hora_fechamento.strftime('%H:%M')} | "
              f"Profissionais: {nomes}")