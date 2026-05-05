from pathlib import Path
import shutil

# --- target folder (change if needed) ---
folder_path = Path("test_files")

# --- create folders based on file types ---
file_types = {
    "Images": [".jpg", ".png", ".jpeg"],
    "Documents": [".pdf", ".txt", ".docx"],
    "Videos": [".mp4", ".mkv"],
    "Others": []
}

# --- create folders ---
for folder in file_types:
    (folder_path / folder).mkdir(exist_ok=True)

# --- organize files ---
for file in folder_path.iterdir():
    if file.is_file():
        moved = False
        for folder, extensions in file_types.items():
            if file.suffix.lower() in extensions:
                shutil.move(str(file), str(folder_path / folder / file.name))
                moved = True
                break
        
        if not moved:
            shutil.move(str(file), str(folder_path / "Others" / file.name))

print("Files organized successfully ✅")