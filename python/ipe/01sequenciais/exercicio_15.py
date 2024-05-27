##################          EXERCÍCIO 15         ##################
print('Problema de impostos.\n')

# Solução #
salario_por_horas = float(input('Informe seu salário por hora.\n'))
horas_trabalhadas = int(input('Informe quantas horas você trabalha no mês.\n'))
salario_mensal_bruto = salario_por_horas*horas_trabalhadas
taxa_ir = 0.11*salario_mensal_bruto
taxa_inss = 0.08*salario_mensal_bruto
taxa_sindicato = 0.05*salario_mensal_bruto
print(f'Seu salário bruto é R${salario_mensal_bruto:.2f}.')
print(f'O valor pago ao INSS é R${taxa_inss:.2f}.')
print(f'O valor pago ao sindicato é R${taxa_sindicato:.2f}.')
print(f'Seu salário líquido é R${salario_mensal_bruto-(taxa_ir+taxa_inss+taxa_sindicato):.2f}.')
print('\n\n')