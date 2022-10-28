def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    return a / b


key_value = {"+": "addition(a, b)", "-": "subtraction(a, b)", "*": "multiplication(a, b)", "/": "division(a, b)"}


def initial_operation():
    global a, b, calculation, result
    a = int(input("What's the first number? "))
    print("+\n-\n*\n/")
    calculation = input("Pick an operation: ")
    b = int(input("What's the second number: "))
    result = round(eval(key_value[calculation]), 3)


def continue_operation(result):
    a = result
    b = int(input("What's your next number? "))
    calculation = input("Pick an operation: ")
    result = round(eval(key_value[calculation]), 3)
    print(f"{a} {calculation} {b} = ", result)



def main():
    initial_operation()
    print(f"{a} {calculation} {b} = ", result)
    proceed = input(f"Type 'y' to continue calculating with , or type 'n' to start a new calculation: ")
    while proceed == "y":
        continue_operation(result)
        proceed = input(f"Type 'y' to continue calculating with , or type 'n' to start a new calculation: ")
    print("\nYou chose to start a new calculation. Hit the Run Button again")

main()
