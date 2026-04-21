import pandas as pd

# --- creating series ---
data = [10, 20, 30, 40, 50]
series = pd.Series(data)

print("Series:\n", series)

# --- creating dataframe ---
data_dict = {
    "Name": ["Car A", "Car B", "Car C"],
    "Price": [500000, 700000, 600000],
    "Mileage": [15, 18, 20]
}

df = pd.DataFrame(data_dict)

print("\nDataFrame:\n", df)

# --- basic operations ---
print("\nHead:\n", df.head())
print("\nTail:\n", df.tail())

print("\nColumns:", df.columns)
print("\nShape:", df.shape)

# --- selecting data ---
print("\nSelect Price column:\n", df["Price"])

print("\nRow 1:\n", df.loc[1])

# --- filtering ---
print("\nCars with price > 600000:\n", df[df["Price"] > 600000])

# --- adding new column ---
df["Price_in_Lakhs"] = df["Price"] / 100000

print("\nUpdated DataFrame:\n", df)

# --- statistics ---
print("\nMean Price:", df["Price"].mean())
print("Max Price:", df["Price"].max())

# --- saving to csv ---
df.to_csv("cars_data.csv", index=False)

print("\nData saved to cars_data.csv")
