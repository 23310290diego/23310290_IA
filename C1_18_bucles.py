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