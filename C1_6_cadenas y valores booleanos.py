#2.2.4
# Cadena básica (texto entre comillas)
print("Yo soy una cadena.")

# Insertar comillas dentro de una cadena usando carácter de escape (\")
print("Me gusta \"Monty Python\"")
# La diagonal invertida (\) evita que la comilla cierre la cadena

# Usar apóstrofes para delimitar la cadena
# Así no necesitamos escapar las comillas internas
print('Me gusta "Monty Python"')

# Insertar un apóstrofe dentro de una cadena delimitada por apóstrofes
# Solución 1: usar carácter de escape (\')
print('It\'s Monty Python')

# Solución 2: usar comillas dobles como delimitador
print("It's Monty Python")

#2.2.5 
# Valores Booleanos
# Valores booleanos básicos
print(True)    # valor verdadero
print(False)   # valor falso

# Comparaciones producen valores booleanos
print(5 > 3)   # True porque 5 es mayor que 3
print(2 < 1)   # False porque 2 no es menor que 1

# Booleanos se comportan como 1 (True) y 0 (False)
print(True > False)   # True porque 1 > 0
print(True < False)   # False porque 1 < 0

# Verificando el tipo de dato
print(type(True))     # muestra que es tipo 'bool'