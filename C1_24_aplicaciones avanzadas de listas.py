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

print("\n")

print("Naturaleza multidimensional de las listas")

# ---------------------------------------------------
# MATRIZ BIDIMENSIONAL: REGISTRO DE TEMPERATURAS
# ---------------------------------------------------

# Creamos una matriz de 31 días y 24 horas
# Cada valor representa una temperatura (float)
temps = [[0.0 for h in range(24)] for d in range(31)]

# Simulación: llenar la matriz con algunos valores de temperatura
# (solo para que el programa tenga datos)
for day in range(31):
    for hour in range(24):
        temps[day][hour] = 15 + (hour * 0.3) + (day * 0.1)

# ---------------------------------------------------
# PROMEDIO DE TEMPERATURA AL MEDIODÍA
# ---------------------------------------------------

# El índice 11 representa el mediodía
total = 0.0

for day in temps:
    total += day[11]

average = total / 31

print("Temperatura promedio al mediodía:", average)


# ---------------------------------------------------
# TEMPERATURA MÁS ALTA DEL MES
# ---------------------------------------------------

highest = -100.0

# Se recorren todos los días
for day in temps:

    # Se recorren todas las horas del día
    for temp in day:

        if temp > highest:
            highest = temp

print("La temperatura más alta fue:", highest)


# ---------------------------------------------------
# CONTAR DÍAS CALUROSOS
# ---------------------------------------------------

# Días donde al mediodía hubo más de 20 grados
hot_days = 0

for day in temps:
    if day[11] > 20.0:
        hot_days += 1

print("Días calurosos:", hot_days)


# ---------------------------------------------------
# ARREGLO TRIDIMENSIONAL (HOTEL)
# ---------------------------------------------------

print("\nSistema de habitaciones de hotel")

# 3 edificios, 15 pisos, 20 habitaciones
# False = habitación libre
# True = habitación ocupada
rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]


# ---------------------------------------------------
# RESERVAR HABITACIÓN
# ---------------------------------------------------

# Segundo edificio, décimo piso, habitación 14
rooms[1][9][13] = True

print("Habitación reservada para recién casados")


# ---------------------------------------------------
# DESOCUPAR HABITACIÓN
# ---------------------------------------------------

# Primer edificio, quinto piso, habitación 2
rooms[0][4][1] = False

print("Habitación liberada")


# ---------------------------------------------------
# CONTAR HABITACIONES DISPONIBLES
# ---------------------------------------------------

# Piso 15 del edificio 3
vacancy = 0

for room_number in range(20):

    if not rooms[2][14][room_number]:
        vacancy += 1

print("Habitaciones disponibles en el piso 15 del edificio 3:", vacancy)