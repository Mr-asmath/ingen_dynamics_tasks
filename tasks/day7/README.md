# User Input Validation in Python

## Overview
This Python script ensures that users enter valid inputs for their name and age. It checks that names contain only letters and that the age is a positive integer.

## Features
- **Name Validation**: Ensures that the entered name consists only of alphabetic characters.
- **Age Validation**: Ensures that the entered age is a positive integer.
- **Error Handling**: Provides appropriate error messages when invalid inputs are detected.

## Code Explanation

### Name Validation Function
```python
def get_valid_name():
    while True:
        name = input("Enter your name: ").strip()
        if name.isalpha():
            return name
        else:
            print("Error: Name must contain only letters!")
```
- Uses a loop to repeatedly prompt for input until a valid name is entered.
- `strip()` removes any leading or trailing spaces.
- `isalpha()` checks if the input consists only of letters.
- Displays an error message for invalid input.

### Age Validation Function
```python
def get_valid_age():
    while True:
        try:
            age = int(input("Enter your age: "))
            if age > 0:
                return age
            else:
                print("Error: Age must be a positive number!")
        except ValueError:
            print("Error: Please enter a valid number!")
```
- Uses a loop to continuously prompt for valid input.
- Tries to convert input into an integer.
- Ensures the age is greater than zero.
- Handles non-numeric inputs with a `ValueError` exception.

### Main Program Execution
```python
# Main Program
name = get_valid_name()
age = get_valid_age()

print(f"Welcome, {name}! You are {age} years old.")
```
- Calls the validation functions to get user input.
- Displays a welcome message including the valid name and age.

## How to Run the Script
1. Save the script as `user_validation.py`.
2. Run the script in a Python environment:
   ```sh
   python user_validation.py
   ```
3. Follow the on-screen prompts to enter a valid name and age.

## Example Usage
**Input:**
```
Enter your name: John123
Error: Name must contain only letters!
Enter your name: John
Enter your age: -5
Error: Age must be a positive number!
Enter your age: 25
```
**Output:**
```
Welcome, John! You are 25 years old.
```

