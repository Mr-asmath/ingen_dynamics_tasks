import inventory as inv
from user import *

def main():
    while True:
        print("\n📌 Inventory Management System")
        print("1️⃣ Register")
        print("2️⃣ Login")
        print("3️⃣ Exit")

        choice = input("Select an option: ")

        if choice == "1":
            register_user()
        elif choice == "2":
            if login_user():
                inventory_menu()  # Redirect to inventory system after successful login
        elif choice == "3":
            print("👋 Exiting the system.")
            break
        else:
            print("⚠️ Invalid choice. Try again.")

def inventory_menu():
    """Handles the inventory system menu."""
    inventory = inv.InventoryManager()

    while True:
        print("\n📦 Inventory Menu")
        print("1️⃣ Add Item")
        print("2️⃣ View Inventory")
        print("3️⃣ Update Item")
        print("4️⃣ Delete Item")
        print("5️⃣ Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            item_id = input("Enter Item ID: ")
            name = input("Enter Item Name: ")
            quantity = int(input("Enter Quantity: "))
            price = float(input("Enter Price: "))
            inventory.add_item(item_id, name, quantity, price)

        elif choice == "2":
            inventory.view_inventory()

        elif choice == "3":
            item_id = input("Enter Item ID to update: ")
            quantity = int(input("Enter new Quantity: "))
            price = float(input("Enter new Price: "))
            inventory.update_item(item_id, quantity, price)

        elif choice == "4":
            item_id = input("Enter Item ID to delete: ")
            inventory.delete_item(item_id)

        elif choice == "5":
            print("🔒 Logging out and returning to main menu.")
            break
        else:
            print("⚠️ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
