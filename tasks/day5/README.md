# Python Data Types, Arithmetic Operations, String Manipulation, Number Guessing Game, Simple Calculator, and Contact List Manager

## Overview
This script demonstrates different fundamental data types in Python, performs basic arithmetic operations, showcases common string manipulations, includes a number guessing game, implements a simple calculator, and provides a contact list manager. It prints the type of various data types, the results of arithmetic computations, string transformations, and offers interactive experiences for games, calculations, and contact management.

## Code Explanation

### Data Types
1. **Integer** (`int`):
   ```python
   num_int = 10  
   print(type(num_int))  # Output: <class 'int'>
   ```
2. **Float** (`float`):
   ```python
   num_float = 10.5  
   print(type(num_float))  # Output: <class 'float'>
   ```
3. **String** (`str`):
   ```python
   text = "Hello, Python!"  
   print(type(text))  # Output: <class 'str'>
   ```
4. **Boolean** (`bool`):
   ```python
   is_python_fun = True  
   print(type(is_python_fun))  # Output: <class 'bool'>
   ```

### Arithmetic Operations
Given:
```python
a = 10
b = 3
```

The following operations are performed:

| Operation       | Code           | Output  |
|---------------|---------------|---------|
| Addition       | `a + b`       | `13`    |
| Subtraction    | `a - b`       | `7`     |
| Multiplication | `a * b`       | `30`    |
| Division       | `a / b`       | `3.3333`|
| Modulus        | `a % b`       | `1`     |
| Exponentiation | `a ** b`      | `1000`  |
| Floor Division | `a // b`      | `3`     |

### String Manipulations
Given:
```python
text = "Hello, Python!"
```

The following operations are performed:

| Operation            | Code                        | Output          |
|----------------------|---------------------------|----------------|
| Convert to Uppercase | `text.upper()`            | "HELLO, PYTHON!" |
| Convert to Lowercase | `text.lower()`            | "hello, python!" |
| Replace a word       | `text.replace("Python", "World")` | "Hello, World!" |
| String Slicing       | `text[0:5]`               | "Hello"         |
| String Slicing (end) | `text[-6:]`              | "Python"        |
| Find Length         | `len(text)`               | `14`            |
| Check word presence | `"Python" in text`        | `True`          |

### Number Guessing Game
This section implements a simple number guessing game where the user must guess a randomly generated number between 1 and 10.

```python
import random

secret_number = random.randint(1, 10)  # Random number between 1 and 10

run = True

print("Guess the number between 1 and 10!")

def start():
    attempts = 0
    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"🎉 Congratulations! You guessed it in {attempts} attempts.")
            break  # Exit the loop

while run:
    start()
    ch = int(input("You are continuing the game!\nYes(1) or No(0): "))
    if ch == 1:
        pass
    else:
        run = False
        print("Bye bye...")
```

### Simple Calculator
This section implements a basic calculator that can perform addition, subtraction, multiplication, and division.

```python
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
print("1) Addition\n2) Subtraction\n3) Multiplication\n4) Division\n5) Exit")

while True:
    operation = int(input("Enter your operation: "))
    if operation == 5:
        print("Exiting calculator.")
        break
    
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
    if cont == "0":
        break
```

### Contact List Manager
This section implements a simple contact list manager to add, view, and delete contacts.

```python
contacts = {}

def add_contact(name, phone):
    contacts[name] = phone
    print(f"Contact {name} added.")

def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        for name, phone in contacts.items():
            print(f"{name}: {phone}")

def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted.")
    else:
        print("Contact not found.")

while True:
    print("\n📞 Contact List Manager")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Delete Contact")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        add_contact(name, phone)
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        name = input("Enter name to delete: ")
        delete_contact(name)
    elif choice == "4":
        print("Exiting Contact Manager.")
        break
    else:
        print("Invalid choice! Please try again.")
```

