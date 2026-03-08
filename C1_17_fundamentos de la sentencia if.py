# Programa que calcula el Impuesto Personal de Ingresos (IPI)

# Pedimos al usuario que ingrese su ingreso anual
ingreso = float(input("Introduce el ingreso anual: "))

# Variable donde se guardará el impuesto
impuesto = 0

# Si el ingreso es menor o igual a 85528
if ingreso <= 85528:
    # Se calcula el 18% del ingreso y se resta la exención fiscal
    impuesto = ingreso * 0.18 - 556.02

# Si el ingreso es mayor a 85528
else:
    # Se calcula un impuesto base más el 32% del excedente
    impuesto = 14839.02 + (ingreso - 85528) * 0.32

# Si el impuesto resulta negativo, se ajusta a 0
if impuesto < 0:
    impuesto = 0

# Se muestra el impuesto redondeado a pesos enteros
print("El impuesto es:", round(impuesto), "pesos","\n")


print("Problema 3.1.12:")
# Programa que determina si un año es bisiesto o común
# según las reglas del calendario Gregoriano.

# Se solicita al usuario que introduzca un año.
# Se usa int() porque el año debe ser un número entero.
year = int(input("Introduce un año: "))

# Primero verificamos si el año es anterior a 1582,
# ya que el calendario Gregoriano comenzó a usarse a partir de ese año.
if year < 1582:
	print("No esta dentro del período del calendario Gregoriano")

# Si el año está dentro del calendario Gregoriano,
# se aplican las reglas para determinar si es bisiesto o común.
else:

	# Si el año no es divisible entre 4,
	# entonces es un año común.
	if year % 4 != 0:
		print("Año Común")

	# Si el año es divisible entre 4 pero no entre 100,
	# entonces es un año bisiesto.
	elif year % 100 != 0:
		print("Año Bisiesto")

	# Si el año es divisible entre 100 pero no entre 400,
	# entonces vuelve a ser un año común.
	elif year % 400 != 0:
		print("Año Común")

	# Si el año es divisible entre 400,
	# entonces es un año bisiesto.
	else:
		print("Año Bisiesto")