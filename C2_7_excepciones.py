print("Jerarquía de Excepciones")

try:
    y = 1 / 0
# ZeroDivisionError es una "hoja" muy específica. 
# Solo atrapa divisiones entre cero.
except ZeroDivisionError:
    print("Uuupsss...")

print("FIN.","\n")




print("Generalización de Excepciones")

try:
    y = 1 / 0
# ArithmeticError es más general que ZeroDivisionError.
# Atrapa errores de división, de desbordamiento (overflow), etc.
except ArithmeticError:
    print("Uuuppsss...")

print("FIN.","\n")




print("Orden de Excepciones")

try:
    y = 1 / 0
# Al ser ArithmeticError el padre de ZeroDivisionError,
# atrapa el error primero y el segundo bloque queda ignorado.
except ArithmeticError:
    print("¡Problema aritmético!")
except ZeroDivisionError:
    print("¡División entre cero!")

print("FIN.","\n")

print("Manejo de excepciones dentro de funciones")

def bad_fun(n):
    try:
        return 1 / n
    # Atrapa cualquier error aritmético (como dividir entre 0)
    except ArithmeticError:
        print("¡Problema aritmético!")
    
    # Si ocurre el error, la función continúa aquí y devuelve None
    return None

# Llamada a la función con un valor que causa error
bad_fun(0)

print("FIN.","\n")




print("Excepciones utiles")
# AssertionError
from math import tan, radians
angle = int(input('Ingresa un angulo entero en grados: '))

# El programa se detiene si la condición es falsa (ej. 90, 270, 450)
assert angle % 180 != 90
print(tan(radians(angle)))


# IndexError
the_list = [1, 2, 3, 4, 5]
ix = 0
do_it = True

while do_it:
    try:
        # Se genera al intentar acceder al índice 5 que no existe
        print(the_list[ix])
        ix += 1
    except IndexError:
        do_it = False

print('Listo')


# KeyboardInterrupt
from time import sleep
seconds = 0

while True:
    try:
        print(seconds)
        seconds += 1
        sleep(1)
    # Se genera cuando el usuario presiona Ctrl+C para interrumpir
    except KeyboardInterrupt:
        print("¡No hagas eso!")
        break


# MemoryError
string = 'x'
try:
    while True:
        # Duplicación masiva hasta agotar la memoria RAM
        string = string + string
        print(len(string))
except MemoryError:
    print('¡Esto no es gracioso!')


# OverflowError
from math import exp
ex = 1

try:
    while True:
        # El cálculo crece hasta superar el límite del tipo float
        print(exp(ex))
        ex *= 2
except OverflowError:
    print('El número es demasiado grande.')


# ImportError
try:
    import math
    import time
    # Se genera porque el módulo 'abracadabra' no está instalado o no existe
    import abracadabra
except ImportError:
    print('Una de tus importaciones ha fallado.')


# KeyError
dictionary = {'a': 'b', 'b': 'c', 'c': 'd'}
ch = 'a'

try:
    while True:
        # Se genera cuando ch se convierte en 'd', que no es una clave del diccionario
        ch = dictionary[ch]
        print(ch)
except KeyError:
    print('No existe tal clave:', ch)

    print("\n")








    print("LAB Leyendo enteros de manera segura ")

def read_int(prompt, min, max):
    ok = False
    while not ok:
        try:
            # Intenta convertir la entrada a entero; lanza ValueError si falla
            value = int(input(prompt))
            ok = True
        except ValueError:
            # Se ejecuta si el usuario ingresa letras o símbolos
            print("Error: entrada incorrecta")
        
        # Si es un entero, verifica que esté dentro de los límites
        if ok:
            ok = value >= min and value <= max
            
        # Si falló la validación del rango, muestra el mensaje y repite el ciclo
        if not ok:
            print("Error: el valor no está dentro del rango permitido (" + str(min) + ".." + str(max) + ")")
            
    return value

v = read_int("Ingresa un número entre -10 y 10: ", -10, 10)

print("El número es:", v)