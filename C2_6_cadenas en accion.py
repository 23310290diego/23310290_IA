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

print("\n")








print("LAB Anagramas")

str_1 = input("Ingresa la primera cadena: ")
str_2 = input("Ingresa la segunda cadena: ")

# Proceso de normalización y ordenamiento:
# 1. replace(' ',''): Elimina espacios.
# 2. upper(): Convierte a mayúsculas para ignorar diferencias.
# 3. list(): Convierte la cadena en una lista de letras.
# 4. sorted(): Ordena las letras alfabéticamente (ej: 'roma' -> ['a', 'm', 'o', 'r']).
# 5. ''.join(): Vuelve a pegar las letras en una sola cadena.
strx_1 = ''.join(sorted(list(str_1.upper().replace(' ',''))))
strx_2 = ''.join(sorted(list(str_2.upper().replace(' ',''))))

# Verificación
if len(strx_1) > 0 and strx_1 == strx_2:
    print("Anagramas")
else:
    print("No son anagramas")
print("\n")






print("LAB El Digito de la Vida")

date = input("Ingresa tu fecha de cumpleaños (8 dígitos): ")

# 1. Validación inicial
if len(date) < 8 or not date.isdigit():
    print("Formato de fecha inválida.")
else:
    # 2. Ciclo de reducción
    # Mientras la cadena tenga más de un carácter, seguimos sumando
    while len(date) > 1:
        the_sum = 0
        for dig in date:
            the_sum += int(dig)
        
        # Convertimos la suma de vuelta a cadena para volver a evaluarla
        date = str(the_sum)
    
    print("Tu Dígito de la Vida es: " + date)
print("\n")









print("LAB Encuentra la palabra")

# 1. Lectura y normalización (todo a mayúsculas para ignorar diferencias)
word = input("Ingresa la palabra que deseas encontrar: ").upper()
strn = input("Ingresa la cadena en donde deseas buscar: ").upper()

found = True
start = 0

# 2. Búsqueda secuencial
for ch in word:
    # Buscamos el carácter 'ch' empezando desde la posición 'start'
    pos = strn.find(ch, start) 
    
    # Si .find() devuelve -1, significa que la letra no existe 
    # en lo que queda de la cadena
    if pos < 0:
        found = False
        break
    
    # Si la encuentra, actualizamos 'start' para que la próxima búsqueda 
    # comience justo después de la letra actual
    start = pos + 1

# 3. Resultado final
if found:
    print("Si")
else:
    print("No")