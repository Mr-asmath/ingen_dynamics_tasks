import pandas as pd
from tabulate import tabulate

INVENTORY_FILE = "inventory_data.csv"

class InventoryManager:
    def __init__(self):
        self.load_inventory()

    def load_inventory(self):
        """Load inventory data from a CSV file"""
        try:
            self.inventory = pd.read_csv(INVENTORY_FILE)
        except FileNotFoundError:
            self.inventory = pd.DataFrame(columns=["ID", "Item Name", "Quantity", "Price"])
            self.inventory.to_csv(INVENTORY_FILE, index=False)

    def save_inventory(self):
        """Save inventory data to the CSV file"""
        self.inventory.to_csv(INVENTORY_FILE, index=False)

    def add_item(self, item_id, name, quantity, price):
        """Add a new item to inventory"""
        new_item = pd.DataFrame([[item_id, name, quantity, price]], columns=self.inventory.columns)
        self.inventory = pd.concat([self.inventory, new_item], ignore_index=True)
        self.save_inventory()
        print("✅ Item added successfully!")

    def view_inventory(self):
        """Display the inventory"""
        if self.inventory.empty:
            print("⚠️ No items in inventory.")
            return
        print("\n📦 Inventory List:")
        print(tabulate(self.inventory, headers="keys", tablefmt="grid"))

    def update_item(self, item_id, quantity, price):
        """Update an existing item's quantity and price"""
        index = self.inventory[self.inventory["ID"] == item_id].index
        if not index.empty:
            self.inventory.loc[index, ["Quantity", "Price"]] = [quantity, price]
            self.save_inventory()
            print("✅ Item updated successfully!")
        else:
            print("🚫 Item not found!")

    def delete_item(self, item_id):
        """Delete an item from inventory"""
        self.inventory = self.inventory[self.inventory["ID"] != item_id]
        self.save_inventory()
        print("❌ Item deleted successfully!")
