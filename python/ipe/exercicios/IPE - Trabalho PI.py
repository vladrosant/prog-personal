# Nome: Pedro Henrique Ferreira Santana
# RA:   N950625

num_max = int(input('Informe um número para receber uma lista de todos números primos até ele.\n'))
if num_max<2:
    print('Não há números primos menores que 2.')
elif num_max==2:
    print('[2]')
else:
# Abaixo declaro um conjunto de números divisíveis, que sabemos que não são primos, indo até o número maximo de entrada.
    div = list(range(4,num_max+1,2))+list(range(6,num_max+1,3))+list(range(10,num_max+1,5))+list(range(14,num_max+1,7))
# Após isso declaro uma lista de todos os números até a entrada
    todos = list(range(2,num_max+1))
# Procurei como fazer a diferença entre duas listas em python na internet e descobri a função set(), assim posso
# comparar as duas e fazer uma subtração, obtendo a lista da diferença entre os dois conjuntos. Essa lista é composta
# pelos números não divisíveis, vulgo os números primos.
    primos = list(set(todos)-set(div))
# Quando tive o resultado inicialmente estava tudo fora de ordem, então descobri a função sort(), que por padrão
# organiza listas em ordem crescente. Infelizmente isso aumentou o tempo de execução do programa.
# Mas na minha opinião ela é indispensável, ainda mais quando o número de entrada é grande.
    primos.sort()
    print(primos)
# Antes de fazer esse programa final, tentei usando repetições, mas a execução era muito mais demorada.
# Acabei com uma solução parecida com a de Erastótenes, mencionada em classe.