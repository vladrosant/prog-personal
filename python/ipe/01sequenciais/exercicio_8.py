##################          EXERCÍCIO 8         ##################
print('Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.\n')

# Solução #
salario_por_horas = float(input('Informe seu ganho por hora.\n'))
horas_trabalhadas = int(input('Quantas horas você trabalha no mês?\n'))
salario_mensal = horas_trabalhadas*salario_por_horas
print(f'Seu salário total no mês é de R${salario_mensal:.2f}.')
print('\n\n')