from model import Pessoa
from dal import PessoaDal

class PessoaControler():
    @classmethod
    def cadastrar(cls, nome, idade, cpf):
        if len(nome) > 2 and idade > 0 and len(cpf) == 11:
            pessoa = Pessoa(nome, idade, cpf)
            try:
                PessoaDal.write(pessoa)
                return True
            except:
                return False
        