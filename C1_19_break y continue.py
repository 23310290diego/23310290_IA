# Ejemplo de la instrucción break
# break se utiliza para terminar un bucle inmediatamente
# cuando se cumple una condición específica.

print("La instrucción break:")

for i in range(1, 6):
    
    # Si la variable i llega al valor 3,
    # el bucle terminará inmediatamente
    if i == 3:
        break
    
    # Esta línea solo se ejecuta mientras i sea 1 o 2
    print("Dentro del bucle.", i)

# Esta línea se ejecuta después de que el bucle termina
print("Fuera del bucle.")



# Ejemplo de la instrucción continue
# continue se utiliza para saltar la iteración actual
# del bucle y continuar con la siguiente.

print("\nLa instrucción continue:")

for i in range(1, 6):
    
    # Cuando i sea igual a 3 se saltará esta iteración
    if i == 3:
        continue
    
    # Esta línea no se ejecutará cuando i sea 3
    print("Dentro del bucle.", i)

print("Fuera del bucle.")



# Programa para encontrar el número más grande
# Este programa permite al usuario ingresar números
# y encuentra el número más grande.
# El programa termina cuando el usuario escribe -1.

largest_number = -99999999  # variable para almacenar el número mayor
counter = 0  # contador de números ingresados

while True:

    number = int(input("Ingresa un número o escribe -1 para finalizar el programa: "))

    # Si el usuario escribe -1 el bucle termina
    if number == -1:
        break

    # Se incrementa el contador
    counter += 1

    # Se compara si el número ingresado es mayor
    # que el número más grande guardado
    if number > largest_number:
        largest_number = number

# Al salir del bucle se verifica si se ingresaron números
if counter != 0:
    print("El número más grande es", largest_number)
else:
    print("No has ingresado ningún número.","\n")



# Programa: Devorador de Vocales
# Este programa pide al usuario una palabra y elimina las vocales A, E, I, O, U utilizando continue.
# Pedimos al usuario que ingrese una palabra
user_word = input("Ingresa una palabra: ")

# Convertimos la palabra a mayúsculas
# para facilitar la comparación con las vocales
user_word = user_word.upper()

# Recorremos cada letra de la palabra usando un bucle for
for letter in user_word:

    # Si la letra es una vocal, usamos continue
    # para saltar esta iteración del bucle
    if letter == "A":
        continue
    elif letter == "E":
        continue
    elif letter == "I":
        continue
    elif letter == "O":
        continue
    elif letter == "U":
        continue

    # Si no es vocal, se imprime la letra
    print(letter)