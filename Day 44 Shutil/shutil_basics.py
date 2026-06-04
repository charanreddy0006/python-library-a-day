import shutil
from pathlib import Path

# Create a sample file
Path("source.txt").write_text(
    "Welcome to the Shutil Library!"
)

# Copy file
shutil.copy(
    "source.txt",
    "copy_source.txt"
)

print("File copied successfully ✅")

# Move file
shutil.move(
    "copy_source.txt",
    "moved_source.txt"
)

print("File moved successfully ✅")

# Display file content
content = Path(
    "moved_source.txt"
).read_text()

print("\nFile Content:")
print(content)