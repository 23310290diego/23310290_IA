#2.4
#VARIABLES

# Creación de variables con diferentes tipos de datos
var = 1                     # variable entera
account_balance = 1000.0    # variable flotante
client_name = 'John Doe'    # variable cadena

# Mostrar varias variables en un mismo print
print(var, account_balance, client_name)


# Concatenación de texto con variables usando +
version = "3.8.5"
print("Python version: " + version)

# Reasignación de variables
var = 1
print("Valor inicial de var:", var)

# Asignamos un nuevo valor
var = 200 + 300
print("Nuevo valor de var (200 + 300):", var)

# Incremento de variable (var = var + 1)
var = var + 1
print("Incremento de var + 1:", var)

# Explicación:
# Aquí el signo = NO significa igualdad matemática,
# significa "asignar".
# Toma el valor actual de var, súmale 1 y guárdalo nuevamente en var.

# Problema matemático: Teorema de Pitágoras

a = 3.0
b = 4.0

# Fórmula: c = √(a² + b²)
c = (a ** 2 + b ** 2) ** 0.5

print("Valor de la hipotenusa (c) =", c)

# Explicación:
# a ** 2 → a al cuadrado
# b ** 2 → b al cuadrado
# (a² + b²) → suma de cuadrados
# ** 0.5 → raíz cuadrada
print("\n")


#2.4.7
# Ejercicio:
print("ejercicio 2.4.7:")
john = 3
mary = 5
adam = 6

print(john, mary, adam, sep=',')

total_apples = john + mary + adam
print('manzanas totales:')
print(total_apples,'\n')



#2.4.9
# Ejercicio:
# Valores iniciales
kilometers = 12.25   # Cantidad en kilómetros
miles = 7.38         # Cantidad en millas

# Sabemos que:
# 1 milla = 1.61 kilómetros

# Convertir millas a kilómetros
# Fórmula: millas * 1.61
miles_to_kilometers = miles * 1.61

# Convertir kilómetros a millas
# Fórmula: kilómetros / 1.61
kilometers_to_miles = kilometers / 1.61

# Mostrar resultados
# print() permite combinar variables y texto usando comas
# round(valor, 2) redondea el resultado a 2 decimales
print('Ejercicio 2.4.9')
print(miles, "millas son", round(miles_to_kilometers, 2), "kilómetros")
print(kilometers, "kilómetros son", round(kilometers_to_miles, 2), "millas","\n")


# Ejercicio 2.4.10
print("ejercicio 2.4.10:")

x = 0
x = float(x)
y = 3 * x**3 - 2 * x**2 + 3 * x - 1
print("y =", y)

x = 1
x = float(x)
y = 3 * x**3 - 2 * x**2 + 3 * x - 1
print("y =", y)

x = -1
y = 3 * x**3 - 2 * x**2 + 3 * x - 1
print("y =", y)
