##################          EXERCÍCIO 11         ##################
print('Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre: o produto do dobro do primeiro com metade do segundo, a soma do triplo do primeiro com o terceiro, o terceiro elevado ao cubo.\n')

# Solução #
inteiro_1 = int(input('Informe um número inteiro.\n'))
inteiro_2 = int(input('Informe um segundo número inteiro.\n'))
num_real = float(input('Agora digite um número real.\n'))
print(f'O produto do dobro do primeiro com metade do segundo é {(2*inteiro_1)*(inteiro_2/2)}.\nA soma do triplo do primeiro com o terceiro é {(3*inteiro_1)+num_real}.\nO terceiro elevado ao cubo é {num_real**3:.2f}.')
print('\n\n')