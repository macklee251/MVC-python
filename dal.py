from model import Pessoa

class PessoaDal():
    @classmethod
    def write(cls, pessoa: Pessoa):
        with open('pessoas.txt', 'a') as file:
            file.write(f'{pessoa.nome},{pessoa.idade},{pessoa.cpf}\n')
            
    @classmethod
    def read(cls):
        pessoas = []
        with open('pessoas.txt', 'r') as file:
            for linha in file:
                nome, idade, cpf = linha.strip().split(',')
                pessoas.append(Pessoa(nome, idade, cpf))
        return pessoas
    