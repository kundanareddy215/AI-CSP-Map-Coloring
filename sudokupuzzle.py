# Sudoku Solver using CSP (Backtracking)

# ---------------------------------------------
# CSP FORMULATION
# Variables: Each cell in the 9x9 grid
# Domain: {1,2,3,4,5,6,7,8,9}
# Constraints:
#   - No repetition in any row
#   - No repetition in any column
#   - No repetition in any 3x3 subgrid
# ---------------------------------------------

# Sample Sudoku (0 represents empty cells)
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Function to print board nicely
def print_board(board):
    print("\nSolved Sudoku:\n")
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)

        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")

            print(board[i][j], end=" ")

        print()

# Find next empty cell
def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None

# Check if valid placement
def is_valid(board, row, col, num):

    # Row check
    if num in board[row]:
        return False

    # Column check
    for i in range(9):
        if board[i][col] == num:
            return False

    # 3x3 subgrid check
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3

    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True

# Backtracking solver
def solve(board):
    empty = find_empty(board)

    if not empty:
        return True

    row, col = empty

    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num

            if solve(board):
                return True

            # Backtrack
            board[row][col] = 0

    return False

# Run solver
if solve(board):
    print_board(board)
else:
    print("No solution exists")
