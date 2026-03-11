# Almacena el actual número más grande aquí.
largest_number = -999999999

# Ingresa el primer valor.
number = int(input("Introduce un número o escribe -1 para detener: "))

# Si el número no es igual a -1, continuaremos
while number != -1:
    # ¿Es el número más grande que el valor de largest_number?
    if number > largest_number:
        # Sí si, se actualiza largest_number.
        largest_number = number
    # Ingresa el siguiente número.
    number = int(input("Introduce un número o escribe -1 para detener: "))

# Imprime el número más grande.
print("El número más grande es:", largest_number,"\n")


# Adivina el número secreto
# Se define el número secreto que el usuario debe adivinar
secret_number = 777

# Se muestra un mensaje de bienvenida y las instrucciones del juego
print(
"""
+================================+
| ¡Bienvenido a mi juego, muggle!|
| Introduce un número entero     |
| y adivina qué número he        |
| elegido para ti.               |
| ¿Cuál es el número secreto?    |
+================================+
"""
)

# Se solicita al usuario que introduzca un número entero
numero = int(input("Ingresa tu número: "))

# Se utiliza un bucle while que se ejecutará mientras
# el número ingresado sea diferente al número secreto
while numero != secret_number:
    
    # Si el número es incorrecto, se muestra un mensaje
    # indicando que el usuario sigue atrapado en el bucle
    print("¡Ja, ja! ¡Estás atrapado en mi bucle!")
    
    # Se vuelve a pedir al usuario que ingrese otro número
    numero = int(input("Intenta nuevamente: "))

# Cuando el usuario finalmente adivina el número secreto,
# el bucle termina y se muestra el mensaje de éxito
print(secret_number)
print("¡Bien hecho, muggle! Eres libre ahora.","\n")




print("Bucle for:")
# Programa de ejemplo para demostrar el uso del bucle for

# El bucle for se utiliza cuando sabemos exactamente
# cuántas veces queremos que se repita una acción.

# range(100) genera una secuencia de números
# que empieza en 0 y termina en 99 (100 repeticiones en total).

for i in range(10):

    # La variable i toma cada valor de la secuencia
    # en cada vuelta del bucle (0, 1, 2, 3, ... , 9)
    pass  # pass significa "no hacer nada", se usa como marcador de posición
print("\n")



# range(2, 8, 3) significa:
# 2 → número inicial
# 8 → límite superior (no se incluye)
# 3 → incremento o salto entre cada número

for i in range(2, 8, 3):
    
    # En cada iteración del bucle, la variable i toma
    # el siguiente valor de la secuencia generada por range()
    
    print("El valor de i es", i)  # Se imprime el valor actual de i
    print("\n")

    # Programa que cuenta segundos usando la técnica "Mississippi"
# Se utiliza para simular el conteo de segundos en tiempo real.

import time  # Se importa la librería time para poder usar pausas en el programa

# Bucle for que contará del 1 al 5
for i in range(1, 6):

    # En cada repetición se imprime el número actual
    # seguido de la palabra "Mississippi"
    print(i, "Mississippi")

    # time.sleep(1) pausa el programa durante 1 segundo
    # Esto hace que cada iteración represente aproximadamente un segundo
    time.sleep(1)

# Después de terminar el conteo, se muestra el mensaje final
print("¡Listos o no, ahí voy!")
print("\n")



print("Bucle while y else")
# Ejemplo donde el bucle while SÍ se ejecuta
# En este caso la condición es verdadera al inicio,
# por lo que el bucle se ejecutará varias veces.

i = 1  # Inicializamos la variable

# El bucle se ejecuta mientras i sea menor que 5
while i < 5:
    
    # Se imprime el valor actual de i
    print(i)
    
    # Se incrementa i en 1 para evitar un bucle infinito
    i += 1

# Cuando la condición del while deja de cumplirse,
# se ejecuta el bloque else
else:
    print("else:", i)


# Ejemplo donde el bucle while NO se ejecuta
# En este caso la condición es falsa desde el inicio,
# por lo que el cuerpo del bucle no se ejecutará.

i = 5  # Inicializamos la variable con 5

# La condición ya es falsa desde el principio
while i < 5:
    
    # Este bloque nunca se ejecutará
    print(i)
    
    i += 1

# El bloque else se ejecuta igualmente
else:
    print("else:", i)

print("\n")


print("uso del bucle for con bloque else")
# Este programa muestra cómo funciona el bloque else
# cuando se utiliza con un bucle for.

# El bucle recorrerá una secuencia de números generada
# por la función range(5), que produce los valores 0,1,2,3,4
for i in range(5):

    # En cada iteración se imprime el valor actual de i
    print(i)

# Cuando el bucle termina normalmente (sin break),
# se ejecuta el bloque else
else:
    print("else:", i)

    print("\n")

print("Altura de una pirámide de bloques")
# Este programa calcula cuántas capas completas de una pirámide se pueden construir con una cantidad dada de bloques.

# Se pide al usuario que ingrese el número de bloques disponibles
bloques = int(input("Introduce la cantidad de bloques: "))

# Variable que representará la altura de la pirámide
altura = 0

# Variable que representa la cantidad de bloques
# necesarios para construir la siguiente capa
bloques_necesarios = 1

# Mientras haya suficientes bloques para construir otra capa
while bloques >= bloques_necesarios:
    
    # Se resta del total la cantidad usada en la capa actual
    bloques -= bloques_necesarios
    
    # Se incrementa la altura de la pirámide
    altura += 1
    
    # La siguiente capa necesitará un bloque más
    bloques_necesarios += 1

# Cuando ya no se puedan construir más capas completas
# se imprime la altura final de la pirámide
print("La altura de la pirámide es:", altura)


print("\n")
print("Conjetura de Collatz")
# Este programa toma un número natural diferente de 0
# y aplica las reglas de la hipótesis de Collatz hasta
# que el valor llegue a 1. También cuenta los pasos
# necesarios y muestra los valores intermedios.

# Se solicita al usuario que ingrese un número natural
c0 = int(input("Introduce un número natural: "))

# Variable para contar la cantidad de pasos realizados
pasos = 0

# El bucle se ejecutará mientras c0 sea diferente de 1
while c0 != 1:

    # Si el número es par
    if c0 % 2 == 0:
        c0 = c0 // 2  # Se divide entre 2

    # Si el número es impar
    else:
        c0 = 3 * c0 + 1  # Se aplica la fórmula 3n + 1

    # Se imprime el valor actual de c0
    print(c0)

    # Se incrementa el contador de pasos
    pasos += 1

# Cuando el valor llega a 1 se muestra el número total de pasos
print("Número total de pasos:", pasos)