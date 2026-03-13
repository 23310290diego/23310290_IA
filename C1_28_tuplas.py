print("tuplas ejemplo")
# Definición de una tupla (se usan paréntesis en lugar de corchetes)
my_tuple = (1, 10, 100, 1000)

# Acceso por índice positivo (empieza en 0)
print(my_tuple[0])    # Imprime 1

# Acceso por índice negativo (empieza desde el final, -1 es el último)
print(my_tuple[-1])   # Imprime 1000

# Slicing: desde el índice 1 hasta el final
print(my_tuple[1:])   # Imprime (10, 100, 1000)

# Slicing: desde el inicio hasta 2 posiciones antes del final
print(my_tuple[:-2])  # Imprime (1, 10)

# Iteración: recorrer cada elemento de la tupla con un ciclo for
for elem in my_tuple:
    print(elem)       # Imprime cada número en una línea nueva

print("\n")
print("Diccionarios")
# Creación de diccionarios con diferentes tipos de datos
# Llave: string | Valor: string
dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}

# Llave: string | Valor: entero (int)
phone_numbers = {'jefe': 5551234567, 'Suzy': 22657854310}

# Diccionario vacío (útil para llenar datos más tarde con un ciclo)
empty_dictionary = {}

# Mostrar el contenido
print(dictionary)
print(phone_numbers)

# Uso de len() para contar cuántos pares (entradas) hay
print(f"El diccionario tiene {len(dictionary)} palabras.") 
# Resultado: 3

print("\n")
print("Combinando tuplas y diccionarios ejemplo")
school_class = {}

while True:
    name = input("Ingresa el nombre del estudiante: ")
    if name == '':
        break
    
    score = int(input("Ingresa la calificación del estudiante (0-10): "))
    if score not in range(0, 11):
        break
    if name in school_class:
        # Si el alumno ya existe, "añadimos" la calificación a su tupla
        # Nota: Realmente estamos creando una tupla nueva y reemplazando la anterior
        school_class[name] += (score,)
    else:
        # Si es nuevo, creamos su primera tupla de un solo elemento
        school_class[name] = (score,)
        
# Procesamiento de resultados
for name in sorted(school_class.keys()):
    adding = 0
    counter = 0
    # Recorremos la tupla de calificaciones almacenada en cada llave
    for score in school_class[name]:
        adding += score
        counter += 1
    
    # Calculamos el promedio: Suma total / cantidad de elementos
    print(name, ":", adding / counter)