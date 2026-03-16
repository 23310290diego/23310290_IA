print("Metodos de cadenas")

# capitalize(): Primera letra en mayúscula, el resto en minúscula
print('aBcD'.capitalize())
print("Alpha".capitalize())
print('ALPHA'.capitalize())
print(' Alpha'.capitalize())
print('123'.capitalize())

# center(): Centra el texto. Puede recibir el ancho y un carácter de relleno
print('[' + 'alpha'.center(10) + ']')
print('[' + 'gamma'.center(20, '*') + ']')

# endswith(): Revisa si la cadena termina con un texto específico
if "epsilon".endswith("on"):
    print("si")
else:
    print("no")

# find(): Busca un texto y devuelve su índice (posición). Devuelve -1 si no existe
print("Eta".find("ta"))
print("Eta".find("mma"))

# isalnum(): True si solo hay letras y números (sin símbolos ni espacios)
print('lambda30'.isalnum())
print('lambda'.isalnum())
print('30'.isalnum())
print('@'.isalnum())
print('lambda_30'.isalnum())
print(''.isalnum())

# isalpha(): True si el contenido son exclusivamente letras
print("Moooo".isalpha())
print('Mu40'.isalpha())

# isdigit(): True si el contenido son exclusivamente números
print('2018'.isdigit())
print("Year2019".isdigit())

# islower(): True si todas las letras son minúsculas
print("Moooo".islower())
print('moooo'.islower())

# isspace(): True si solo contiene espacios, saltos de línea (\n) o tabulaciones
print(' \n '.isspace())
print(" ".isspace())
print("mooo mooo mooo".isspace())

# isupper(): True si todas las letras son mayúsculas
print("Moooo".isupper())
print('moooo'.isupper())
print('MOOOO'.isupper())

# join(): Une una lista de cadenas usando la cadena base como pegamento
print(",".join(["omicron", "pi", "rho"]))

# lower(): Convierte todo el texto a minúsculas
print("SiGmA=60".lower())

# lstrip(): Elimina los espacios en blanco solo al inicio (izquierda)
print("[" + " tau ".lstrip() + "]")

# replace(): Reemplaza un texto por otro. El tercer número limita los cambios
print("www.netacad.com".replace("netacad.com", "pythoninstitute.org"))
print("This is it!".replace("is", "are"))
print("Apple juice".replace("juice", ""))
print("This is it!".replace("is", "are", 1))
print("This is it!".replace("is", "are", 2))

# rfind(): Busca desde la derecha. Puede recibir límites (inicio, fin)
print("tau tau tau".rfind("ta"))
print("tau tau tau".rfind("ta", 9))
print("tau tau tau".rfind("ta", 3, 9))

# rstrip(): Elimina espacios o caracteres específicos al final (derecha)
print("[" + " upsilon ".rstrip() + "]")
print("cisco.com".rstrip(".com"))

# split(): Divide la cadena en una lista (usa espacios por defecto)
print("phi           chi\npsi".split())

# startswith(): Revisa si la cadena empieza con un texto específico
print("omega".startswith("meg"))
print("omega".startswith("om"))

print()
# strip(): Elimina espacios en blanco al inicio y al final
print("[" + "    aleph    ".strip() + "]")

# swapcase(): Cambia mayúsculas a minúsculas y viceversa
print("Yo solo sé que no sé nada".swapcase())

print()
# title(): Formato de título (primera letra de cada palabra en mayúscula)
print("Yo solo sé que no sé nada. Parte 1.".title())

print()
# upper(): Convierte todo el texto a mayúsculas
print("Yo solo sé que no sé nada. Parte 2.".upper())

print("\m")
print("LAB Tu propio separador")
def mysplit(strng):
    # 1. Si la cadena está vacía, regresamos lista vacía de inmediato
    if not strng or strng.isspace():
        return []

    lista_palabras = []
    palabra_actual = ""
    en_palabra = False # Nos indica si estamos dentro de una palabra o en espacios

    for caracter in strng:
        if caracter != " ": # Si el carácter NO es un espacio...
            palabra_actual += caracter
            en_palabra = True
        else: # Si encontramos un espacio...
            if en_palabra: # ...y veníamos escribiendo una palabra
                lista_palabras.append(palabra_actual)
                palabra_actual = ""
                en_palabra = False
    
    # Al terminar el ciclo, agregamos la última palabra si quedó algo pendiente
    if en_palabra:
        lista_palabras.append(palabra_actual)

    return lista_palabras

# Pruebas requeridas
print(mysplit("Ser o no ser, esa es la cuestión"))
print(mysplit("Ser o no ser, esa es la cuestión"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))