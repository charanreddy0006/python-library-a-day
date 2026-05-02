from pathlib import Path

# --- current directory ---
current_path = Path.cwd()
print("Current Path:", current_path)

# --- create a new folder ---
folder = Path("my_folder")
folder.mkdir(exist_ok=True)
print("Folder created")

# --- create a file ---
file = folder / "sample.txt"
file.write_text("Hello, this is a sample file!")

print("File created:", file)

# --- check if file exists ---
print("File exists?", file.exists())

# --- read file content ---
content = file.read_text()
print("File Content:", content)

# --- file info ---
print("File Name:", file.name)
print("File Size:", file.stat().st_size, "bytes")

# --- list files in directory ---
print("\nFiles in folder:")
for f in folder.iterdir():
    print(f)

# --- delete file and folder ---
file.unlink()  # delete file
folder.rmdir()  # delete folder

print("\nCleanup done")