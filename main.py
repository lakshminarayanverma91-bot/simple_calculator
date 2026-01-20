# Function to add two numbers
def add(a, b):
    return a + b

# Function to find absolute difference
def diff(a, b):
    return abs(a - b)

# Function to multiply two numbers
def product(a, b):
    return a * b

# Function to divide two numbers
def division(a, b):
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed")
    else:
        return (a / b)


try:
    # Taking input from user
    num1 = float(input("Enter First Number: "))
    op = input("Choose an operation (+, -, *, /): ")
    num2 = float(input("Enter Second Number: "))

    # Performing operation based on user choice
    if op == "+":
        print("Sum:", add(num1, num2))

    elif op == "-":
        print("Subtraction:", diff(num1, num2))

    elif op == "*":
        print("Product:", product(num1, num2))

    elif op == "/":
        print("Division:", division(num1, num2))

    else:
        print("Invalid Operation")

# Handles wrong number input (e.g. letters instead of numbers)
except ValueError:
    print("Please enter valid numeric values.")

# Handles division by zero error
except ZeroDivisionError as e:
    print("Error:", e)

# Handles any unexpected error
except Exception as e:
    print("Unexpected Error:", e)

finally:
    # Always runs
    print("Program ended.")


    