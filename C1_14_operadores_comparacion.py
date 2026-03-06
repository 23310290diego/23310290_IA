#3.1
# Operador de asignación (=) y comparación (==)

# Asignamos el valor 0 a la variable var
var = 0

# Comparamos si var es igual a 0
print("¿var es igual a 0?", var == 0)  # True porque 0 == 0


# Ahora cambiamos el valor de la variable
var = 1

# Volvemos a comparar
print("¿var es igual a 0?", var == 0)  # False porque 1 != 0




#  Operador de desigualdad (!=)

var = 0

# Preguntamos si var es diferente de 0
print("¿var es diferente de 0?", var != 0)  # False porque 0 sí es igual a 0


var = 1

# Volvemos a preguntar
print("¿var es diferente de 0?", var != 0)  # True porque 1 es diferente de 0


#  Operador mayor que (>)


black_sheep = 10
white_sheep = 5

# Comparamos si hay más ovejas negras que blancas
print("¿Hay más ovejas negras que blancas?", black_sheep > white_sheep)
# True porque 10 es mayor que 5



# Operador mayor o igual que (>=)


centigrade_outside = -2

# Preguntamos si la temperatura es mayor o igual a 0
print("¿La temperatura es mayor o igual a 0°C?", centigrade_outside >= 0.0)
# False porque -2 es menor que 0


# Operador menor que (<)


current_velocity_mph = 80

# Comparamos si la velocidad es menor que 85
print("¿La velocidad es menor que 85?", current_velocity_mph < 85)
# True porque 80 es menor que 85



# Operador menor o igual que (<=)

# Comparamos si la velocidad es menor o igual que 85
print("¿La velocidad es menor o igual que 85?", current_velocity_mph <= 85)
# True porque 80 es menor que 85

print("\n")

print("problema 3.1.6:\ncomprobar si un numero es mayor a 100")
n = int(input("Ingresa un número: "))
print(n >= 100)
