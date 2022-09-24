def show_board(board):
    for i in board:
        print(*i, sep=" | ")
        print("---------")

def prompt_player(msg: str, board):
    number = 0

    while True:
        try:
            number = int(input(msg))
            return number
        except ValueError:
            show_board(board)
            msg = "Por favor introduzca una casilla valida: "

def set_pos(board, n: int, player: str):
    board_changed = False

    for k, i in enumerate(board):
        for l, j in enumerate(i):
            if (j == n):
                board_changed = True
                board[k][l] = player

    if not board_changed:
        show_board(board)
        number = prompt_player("Por favor introduzca una casilla no tomada: ", board)
        set_pos(board, number, player)

    return board


def win_check(board):
    if board[0][0] == board[0][1] == board[0][2]:
        return board[0][0]
    elif board[1][0] == board[1][1] == board[1][2]:
        return board[1][0]
    elif board[2][0] == board[2][1] == board[2][2]:
        return board[2][0]
    elif board[0][0] == board[1][0] == board[2][0]:
        return board[0][0]
    elif board[0][1] == board[1][1] == board[2][1]:
        return board[0][1]
    elif board[0][2] == board[1][2] == board[2][2]:
        return board[0][2]
    elif board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    elif board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]
    return False

def is_draw(board):
    draw = True

    for i in board:
        for j in i:
            if j != "O" and j != "X":
                draw = False
                break

    return draw

def tricky_game():
    count = 1
    board = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]

    while True:
        show_board(board)    
        if winner := win_check(board):
            print(f"El ganador fue {winner}")
            break
        if count % 2 != 0:
            number = prompt_player("Ingrese la casilla jugador 1 (X): ", board)
            board = set_pos(board, number, "X")
        else:
            number = prompt_player("Ingrese la casilla jugador 2 (O):", board)
            board = set_pos(board, number, "O")

        if is_draw(board):
            print("Ambos jugadores empataron")
            break

        count += 1 

    print("Partida terminada")

if __name__ == "__main__":
    tricky_game()