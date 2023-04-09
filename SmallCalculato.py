# Define the function that performs addition
def add(num1, num2):
    return num1 + num2

# Define the function that performs subtraction
def subtract(num1, num2):
    return num1 - num2

# Define the function that performs multiplication
def multiply(num1, num2):
    return num1 * num2

# Define the function that performs division
def divide(num1, num2):
    return num1 / num2

# Get input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter an operation (+, -, *, /): ")

# Call the appropriate function based on the user's input
if operation == "+":
    result = add(num1, num2)
elif operation == "-":
    result = subtract(num1, num2)
elif operation == "*":
    result = multiply(num1, num2)
elif operation == "/":
    result = divide(num1, num2)
else:
    print("Invalid operation. Please try again.")
    exit()

# Print the result
print("The result is:", result)
