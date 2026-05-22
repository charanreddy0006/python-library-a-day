import argparse

# --- create parser ---
parser = argparse.ArgumentParser(
    description="Simple Calculator using argparse"
)

# --- add arguments ---
parser.add_argument(
    "num1",
    type=int,
    help="First number"
)

parser.add_argument(
    "num2",
    type=int,
    help="Second number"
)

# --- parse arguments ---
args = parser.parse_args()

# --- perform calculation ---
result = args.num1 + args.num2

print("Result:", result)