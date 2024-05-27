##################          EXERCÍCIO 12         ##################
print('Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58\n')

# Solução #
altura = float(input('Informe sua altura em metros.\n'))
peso_ideal = (72.7*altura)-58
print(f'O peso ideal para sua altura é {peso_ideal:.1f}.')
print('\n\n')