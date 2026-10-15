from views.tela_abstrata import TelaAbstrata


class TelaAtendimento(TelaAbstrata):
    def tela_opcoes(self) -> int:
        print("\n----- ATENDIMENTOS -----")
        print("1 - Incluir")
        print("2 - Alterar")
        print("3 - Listar")
        print("4 - Excluir")
        print("0 - Voltar")
        return self.le_inteiro("Escolha a opção: ", [0, 1, 2, 3, 4])

    def pega_codigo(self) -> int:
        return self.le_inteiro("Código do atendimento: ")

    def pega_dados_atendimento(self) -> dict:
        return {
            "nome_clinica": self.le_texto("Nome da clínica: "),
            "cpf_paciente": self.le_cpf("CPF do paciente: "),
            "cpf_profissional": self.le_cpf("CPF do profissional: "),
            "codigo_tipo": self.le_inteiro("Código do tipo de atendimento: "),
            "data": self.le_data("Data (dd/mm/aaaa): "),
            "hora_inicio": self.le_hora("Hora de início (hh:mm): "),
            "hora_fim": self.le_hora("Hora de fim (hh:mm): "),
            "valor": self.le_decimal_positivo("Valor: "),
        }

    def pega_dados_alteracao(self) -> dict:
        return {
            "data": self.le_data("Nova data (dd/mm/aaaa): "),
            "hora_inicio": self.le_hora("Nova hora de início (hh:mm): "),
            "hora_fim": self.le_hora("Nova hora de fim (hh:mm): "),
            "valor": self.le_decimal_positivo("Novo valor: "),
        }

    def mostra_atendimento(self, atendimento):
        pago = sum(p.valor_pago for p in atendimento.pagamentos)
        print(f"Código: {atendimento.codigo} | Clínica: {atendimento.clinica.nome} | "
              f"Paciente: {atendimento.paciente.nome} | "
              f"Profissional: {atendimento.profissional.nome} | "
              f"Tipo: {atendimento.tipo_atendimento.descricao} | "
              f"{atendimento.data.strftime('%d/%m/%Y')} "
              f"{atendimento.hora_inicio.strftime('%H:%M')}-"
              f"{atendimento.hora_fim.strftime('%H:%M')} | "
              f"Valor: R$ {atendimento.valor:.2f} | Pago: R$ {pago:.2f} | "
              f"Restante: R$ {atendimento.calcular_valor_restante():.2f}")