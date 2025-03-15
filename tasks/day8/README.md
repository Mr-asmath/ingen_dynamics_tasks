# Bank Account Management in Python

## Overview
This Python script defines a `BankAccount` class to simulate a simple bank account system. It allows users to deposit money, withdraw money, and check their balance while maintaining data security with private attributes.

## Features
- **Encapsulation**: The account balance is stored as a private attribute.
- **Deposit Function**: Allows adding money to the account with validation.
- **Withdraw Function**: Ensures that the user cannot withdraw more than the available balance.
- **Balance Inquiry**: Provides a method to check the account balance.

## Code Explanation

### `BankAccount` Class
```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  # Private attribute
```
- The constructor (`__init__`) initializes the account owner and balance.
- `__balance` is marked as private to restrict direct access.

### Deposit Method
```python
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__balance}")
        else:
            print("Deposit amount must be positive!")
```
- Ensures that only positive deposit amounts are accepted.
- Updates the balance after a successful deposit.

### Withdraw Method
```python
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn ${amount}. New balance: ${self.__balance}")
        else:
            print("Insufficient funds or invalid amount!")
```
- Prevents withdrawing more than the available balance.
- Checks for valid withdrawal amounts.

### Get Balance Method
```python
    def get_balance(self):
        return self.__balance
```
- Allows checking the current balance securely.

## Example Usage
```python
# Example usage
account = BankAccount("Arshad", 500)

account.deposit(200)
account.withdraw(100)
print("Final balance:", account.get_balance())
```
### Output:
```
Deposited $200. New balance: $700
Withdrawn $100. New balance: $600
Final balance: 600
```

## How to Run the Script
1. Save the script as `bank_account.py`.
2. Run the script in a Python environment:
   ```sh
   python bank_account.py
   ```
3. Modify the class to add more functionality if needed!

## Future Enhancements
- Add transaction history tracking.
- Implement user authentication for security.
- Extend functionality to support multiple account types.

This script provides a basic but functional banking system. 🚀

