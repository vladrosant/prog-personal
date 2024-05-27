##################          EXERCÍCIO 17         ##################
print('Programa da loja de tintas complicado.\n')

# Solução #
area_simples = float(input('Informe a área para ser pintada em metros quadrados.\n'))
while area_simples<=0:
    area_simples = float(input('Número inválido. Tente novamente.\n'))
else:
    latas_18L = int(area_simples/108)
    latas_3L = int(area_simples/21.6)
    if (area_simples%108)!=0:
        latas_18L+=1
    if (area_simples%21.6)!=0:
        latas_3L+=1
    latas_hib_18L = int((area_simples*1.1)/108)
    latas_hib_3L = int((area_simples*1.1)/21.6)
    if (((area_simples*1.1)%108)%21.6)!=0:
        latas_hib_3L+=1
    print(f'Suas opções sao:\n{latas_18L} latas de 18 litros por R${latas_18L*80:.2f};\n{latas_3L} latas de 3.6 litros por R${latas_3L*25:.2f};\n{latas_hib_18L} latas de 18 litros e {latas_hib_3L} latas de 3.6 litros por R${(latas_hib_18L*80)+(latas_hib_3L*25):.2f}.')
    print('\n\n')