def fatorial(n):
    if n<0:
        return print('Entrada inválida(número negativo).')
    elif n==0 or n==1:
        return 1
    else:
        return n*fatorial(n-1)
