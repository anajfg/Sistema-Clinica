from abc import ABC
from datetime import date, datetime, time

from exception.opcao_invalida_exception import OpcaoInvalidaException
from exception.valor_invalido_exception import ValorInvalidoException


class TelaAbstrata(ABC):
    def mostra_mensagem(self, mensagem: str):
        print(mensagem)

    def le_texto(self, mensagem: str) -> str:
        while True:
            try:
                texto = input(mensagem).strip()
                if not texto:
                    raise ValorInvalidoException("O campo não pode ficar vazio.")
                return texto
            except ValorInvalidoException as e:
                print(e)

    def le_inteiro(self, mensagem: str, validos: list = None) -> int:
        while True:
            try:
                valor = int(input(mensagem))
                if validos is not None and valor not in validos:
                    raise OpcaoInvalidaException()
                return valor
            except ValueError:
                print("Digite um número inteiro.")
            except OpcaoInvalidaException as e:
                print(e)

    def le_decimal_positivo(self, mensagem: str) -> float:
        while True:
            try:
                valor = float(input(mensagem).replace(",", "."))
                if valor <= 0:
                    raise ValorInvalidoException("O valor deve ser maior que zero.")
                return valor
            except ValueError:
                print("Digite um número válido (ex.: 150,50).")
            except ValorInvalidoException as e:
                print(e)

    def le_data(self, mensagem: str) -> date:
        while True:
            try:
                return datetime.strptime(input(mensagem), "%d/%m/%Y").date()
            except ValueError:
                print("Data inválida. Use o formato dd/mm/aaaa.")

    def le_hora(self, mensagem: str) -> time:
        while True:
            try:
                return datetime.strptime(input(mensagem), "%H:%M").time()
            except ValueError:
                print("Hora inválida. Use o formato hh:mm.")

    def le_cpf(self, mensagem: str) -> str:
        while True:
            try:
                cpf = input(mensagem).replace(".", "").replace("-", "").strip()
                if not (cpf.isdigit() and len(cpf) == 11):
                    raise ValorInvalidoException("CPF inválido. Digite os 11 números.")
                return cpf
            except ValorInvalidoException as e:
                print(e)