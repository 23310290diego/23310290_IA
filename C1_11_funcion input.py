# Ejemplo del uso de la función input()

# print() muestra un mensaje en la consola
print("Dime lo que sea...")

# input() espera a que el usuario escriba algo en el teclado
# lo que el usuario escriba se guarda en la variable "anything"
anything = input()

# print() muestra nuevamente el texto que escribió el usuario
# demostrando que el programa puede leer y usar datos de entrada
print("Hmm...", anything, "... ¿en serio?")

anything = input("Dime lo que sea...")
print("Hmm...", anything, "...¿en serio?")
print("\n")

#promlema 2.6.5
print("problema2.6.5:")
# input() pide un dato al usuario desde la consola.
# Normalmente input() devuelve un texto (string), por eso usamos float()
# para convertir ese texto a un número decimal que sí se pueda usar en cálculos.
anything = float(input("Ingresa un número: "))

# ** es el operador de potencia en Python.
# Aquí elevamos el número ingresado al cuadrado.
something = anything ** 2

# print() muestra el resultado en pantalla combinando texto y variables.
print(anything, "al cuadrado es", something,"\n")



#2.6.6
print("problema 2.6.6:")
# Este programa calcula la longitud de la hipotenusa de un triángulo rectángulo
# utilizando el Teorema de Pitágoras.

# input() pide al usuario la longitud del primer cateto.
# float() convierte el valor ingresado (texto) a número decimal.
leg_a = float(input("Ingresa la longitud del primer cateto: "))

# Se repite el proceso para el segundo cateto.
leg_b = float(input("Ingresa la longitud del segundo cateto: "))

# Aplicamos el Teorema de Pitágoras:
# hipotenusa² = cateto1² + cateto2²
# Para obtener la hipotenusa se calcula la raíz cuadrada (**0.5).
hypo = (leg_a**2 + leg_b**2) ** .5

# print() muestra el resultado final en pantalla
print("La longitud de la hipotenusa es:", hypo)