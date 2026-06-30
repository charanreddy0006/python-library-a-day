import polars as pl

# Create DataFrame
df = pl.DataFrame(
    {
        "Name": ["Alice", "Bob", "Charlie"],
        "Age": [23, 30, 27],
        "City": ["Delhi", "Mumbai", "Hyderabad"]
    }
)

print("Original DataFrame:\n")
print(df)

print("\nFirst 2 Rows:")
print(df.head(2))

print("\nColumns:")
print(df.columns)

print("\nAverage Age:")
print(df["Age"].mean())

print("\nFiltered Data:")
print(df.filter(pl.col("Age") > 25))