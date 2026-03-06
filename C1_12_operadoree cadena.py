print('2.6.7 Operadores cadena',"\n")

# Imprime la parte superior de una caja
# "+" se concatena con "-" repetido 10 veces y luego otro "+"
print("+" + 10 * "-" + "+")

# Imprime las paredes de la caja
# "|" es el borde izquierdo
# " " * 10 crea 10 espacios dentro de la caja
# "|\n" cierra la pared derecha y agrega salto de línea
# Todo el patrón se repite 5 veces para crear la altura de la caja
# end="" evita que print agregue un salto de línea extra al final
print(("|" + " " * 10 + "|\n") * 5, end="")

# Imprime la parte inferior de la caja
# Igual que la parte superior
print("+" + 10 * "-" + "+")