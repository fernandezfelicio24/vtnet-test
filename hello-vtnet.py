def hello_world_function():  # Removed indentation
    print("WELCOME")
    print("This is hello world function")


def calculator_function():
    print("Simple Calculator")
    print("Operations: +, -, *, /")
    try:
        # Prompt user for input
        num1 = float(input("Enter first number: "))
        op = input("Enter operation (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        # Perform calculation based on operation
        if op == "+":
            result = num1 + num2
            print(f"{num1} + {num2} = {result}")
        elif op == "-":
            result = num1 - num2
            print(f"{num1} - {num2} = {result}")
        elif op == "*":
            result = num1 * num2
            print(f"{num1} * {num2} = {result}")
        elif op == "/":
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
            else:
                result = num1 / num2
                print(f"{num1} / {num2} = {result}")
        else:
            print("Error: Invalid operation. Please use +, -, *, or /.")
    except ValueError:
        print("Error: Please enter valid numbers.")


if __name__ == "__main__":
    #hello_world_function()  # Uncommented to run the function
    calculator_function()