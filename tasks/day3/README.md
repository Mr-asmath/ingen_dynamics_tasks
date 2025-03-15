# Python Data Types, Arithmetic Operations, String Manipulation, and Number Guessing Game

## Overview
This script demonstrates different fundamental data types in Python, performs basic arithmetic operations, showcases common string manipulations, and includes a number guessing game. It prints the type of various data types, the results of arithmetic computations, string transformations, and provides an interactive game experience.

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

## Expected Output
```
<class 'int'>
<class 'float'>
<class 'str'>
<class 'bool'>
13
7
30
3.3333333333333335
1
1000
3
HELLO, PYTHON!
hello, python!
Hello, World!
Hello
Python
14
True
Guess the number between 1 and 10!
Enter your guess: 5
Too low! Try again.
Enter your guess: 7
🎉 Congratulations! You guessed it in 2 attempts.
You are continuing the game!
Yes(1) or No(0): 0
Bye bye...
```

## How to Run the Code
1. Ensure you have Python installed (Python 3.x recommended).
2. Copy and paste the script into a Python file (e.g., `script.py`).
3. Run the script using:
   ```sh
   python script.py
   ```

This will display the expected output in the terminal.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

