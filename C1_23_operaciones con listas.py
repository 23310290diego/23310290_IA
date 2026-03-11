print("Rebanadas en listas (slicing)")

# Una rebanada permite copiar una lista completa o una parte de ella.
# La sintaxis general es: lista[inicio:fin]
# Copia los elementos desde el índice "inicio" hasta "fin - 1".

print("Copiar una lista completa")

# Se crea una lista original
list_1 = [1]

# Se copia toda la lista usando [:]
# Esto crea una nueva lista independiente
list_2 = list_1[:]

# Se modifica el valor de la lista original
list_1[0] = 2

# La copia no cambia porque es una lista diferente
print(list_2)


print("\n")
print("Copiar una parte de una lista")

# Lista original
my_list = [10, 8, 6, 4, 2]

# Se copia solo una parte de la lista
# desde el índice 1 hasta el índice 2 (3 no se incluye)
new_list = my_list[1:3]

# Se imprime la nueva lista creada con la rebanada
print(new_list)
print("\n")

print("Rebanadas con índices negativos")

# Las rebanadas permiten copiar una parte de una lista.
# La forma general es: lista[inicio:fin]
# "inicio" es el primer elemento incluido
# "fin" es el primer elemento que NO se incluye.

my_list = [10, 8, 6, 4, 2]

# Aquí se toma desde el índice 1 hasta el -1
# -1 representa el último elemento, pero no se incluye en la rebanada
new_list = my_list[1:-1]

print(new_list)


print("\n")
print("Rebanada vacía")

# Si el índice inicial está después del índice final,
# el resultado será una lista vacía

my_list = [10, 8, 6, 4, 2]
new_list = my_list[-1:1]

print(new_list)


print("\n")
print("Rebanada desde el inicio")

# Si se omite el inicio, Python empieza desde el índice 0

my_list = [10, 8, 6, 4, 2]
new_list = my_list[:3]

print(new_list)


print("\n")
print("Rebanada hasta el final")

# Si se omite el final, Python toma los elementos
# desde el índice indicado hasta el final de la lista

my_list = [10, 8, 6, 4, 2]
new_list = my_list[3:]

print(new_list)


print("\n")
print("Copiar toda la lista con rebanada")

# Usar [:] copia toda la lista creando una nueva lista independiente

my_list = [10, 8, 6, 4, 2]
new_list = my_list[:]

print(new_list)


print("\n")
print("Eliminar una parte de la lista con del")

# La instrucción del también puede eliminar rebanadas de la lista

my_list = [10, 8, 6, 4, 2]

# Se eliminan los elementos desde el índice 1 hasta el 2
del my_list[1:3]

print(my_list)


print("\n")
print("Eliminar todos los elementos de la lista")

# Se eliminan todos los elementos de la lista

my_list = [10, 8, 6, 4, 2]
del my_list[:]

print(my_list)
print("\n")
print("Operadores in y not in")

# Los operadores in y not in se usan para verificar
# si un elemento está o no dentro de una lista.

# Lista de ejemplo
my_list = [0, 3, 12, 8, 2]

# El operador in devuelve True si el elemento está en la lista
print(5 in my_list)

# El operador not in devuelve True si el elemento NO está en la lista
print(5 not in my_list)

# Aquí se verifica si el número 12 está dentro de la lista
print(12 in my_list)
print("\n")


print("Operadores in y not in")

# Los operadores in y not in se usan para verificar
# si un elemento está o no dentro de una lista.

my_list = [0, 3, 12, 8, 2]

# Verifica si 5 está en la lista
print(5 in my_list)

# Verifica si 5 NO está en la lista
print(5 not in my_list)

# Verifica si 12 está en la lista
print(12 in my_list)


print("\n")
print("Encontrar el número más grande de una lista")

# Este programa busca el número mayor dentro de una lista
# comparando cada elemento con el mayor encontrado hasta ahora

my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]

# Se asume inicialmente que el primer elemento es el mayor
largest = my_list[0]

# Se recorren los elementos de la lista
for i in my_list:
    if i > largest:
        largest = i

print("El número mayor es:", largest)


print("\n")
print("Encontrar un elemento en una lista")

# Este programa busca si un número específico está en la lista
# y muestra su posición si se encuentra

my_list = [1,2,3,4,5,6,7,8,9,10]
to_find = 5
found = False

# Se recorren los índices de la lista
for i in range(len(my_list)):

    # Se verifica si el elemento coincide con el buscado
    found = my_list[i] == to_find

    if found:
        break

# Se muestra el resultado de la búsqueda
if found:
    print("Elemento encontrado en el índice", i)
else:
    print("ausente")


print("\n")
print("Simulación de aciertos en la lotería")

# Este programa cuenta cuántos números de una apuesta
# coinciden con los números que salieron en el sorteo

drawn = [5, 11, 9, 42, 3, 49]
bets = [3, 7, 11, 42, 34, 49]

# Variable para contar los aciertos
hits = 0

# Se revisa cada número apostado
for number in bets:

    # Si el número está dentro de los sorteados
    if number in drawn:
        hits += 1

print("Cantidad de aciertos:", hits)

print("\n")
print("Eejercicio 3.6.6")
# Lista original con elementos repetidos
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

# Lista nueva donde se guardarán solo los elementos únicos
unique_list = []

# Recorremos cada elemento de la lista original
for number in my_list:
    
    # Si el número NO está en la nueva lista
    # significa que todavía no se ha agregado
    if number not in unique_list:
        unique_list.append(number)  # Se agrega a la lista de únicos

# Mostramos la lista sin elementos repetidos
print("La lista con elementos únicos:")
print(unique_list)