import pandas as pd
import pingouin as pg

df = pd.read_csv("students.csv")

print("=" * 45)
print(" STUDENT EXAM STATISTICS ")
print("=" * 45)

print("\nStudent Data")
print(df)

print("\nSummary Statistics")
print(df["Marks"].describe())

print("\nMean Marks :", round(df["Marks"].mean(), 2))
print("Median Marks :", df["Marks"].median())
print("Standard Deviation :", round(df["Marks"].std(), 2))

normality = pg.normality(df["Marks"])

print("\nNormality Test")
print(normality)