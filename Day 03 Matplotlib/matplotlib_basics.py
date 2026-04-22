import matplotlib.pyplot as plt

# --- sample data ---
cars = ["Car A", "Car B", "Car C", "Car D"]
prices = [500000, 700000, 600000, 900000]
mileage = [15, 18, 20, 12]

# --- line plot ---
plt.figure()
plt.plot(cars, prices, marker='o')
plt.title("Car Prices")
plt.xlabel("Cars")
plt.ylabel("Price")
plt.grid()
plt.show()

# --- bar chart ---
plt.figure()
plt.bar(cars, mileage)
plt.title("Mileage Comparison")
plt.xlabel("Cars")
plt.ylabel("Mileage (km/l)")
plt.show()

# --- pie chart ---
plt.figure()
plt.pie(prices, labels=cars, autopct='%1.1f%%')
plt.title("Price Distribution")
plt.show()

# --- scatter plot ---
plt.figure()
plt.scatter(mileage, prices)
plt.title("Mileage vs Price")
plt.xlabel("Mileage")
plt.ylabel("Price")
plt.show()