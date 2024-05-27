from imc_funcoes import *

loop = "S"
while loop in {"S","s", "Sim", "SIM", "sim"}:
    ShowMenu()
    n = int(input())
    while n<1 or n>3:
        print('\n---------- ENTRADA INVÁLIDA! ----------')
        ShowMenu()
        n = int(input())
    if n!=3:
        altura = float(input("\nDigite sua altura: "))
        if n==1:
            op1(altura)
        if n==2:
            op2(altura)
    else:
        ClearScreen()
    loop = input("\nDeseja executar novamente? (S/N): ")
ClearScreen()