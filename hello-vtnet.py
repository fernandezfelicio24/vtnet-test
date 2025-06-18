def hello_world_function():  # Fixed function name typo and added colon
    print("WELCOME")
    print("This is hello world function")
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

if __name__ == "__main__":  # Main entry point
    hello_world_function()  # Call your function here
    #odd_even_function()
