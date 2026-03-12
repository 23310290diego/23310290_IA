print("4.3.1 Return con expresion")
# Definición de la función llamada boring_function
def boring_function():
    # La función devuelve el número 123 usando return
    return 123


# Se llama a la función y el valor que devuelve
# se guarda en la variable x
x = boring_function()


# Se imprime un mensaje junto con el valor que devolvió la función
print("La función boring_function ha devuelto su resultado. Es:", x, "\n")

print("4.3.3 listas y funciones")
# Definición de la función list_sum
# Esta función recibe una lista como parámetro
def list_sum(lst):

    # Variable para almacenar la suma total
    s = 0

    # Se recorre cada elemento de la lista
    for elem in lst:

        # Se suma cada elemento al total
        s += elem

    # Se devuelve el resultado final
    return s


# Se llama a la función enviando una lista como argumento
# La función sumará los elementos de la lista
print(list_sum([5, 4, 3]))
print("\n")

# Definición de la función strange_list_fun
# La función recibe un número n como parámetro
def strange_list_fun(n):

    # Se crea una lista vacía
    strange_list = []
    
    # Se recorre desde 0 hasta n-1
    for i in range(0, n):

        # insert(0, i) agrega el número i al inicio de la lista
        # Esto hace que los elementos se vayan colocando al revés
        strange_list.insert(0, i)
    
    # La función devuelve la lista creada
    return strange_list


# Se llama a la función con el valor 5
# y se imprime la lista que devuelve
print(strange_list_fun(5))
print("\n")
print("Ejercicio año bisiesto")
# Función que determina si un año es bisiesto
def is_year_leap(year):

    # Si el año no es divisible entre 4, no es bisiesto
    if year % 4 != 0:
        return False

    # Si es divisible entre 4 pero NO entre 100, sí es bisiesto
    elif year % 100 != 0:
        return True

    # Si es divisible entre 100 pero NO entre 400, no es bisiesto
    elif year % 400 != 0:
        return False

    # Si es divisible entre 400, sí es bisiesto
    else:
        return True


# Lista de años de prueba
test_data = [1900, 2000, 2016, 1987]

# Resultados correctos esperados
test_results = [False, True, True, False]

# Se recorren los datos de prueba
for i in range(len(test_data)):

    # Se obtiene el año de la lista
    yr = test_data[i]

    # Se imprime el año
    print(yr, "-> ", end="")

    # Se llama a la función para saber si es bisiesto
    result = is_year_leap(yr)

    # Se compara el resultado con el esperado
    if result == test_results[i]:
        print("OK")       # Si coincide
    else:
        print("Fallido",)  # Si no coincide

    print("\n")
    print("4.3.6 Día del año")
    # Función que determina si un año es bisiesto
def is_year_leap(year):

    # Si el año no es divisible entre 4, no es bisiesto
    if year % 4 != 0:
        return False

    # Si es divisible entre 4 pero NO entre 100, sí es bisiesto
    elif year % 100 != 0:
        return True

    # Si es divisible entre 100 pero NO entre 400, no es bisiesto
    elif year % 400 != 0:
        return False

    # Si es divisible entre 400, sí es bisiesto
    else:
        return True


# Función que devuelve la cantidad de días de un mes
def days_in_month(year, month):

    # Verifica que el año y el mes sean válidos
    if year < 1582 or month < 1 or month > 12:
        return None

    # Lista con los días de cada mes
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Se obtiene el número de días del mes
    res = days[month - 1]

    # Si es febrero y el año es bisiesto
    if month == 2 and is_year_leap(year):
        res = 29

    return res


# Función que calcula el número de día dentro del año
def day_of_year(year, month, day):

    days = 0

    # Suma los días de todos los meses anteriores
    for m in range(1, month):

        md = days_in_month(year, m)

        # Si el mes no es válido
        if md == None:
            return None

        days += md

    # Obtiene los días del mes actual
    md = days_in_month(year, month)

    # Verifica si el día es válido
    if day >= 1 and day <= md:
        return days + day
    else:
        return None


# Ejemplo de prueba
print(day_of_year(2000, 12, 31))