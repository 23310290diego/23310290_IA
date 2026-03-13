from random import randrange

# Crear el tablero inicial
# Cada fila es una lista dentro de otra lista
board = [[1, 2, 3],
         [4, "X", 6],   # La máquina empieza colocando X en el centro
         [7, 8, 9]]


# Función para mostrar el tablero
def display_board(board):

    for row in range(3):
        print("+-------+-------+-------+")
        print("|       |       |       |")

        for col in range(3):
            print("|  ", board[row][col], " ", end="")

        print("|")
        print("|       |       |       |")

    print("+-------+-------+-------+")


# Función para que el usuario haga su movimiento
def enter_move(board):

    while True:
        move = int(input("Ingresa tu movimiento: "))

        if move < 1 or move > 9:
            print("Movimiento inválido.")
            continue

        for row in range(3):
            for col in range(3):
                if board[row][col] == move:
                    board[row][col] = "O"
                    return

        print("Ese cuadro ya está ocupado.")


# Función que devuelve los cuadros libres
def make_list_of_free_fields(board):

    free = []

    for row in range(3):
        for col in range(3):
            if board[row][col] != "O" and board[row][col] != "X":
                free.append((row, col))

    return free


# Movimiento de la máquina (aleatorio)
def draw_move(board):

    free = make_list_of_free_fields(board)

    if len(free) > 0:
        move = randrange(len(free))
        row, col = free[move]
        board[row][col] = "X"


# Verificar si alguien ganó
def victory_for(board, sign):

    # filas
    for row in range(3):
        if board[row][0] == sign and board[row][1] == sign and board[row][2] == sign:
            return True

    # columnas
    for col in range(3):
        if board[0][col] == sign and board[1][col] == sign and board[2][col] == sign:
            return True

    # diagonales
    if board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
        return True

    if board[0][2] == sign and board[1][1] == sign and board[2][0] == sign:
        return True

    return False


# Bucle principal del juego
while True:

    display_board(board)

    enter_move(board)

    if victory_for(board, "O"):
        display_board(board)
        print("¡Has ganado!")
        break

    if len(make_list_of_free_fields(board)) == 0:
        display_board(board)
        print("Empate")
        break

    draw_move(board)

    if victory_for(board, "X"):
        display_board(board)
        print("La máquina ganó")
        break