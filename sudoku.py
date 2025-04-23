import math

def print_board(board):
    n = len(board)
    box_size = int(math.sqrt(n))
    for i in range(n):
        if i % box_size == 0 and i != 0:
            print("-" * (n * 2 + box_size - 1))
        for j in range(n):
            if j % box_size == 0 and j != 0:
                print("|", end=" ")
            val = board[i][j]
            print(val if val != 0 else ".", end=" ")
        print()

def is_valid(board, row, col, num):
    n = len(board)
    box_size = int(math.sqrt(n))
    
    # Check row and column
    for i in range(n):
        if board[row][i] == num or board[i][col] == num:
            return False

    # Check box
    start_row = row - row % box_size
    start_col = col - col % box_size
    for i in range(box_size):
        for j in range(box_size):
            if board[start_row + i][start_col + j] == num:
                return False

    return True

def solve(board):
    n = len(board)
    for row in range(n):
        for col in range(n):
            if board[row][col] == 0:
                for num in range(1, n + 1):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve(board):
                            return True
                        board[row][col] = 0
                return False
    return True

def input_board():
    size = int(input("Enter the size of the board (e.g., 4, 9, 16): "))
    sqrt_val = math.sqrt(size)
    if sqrt_val != int(sqrt_val):
        print("Only sizes with whole square roots are supported (e.g., 4, 9, 16)")
        return None

    board = []
    print(f"Enter the Sudoku board row by row (use 0 for empty cells):")
    for i in range(size):
        row = list(map(int, input(f"Row {i + 1}: ").strip().split()))
        if len(row) != size:
            print(f"Each row must have {size} numbers.")
            return None
        board.append(row)

    return board

# Main
board = input_board()
if board:
    print("\nInitial Board:")
    print_board(board)

    if solve(board):
        print("\nSolved Sudoku:")
        print_board(board)
    else:
        print("No solution exists for the given Sudoku.")
