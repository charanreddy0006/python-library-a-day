import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# --- sample dataset ---
data = {
    "Car": ["BMW", "Audi", "Tesla", "Toyota", "Hyundai"],
    "Price": [55, 48, 70, 30, 25],
    "Mileage": [15, 18, 12, 22, 20]
}

df = pd.DataFrame(data)

# --- bar plot ---
sns.barplot(x="Car", y="Price", data=df)

plt.title("Car Prices")
plt.xlabel("Car Brands")
plt.ylabel("Price (Lakhs)")

plt.show()

# --- scatter plot ---
sns.scatterplot(x="Mileage", y="Price", data=df)

plt.title("Mileage vs Price")

plt.show()

# --- histogram ---
sns.histplot(df["Price"], kde=True)

plt.title("Price Distribution")

plt.show()