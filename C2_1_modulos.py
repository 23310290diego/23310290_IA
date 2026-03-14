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