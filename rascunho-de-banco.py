class ContaBancaria:
    def __init__(self, numero_conta, saldo_inicial=0):
        self.numero_conta = numero_conta
        self.saldo = saldo_inicial

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de {valor} realizado. Novo saldo: {self.saldo}")
        else:
            print("Valor inválido para depósito.")

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de {valor} realizado. Novo saldo: {self.saldo}")
        else:
            print("Saldo insuficiente ou valor inválido para saque.")

    def exibir_saldo(self):
        print(f"Saldo da conta {self.numero_conta}: {self.saldo}")


conta = ContaBancaria("12345", 1000)
conta.exibir_saldo()
conta.depositar(500)
conta.sacar(300)
conta.exibir_saldo()