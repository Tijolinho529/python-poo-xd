from enum import Enum
import os
os.system("cls || clear")

class Funcionario:
    def __init__(self, id: str, nome: str, salario: float, setor: Setor, sexo: Sexo, idade: int) -> None:
        self.id: str = id
        self.nome: str = nome
        self.salario: float = salario
        self.setor: Setor = setor
        self.sexo: Sexo = sexo
        self.idade: int = idade

    def exibir_dados(self) -> str:
        return ( f"Id: {self.id}"
                 f"\nNome: {self.nome}"
                 f"\n"
               )    

class Sexo(Enum):
    MASCULINO = "Masculino"
    FEMININO = "Feminino"

class Setor(Enum):
    FINANCEIRO = "Financeira"
    RECURSOS_HUMANOS = "Recursos Humanos"
    VENDAS = "Vendas"
    MARKETING = "Marketing"

print(f"Sexo: {Sexo.FEMININO}")
print(f"Sexo: {Sexo.FEMININO.name}")
print(f"Sexo: {Sexo.FEMININO.value}")

print()
