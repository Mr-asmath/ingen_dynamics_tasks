import csv
import os
from tabulate import tabulate

class ExpenseTracker:
    FILE_NAME = "expenses.csv"

    def __init__(self):
        self.expenses = []
        self.load_expenses()

    def load_expenses(self):
        """Load expenses from CSV file"""
        if os.path.exists(self.FILE_NAME):
            with open(self.FILE_NAME, "r") as file:
                reader = csv.reader(file)
                self.expenses = list(reader)

    def save_expenses(self):
        """Save expenses to CSV file"""
        with open(self.FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(self.expenses)

    def add_expense(self, date, category, amount):
        """Add a new expense"""
        self.expenses.append([date, category, amount])
        self.save_expenses()
        print("✅ Expense added successfully!")

    def view_expenses(self):
        """Display expenses in a table format"""
        if not self.expenses:
            print("No expenses recorded yet.")
            return
        print("\n📊 Expense List:")
        print(tabulate(self.expenses, headers=["Date", "Category", "Amount"], tablefmt="grid"))

    def delete_expense(self, index):
        """Delete an expense by index"""
        try:
            del self.expenses[index]
            self.save_expenses()
            print("❌ Expense deleted successfully!")
        except IndexError:
            print("⚠️ Invalid index. Try again.")
