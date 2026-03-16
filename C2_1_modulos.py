import math # Paso 1: Importamos el módulo completo. 
            # Esto crea el namespace 'math'.
def sin(x):

    if 2 * x == pi:
        return 0.99999999
    else:
        return None

# Definimos nuestra propia constante pi con baja precisión
pi = 3.14

# Llamada a nuestra función local:
# Aquí Python busca 'sin' y 'pi' en nuestro archivo actual.
# Como x es (3.14 / 2), entonces 2 * x es 3.14.
print(sin(pi/2))          
# Llamada al espacio de nombres de 'math':
print(math.sin(math.pi/2))
# Importación directa al espacio de nombres local.
# En este momento, 'sin' y 'pi' apuntan a las funciones reales de Python.
from math import sin, pi
# Esta llamada usa la función matemática real.
# Salida esperada: 1.0
print(sin(pi / 2)) 
# Aquí empezamos a "sobrescribir" los nombres que importamos.

# Redefinimos 'pi'. 
# El valor preciso de math.pi se pierde y ahora vale 3.14.
pi = 3.14

# Redefinimos 'sin'.
# La función matemática real de math.sin es reemplazada por nuestra lógica.
def sin(x): 
    if 2 * x == pi:
        return 0.99999999
    else:
        return None
# Segunda llamada.
# Como x es (3.14 / 2), la condición (2 * x == 3.14) es verdadera.
print(sin(pi / 2),("\n"))

print("Ejercicio invertido")
# Definición inicial de variables y funciones locales
pi = 3.14

def sin(x):
    # Condición basada en el valor local de pi
    if 2 * x == pi:
        return 0.99999999
    else:
        return None

# Se ejecuta la función definida arriba. 
# El nombre 'sin' apunta todavía al bloque de código local.
print(sin(pi / 2))  

# CAMBIO DE REFERENCIA:
# Las etiquetas 'sin' y 'pi' dejan de apuntar a lo anterior y se vinculan a 'math'.
from math import sin, pi

# Se ejecuta la función de la biblioteca estándar.
# El acceso a la función local se ha perdido permanentemente en este punto.
print(sin(pi / 2)) 
print("\n")
print("aliasing o renombrado")
#módulo math ahora se identifica como m.
# Esto se hace para acortar el nombre original y evitar conflictos de nombres.
import math as m

# Para usar las entidades (sin y pi), ahora es obligatorio anteponer el alias 'm'.
# Esto demuestra que el espacio de nombres original ('math') ha sido renombrado.
print(m.sin(m.pi/2))







# Se importan entidades específicas directamente. 
# Esto permite usarlas sin el prefijo 'math.'
from math import pi, radians, degrees, sin, cos, tan, asin

ad = 90
ar = radians(ad) # Convierte 90 grados a radianes (pi / 2)
ad = degrees(ar) # Convierte los radianes de vuelta a grados (90.0)

# Comparación de conversión:
# Al convertir de ida y vuelta, el resultado es 90.0 (punto flotante).
print(ad == 90.) 

# Comparación de valor constante:
# Verifica si 'ar' es exactamente igual a la constante pi dividida entre 2.
print(ar == pi / 2.) 

# Identidad trigonométrica: tan(x) = sin(x) / cos(x)
# Python evalúa si ambos cálculos dan el mismo resultado binario.
print(sin(ar) / cos(ar) == tan(ar)) 

# Función inversa: el arcoseno del seno de un ángulo debe ser el mismo ángulo.
print(asin(sin(ar)) == ar) 

print("\m")
print("Funciones selectas del modulo math")
# Importación directa: permite usar las funciones sin poner 'math.' antes
from math import pi, radians, degrees, sin, cos, tan, asin

ad = 90             # Definir grados iniciales
ar = radians(ad)    # Convertir a radianes (pi / 2)
ad = degrees(ar)    # Convertir de vuelta a grados (90.0)

# Verificaciones de precisión:
print(ad == 90.)    # True: el valor regresó a su origen
print(ar == pi / 2.) # True: 90 grados equivalen a medio pi
print(sin(ar) / cos(ar) == tan(ar)) # True: se cumple la identidad de la tangente
print(asin(sin(ar)) == ar)          # True: el arco seno anula al seno

# Importación directa de la constante 'e' y funciones de exponente y logaritmo
from math import e, exp, log

# Comprobación 1: e^1 es igual a e^(ln(e))
# pow(e, 1) es 'e'. log(e) es 1. exp(1) es 'e'.
print(pow(e, 1) == exp(log(e)))     # True

# Comprobación 2: Identidad logarítmica (a^b = e^(b * ln(a)))
# 2^2 es 4. exp(2 * ln(2)) también resulta en 4.
print(pow(2, 2) == exp(2 * log(2))) # True

# Comprobación 3: Logaritmo con base y exponente cero
# log(e, e) es logaritmo base 'e' de 'e' (1). exp(0) es e^0 (1).
print(log(e, e) == exp(0))          # True
print("\n")




print("Funciones del modulo random")
# Se importa la función random() desde el módulo random
from random import random

# El bucle genera 5 iteraciones
for i in range(5):
    # random() devuelve un flotante x donde: 0.0 <= x < 1.0
    # El valor nunca llegará a ser exactamente 1.0
    print(random())


print("Función seed:")
# Importación de la función generadora y la función de control (seed)
from random import random, seed

# Establecer la semilla en 0. 
# Esto fija el estado inicial del generador pseudoaleatorio.
seed(0)

# El bucle generará siempre los mismos 5 números cada vez que se ejecute el programa
for i in range(5):
    # Genera un flotante entre 0.0 y 1.0 (excluido)
    print(random())
    print("\n")



print("Funciones choice y sample:")
# Importación de funciones para elegir elementos de una secuencia
from random import choice, sample

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Elige un ÚNICO elemento al azar de la lista.
# Devuelve el valor directamente (un entero en este caso).
print(choice(my_list))

# Elige una cantidad específica de elementos (5) sin repetir ninguno.
# Devuelve una LISTA con los elementos en orden aleatorio.
print(sample(my_list, 5))

# Elige todos los elementos de la lista (10) en un orden nuevo.
# Es útil para "barajar" la lista completa en una nueva variable.
print(sample(my_list, 10))
print("\n")



print("Función platform:")
# Importación de la función para leer datos del sistema
from platform import platform

# 1. Llamada estándar: parámetros por defecto (aliased=False, terse=False)
# Devuelve la descripción completa y común del sistema.
print(platform())

# 2. Uso de 'aliased' (aliased=True):
# Usa el valor 1 (distinto a cero) para intentar mostrar nombres alternativos del sistema.
print(platform(1))

# 3. Uso de 'terse' (aliased=False, terse=True):
# El segundo parámetro en 1 (True) solicita la versión más breve posible del resultado.
print(platform(0, 1))