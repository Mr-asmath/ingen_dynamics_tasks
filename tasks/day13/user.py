import hashlib
import csv
import os

USER_FILE = "users.csv"

# Hash password using SHA-256
def hash_password(password):
    """Hash a password before storing it."""
    return hashlib.sha256(password.encode()).hexdigest()

# Verify password
def check_password(stored_password, provided_password):
    """Verify password during login."""
    return stored_password.strip() == hash_password(provided_password).strip()

# Register a user
def register_user():
    """Register a new user."""
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()

    if os.path.exists(USER_FILE):
        with open(USER_FILE, "r", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                if row and row[0] == username:  # Check if username already exists
                    print("⚠️ Username already exists. Try another one.")
                    return

    # Write user credentials to file
    with open(USER_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([username, hash_password(password)])
    
    print("✅ User registered successfully!")

# User login
def login_user():
    """Authenticate user login."""
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()

    if not os.path.exists(USER_FILE):
        print("⚠️ No users registered. Please register first.")
        return False

    with open(USER_FILE, "r", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            if row and row[0] == username and check_password(row[1], password):
                print("🔓 Login successful!")
                return True

    print("🚫 Invalid username or password.")
    return False
