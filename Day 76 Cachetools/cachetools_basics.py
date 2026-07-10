from cachetools import cached, TTLCache
import time

# Cache stores up to 100 items for 30 seconds
cache = TTLCache(maxsize=100, ttl=30)

@cached(cache)
def square(number):
    print("Calculating...")
    time.sleep(2)  # Simulate slow operation
    return number * number

# First call
print(square(10))

# Second call (uses cache)
print(square(10))

# Different value
print(square(20))