def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

print("Simple Calculator")
print("Select the Operation:")
print("1)Addition\n2)Subtraction\3)Multiply\n4)Division\n5)Exit")

while True:
    operation = int(input("Enter your operation:"))
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if operation == 1:
        print("Result:", add(num1, num2))
    elif operation == 2:
        print("Result:", subtract(num1, num2))
    elif operation == 3:
        print("Result:", multiply(num1, num2))
    elif operation == 4:
        print("Result:", divide(num1, num2))
    else:
        print("Invalid operation!")

    cont = input("Do you want to calculate again? \nYes(1)/No(0): ")
    if cont == 0:
        break
