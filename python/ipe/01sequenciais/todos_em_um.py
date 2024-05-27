##################          EXERCÍCIO 1         ##################
print('Exercício 1: Faça um Programa que mostre a mensagem "Alo mundo" na tela.\n')

# Solução #
print("Alo mundo")
print('\n\n')




##################          EXERCÍCIO 2         ##################
print('Exercício 2: Faça um Programa que peça umn número e então mostre a mensagem "O número informado foi [número].\n')

# Solução #
numero_de_entrada = float(input("Digite um número qualquer.\n"))       # declaração de uma variável para o número de entrada junto ao seu prompt
print(f"O número informado foi {numero_de_entrada}.")
print("\n\n")




##################          EXERCÍCIO 3         ##################
print('Exercício 3: Faça um Programa que peça dois números e imprima a soma.\n')

# Solução # 
print('Informe dois números')
numero_1 = float(input())
numero_2 = float(input())
print(f"A soma dos dois números informados é {numero_1+numero_2}")
print("\n\n")




##################          EXERCÍCIO 4         ##################
print('Faça um Programa que peça as 4 notas bimestrais e mostre a média.\n')

# Solução #
print('Informe suas quatro notas bimestrais para descobrir sua média.')
nota_1 = float(input("Primeiro nota bimestral: "))
nota_2 = float(input("Segunda nota bimestral: "))
nota_3 = float(input("Terceira nota bimestral: "))
nota_4 = float(input("Quarta nota bimestral: "))
print(f'Sua média é {(nota_1+nota_2+nota_3+nota_4)/4:.2f}. Bom trabalho!')      # equação para nota bimestral declarada dentro do print de solução
print('\n\n')




##################          EXERCÍCIO 5         ##################
print('Faça um Programa que converta metros para centímetros.\n')

# Solução #
entrada_metros = float(input('Informe o comprimento em metros.\n'))
print(f'Após a conversão, o valor é {entrada_metros*100}cm.')
print('\n\n')




##################          EXERCÍCIO 6         ##################
print('Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.\n')

# Solução #
raio = float(input('Informe o raio do círculo para calcular sua área.\n'))
print(f'A área do círculo cujo raio mede {raio}um é {3.1415*(raio**2):.2f}um².')        # novamente calculando o resultado dentro do print
print('\n\n')




##################          EXERCÍCIO 7         ##################
print('Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.\n')

# Solução #
comprimento_lado = float(input('Informe o comprimento do lado do quadrado.\n'))
print(f'A área do quadrado de lado {comprimento_lado} é {comprimento_lado**2} e seu dobro é {(comprimento_lado**2)*2}.')
print('\n\n')




##################          EXERCÍCIO 8         ##################
print('Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.\n')

# Solução #
salario_por_horas = float(input('Informe seu ganho por hora.\n'))
horas_trabalhadas = int(input('Quantas horas você trabalha no mês?\n'))
salario_mensal = horas_trabalhadas*salario_por_horas
print(f'Seu salário total no mês é de R${salario_mensal:.2f}.')
print('\n\n')




##################          EXERCÍCIO 9         ##################
print('Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.\n')

# Solução #
graus_f = float(input('Informe a temperatura em Fahrenheit para fazer a conversão.\n'))
graus_c = (5/9)*(graus_f-32)
print(f'{graus_f} Fahrenheit equivale a {graus_c:.2f} Celsius.')
print('\n\n')




##################          EXERCÍCIO 10         ##################
print('Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.\n')

# Solução #
graus_c = float(input('Informe a temperatura em Celsius para fazer a conversão.\n'))
graus_f = ((9/5)*(graus_c))+32
print(f'{graus_c} Celsius equivale a {graus_f:.2f} Fahrenheit.')
print('\n\n')




##################          EXERCÍCIO 11         ##################
print('Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre: o produto do dobro do primeiro com metade do segundo, a soma do triplo do primeiro com o terceiro, o terceiro elevado ao cubo.\n')

# Solução #
inteiro_1 = int(input('Informe um número inteiro.\n'))
inteiro_2 = int(input('Informe um segundo número inteiro.\n'))
num_real = float(input('Agora digite um número real.\n'))
print(f'O produto do dobro do primeiro com metade do segundo é {(2*inteiro_1)*(inteiro_2/2)}.\nA soma do triplo do primeiro com o terceiro é {(3*inteiro_1)+num_real}.\nO terceiro elevado ao cubo é {num_real**3:.2f}.')
print('\n\n')




##################          EXERCÍCIO 12         ##################
print('Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58\n')

# Solução #
altura = float(input('Informe sua altura em metros.\n'))
peso_ideal = (72.7*altura)-58
print(f'O peso ideal para sua altura é {peso_ideal:.1f}.')
print('\n\n')




##################          EXERCÍCIO 13         ##################
print('Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas: Para homens: (72.7*h) - 58; Para mulheres: (62.1*h) - 44.7.\n')

# Solução #
altura = float(input('Informe sua altura em metros.\n'))
peso_ideal_m = (72.7*altura)-58
peso_ideal_f = (62.1*altura)-44.7
print(f'O peso ideal para sua altura é:\n{peso_ideal_m:.1f} para homens e {peso_ideal_f:.1f} para mulheres.')
print('\n\n')




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




##################          EXERCÍCIO 16         ##################
print('Programa da loja de tintas.\n')

# Solução #
area_pintar = float(input('Informe a área para ser pintada em metros quadrados.\n'))
latas_tinta = area_pintar/54
if latas_tinta%54!=0:
    latas_tinta=latas_tinta+1
print(f'Quantidade de latas para realizar a pintura: {int(latas_tinta)}.\nO preço da pintura é R${int(latas_tinta)*80:.2f}.')
print('\n\n')




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



##################          EXERCÍCIO 18         ##################
print('Programa de velocidade de download.\n')

# Solução #
file_size = int(input('Informe o tamanho do arquivo em MB.\n'))
velocidade_internet = int(input('Agora informe a velocidade da sua conexão em Mbps.\n'))
tempo_download = (file_size*8)/velocidade_internet
print(f'O tempo estimado de download é {int(tempo_download/60)} minutos e {int(tempo_download%60)} segundos.')
print('\n\n')