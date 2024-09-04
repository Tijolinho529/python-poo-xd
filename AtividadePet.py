import os
os.system("clear")

class Pet:
    def __init__(self, nome: str, idade: int, raca: str, porte: str, alimentacao: str) -> None:
        self.nome = nome
        self.idade = idade
        self.raca = raca
        self.porte = porte
        self.alimentacao = alimentacao

    def exibir_dados(self) -> str:
        return f"Nome: {self.nome} \nIdade: {self.idade} \nRaça: {self.raca} \nPorte: {self.porte} \nAlimentação: {self.alimentacao}"
    
pet = Pet("Sacaninha", 6, "Salsicha Preto", "Pequeno", "Comida")

print(pet.exibir_dados())

