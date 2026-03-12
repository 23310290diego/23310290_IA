print("Código repetido sin funciones")

# Este código pide tres valores al usuario.
# El mensaje se repite varias veces.

print("Ingresa un valor:")
a = int(input())

print("Ingresa un valor:")
b = int(input())

print("Ingresa un valor:")
c = int(input())

print("Valores capturados:", a, b, c)


print("\n")
print("Uso de funciones para evitar repetir código")

# Una función permite agrupar instrucciones
# para reutilizarlas cuando sea necesario.

def message():
    print("Ingresa un valor:")


# Aquí usamos la función varias veces
message()
a = int(input())

message()
b = int(input())

message()
c = int(input())

print("Valores capturados:", a, b, c)


print("\n")
print("Ejemplo simple de invocación de función")

# Definición de la función
def message():
    print("Ingresar valor:")

print("Inicia aquí.")

# Invocación de la función
message()

print("Termina aquí.")




print("Cómo funcionan las funciones")

# DEFINICIÓN DE UNA FUNCIÓN

# Primero se define la función
def message():
    print("Ingresar valor:")

print("Inicia aquí.")

# Luego se invoca la función
message()

print("Termina aquí.")


print("\n")
print("Ejemplo correcto: función definida antes de usarse")

# Python lee el código de arriba hacia abajo,
# por eso la función debe definirse antes de invocarse.

def message():
    print("Ingresar valor:")

message()
a = int(input())

message()
b = int(input())

message()
c = int(input())

print("Valores ingresados:", a, b, c)


print("\n")
print("Ejemplo incorrecto (comentado para evitar error)")

# Si se intenta usar la función antes de definirla
# Python genera un error NameError

# print("Inicia aqui.")
# message()
# print("Termina aqui.")

# def message():
#     print("Ingresar valor:")


print("\n")
print("Ejemplo incorrecto: función y variable con el mismo nombre")

# Una función y una variable no pueden tener el mismo nombre
# porque la variable reemplaza a la función.

def saludo():
    print("Hola")

saludo()

# Aquí se cambia el nombre de la función por una variable
saludo = 1

print("La función ya no existe, ahora saludo vale:", saludo)
print("\n")

print("4.2.2 Funciones con parámetros y argumentos posicionales")
# FUNCIÓN CON PARÁMETROS
# La función recibe dos parámetros: what y number
def message(what, number):
    print("Ingresa", what, "número", number)

# Al llamar la función se envían argumentos
message("teléfono", 11)
message("precio", 5)
message("número", "number")


print("\n")
print("Paso de parámetros posicionales")

# En el paso posicional, los valores se asignan
# según el orden en que aparecen

def my_function(a, b, c):
    print(a, b, c)

# 1 se asigna a 'a'
# 2 se asigna a 'b'
# 3 se asigna a 'c'
my_function(1, 2, 3)


print("\n")
print("Ejemplo de presentación")

# Función con dos parámetros
def introduction(first_name, last_name):
    print("Hola, mi nombre es", first_name, last_name)

# Los argumentos se asignan por posición
introduction("Luke", "Skywalker")
introduction("Jesse", "Quick")
introduction("Clark", "Kent")
Print("\n")
Print("4.2.4")
def adding(a, b, c):
    print(a, "+", b, "+", c, "=", a + b + c)
    adding(1, 2, 3)