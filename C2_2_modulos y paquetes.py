# EL MÓDULO (Simula 'module.py')
# Si esto fuera un archivo aparte, se llamaría module.py

__counter = 0

def suml(the_list):
    global __counter
    __counter += 1
    the_sum = 0
    for element in the_list:
        the_sum += element
    return the_sum

def prodl(the_list):
    global __counter
    __counter += 1
    prod = 1
    for element in the_list:
        prod *= element
    return prod

if __name__ == "__main__":
    # Este bloque solo corre cuando el archivo se ejecuta directamente.
    # Si este archivo fuera IMPORTADO desde otro, esto NO se imprimiría.
    print("EJECUCIÓN LOCAL: Realizando pruebas internas...")
    my_list = [i+1 for i in range(5)]
    print(f"Prueba Suma: {suml(my_list) == 15}")
    print(f"Prueba Producto: {prodl(my_list) == 120}")



# EL CLIENTE (Simula 'main.py')

# En un entorno real, se usaria 'import module'
# y 'path.append' si estuviera en otra carpeta.

print("\n--- INICIO DEL PROGRAMA PRINCIPAL ---")

# Simulamos el uso del módulo
zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]

# Si estuvieran separados, usarías: module.suml(zeroes)
print(f"Resultado suma de ceros: {suml(zeroes)}")
print(f"Resultado producto de unos: {prodl(ones)}")

# Explicación de la variable __name__:
print(f"\nValor actual de __name__: {__name__}")
# Nota: Aquí siempre será "__main__" porque todo está en el mismo archivo.