from abc import ABC, abstractmethod
import os
os.system("clear")

class Endereco:
    def __init__(self, logradouro: str, numero: str, complemento: str, cep: str, cidade: str) -> None:
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento
        self.cep = cep
        self.cidade = cidade
        pass

    def __str__(self) -> str:
        return f"Logradouro"
        