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

print("\n")
print("Funcion ord y chr")

# ord() hace el camino de IDA: de letra a número
char_1 = 'a'
char_2 = ' '  # Un espacio también es un carácter
print(ord(char_1)) # Salida: 97
print(ord(char_2)) # Salida: 32

# chr() hace el camino de VUELTA: de número a letra
print(chr(97))     # Salida: a
print(chr(945))    # Salida: α

print("\n")
print("Cadenas como secuencias")

the_string = 'silly walks'

# Usamos len() para saber cuántas letras hay y range() para generar los índices
for ix in range(len(the_string)):
    # Imprimimos la letra que está en la posición 'ix'
    # end=' ' hace que las letras salgan seguidas en lugar de una por línea
    print(the_string[ix], end=' ')

print() # Solo para dar un salto de línea al final

print("\n")
print("Rebanadas")

alpha = "abdefg"

# [inicio : fin] -> El "fin" no se incluye
print(alpha[1:3])    # Salida: bd (del índice 1 al 2)

# [inicio : ] -> Desde el inicio hasta el final
print(alpha[3:])     # Salida: efg (del índice 3 hasta acabar)

# [ : fin] -> Desde el principio hasta antes del fin
print(alpha[:3])     # Salida: abd (del inicio al índice 2)

# Con números negativos (contando desde atrás)
print(alpha[3:-2])   # Salida: e (del índice 3 hasta antes de los últimos 2)
print(alpha[-3:4])   # Salida: e (del tercero de atrás para adelante hasta el índice 4)

# [inicio : fin : paso]
print(alpha[::2])    # Salida: adf (salta de 2 en 2: a, d, f)
print(alpha[1::2])   # Salida: beg (empieza en 1 y salta de 2 en 2: b, e, g)

print("\n")
print("Operadores in y not in")
print("Operadores in")

alphabet = "abcdefghijklmnopqrstuvwxyz"

# El operador 'in' busca si un texto está dentro de otro
print("f" in alphabet)      # True (la f sí está)
print("F" in alphabet)      # False (Python distingue entre mayúsculas y minúsculas)
print("1" in alphabet)      # False (el 1 no es parte del abecedario)
print("ghi" in alphabet)    # True (puedes buscar pedazos completos de texto)
print("Xyz" in alphabet)    # False (la X mayúscula hace que no coincida)

print("Operador not in")

alphabet = "abcdefghijklmnopqrstuvwxyz"

# 'not in' devuelve True si el texto NO se encuentra adentro
print("f" not in alphabet)      # False (porque la 'f' SÍ está)
print("F" not in alphabet)      # True (porque la 'F' mayúscula NO está)
print("1" not in alphabet)      # True (porque el '1' NO está)
print("ghi" not in alphabet)    # False (porque 'ghi' SÍ está)
print("Xyz" not in alphabet)    # True (porque 'Xyz' con mayúscula NO está)