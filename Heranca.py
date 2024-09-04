from abc import ABC, abstractmethod
import os
os.system("clear")

class Funcionario(ABC):
    def __init__(self) -> None:
        self.nome = nome
        self.salario = salario
        
    @abstractmethod
    def salario_final(self) -> float:
        pass

    def __str__(self) -> str:
        return f"\nNome: {self.nome} \nSalário: {self.salario}"
    
class Motoboy(Funcionario):
    def salario_final(self) -> float:
        resultado = self.salario * self.BONIFICACAO
        return resultado
    
class Engenheiro(Funcionario):
    def __init__(self, nome) -> None:
        super().__init__()
    
motoboy = Motoboy("Salsicha", 300.12)