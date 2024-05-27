saldo = float(input('Saldo inicial: '))
debitos = float(input('Total debitado:: '))
creditos = float(input('Valor creditado: '))
saldo_f = saldo + creditos - debitos
print(f'Saldo final: {saldo_f}')
if saldo_f>0:
    print('Saldo final positivo.')  
elif saldo_f<0:
    print('Saldo final negativo.')
else:
    print('Saldo final nulo.')