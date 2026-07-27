# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 9
# =============================================================================
#
# TASK: Console-Based Simple Calculator
#
# Build a calculator program that runs in the console and performs basic
# arithmetic operations based on the user's input.
#
# -----------------------------------------------------------------------------
# OPERATIONS YOUR CALCULATOR MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Addition          ( + )    e.g.  10 + 3  =  13
#   2. Subtraction       ( - )    e.g.  10 - 3  =  7
#   3. Multiplication    ( * )    e.g.  10 * 3  =  30
#   4. Division          ( / )    e.g.  10 / 3  =  3.33
#   5. Modulus           ( % )    e.g.  10 % 3  =  1  (remainder)
#   6. Exponentiation    ( ** )   e.g.  2 ** 8  =  256
#   7. Quit
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ============================
#        SIMPLE CALCULATOR
#   ============================
#   1. Addition
#   2. Subtraction
#   3. Multiplication
#   4. Division
#   5. Modulus
#   6. Exponentiation
#   7. Quit
#   Select an operation (1-7):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Select an operation (1-7): 4
#   Enter first number : 10
#   Enter second number: 3
#   Result: 10 / 3 = 3.33
#
#   Select an operation (1-7): 4
#   Enter first number : 5
#   Enter second number: 0
#   Error: Cannot divide by zero.
#
#   Select an operation (1-7): 7
#   Goodbye!
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Each arithmetic operation MUST be written as its own function.
# - Use a loop so the calculator keeps running until the user selects Quit.
# - Division by zero must be caught and handled with a clear error message
#   (do NOT let the program crash).
# - Division results should be rounded to 2 decimal places.
# - Handle invalid menu choices gracefully.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    if b == 0:
        return None
    return a / b


def modulus(a, b):
    return a % b


def exponentiation(a, b):
    return a ** b


def show_menu():
    print("=============================")
    print("     SIMPLE CALCULATOR")
    print("=============================")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exponentiation")
    print("7. Quit")


def get_number(prompt):
    while True:
        user_input = input(prompt).strip()
        if user_input.lower() in {"q", "quit", "exit"}:
            return None
        try:
            return float(user_input)
        except ValueError:
            print("Error: Please enter a numeric value or Q to quit.")


if __name__ == "__main__":
    while True:
        show_menu()
        choice = input("Select an operation (1-7): ").strip()
        if choice == "7":
            print("Goodbye!")
            break

        if choice not in {"1", "2", "3", "4", "5", "6"}:
            print("Error: Please select a valid operation between 1 and 7.")
            continue

        first = get_number("Enter first number (or Q to quit): ")
        if first is None:
            continue

        second = get_number("Enter second number (or Q to quit): ")
        if second is None:
            continue

        if choice == "1":
            result = addition(first, second)
            print(f"Result: {first} + {second} = {result}")
        elif choice == "2":
            result = subtraction(first, second)
            print(f"Result: {first} - {second} = {result}")
        elif choice == "3":
            result = multiplication(first, second)
            print(f"Result: {first} * {second} = {result}")
        elif choice == "4":
            result = division(first, second)
            if result is None:
                print("Error: Cannot divide by zero.")
            else:
                print(f"Result: {first} / {second} = {result:.2f}")
        elif choice == "5":
            if second == 0:
                print("Error: Cannot divide by zero.")
            else:
                result = modulus(first, second)
                print(f"Result: {first} % {second} = {result}")
        elif choice == "6":
            result = exponentiation(first, second)
            print(f"Result: {first} ** {second} = {result}")

