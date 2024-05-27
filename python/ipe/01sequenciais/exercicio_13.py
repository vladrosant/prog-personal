##################          EXERCÍCIO 13         ##################
print('Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas: Para homens: (72.7*h) - 58; Para mulheres: (62.1*h) - 44.7.\n')

# Solução #
altura = float(input('Informe sua altura em metros.\n'))
peso_ideal_m = (72.7*altura)-58
peso_ideal_f = (62.1*altura)-44.7
print(f'O peso ideal para sua altura é:\n{peso_ideal_m:.1f} para homens e {peso_ideal_f:.1f} para mulheres.')
print('\n\n')