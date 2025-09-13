import pandas as pd
import re

# Read scraped data
df = pd.read_csv("books_raw.csv")

# Clean the 'price' column
df["price"] = (
    df["price"]
    .str.replace("£", "", regex=False)   # remove pound sign
    .str.replace("Â", "", regex=False)   # remove unwanted character
    .astype(float)                       # convert to float
)
# Clean the 'rating' column (map words to numbers)
rating_map = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

if "rating" in df.columns:
    df["rating"] = df["rating"].map(rating_map)

# Save cleaned file
df.to_csv("books_clean.csv", index=False)
print("✅ Cleaned data saved to books_clean.csv")
print(df.head())

# Extract number from availability (e.g. "In stock (22 available)")
def extract_num(text):
    match = re.search(r"\d+", text)
    return int(match.group()) if match else 0

df["availability_count"] = df["availability"].apply(extract_num)

# Save cleaned data
df.to_csv("books_clean.csv", index=False)
print("Cleaned data saved to books_clean.csv")
