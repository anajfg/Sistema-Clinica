from views.tela_abstrata import TelaAbstrata


class TelaSistema(TelaAbstrata):
    def tela_opcoes(self) -> int:
        print("\n========== SISTEMA DE CLÍNICAS ==========")
        print("--- Cadastros ---")
        print("1 - Pacientes")
        print("2 - Profissionais de saúde")
        print("3 - Clínicas")
        print("4 - Tipos de atendimento")
        print("\n--- Registros ---")
        print("5 - Atendimentos")
        print("6 - Procedimentos")
        print("7 - Pagamentos")
        print("\n--- Relatórios ---")
        print("8 - Relatórios")
        print("0 - Sair")
        return self.le_inteiro("Escolha a opção: ", [0, 1, 2, 3, 4, 5, 6, 7, 8])