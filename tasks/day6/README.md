# Python Data Types, Arithmetic Operations, String Manipulation, Number Guessing Game, Simple Calculator, Contact List Manager, and To-Do List Manager

## Overview
This script demonstrates different fundamental data types in Python, performs basic arithmetic operations, showcases common string manipulations, includes a number guessing game, implements a simple calculator, provides a contact list manager, and a to-do list manager. It prints the type of various data types, the results of arithmetic computations, string transformations, and offers interactive experiences for games, calculations, contact management, and task management.

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

### To-Do List Manager
This section implements a simple to-do list manager to add, view, and remove tasks.

```python
import os

FILE_NAME = "tasks.txt"

def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return [task.strip() for task in file.readlines()]
    return []

def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

tasks = load_tasks()

while True:
    print("\n📝 To-Do List Manager")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        if not tasks:
            print("No tasks found.")
        else:
            for idx, task in enumerate(tasks, start=1):
                print(f"{idx}. {task}")
    elif choice == "2":
        task = input("Enter task: ")
        tasks.append(task)
        save_tasks(tasks)
        print(f"Task '{task}' added!")
    elif choice == "3":
        task_number = int(input("Enter task number to remove: ")) - 1
        if 0 <= task_number < len(tasks):
            removed_task = tasks.pop(task_number)
            save_tasks(tasks)
            print(f"Task '{removed_task}' removed!")
        else:
            print("Invalid task number.")
    elif choice == "4":
        print("Exiting To-Do List Manager.")
        break
    else:
        print("Invalid choice! Please try again.")
```

