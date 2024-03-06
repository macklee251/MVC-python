from controller import PessoaControler
from dal import PessoaDal
while True:
    decisao = input('1 - Cadastrar \n2 - Listar\n')
    if decisao == '1':
        nome = input('Nome: ')
        idade = int(input('Idade: '))
        cpf = input('CPF: ')
        PessoaControler.cadastrar(nome, idade, cpf)
        break
    elif decisao == '2':
        for pessoa in PessoaDal.read():
            print(pessoa)
        break
    else:
        print("Try again!")
        
    