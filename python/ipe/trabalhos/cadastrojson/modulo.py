import os
import json


def ExibirMenu():
    print('''
<>----------------------------------------------<>
                    SysAcademy
<>----------------------------------------------<>
    Digite a opção desejada:
1. Cadastrar Aluno
2. Exibir lista de alunos
3. Buscar aluno por ID
4. Filtrar alunos por IMC
5. Sair
<>----------------------------------------------<>
Opção: ''', end='')


def LimparTela():
    input('Pressione qualquer tecla...')
    if os.name =='nt':
        os.system('cls')
    else:
        os.system("clear")


def CadastrarAluno():
    nome = input('Nome: ')
    telefone = int(input('Telefone: '))
    peso = float(input('Peso: '))
    altura = float(input('Altura: '))
    mensalidade = float(input('Mensalidade: '))
    sexo = input('Sexo(F ou M): ')
    aluno = {
        "id": '',
        "nome": nome,
        "telefone": telefone,
        "peso": peso,
        "altura": altura,
        "mensalidade": mensalidade,
        "sexo": sexo
    }
    return aluno

    
def ExibeLista(alunos):
    for i in range(len(alunos)):
        print(f'{alunos[i]}\n<>----------------------------------------------<>')


def BuscarID():
    id = int(input('Digite o ID do aluno que deseja buscar: '))
    from projeto import alunos
    print(alunos[id])


