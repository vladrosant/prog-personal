import math
a = float(input('Informe o valor do coeficiente ângular da equação:   '))
if a==0:
    print('Valor incorreto.\nEncerrando...')
else:
    b = float(input('Informe o valor do coeficiente linear:    '))
    c = float(input('Informe o ponto de intercessão no eixo Y:    '))
    delta = (b**2)-(4*a*c)
    if delta>0:
        raiz_1 = (-b+(math.sqrt(delta)))/(2*a)
        raiz_2 = (-b-(math.sqrt(delta)))/(2*a)
        print(f'A equação intercepta o eixo X nos pontos {raiz_1} e {raiz_2}')
    elif delta==0:
        raiz_1 = (-b+(math.sqrt(delta)))/(2*a)
        print(f'A equação intercepta o eixo X apenas no ponto {raiz_1}')
    else:
        print('Esta equação não possui raizes reais.')
print(f'{math.pi:.48f}')