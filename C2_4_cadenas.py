# Ejemplo 1: ¿Cuántas letras hay?
word = 'by'
print(len(word))  # Salida: 2 (la 'b' y la 'y')


# Ejemplo 2: Cadena vacía
empty = ''
print(len(empty)) # Salida: 0 (no hay nada adentro)


# Ejemplo 3:
# La \ no cuenta porque es solo un aviso para Python.
# \' significa una comilla
i_am = 'I\'m'
print(len(i_am))  # Salida: 3 (la 'I', la comilla y la 'm')

print("\n")
print("Cadenas Multilinea")
# Las comillas triples (''' o """) sirven para textos de varias líneas
multiline = '''Línea #1
Línea #2'''
# "Línea #1" -> 8 caracteres
# El "Enter" (salto de línea) -> 1 carácter (invisible, pero cuenta)
# "Línea #2" -> 8 caracteres
# TOTAL: 8 + 1 + 8 = 17

print(len(multiline))
print("\n")

print("Operaciones con cadenas")

str1 = 'a'
str2 = 'b'

# Concatenación (Sumar cadenas): Pega una después de la otra
print(str1 + str2)  # Salida: ab
print(str2 + str1)  # Salida: ba

# Replicación (Multiplicar cadenas): Repite el texto varias veces
print(5 * 'a')      # Salida: aaaaa
print('b' * 4)      # Salida: bbbb