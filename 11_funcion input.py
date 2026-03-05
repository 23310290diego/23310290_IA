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
print(anything, "al cuadrado es", something)