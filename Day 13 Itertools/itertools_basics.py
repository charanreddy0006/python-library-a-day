import itertools

data = [1, 2, 3]

# --- permutations ---
perm = list(itertools.permutations(data))
print("Permutations:", perm)

# --- combinations ---
comb = list(itertools.combinations(data, 2))
print("\nCombinations (2):", comb)

# --- combinations with replacement ---
comb_rep = list(itertools.combinations_with_replacement(data, 2))
print("\nCombinations with replacement:", comb_rep)

# --- product (cartesian product) ---
prod = list(itertools.product(data, repeat=2))
print("\nProduct:", prod)

# --- count (infinite iterator) ---
counter = itertools.count(start=1, step=2)

print("\nFirst 5 values from count:")
for i in range(5):
    print(next(counter), end=" ")

# --- cycle ---
cycler = itertools.cycle(['A', 'B', 'C'])

print("\n\nCycle (first 6):")
for i in range(6):
    print(next(cycler), end=" ")