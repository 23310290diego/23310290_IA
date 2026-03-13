from random import randrange

# Crear el tablero inicial como una lista de listas (3x3)
# Cada posición contiene un número que representa una casilla libre
board = [[1, 2, 3],
         [4, "X", 6],   # La máquina comienza colocando 'X' en el centro
         [7, 8, 9]]



# Función para mostrar el tablero en pantalla
# Recibe el tablero como parámetro

def display_board(board):

    # Recorre cada fila del tablero
    for row in range(3):
        print("+-------+-------+-------+")
        print("|       |       |       |")

        # Recorre cada columna de la fila
        for col in range(3):
            # Muestra el contenido de la casilla
            print("|  ", board[row][col], " ", end="")

        print("|")
        print("|       |       |       |")

    print("+-------+-------+-------+")



# Función para que el usuario ingrese su movimiento
# Valida que el número sea correcto y que la casilla esté libre

def enter_move(board):

    while True:

        # Solicita al usuario un número del 1 al 9
        move = int(input("Ingresa tu movimiento: "))

        # Verifica que el número esté dentro del rango válido
        if move < 1 or move > 9:
            print("Movimiento inválido.")
            continue

        # Busca el número dentro del tablero
        for row in range(3):
            for col in range(3):

                # Si la casilla coincide con el número ingresado
                # significa que está libre
                if board[row][col] == move:
                    board[row][col] = "O"   # Coloca la ficha del jugador
                    return                  # Sale de la función

        # Si no encontró la casilla significa que ya estaba ocupada
        print("Ese cuadro ya está ocupado.")



# Función que devuelve una lista con las posiciones libres
# Cada posición se guarda como una tupla (fila, columna)

def make_list_of_free_fields(board):

    free = []

    # Recorre todo el tablero
    for row in range(3):
        for col in range(3):

            # Si la casilla no contiene 'X' ni 'O', está libre
            if board[row][col] != "O" and board[row][col] != "X":
                free.append((row, col))

    return free


# Movimiento de la máquina
# Selecciona una casilla libre al azar

def draw_move(board):

    # Obtiene todas las casillas libres
    free = make_list_of_free_fields(board)

    # Si hay espacios disponibles
    if len(free) > 0:

        # Elige una posición aleatoria
        move = randrange(len(free))

        # Obtiene fila y columna de la tupla seleccionada
        row, col = free[move]

        # Coloca la ficha 'X'
        board[row][col] = "X"



# Función que verifica si alguien ganó
# Recibe el tablero y el símbolo a comprobar ('X' o 'O')

def victory_for(board, sign):

    # Revisar filas
    for row in range(3):
        if board[row][0] == sign and board[row][1] == sign and board[row][2] == sign:
            return True

    # Revisar columnas
    for col in range(3):
        if board[0][col] == sign and board[1][col] == sign and board[2][col] == sign:
            return True

    # Revisar diagonales
    if board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
        return True

    if board[0][2] == sign and board[1][1] == sign and board[2][0] == sign:
        return True

    # Si ninguna condición se cumple, no hay ganador
    return False



# Bucle principal del juego
# Se ejecuta hasta que alguien gane o haya empate

while True:

    # Mostrar el tablero actual
    display_board(board)

    # Turno del jugador
    enter_move(board)

    # Verificar si el jugador ganó
    if victory_for(board, "O"):
        display_board(board)
        print("¡Has ganado!")
        break

    # Verificar empate (no hay casillas libres)
    if len(make_list_of_free_fields(board)) == 0:
        display_board(board)
        print("Empate")
        break

    # Turno de la máquina
    draw_move(board)

    # Verificar si la máquina ganó
    if victory_for(board, "X"):
        display_board(board)
        print("La máquina ganó")
        break