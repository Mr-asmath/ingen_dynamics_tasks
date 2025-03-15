import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("sales_data.csv")

# Line chart for sales growth
plt.plot(df["Year"], df["Sales"], marker="o", linestyle="-", color="b", label="Sales")
plt.xlabel("Year")
plt.ylabel("Sales ($)")
plt.title("Sales Growth Over Years")
plt.legend()
plt.grid(True)
plt.show()
