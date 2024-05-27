##################          EXERCÍCIO 14         ##################
print('Problema do João Papo-de-Pescador.\n')

# Solução #
peso = float(input('Informe o peso dos peixes.\n'))
excesso = peso-50
multa = int(excesso)*4       # aqui eu peguei só a parte inteira do excesso porque no enunciado diz que a multa é 4 reais para cada quilo excedido
if excesso>0:
    print(f'A multa a ser paga é de R${multa}.00.')
else:
    print('Não há multa a ser paga.')
print('\n\n')