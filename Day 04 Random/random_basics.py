import random

# --- random numbers ---
print("Random Float (0 to 1):", random.random())

print("Random Integer (1 to 10):", random.randint(1, 10))

print("Random Range (step allowed):", random.randrange(0, 20, 2))

# --- list operations ---
cars = ["BMW", "Audi", "Tesla", "Toyota", "Hyundai"]

print("\nRandom Choice:", random.choice(cars))

print("Random Sample (2 items):", random.sample(cars, 2))

# --- shuffle list ---
random.shuffle(cars)
print("Shuffled List:", cars)

# --- uniform distribution ---
print("\nRandom Float (5 to 10):", random.uniform(5, 10))

# --- real-life example: lottery ---
lottery = random.sample(range(1, 50), 6)
print("\nLottery Numbers:", lottery)

# --- dice simulation ---
dice = random.randint(1, 6)
print("Dice Roll:", dice)