def calc_dias(total_goraca, diario_goraca, total_deja, diario_deja):
    days = 0

    while total_deja <= total_goraca:
        days += 1
        total_goraca += diario_goraca
        total_deja += diario_deja
    return days

# teste 
total_goraca = 217930581705
diario_goraca = 161080181
total_deja = 200232727038
diario_deja = 256647002

resultado_dias = calc_dias(total_goraca, diario_goraca, total_deja, diario_deja)
print("Deja passará Goraca em", resultado_dias, "dias. Será?")