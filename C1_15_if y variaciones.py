# SENTENCIA IF (condición simple)

# Si la condición es verdadera, se ejecuta el código con sangría.

sheep_counter = 130

if sheep_counter >= 120:
    print("Ya contaste suficientes ovejas, puedes dormir.")

print("Programa terminado\n")




# 2. IF CON VARIAS INSTRUCCIONES

# Todas las instrucciones con la misma sangría
# pertenecen al bloque del if.

sheep_counter = 125

if sheep_counter >= 120:
    print("Hacer la cama")
    print("Tomar una ducha")
    print("Dormir y soñar")

print("Alimentar a los perros\n")


# SENTENCIA IF - ELSE


# Permite ejecutar una acción si la condición es verdadera
# y otra diferente si es falsa.

weather_is_good = True

if weather_is_good:
    print("Salir a caminar")
else:
    print("Ir al cine")

print("Después vamos a almorzar\n")




#  IF - ELSE CON VARIAS INSTRUCCIONES

weather_is_good = False

if weather_is_good:
    print("Salir a caminar")
    print("Divertirse mucho")
else:
    print("Ir al cine")
    print("Disfrutar la película")

print("Luego almorzar\n")



# IF ANIDADOS (condiciones dentro de otras)

weather_is_good = True
restaurant_found = False

if weather_is_good:
    print("Salir a caminar")

    if restaurant_found:
        print("Comer en restaurante")
    else:
        print("Comer un sandwich")

else:
    print("Ir al cine")

print()



# IF - ELIF - ELSE (cascada de condiciones)

weather_is_good = False
tickets_available = True
table_available = False

if weather_is_good:
    print("Salir a caminar")

elif tickets_available:
    print("Ir al cine")

elif table_available:
    print("Ir a comer")

else:
    print("Quedarse en casa y jugar ajedrez")

print()




# EJEMPLO: ENCONTRAR EL NÚMERO MAYOR DE DOS

number1 = int(input("Ingresa el primer número: "))
number2 = int(input("Ingresa el segundo número: "))

if number1 > number2:
    larger_number = number1
else:
    larger_number = number2

print("El número mayor es:", larger_number)
print()



# EJEMPLO: ENCONTRAR EL MAYOR DE TRES NÚMEROS

number1 = int(input("Ingresa el primer número: "))
number2 = int(input("Ingresa el segundo número: "))
number3 = int(input("Ingresa el tercer número: "))

largest_number = number1

if number2 > largest_number:
    largest_number = number2

if number3 > largest_number:
    largest_number = number3

print("El número más grande es:", largest_number)