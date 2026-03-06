# Se pide al usuario que ingrese un número y se convierte a tipo float
a = float(input("Ingresa el valor de a: "))

# Se pide otro número y también se convierte a float
b = float(input("Ingresa el valor de b: "))

# Se muestra el resultado de la suma
print("Suma:", a + b)

# Se muestra el resultado de la resta
print("Resta:", a - b)

# Se muestra el resultado de la multiplicación
print("Multiplicación:", a * b)

# Se muestra el resultado de la división
print("División:", a / b)

# Mensaje final del programa
print("\n¡Eso es todo, amigos!","\n")


print("ejercicio 2.6.10:")
# Ejercicio: Evaluar la siguiente expresión matemática:
# y = 1 / (x + (1 / (x + (1 / (x + (1 / x))))))

# La idea del ejercicio es:
# 1. Pedir al usuario un valor para x.
# 2. Convertir ese valor a número (float) para poder hacer cálculos.
# 3. Evaluar la expresión matemática usando operadores de Python.
# 4. Mostrar el resultado en pantalla.

# input() permite que el usuario escriba un valor desde la consola.
# float() convierte ese valor (que originalmente es texto) a número decimal.
x = float(input("Ingresa el valor para x: "))

# Aquí se calcula la expresión matemática dada en el ejercicio.
# Se usan varios paréntesis para respetar el orden correcto de las operaciones.
# Python evaluará primero las expresiones más internas.
y = 1 / (x + (1 / (x + (1 / (x + (1 / x))))))

# print() muestra el resultado final en la consola.
print("y =", y,"\n")



print("ejercicio 2.3.11:")
# Se pide al usuario la hora de inicio (0 a 23)
hour = int(input("Hora de inicio (horas): "))

# Se pide el minuto de inicio (0 a 59)
mins = int(input("Minuto de inicio (minutos): "))

# Se pide la duración del evento en minutos
dura = int(input("Duración del evento (minutos): "))

# Primero sumamos los minutos actuales con la duración del evento
mins = mins + dura

# Calculamos cuántas horas adicionales se generan al pasar de 60 minutos
hour = hour + mins // 60

# Usamos % para obtener los minutos finales (los que sobran después de dividir entre 60)
mins = mins % 60

# Usamos % 24 para mantener la hora dentro del formato de 24 horas (0–23)
hour = hour % 24

# Mostramos la hora final
print("La hora de finalización es:", hour, ":", mins)