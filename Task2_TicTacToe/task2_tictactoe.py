import math

def print_board(board):
    for row in board:
        print(row)
    print()

def check_winner(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):
            return True
        if all(board[j][i] == player for j in range(3)):
            return True
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

def empty_cells(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]

def minimax(board, depth, is_maximizing):
    if check_winner(board, "O"):
        return 1
    if check_winner(board, "X"):
        return -1
    if not empty_cells(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for (i, j) in empty_cells(board):
            board[i][j] = "O"
            score = minimax(board, depth + 1, False)
            board[i][j] = " "
            best_score = max(best_score, score)
        return best_score
    else:
        best_score = math.inf
        for (i, j) in empty_cells(board):
            board[i][j] = "X"
            score = minimax(board, depth + 1, True)
            board[i][j] = " "
            best_score = min(best_score, score)
        return best_score

def best_move(board):
    best_score = -math.inf
    move = None
    for (i, j) in empty_cells(board):
        board[i][j] = "O"
        score = minimax(board, 0, False)
        board[i][j] = " "
        if score > best_score:
            best_score = score
            move = (i, j)
    return move

def play_game():
    board = [[" "]*3 for _ in range(3)]
    print("Tic-Tac-Toe Game: You are X, AI is O")

    while True:
        print_board(board)
        row = int(input("Enter row (0-2): "))
        col = int(input("Enter col (0-2): "))

        if board[row][col] != " ":
            print("Position already taken. Try again.")
            continue

        board[row][col] = "X"

        if check_winner(board, "X"):
            print_board(board)
            print("You win.")
            break

        if not empty_cells(board):
            print_board(board)
            print("Game ended in a tie.")
            break

        ai_row, ai_col = best_move(board)
        board[ai_row][ai_col] = "O"

        if check_winner(board, "O"):
            print_board(board)
            print("AI wins.")
            break

        if not empty_cells(board):
            print_board(board)
            print("Game ended in a tie.")
            break

play_game()
