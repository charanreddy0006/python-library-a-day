import subprocess

# --- run a simple command ---
result = subprocess.run(
    ["echo", "Hello from Python!"],
    capture_output=True,
    text=True
)

print("Output:", result.stdout)

# --- check Python version ---
version = subprocess.run(
    ["python", "--version"],
    capture_output=True,
    text=True
)

print("Python Version:", version.stdout)

# --- list files in current directory ---
files = subprocess.run(
    ["dir"],   # use ["ls"] for Linux/Mac
    shell=True,
    capture_output=True,
    text=True
)

print("\nFiles in Directory:\n")
print(files.stdout)