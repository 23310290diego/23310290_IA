#2.3.2
# Suma (+)
print(5 + 3)   # 8

# Resta (-)
print(10 - 4)  # 6

# Multiplicación (*)
print(6 * 2)   # 12

# División normal (/)
print(7 / 2)   # 3.5 → siempre devuelve float

# División entera (//)
print(7 // 2)  # 3 → solo la parte entera

# Módulo (%) → residuo de la división
print(7 % 2)   # 1

# Exponente (**)
print(2 ** 3)  # 8 → 2 elevado a la 3

# * y % tienen la misma prioridad
# Se resuelve de izquierda a derecha
print(2 * 3 % 5)  # (2 * 3) = 6 → 6 % 5 = 1

print(2 + 3 * 4)

# Paso 1: 25 % 13 = 12
# Paso 2: 12 + 100 = 112
# Paso 3: 2 * 13 = 26
# Paso 4: 5 * 112 = 560
# Paso 5: 560 / 26 = 21.53846153846154
# Paso 6: 21.538... // 2 = 10.0
print("nurvo reto (5 * ((25 % 13) + 100) / (2 * 13)) // 2")
print((5 * ((25 % 13) + 100) / (2 * 13)) // 2)