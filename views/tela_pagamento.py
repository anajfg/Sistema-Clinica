from views.tela_abstrata import TelaAbstrata


class TelaPagamento(TelaAbstrata):
    MODALIDADES = {1: "Dinheiro", 2: "PIX", 3: "Cartão de crédito"}

    def tela_opcoes(self) -> int:
        print("\n----- PAGAMENTOS -----")
        print("1 - Incluir")
        print("2 - Alterar (data e valor)")
        print("3 - Listar")
        print("4 - Excluir")
        print("0 - Voltar")
        return self.le_inteiro("Escolha a opção: ", [0, 1, 2, 3, 4])

    def pega_codigo_atendimento(self) -> int:
        return self.le_inteiro("Código do atendimento: ")

    def pega_codigo(self) -> int:
        return self.le_inteiro("Código do pagamento: ")

    def le_numero_cartao(self) -> str:
        while True:
            numero = input("Número do cartão: ").replace(" ", "")
            if numero.isdigit() and 13 <= len(numero) <= 19:
                return numero
            print("Número de cartão inválido.")

    def pega_dados_pagamento(self) -> dict:
        dados = {
            "data": self.le_data("Data do pagamento (dd/mm/aaaa): "),
            "valor_pago": self.le_decimal_positivo("Valor pago: "),
            "cpf_pagador": None,
            "numero_cartao": None,
            "bandeira": None,
        }
        print("1 - Dinheiro | 2 - PIX | 3 - Cartão de crédito")
        opcao = self.le_inteiro("Modalidade: ", [1, 2, 3])
        dados["modalidade"] = self.MODALIDADES[opcao]
        if opcao == 2:
            dados["cpf_pagador"] = self.le_cpf("CPF do pagador: ")
        elif opcao == 3:
            dados["numero_cartao"] = self.le_numero_cartao()
            dados["bandeira"] = self.le_texto("Bandeira: ")
        return dados

    def pega_dados_alteracao(self) -> dict:
        return {
            "data": self.le_data("Nova data do pagamento (dd/mm/aaaa): "),
            "valor_pago": self.le_decimal_positivo("Novo valor pago: "),
        }

    def mostra_pagamento(self, atendimento, pagamento):
        extra = ""
        if pagamento.cpf_pagador:
            extra = f" | CPF do pagador: {pagamento.cpf_pagador}"
        if pagamento.numero_cartao:
            extra = (f" | Cartão final {pagamento.numero_cartao[-4:]} "
                     f"({pagamento.bandeira})")
        print(f"Código: {pagamento.codigo} | Atendimento: {atendimento.codigo} | "
              f"Paciente: {atendimento.paciente.nome} | "
              f"Data: {pagamento.data.strftime('%d/%m/%Y')} | "
              f"Valor pago: R$ {pagamento.valor_pago:.2f} | "
              f"Modalidade: {pagamento.modalidade}{extra} | "
              f"Restante do atendimento: R$ {atendimento.calcular_valor_restante():.2f}")