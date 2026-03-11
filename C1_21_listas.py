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
print("Nuevo contenido de la lista:", numbers,)
print("\n")

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
print("\n")


print("Métodos append() e insert() en listas")

# Se crea una lista inicial con algunos números
numbers = [111, 7, 2, 1]

# Se imprime la longitud de la lista y su contenido actual
print("Longitud:", len(numbers))
print("Lista:", numbers)

# El método append() agrega un elemento al final de la lista
numbers.append(4)

# Se vuelve a imprimir la longitud y el contenido
print("Longitud después de append:", len(numbers))
print("Lista después de append:", numbers)

# El método insert() permite agregar un elemento en una posición específica
# En este caso se inserta el número 222 en la posición 0 (inicio de la lista)
numbers.insert(0, 222)

print("Longitud después de insert en posición 0:", len(numbers))
print("Lista después de insert en posición 0:", numbers)

# Aquí se inserta el número 333 en la posición 1
# Los elementos existentes se desplazan una posición a la derecha
numbers.insert(1, 333)

print("Longitud final:", len(numbers))
print("Lista final:", numbers)
print("/n")
print("Crear una lista usando append() y un bucle for")

# Se crea una lista vacía
my_list = []

# Se usa un bucle for para repetir el proceso 5 veces
for i in range(5):
    
    # En cada iteración se agrega a la lista el valor de i + 1
    # append() coloca el nuevo elemento al final de la lista
    my_list.append(i + 1)

# Al finalizar el bucle se imprime la lista completa
print(my_list)
print("/n")



print("Intercambiar variables y revertir una lista")

# Primero se muestra cómo intercambiar el valor de dos variables

variable_1 = 1
variable_2 = 2

# Python permite intercambiar valores en una sola línea
variable_1, variable_2 = variable_2, variable_1

print("variable_1:", variable_1)
print("variable_2:", variable_2)


print("\n")

print("Invertir el orden de los elementos de una lista")

# Se crea una lista de ejemplo
my_list = [10, 1, 8, 3, 5]

# Se obtiene la longitud de la lista
length = len(my_list)

# El bucle for recorre solo la mitad de la lista
# porque cada intercambio afecta dos posiciones
for i in range(length // 2):

    # Se intercambia el elemento del inicio
    # con el correspondiente desde el final
    my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]

# Se imprime la lista ya invertida
print("Lista invertida:", my_list)
print("/n")


print("Cambios en la banda The Beatles")

# paso 1: crear una lista vacía
beatles = []
print("Paso 1:", beatles)

# paso 2: agregar los primeros miembros de la banda
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Paso 2:", beatles)

# paso 3: pedir al usuario agregar dos miembros más usando un bucle for
for i in range(2):
    nuevo_miembro = input("Agrega un miembro de la banda: ")
    beatles.append(nuevo_miembro)

print("Paso 3:", beatles)

# paso 4: eliminar a Stu Sutcliffe y Pete Best
del beatles[3]
del beatles[3]

print("Paso 4:", beatles)

# paso 5: agregar a Ringo Starr al inicio de la lista
beatles.insert(0, "Ringo Starr")

print("Paso 5:", beatles)

# probando la longitud de la lista
print("Los Fav", len(beatles))