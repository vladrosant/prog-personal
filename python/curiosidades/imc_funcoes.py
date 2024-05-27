import os

def ShowMenu():
    print('''
    Escolha uma opção
<>--------------------<>
1. Descobrir seu IMC a partir de seu peso e altura
2. Descobrir o peso necessário para alcançar um IMC
3. Limpar a tela
<>--------------------<>

Opção: ''', end='')

def op1(altura):
    peso = float(input("Peso em kg: "))
    imc = peso/altura**2
    if imc<18.5:
        resultado = "magreza"
    elif imc<25:
        resultado = "normal"
    elif imc<30:
        resultado = "sobrepeso"
    elif imc<35:
        resultado = "obesidade grau I"
    elif imc<40:
        resultado = "obesidade grau II"
    else:
        resultado = "obesidade grau III"
    return(print(f"Seu IMC é {imc:.2f}. Você está na categoria de {resultado}."))

def op2(altura):
    imcx = float(input("IMC desejado: "))
    peso = imcx*(altura**2)
    return(print(f"Para atingir o IMC de {imcx} seu peso deve ser de {peso:.1f}."))

def ClearScreen():
    if os.name =='nt':
        os.system('cls')
    else:
        os.system("clear")



