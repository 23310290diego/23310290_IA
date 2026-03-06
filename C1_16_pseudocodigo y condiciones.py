# 3.1.9 PSEUDOCÓDIGO 
# Ejemplo de pseudocódigo para encontrar el número mayor:

"""
largest_number = -999999999

leer numero

si numero == -1:
    imprimir largest_number
    terminar programa

si numero > largest_number:
    largest_number = numero

repetir
"""

# La idea es repetir el proceso muchas veces, se le llama un BUCLЕ (loop).


print("EJEMPLO: ENCONTRAR EL NÚMERO MAYOR DE TRES NÚMEROS")

# Se leen tres números desde el teclado
number1 = int(input("Ingresa el primer número: "))
number2 = int(input("Ingresa el segundo número: "))
number3 = int(input("Ingresa el tercer número: "))

# Asumimos temporalmente que el primer número es el mayor
largest_number = number1

# Comparamos el segundo número con el mayor actual
if number2 > largest_number:
    largest_number = number2

# Comparamos el tercer número con el mayor actual
if number3 > largest_number:
    largest_number = number3

# Mostramos el resultado
print("El número más grande es:", largest_number,"\n")




print("EJEMPLO USANDO FUNCIÓN INCORPORADA max()")
# La función max() devuelve el número mayor.

largest_number2 = max(number1, number2, number3)

print("Usando la función max(), el número mayor es:", largest_number2,"\n")



print("EJECUCIÓN CONDICIONAL (if)")
# Una sentencia if permite ejecutar código solo si se cumple una condición.

temperature = int(input("Ingresa la temperatura actual: "))

if temperature > 25:
    print("Hace calor, puedes salir a caminar.")

print("Este mensaje siempre se ejecuta.","\n")




print("SENTENCIA if - else")

# Permite ejecutar un bloque si la condición es verdadera y otro bloque si es falsa.

weather = input("¿El clima es bueno? (si/no): ")

if weather == "si":
    print("Vamos a caminar.")
else:
    print("Vamos al cine.")




# SENTENCIA if - elif - else
# Se usa cuando existen varias condiciones posibles.

number = int(input("Ingresa un número: "))

if number > 0:
    print("El número es positivo.")

elif number == 0:
    print("El número es cero.")

else:
    print("El número es negativo.","\n")


print("LABORATORIO: EL PROGRAMA DEL ESPATIFILO")

# Este programa lee el nombre de una planta y responde
# dependiendo de lo que el usuario escriba.

plant = input("Ingresa el nombre de una planta: ")

# Si la palabra es ESPATIFILIO en MAYÚSCULAS
if plant == "ESPATIFILIO":
    print("Si - ¡El Espatifilo! es la mejor planta de todos los tiempos!")

# Si la palabra es espatifilo en minúsculas
elif plant == "espatifilo":
    print("No, ¡quiero un gran Espatifilo!")

# Si el usuario escribe cualquier otra cosa
else:
    print("¡Espatifilo!, ¡No", plant + "!")
