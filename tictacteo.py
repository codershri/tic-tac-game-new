# def evaluate(board):
#     # Check rows and columns
#     for i in range(3):
#         if board[i][0] != '.' and board[i][0] == board[i][1] == board[i][2]:
#             return 10 if board[i][0] == 'X' else -10
#         if board[0][i] != '.' and board[0][i] == board[1][i] == board[2][i]:
#             return 10 if board[0][i] == 'X' else -10
#     # Check diagonals
#     if board[0][0] != '.' and board[0][0] == board[1][1] == board[2][2]:
#         return 10 if board[0][0] == 'X' else -10
#     if board[0][2] != '.' and board[0][2] == board[1][1] == board[2][0]:
#         return 10 if board[0][2] == 'X' else -10

#     return 0  # No winner

# def board_to_string(board):
#     return ''.join(cell for row in board for cell in row)

# def minimax(board, is_max, memo):
#     board_state = board_to_string(board)
#     if board_state in memo:
#         return memo[board_state]

#     score = evaluate(board)
#     if score != 0:
#         return score

#     if not any(cell == '.' for row in board for cell in row):
#         return 0

#     if is_max:
#         best = -float('inf')
#         for i in range(3):
#             for j in range(3):
#                 if board[i][j] == '.':
#                     board[i][j] = 'X'
#                     best = max(best, minimax(board, not is_max, memo))
#                     board[i][j] = '.'
#         memo[board_state] = best
#         return best
#     else:
#         best = float('inf')
#         for i in range(3):
#             for j in range(3):
#                 if board[i][j] == '.':
#                     board[i][j] = 'O'
#                     best = min(best, minimax(board, not is_max, memo))
#                     board[i][j] = '.'
#         memo[board_state] = best
#         return best

# if __name__ == "__main__":
#     board = [['.' for _ in range(3)] for _ in range(3)]
#     memo = {}
#     result = minimax(board, True, memo)
#     print(f"Best move score: {result}")
def print_board(board):
    for row in board:
        print(' '.join(row))
    print()

def is_board_full(board):
    return all(cell != '.' for row in board for cell in row)

def evaluate(board):
    # Check rows and columns
    for i in range(3):
        if board[i][0] != '.' and board[i][0] == board[i][1] == board[i][2]:
            return 10 if board[i][0] == 'X' else -10
        if board[0][i] != '.' and board[0][i] == board[1][i] == board[2][i]:
            return 10 if board[0][i] == 'X' else -10
    # Check diagonals
    if board[0][0] != '.' and board[0][0] == board[1][1] == board[2][2]:
        return 10 if board[0][0] == 'X' else -10
    if board[0][2] != '.' and board[0][2] == board[1][1] == board[2][0]:
        return 10 if board[0][2] == 'X' else -10

    return 0

def is_valid_move(board, row, col):
    return 0 <= row < 3 and 0 <= col < 3 and board[row][col] == '.'

def main():
    board = [['.' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    while True:
        print_board(board)
        row, col = map(int, input(f"Player {current_player}, enter your move (row and column): ").split())

        if not is_valid_move(board, row, col):
            print("Invalid move. Try again.")
            continue

        board[row][col] = current_player

        result = evaluate(board)
        if result == 10:
            print_board(board)
            print("Player X wins!")
            break
        elif result == -10:
            print_board(board)
            print("Player O wins!")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    main()
