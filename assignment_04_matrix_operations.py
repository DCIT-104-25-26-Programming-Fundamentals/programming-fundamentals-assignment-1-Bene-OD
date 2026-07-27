# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def read_matrix(rows, cols):
    matrix = []
    for row_index in range(rows):
        while True:
            row_input = input(f"Enter row {row_index + 1}: ").strip().split()
            if len(row_input) != cols:
                print(f"Error: Please enter exactly {cols} values.")
                continue
            try:
                row = [int(value) for value in row_input]
                break
            except ValueError:
                print("Error: Please enter integer values only.")
        matrix.append(row)
    return matrix


def print_matrix(matrix):
    for row in matrix:
        print(" ".join(f"{value:>5}" for value in row))


def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    transpose = []
    for col in range(cols):
        new_row = []
        for row in range(rows):
            new_row.append(matrix[row][col])
        transpose.append(new_row)
    return transpose


def add_matrices(matrix_a, matrix_b):
    rows = len(matrix_a)
    cols = len(matrix_a[0])
    result = []
    for row in range(rows):
        result_row = []
        for col in range(cols):
            result_row.append(matrix_a[row][col] + matrix_b[row][col])
        result.append(result_row)
    return result


def multiply_matrices(matrix_a, matrix_b):
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0])
    cols_b = len(matrix_b[0])
    result = []
    for row in range(rows_a):
        result_row = []
        for col in range(cols_b):
            total = 0
            for k in range(cols_a):
                total += matrix_a[row][k] * matrix_b[k][col]
            result_row.append(total)
        result.append(result_row)
    return result


def get_positive_int(prompt):
    while True:
        value_input = input(prompt).strip()
        if value_input.lower() in {"q", "quit", "exit"}:
            return None
        try:
            value = int(value_input)
        except ValueError:
            print("Error: Please enter a positive integer or Q to quit.")
            continue

        if value <= 0:
            print("Error: Value must be positive.")
            continue

        return value


def show_menu():
    print("=============================")
    print("      MATRIX OPERATIONS")
    print("=============================")
    print("1. Transpose a matrix")
    print("2. Add two matrices")
    print("3. Multiply two matrices")
    print("4. Quit")


if __name__ == "__main__":
    while True:
        show_menu()
        choice = input("Select an option (1-4): ").strip()
        if choice == "4":
            print("Goodbye!")
            break
        elif choice == "1":
            rows = get_positive_int("Enter number of rows (or Q to quit): ")
            if rows is None:
                continue
            cols = get_positive_int("Enter number of columns (or Q to quit): ")
            if cols is None:
                continue
            matrix = read_matrix(rows, cols)
            print("\nOriginal Matrix:")
            print_matrix(matrix)
            print("\nTransposed Matrix:")
            print_matrix(transpose_matrix(matrix))
        elif choice == "2":
            rows = get_positive_int("Enter number of rows for both matrices (or Q to quit): ")
            if rows is None:
                continue
            cols = get_positive_int("Enter number of columns for both matrices (or Q to quit): ")
            if cols is None:
                continue
            matrix_a = read_matrix(rows, cols)
            matrix_b = read_matrix(rows, cols)
            print("\nMatrix Sum:")
            print_matrix(add_matrices(matrix_a, matrix_b))
        elif choice == "3":
            rows_a = get_positive_int("Enter number of rows for matrix A (or Q to quit): ")
            if rows_a is None:
                continue
            cols_a = get_positive_int("Enter number of columns for matrix A (or Q to quit): ")
            if cols_a is None:
                continue
            rows_b = get_positive_int("Enter number of rows for matrix B (or Q to quit): ")
            if rows_b is None:
                continue
            cols_b = get_positive_int("Enter number of columns for matrix B (or Q to quit): ")
            if cols_b is None:
                continue
            if cols_a != rows_b:
                print("Error: Number of columns in A must equal number of rows in B.")
                continue
            matrix_a = read_matrix(rows_a, cols_a)
            matrix_b = read_matrix(rows_b, cols_b)
            print("\nMatrix Product A x B:")
            print_matrix(multiply_matrices(matrix_a, matrix_b))
        else:
            print("Error: Please select a valid option between 1 and 4.")

