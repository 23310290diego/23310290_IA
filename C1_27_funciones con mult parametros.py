print("Calcular el IMC y convertir unidades del Sistema Inglés al Sistema Métrico")
def bmi(weight, height):
    # Verifica si los valores están dentro de un rango razonable
    if height < 1.0 or height > 2.5 or weight < 20 or weight > 200:
        return None

    # Calcula el índice de masa corporal
    return weight / height ** 2


# Ejemplo con valores válidos
print(bmi(70, 1.65))

print("\n")
print("Calculadora de BMI con conversión de unidades")
# Función que convierte pies y pulgadas a metros
# Recibe dos parámetros: ft (pies) e inch (pulgadas)
# inch tiene un valor por defecto de 0.0
def ft_and_inch_to_m(ft, inch = 0.0):

    # Se devuelve la altura convertida a metros
    # 1 pie = 0.3048 m
    # 1 pulgada = 0.0254 m
    return ft * 0.3048 + inch * 0.0254


# Función que convierte libras a kilogramos
# Recibe un parámetro: lb (libras)
def lb_to_kg(lb):

    # Devuelve el peso en kilogramos
    # 1 libra = 0.4535923 kg
    return lb * 0.4535923


# Función que calcula el Índice de Masa Corporal (BMI)
# Recibe dos parámetros: weight (peso en kg) y height (altura en metros)
def bmi(weight, height):

    # Verifica si los valores están dentro de un rango razonable
    # Si no lo están, la función devuelve None
    if height < 1.0 or height > 2.5 or weight < 20 or weight > 200:
        return None

    # Calcula y devuelve el BMI usando la fórmula
    return weight / height ** 2


# Se llama a la función bmi usando argumentos de palabra clave
# Primero se convierten las libras a kg y pies/pulgadas a metros
print(bmi(weight = lb_to_kg(176), height = ft_and_inch_to_m(5, 7)),"\n")
print("funciones: triangulos")
# Definición de la función is_a_triangle
# Esta función recibe tres parámetros: a, b y c
# que representan las longitudes de los lados de un posible triángulo
def is_a_triangle(a, b, c):

    # Primera condición del triángulo:
    # la suma de dos lados debe ser mayor que el tercer lado
    # si a + b es menor o igual que c, no se puede formar un triángulo
    if a + b <= c:
        return False

    # Segunda condición
    # si b + c es menor o igual que a, tampoco es triángulo
    if b + c <= a:
        return False

    # Tercera condición
    # si c + a es menor o igual que b, tampoco es triángulo
    if c + a <= b:
        return False

    # Si ninguna condición anterior se cumple,
    # significa que los tres lados sí pueden formar un triángulo
    return True


# Llamada a la función con lados 1,1,1
# Como todos los lados cumplen la regla del triángulo, devolverá True
print(is_a_triangle(1, 1, 1))

# Llamada a la función con lados 1,1,3
# 1 + 1 = 2, y 2 no es mayor que 3, por lo tanto no es un triángulo
# la función devolverá False
print(is_a_triangle(1, 1, 3),"\n")

print("Version compacta")

# Definición de la función is_a_triangle
# Recibe tres parámetros: a, b y c que representan
# las longitudes de los lados de un posible triángulo
def is_a_triangle(a, b, c):
    # Si todas son verdaderas devuelve True, si alguna falla devuelve False.
    return a + b > c and b + c > a and c + a > b


# Llamada a la función con lados 1, 1 y 1
# Cumple todas las condiciones, por lo tanto imprime True
print(is_a_triangle(1, 1, 1))

# Llamada a la función con lados 1, 1 y 3
# 1 + 1 no es mayor que 3, por lo tanto imprime False
print(is_a_triangle(1, 1, 3))

