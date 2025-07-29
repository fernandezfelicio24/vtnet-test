def hello_world():
    """Prints a welcome message and function description."""
    print("Welcome!\nThis is the hello world function.")

def odd_even_function():
    print("This is Odd Even Test :")
    try:
        # Prompt user for input
        number = int(input("Enter a number: "))
        # Check if the number is odd or even
        if number % 2 == 0:
            print(f"{number} is an even number.")
        else:
            print(f"{number} is an odd number.")
    except ValueError:
        print("Please enter a valid integer.")



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
    while True:
        print("\n=== Menu ===")
        print("1. Run Hello World Function")
        print("2. Run Odd Even Test")
        print("3. Run Calculator")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            hello_world()
        elif choice == "2":
            odd_even_function()
        elif choice == "3":
            calculator_function()
        elif choice == "4":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

