import os
os.system("clear")

class ContaBancaria:
    def __init__(self, banco: str, agencia: str, numeroDaConta: str, tipoDaConta: str, saldoAtual: float, limiteDisponível: float) -> None:
        self.banco = banco
        self.agencia = agencia
        self.numeroDaConta = numeroDaConta
        self.tipoDaConta = tipoDaConta
        self.saldoAtual = saldoAtual
        self.limiteDisponível = limiteDisponível

    def __str__(self) -> str:
        return (f"Banco: {self.banco} \nAgência: {self.agencia} \nNúmero da Conta: {self.numeroDaConta} \nTipo da Conta: {self.tipoDaConta} \nSaldo Atual: {self.saldoAtual} \nLimite Disponível: {self.limiteDisponível}")
    
    
    