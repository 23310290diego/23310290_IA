print("Listas dentro de listas y matrices en Python")

# En Python una lista puede contener otras listas.
# Esto permite representar estructuras como tablas o tableros.

print("Crear una fila con un bucle")

WHITE_PAWN = "P"

row = []

# Se agregan 8 peones blancos a la fila
for i in range(8):
    row.append(WHITE_PAWN)

print(row)


print("\n")
print("Crear una fila usando comprensión de lista")

# La comprensión de lista permite crear listas de forma más corta
row = [WHITE_PAWN for i in range(8)]

print(row)


print("\n")
print("Ejemplo de comprensión de listas: cuadrados")

# Se crea una lista con los cuadrados de los números del 0 al 9
squares = [x ** 2 for x in range(10)]

print(squares)


print("\n")
print("Ejemplo de comprensión de listas: potencias de 2")

# Se crean las primeras 8 potencias de 2
twos = [2 ** i for i in range(8)]

print(twos)


print("\n")
print("Ejemplo de comprensión de listas: números impares")

# Se crea una lista con solo los números impares de la lista squares
odds = [x for x in squares if x % 2 != 0]

print(odds)


print("\n")
print("Crear un arreglo bidimensional (tablero)")

# Supongamos que EMPTY representa un espacio vacío
EMPTY = "."

board = []

# Se crean 8 filas para el tablero
for i in range(8):

    # Cada fila tendrá 8 espacios vacíos
    row = [EMPTY for i in range(8)]

    # Se agrega la fila al tablero
    board.append(row)

print(board)


print("\n")
print("Crear tablero con comprensión de listas")

# Se crea el mismo tablero 8x8 pero en una sola línea
board = [[EMPTY for i in range(8)] for j in range(8)]

print(board)


print("\n")
print("Acceder a un elemento del tablero")

# Para acceder a un elemento se usan dos índices
# primero la fila y luego la columna
print(board[0][0])