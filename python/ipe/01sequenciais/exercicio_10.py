##################          EXERCÍCIO 10         ##################
print('Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.\n')

# Solução #
graus_c = float(input('Informe a temperatura em Celsius para fazer a conversão.\n'))
graus_f = ((9/5)*(graus_c))+32
print(f'{graus_c} Celsius equivale a {graus_f:.2f} Fahrenheit.')
print('\n\n')