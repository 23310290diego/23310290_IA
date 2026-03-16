print("Funcion sorted")

first_greek = ['omega', 'alpha', 'pi', 'gamma']

# sorted() crea una NUEVA lista ordenada y no toca la original
first_greek_2 = sorted(first_greek)

print(first_greek) 
print(first_greek_2) 

print()
print("\n")



print("Metodo sort")

second_greek = ['omega', 'alpha', 'pi', 'gamma']
print(second_greek) # Lista original

# .sort() ordena la lista ORIGINAL. No crea una nueva, modifica la que ya existe.
second_greek.sort()
print(second_greek)

print("\n")
print("Cadenas versus números")

itg = 13
flt = 1.3

# str() convierte números (enteros o flotantes) en cadenas de texto
si = str(itg)
sf = str(flt)

# Al ser ya cadenas, se pueden concatenar con el espacio ' '
print(si + ' ' + sf) 

print("Simulador de Display LED")

def mostrar_leds(numero):
    # Definimos los patrones de los dígitos del 0 al 9
    # Cada lista tiene 5 cadenas, una por cada fila del display
    patrones = [
        ["###", "# #", "# #", "# #", "###"], # 0
        ["  #", "  #", "  #", "  #", "  #"], # 1
        ["###", "  #", "###", "#  ", "###"], # 2
        ["###", "  #", "###", "  #", "###"], # 3
        ["# #", "# #", "###", "  #", "  #"], # 4
        ["###", "#  ", "###", "  #", "###"], # 5
        ["###", "#  ", "###", "# #", "###"], # 6
        ["###", "  #", "  #", "  #", "  #"], # 7
        ["###", "# #", "###", "# #", "###"], # 8
        ["###", "# #", "###", "  #", "###"]  # 9
    ]

    # Convertimos el número a cadena para procesar cada dígito
    str_num = str(numero)
    
    # Vamos a construir el display fila por fila (son 5 filas en total)
    for i in range(5):
        linea = ""
        for digito in str_num:
            # Obtenemos el patrón del dígito actual y su fila correspondiente
            linea += patrones[int(digito)][i] + " "
        print(linea)

# Entrada del usuario
entrada = input("Ingresa un número entero no negativo: ")

if entrada.isdigit():
    mostrar_leds(entrada)
else:
    print("Error: Por favor ingresa solo números.")
    print("\n")





    print("LAB Palindromos")

text = input("Ingresa un texto: ")

# 1. Eliminamos los espacios para que frases como "anita lava la tina" funcionen
text = text.replace(' ', '')

# 2. Verificación de palíndromo
# - len(text) > 0: Asegura que no sea una cadena vacía
# - text.upper(): Ignora la diferencia entre mayúsculas y minúsculas
# - text[::-1]: Invierte la cadena completamente
if len(text) > 0 and text.upper() == text[::-1].upper():
    print("Es un palíndromo")
else:
    print("No es un palíndromo")