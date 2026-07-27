# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 6
# Topic: Loops and Functions
# =============================================================================
#
# TASK: Multiplication Table Generator
#
# Write a Python program that generates multiplication tables using loops
# and functions.
#
# -----------------------------------------------------------------------------
# PART A — Single Table
# -----------------------------------------------------------------------------
# - Ask the user to enter a number.
# - Print the multiplication table for that number from 1 to 12.
#
# Expected output (if user enters 5):
#
#   Multiplication Table for 5:
#   5  x  1  =  5
#   5  x  2  =  10
#   5  x  3  =  15
#   ...
#   5  x  12 =  60
#
# -----------------------------------------------------------------------------
# PART B — Bonus: Tables from 1 to N
# -----------------------------------------------------------------------------
# - Ask the user to enter a number N.
# - Print the full multiplication table for every number from 1 to N.
# - Add a separator line (e.g. "---") between each table.
#
# Expected output (if user enters 3):
#
#   Multiplication Table for 1:
#   1  x  1  =  1
#   ...
#   1  x  12 =  12
#   ---------------------------
#   Multiplication Table for 2:
#   2  x  1  =  2
#   ...
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - N must be a positive integer. If the user enters an invalid value,
#   print an error message and stop.
# - Each part must be in its own function (see scaffold below).
# - Complete Part A before attempting Part B.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def print_single_table(number):
    print(f"Multiplication Table for {number}:")
    for i in range(1, 13):
        print(f"{number}  x  {i}  =  {number * i}")


def print_tables_up_to(n):
    for number in range(1, n + 1):
        print(f"Multiplication Table for {number}:")
        for i in range(1, 13):
            print(f"{number}  x  {i}  =  {number * i}")
        if number != n:
            print("---------------------------")


def get_positive_int(prompt):
    while True:
        user_input = input(prompt).strip()
        if user_input.lower() in {"q", "quit", "exit"}:
            return None
        try:
            value = int(user_input)
        except ValueError:
            print("Error: Please enter a valid integer or Q to quit.")
            continue
        if value <= 0:
            print("Error: Please enter a positive integer.")
            continue
        return value


def show_menu():
    print("=============================")
    print("   MULTIPLICATION TABLES")
    print("=============================")
    print("1. Print single table")
    print("2. Print tables from 1 to N")
    print("3. Quit")


if __name__ == "__main__":
    while True:
        show_menu()
        choice = input("Select an option (1-3): ").strip()
        if choice == "3":
            print("Goodbye!")
            break
        elif choice == "1":
            number = get_positive_int("Enter a number (or Q to quit): ")
            if number is None:
                continue
            print_single_table(number)
        elif choice == "2":
            n = get_positive_int("Enter a number N (or Q to quit): ")
            if n is None:
                continue
            print_tables_up_to(n)
        else:
            print("Error: Please select a valid option between 1 and 3.")

