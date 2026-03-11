print("Uso del operador lógico AND")

# El operador AND se usa cuando queremos que dos
# condiciones se cumplan al mismo tiempo.

counter = 5
value = 100

# La condición será True solo si ambas partes son verdaderas
print(counter > 0 and value == 100)


print("equivalencia de expresiones lógicas")

# Aquí demostramos que dos expresiones diferentes
# pueden producir el mismo resultado lógico.

var = 1

# Verifica si var es mayor que 0
print(var > 0)

# Esta expresión significa lo mismo:
# "no es cierto que var sea menor o igual a 0"
print(not (var <= 0),"\n")



print("Valores lógicos y uso de NOT")
# En Python, cualquier número distinto de 0 se considera True.
# El número 0 se considera False.

i = 1

# not not i convierte el valor en booleano
# Si i es diferente de 0 el resultado será True
j = not not i

print(j)


# otra equivalencia lógica
# Estas dos expresiones también significan lo mismo.

# Verifica si var es diferente de 0
print(var != 0)

# Significa: "no es cierto que var sea igual a 0"
print(not (var == 0))

print("Comprobar el estado de un bit")
# Este programa demuestra cómo verificar si un bit específico
# dentro de un número está activado o desactivado usando una máscara.

# Variable que almacena varios bits
flag_register = 0x1234

# Máscara para el tercer bit (2^3 = 8)
the_mask = 8

# Verificamos si el tercer bit está encendido
if flag_register & the_mask:
    print("Mi bit está activado (1)")
else:
    print("Mi bit está desactivado (0)")


print("\n")
print("Reiniciar (apagar) un bit")
# Este ejemplo muestra cómo apagar un bit específico
# sin modificar los demás bits del número.

# Se usa AND con la negación de la máscara
flag_register = flag_register & ~the_mask

print("Registro después de reiniciar el bit:", flag_register)


print("\n")
print("Establecer (encender) un bit")
# Este ejemplo muestra cómo activar un bit específico
# usando el operador OR.

flag_register = flag_register | the_mask

print("Registro después de activar el bit:", flag_register)


print("\n")
print("Negar (invertir) un bit")
# Este ejemplo muestra cómo invertir el valor de un bit.
# Si era 1 se vuelve 0 y si era 0 se vuelve 1.

flag_register = flag_register ^ the_mask

print("Registro después de negar el bit:", flag_register)

print("Desplazamiento binario a la derecha")
# Este programa demuestra cómo funciona el desplazamiento
# de bits hacia la derecha en números enteros.

# Se define una variable con valor entero
var = 17

# Desplazar un bit a la derecha equivale a dividir entre 2
var_right = var >> 1

# Se imprime el resultado
print("Valor original:", var)
print("Resultado del desplazamiento a la derecha:", var_right)


print("\n")
print("Desplazamiento binario a la izquierda")
# Este ejemplo muestra cómo funciona el desplazamiento
# de bits hacia la izquierda.

# Desplazar dos bits a la izquierda equivale a multiplicar por 2^2
var_left = var << 2

# Se imprime el resultado
print("Valor original:", var)
print("Resultado del desplazamiento a la izquierda:", var_left)


print("\n")
print("Resultados finales")
# Se muestran todos los valores juntos para comparar

print(var, var_left, var_right)