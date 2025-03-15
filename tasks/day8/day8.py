class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__balance}")
        else:
            print("Deposit amount must be positive!")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn ${amount}. New balance: ${self.__balance}")
        else:
            print("Insufficient funds or invalid amount!")

    def get_balance(self):
        return self.__balance

# Example usage
account = BankAccount("Arshad", 500)

account.deposit(200)
account.withdraw(100)
print("Final balance:", account.get_balance())
