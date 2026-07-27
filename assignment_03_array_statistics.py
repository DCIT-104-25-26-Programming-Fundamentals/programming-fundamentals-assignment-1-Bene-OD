# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 3
# Topic: Lists (Arrays), Loops, and Functions
# =============================================================================
#
# TASK: Array Statistics Calculator
#
# Write a Python program that reads a collection of numbers from the user
# and computes key statistical values using separate functions.
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLE
# -----------------------------------------------------------------------------
#
#   How many numbers? 5
#   Enter number 1: 4
#   Enter number 2: 7
#   Enter number 3: 2
#   Enter number 4: 9
#   Enter number 5: 1
#
#   Results:
#   Sum:     23
#   Average: 4.6
#   Maximum: 9
#   Minimum: 1
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST implement each calculation in its own function (see scaffold).
# - You may NOT use Python's built-in sum(), max(), or min() functions.
#   Implement the logic yourself using loops inside each function.
# - N must be a positive integer. If the user enters 0 or a negative
#   number, print an error message and stop.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def calculate_sum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total


def calculate_average(numbers):
    return calculate_sum(numbers) / len(numbers)


def find_max(numbers):
    maximum = numbers[0]
    for number in numbers[1:]:
        if number > maximum:
            maximum = number
    return maximum


def find_min(numbers):
    minimum = numbers[0]
    for number in numbers[1:]:
        if number < minimum:
            minimum = number
    return minimum


def get_float_input(prompt):
    while True:
        value_input = input(prompt).strip()
        if value_input.lower() in {"q", "quit", "exit"}:
            return None
        try:
            return float(value_input)
        except ValueError:
            print("Invalid input. Please enter a number or Q to quit.")


if __name__ == "__main__":
    while True:
        user_input = input("How many numbers? (or Q to quit): ").strip()
        if user_input.lower() in {"q", "quit", "exit"}:
            print("Goodbye!")
            break

        try:
            count = int(user_input)
        except ValueError:
            print("Error: Please enter a positive integer.")
            continue

        if count <= 0:
            print("Error: Number of values must be positive.")
            continue

        numbers = []
        for i in range(1, count + 1):
            value = get_float_input(f"Enter number {i}: ")
            if value is None:
                print("Operation cancelled. Returning to main menu.")
                break
            numbers.append(value)

        if len(numbers) != count:
            continue

        print("\nResults:")
        print(f"Sum:     {calculate_sum(numbers)}")
        print(f"Average: {calculate_average(numbers)}")
        print(f"Maximum: {find_max(numbers)}")
        print(f"Minimum: {find_min(numbers)}")

