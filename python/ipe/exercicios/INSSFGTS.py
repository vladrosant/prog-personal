nome = input('Insira seu nome: ')
sal = float(input('Informe seu salário: '))
num_dep = int(input('Número de dependentes: '))
if sal/1212>6:
    ftgs = 0.09
    inss = 0.07
elif sal/1212>3:
    fgts = 0.085
    inss = 0.06
else:
    fgts = 0.08
    inss = 0.05
sal_fam = sal*(num_dep*0.05)
sal_liq = (sal+sal_fam)*(1-(fgts-inss))
