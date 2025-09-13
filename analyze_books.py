import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned data
df = pd.read_csv("books_clean.csv")

# 1. Basic info
print("Total books:", len(df))
print("Average price:", df["price"].mean())
print("Most expensive book:", df.loc[df["price"].idxmax(), "title"], "-", df["price"].max())
print("Cheapest book:", df.loc[df["price"].idxmin(), "title"], "-", df["price"].min())

# 2. Availability count
print("\nAvailability:")
print(df["availability"].value_counts())

# 3. Plot a histogram of prices
plt.hist(df["price"], bins=10, color="skyblue", edgecolor="black")
plt.xlabel("Price (£)")
plt.ylabel("Number of Books")
plt.title("Book Price Distribution")
plt.show()
