def get_valid_name():
    while True:
        name = input("Enter your name: ").strip()
        if name.isalpha():
            return name
        else:
            print("Error: Name must contain only letters!")

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

# Main Program
name = get_valid_name()
age = get_valid_age()

print(f"Welcome, {name}! You are {age} years old.")
