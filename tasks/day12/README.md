# Expense Tracker

## Overview
This Python-based **Expense Tracker** allows users to record, view, and delete expenses. It stores data in a CSV file and displays expenses in a tabular format using the `tabulate` library for better readability.

## Features
- ✅ **Add Expenses** - Save date, category, and amount.
- ✅ **View Expenses** - Display recorded expenses in a table format.
- ✅ **Delete Expenses** - Remove an expense by index.
- ✅ **Data Persistence** - Stores expenses in `expenses.csv`.

## Requirements
- Python 3.x
- Required libraries: `csv`, `os`, `tabulate`

## Installation
1. Install the required dependency:
   ```sh
   pip install tabulate
   ```
2. Ensure `Expense.py` and `main.py` are in the same directory.

## Usage
1. Run the script:
   ```sh
   python main.py
   ```  
2. Follow the menu options to add, view, or delete expenses.

## Expected CSV Format (`expenses.csv`)
```
Date,Category,Amount
2025-03-15,Food,15.50
2025-03-16,Transport,10.00
```

## Example Input/Output
```
📌 Expense Tracker Menu  
1️⃣ Add Expense  
2️⃣ View Expenses  
3️⃣ Delete Expense  
4️⃣ Exit  

Enter your choice: 2  

📊 Expense List:  
+------------+------------+--------+  
| Date       | Category   | Amount |  
+------------+------------+--------+  
| 2025-03-15 | Food      | 15.50  |  
| 2025-03-16 | Transport | 10.00  |  
+------------+------------+--------+  
```

## Future Enhancements
- 🚀 **Store data in a database for better management.**
- 🚀 **Generate reports and expense summaries.**
- 🚀 **Provide category-wise spending insights.**

