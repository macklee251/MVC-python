import logging
class Pessoa():
    def __init__(self, nome: str, idade: int, cpf: str) -> None:
        self.nome = nome
        self.idade = idade
        self.cpf = cpf

    def valida_cpf(self) -> bool:
        return True if len(self.cpf) == 11 else False
        
    def __str__(self) -> str:
        return f'Nome: {self.nome}, Idade: {self.idade}, CPF: {self.cpf}'

