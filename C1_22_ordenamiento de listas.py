print("Ordenamiento burbuja")

# El ordenamiento burbuja es un algoritmo que sirve para ordenar una lista. Funciona comparando elementos vecinos y cambiándolos de posición si están en el orden incorrecto. Este proceso se repite hasta que ya no sea necesario hacer más intercambios.

# Lista que se desea ordenar
my_list = [8, 10, 6, 2, 4]

# Variable que indica si ocurrió algún intercambio
swapped = True

# El ciclo se repite mientras haya intercambios
while swapped:

    # Se asume que no habrá intercambios en esta pasada
    swapped = False

    # Se recorre la lista comparando cada elemento con el siguiente
    for i in range(len(my_list) - 1):

        # Si el número actual es mayor que el siguiente
        if my_list[i] > my_list[i + 1]:

            # Se intercambian las posiciones de los elementos
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

            # Se indica que sí ocurrió un intercambio
            swapped = True

# Cuando ya no hay intercambios, la lista está ordenada
print("Lista ordenada:", my_list)
print("/n")

print("Ordenamiento burbuja interactivo")

# El ordenamiento burbuja es un algoritmo que organiza una lista
# comparando elementos vecinos e intercambiándolos si están en
# el orden incorrecto. Este proceso se repite hasta que ya no
# ocurran intercambios y la lista quede ordenada.

# Se crea una lista vacía donde se guardarán los números
my_list = []

# Variable que indicará si ocurrió algún intercambio
swapped = True

# Se pregunta al usuario cuántos elementos quiere ordenar
num = int(input("¿Cuántos elementos deseas ordenar?: "))

# Se usa un bucle for para pedir los elementos de la lista
for i in range(num):

    # El usuario ingresa cada número
    val = float(input("Ingresa un elemento de la lista: "))

    # Se agrega el número al final de la lista
    my_list.append(val)

# Mientras haya intercambios el algoritmo seguirá ejecutándose
while swapped:

    # Se asume que no habrá intercambios en esta pasada
    swapped = False

    # Se recorren los elementos de la lista
    for i in range(len(my_list) - 1):

        # Si el elemento actual es mayor que el siguiente
        if my_list[i] > my_list[i + 1]:

            # Se intercambian las posiciones de los elementos
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

            # Se indica que ocurrió un intercambio
            swapped = True

# Cuando ya no hay intercambios la lista está ordenada
print("\nOrdenada:")
print(my_list)


print("Ordenar una lista con sort()")

# Python tiene una forma más sencilla de ordenar listas
# usando el método incorporado sort()

my_list = [8, 10, 6, 2, 4]

# El método sort() ordena automáticamente los elementos
my_list.sort()

# Se imprime la lista ordenada
print(my_list)