text = "Hello, Python!"

# Convert to uppercase
print(text.upper())   # "HELLO, PYTHON!"

# Convert to lowercase
print(text.lower())   # "hello, python!"

# Replace a word
print(text.replace("Python", "World"))  # "Hello, World!"

# String slicing
print(text[0:5])  # "Hello" (from index 0 to 4)
print(text[-6:])  # "Python" (last 6 characters)

# Find length of a string
print(len(text))  # 14

# Check if a string contains a word
print("Python" in text)  # True
