from tqdm import tqdm
import time

# Progress Bar Example
for i in tqdm(range(20), desc="Processing"):

    time.sleep(0.2)

print("\nTask Completed Successfully ✅")