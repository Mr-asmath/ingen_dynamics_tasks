import Expense

def main():
    tracker = Expense.ExpenseTracker()

    while True:
        print("\n📌 Expense Tracker Menu")
        print("1️⃣ Add Expense")
        print("2️⃣ View Expenses")
        print("3️⃣ Delete Expense")
        print("4️⃣ Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            date = input("Enter date (YYYY-MM-DD): ")
            category = input("Enter category (Food, Travel, Rent, etc.): ")
            amount = input("Enter amount: ")
            tracker.add_expense(date, category, amount)

        elif choice == "2":
            tracker.view_expenses()

        elif choice == "3":
            tracker.view_expenses()
            try:
                index = int(input("Enter the index of expense to delete: ")) - 1
                tracker.delete_expense(index)
            except ValueError:
                print("⚠️ Please enter a valid number.")

        elif choice == "4":
            print("👋 Exiting Expense Tracker. Have a great day!")
            break
        else:
            print("⚠️ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
