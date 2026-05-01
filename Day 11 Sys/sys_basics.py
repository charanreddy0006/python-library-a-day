import sys

# --- print command line arguments ---
print("Command Line Arguments:", sys.argv)

# --- number of arguments ---
print("Number of arguments:", len(sys.argv))

# --- accessing arguments ---
if len(sys.argv) > 1:
    print("First argument:", sys.argv[1])

# --- Python version ---
print("\nPython Version:", sys.version)

# --- exit program ---
# sys.exit("Program ended")

# --- mini example: add two numbers from command line ---
if len(sys.argv) == 3:
    try:
        a = int(sys.argv[1])
        b = int(sys.argv[2])
        print("\nSum:", a + b)
    except ValueError:
        print("Please enter valid numbers")
else:
    print("\nUsage: python sys_basics.py 5 10")