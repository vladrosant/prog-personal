notas_string = input("Digite suas notas no seguinte formato: n1, n2, n3, n4...\n")
notas_lista = notas_string.split(",")

media = 0.0

for i in range(len(notas_lista)):
    media  += float(notas_lista[i])
media /= len(notas_lista)

print(f"media do semestres: {media:.2f}")