def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

    # exception ZeroDivisionError
    # Raised when the second argument of a division or modulo operation is zero. The associated value is a string 
    # indicating the type of the operands and the operation.
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b

def calc():
    while True:
        print("Select operation.")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")

        # exception ValueError
        # Raised when an operation or function receives an argument that has the right type but an inappropriate
        # value, and the situation is not described by a more precise exception such as IndexError.
        # tldr: Inappropriate argument value (of correct type).

        try:
            choice = int(input("Enter choice: (1/2/3/4): "))
            if choice < 1 or choice > 4:
                raise ValueError
        except ValueError:
            print("Invalid. Please enter a valid choice.")
            continue

        try:
            number1 = float(input("Enter first number: "))
            number2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid. Please enter valid numbers.")
            continue

        if choice == 1:
            result = add(number1, number2)
            assign_operator = "+"
        elif choice == 2:
            result = subtract(number1, number2)
            assign_operator = "-"
        elif choice == 3:
            result = multiply(number1, number2)
            assign_operator = "*"
        else:
            try:
                result = divide(number1, number2)
                assign_operator = "/"
            except Exception as e:
                print(e)        
                continue

        print('{} {} {} = {}'.format(number1, assign_operator, number2, result))

        choice = input("Would you like to do a new calculation? (yes/no): ")
        if choice.lower() == "no":
            break

    print("see you space cowboy.")

calc()

# :
# https://docs.python.org/3/library/exceptions.html?highlight=#ValueError
# https://docs.python.org/3/library/exceptions.html?highlight=#ZeroDivisionError
# https://www.geeksforgeeks.org/python-raise-keyword/
# https://www.w3schools.com/python/python_try_except.asp
