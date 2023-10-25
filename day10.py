# Calculator
# from art import logo

def add(n1, n2):
    """add numbers"""
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
        should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculator_function = operations[operation_symbol]

        answer = calculator_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        continue_answer = input(
            f"Type 'y' to continue {answer}, otherwise type 'n': ")

        if continue_answer == "y":
            num1 = answer
        elif continue_answer == "n":
            should_continue = False
            calculator()


calculator()
