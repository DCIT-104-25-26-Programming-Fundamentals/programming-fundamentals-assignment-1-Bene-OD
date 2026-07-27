# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 5
# Topic: Loops, Sequences, and Functions
# =============================================================================
#
# TASK: Fibonacci Sequence Generator
#
# The Fibonacci sequence is a series of numbers where each number is the sum
# of the two numbers before it:
#
#   0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
#
# Write a Python program with TWO parts, each implemented as a function.
#
# -----------------------------------------------------------------------------
# PART A — Print the First N Terms
# -----------------------------------------------------------------------------
# - Ask the user how many terms (N) to display.
# - Print the first N numbers of the Fibonacci sequence on one line.
#
# Example:
#   How many terms? 7
#   Fibonacci sequence: 0 1 1 2 3 5 8
#
# -----------------------------------------------------------------------------
# PART B — Check if a Number Belongs to the Sequence
# -----------------------------------------------------------------------------
# - Ask the user to enter a number.
# - Determine whether that number is a Fibonacci number.
# - Print an appropriate message.
#
# Example:
#   Enter a number to check: 13
#   13 is a Fibonacci number.
#
#   Enter a number to check: 20
#   20 is NOT a Fibonacci number.
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use a loop (not recursion) to generate the sequence in both parts.
# - N must be a positive integer. If it is not, print an error message.
# - Each part must be implemented in its own function (see scaffold below).
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def generate_fibonacci(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence


def is_fibonacci_number(number):
    if number < 0:
        return False

    a, b = 0, 1
    while a < number:
        a, b = b, a + b
    return a == number


def show_menu():
    print("=============================")
    print("     FIBONACCI SEQUENCE")
    print("=============================")
    print("1. Print the first N terms")
    print("2. Check if a number belongs to the sequence")
    print("3. Quit")


def get_positive_int(prompt):
    while True:
        user_input = input(prompt).strip()
        if user_input.lower() in {"q", "quit", "exit"}:
            return None
        try:
            value = int(user_input)
        except ValueError:
            print("Error: Please enter a positive integer or Q to quit.")
            continue
        if value <= 0:
            print("Error: Please enter a positive integer.")
            continue
        return value


def get_int(prompt):
    while True:
        user_input = input(prompt).strip()
        if user_input.lower() in {"q", "quit", "exit"}:
            return None
        try:
            return int(user_input)
        except ValueError:
            print("Error: Please enter an integer or Q to quit.")


if __name__ == "__main__":
    while True:
        show_menu()
        choice = input("Select an option (1-3): ").strip()
        if choice == "3":
            print("Goodbye!")
            break
        if choice == "1":
            n = get_positive_int("How many terms? (or Q to quit): ")
            if n is None:
                continue
            sequence = generate_fibonacci(n)
            print("Fibonacci sequence:", " ".join(str(value) for value in sequence))
        elif choice == "2":
            number_to_check = get_int("Enter a number to check (or Q to quit): ")
            if number_to_check is None:
                continue
            if is_fibonacci_number(number_to_check):
                print(f"{number_to_check} is a Fibonacci number.")
            else:
                print(f"{number_to_check} is NOT a Fibonacci number.")
        else:
            print("Error: Please select a valid option between 1 and 3.")

