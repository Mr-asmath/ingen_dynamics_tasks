# Inventory Management System

## Overview
This Inventory Management System allows users to register, log in, and manage inventory records. Users can add, view, update, and delete inventory items with ease using a command-line interface. The system securely handles user authentication and stores inventory data in a CSV file.

## Features
- User authentication (register & login)
- Add, view, update, and delete inventory items
- Stores inventory data in a CSV file
- Secure password hashing for user authentication
- Tabular display of inventory using the `tabulate` library

## Requirements
- Python 3.x
- Required libraries: `pandas`, `tabulate`, `hashlib`, `csv`

## Installation
1. Install the required dependencies if not already installed:
   ```sh
   pip install pandas tabulate
   ```
2. Ensure the following files are in the same directory:
   - `main.py` (Main application script)
   - `inventory.py` (Handles inventory management)
   - `user.py` (Handles user authentication)

## Usage
1. Run the script:
   ```sh
   python main.py
   ```
2. Follow the on-screen menu to register, log in, and manage inventory.

## Functionalities
### User Authentication (`user.py`)
- **Register a new user**: Stores hashed passwords in `users.csv`
- **Login system**: Validates credentials securely

### Inventory Management (`inventory.py`)
- **Add Item**: Enter an item ID, name, quantity, and price
- **View Inventory**: Displays all stored items in a tabular format
- **Update Item**: Modify quantity and price of an existing item
- **Delete Item**: Remove an item from inventory

## Expected CSV Formats
### `users.csv`
```
username,password_hash
```
### `inventory_data.csv`
```
ID,Item Name,Quantity,Price
101,Laptop,5,1200.50
102,Mouse,15,25.00
```

## Future Enhancements
- Implement a graphical user interface (GUI)
- Add role-based access control (admin/user)
- Integrate a database for persistent storage

## License
This project is open-source and free to use.

