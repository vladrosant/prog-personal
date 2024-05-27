number_max = int(input('Até qual número você deseja ver os primos?\n'))
primos = []
for i in range(2,number_max):
    for j in range(2,10):
        if j>i:
            break
        if i%j==0:
            primos.append(i)
print(primos)