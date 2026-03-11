print("Indexación de listas")
# Este programa demuestra cómo acceder y modificar
# elementos dentro de una lista utilizando índices.

# Se crea una lista con varios números
numbers = [10, 5, 7, 2, 1]

# Se imprime el contenido original de la lista
print("Contenido de la lista original:", numbers)

# Se cambia el valor del primer elemento de la lista
numbers[0] = 111

# Se muestra la lista después del cambio
print("\nContenido de la lista con cambio:", numbers)

# Se copia el valor del quinto elemento al segundo elemento
numbers[1] = numbers[4]

# Se imprime la lista después del intercambio
print("Contenido de la lista con intercambio:", numbers)


print("\n")
print("Acceso a elementos de la lista")
# Este ejemplo muestra cómo acceder a un elemento específico
# de la lista usando su índice.

# Se imprime el primer elemento de la lista
print("Primer elemento de la lista:", numbers[0])

# Se imprime la longitud de la lista usando la función len()
print("Longitud de la lista:", len(numbers))


print("\n")
print("Eliminar elementos de una lista")
# Este ejemplo muestra cómo eliminar un elemento de la lista
# utilizando la instrucción del.

# Se elimina el segundo elemento de la lista
del numbers[1]

# Se imprime la nueva longitud de la lista
print("Longitud de la nueva lista:", len(numbers))

# Se imprime el contenido actualizado de la lista
print("Nuevo contenido de la lista:", numbers,"/n")

print("Indexación negativa en listas")
# Se crea una lista con algunos números
numbers = [111, 7, 2, 1]

# En Python también se puede acceder a los elementos usando índices negativos.
# Los índices negativos comienzan a contar desde el final de la lista.
# En este caso se imprime el elemento que está en la posición -2,
# es decir, el segundo elemento contando desde el final de la lista.
print(numbers[-2],"\n")

print("Lista del sombrero")

# Esta es la lista inicial con cinco números
hat_list = [1, 2, 3, 4, 5]

# Paso 1: se pide al usuario un número entero
# y se reemplaza el número central de la lista (índice 2)
hat_list[2] = int(input("Introduce un número entero: "))

# Paso 2: se elimina el último elemento de la lista
del hat_list[4]

# Paso 3: se imprime la longitud actual de la lista
print("Longitud de la lista:", len(hat_list))

# Se muestra la lista final
print(hat_list)