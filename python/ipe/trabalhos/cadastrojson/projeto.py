import os
from modulo import *

# projeto incompleto.. estava fazendo com lista de dicionarios quando percebi que era com json.

opc = 0
alunos = []
while opc!=5:
    ExibirMenu()
    opc = int(input())
    while opc<1 and opc>5:
           print('Entrada inválida!')
           ExibirMenu()
    if opc==1:
        cadastro = json.load(open('lista.json'))
        info = CadastrarAluno()
        cadastro.append(info)
        LimparTela()
        pass
    elif opc==2:
        ExibeLista()
        LimparTela()
        pass
    elif opc==3:
        BuscarID()
        LimparTela()
        pass
    elif opc==4:
        #filtrar
        LimparTela()
        pass
    elif opc==5:
        #perguntareSalvar
        LimparTela()
        pass
    else:
        print('Opção inválida!')
        LimparTela()        