##################          EXERCÍCIO 16         ##################
print('Programa da loja de tintas.\n')

# Solução #
area_pintar = float(input('Informe a área para ser pintada em metros quadrados.\n'))
latas_tinta = area_pintar/54
if latas_tinta%54!=0:
    latas_tinta=latas_tinta+1
print(f'Quantidade de latas para realizar a pintura: {int(latas_tinta)}.\nO preço da pintura é R${int(latas_tinta)*80:.2f}.')
print('\n\n')