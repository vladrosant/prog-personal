##################          EXERCÍCIO 9         ##################
print('Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.\n')

# Solução #
graus_f = float(input('Informe a temperatura em Fahrenheit para fazer a conversão.\n'))
graus_c = (5/9)*(graus_f-32)
print(f'{graus_f} Fahrenheit equivale a {graus_c:.2f} Celsius.')
print('\n\n')