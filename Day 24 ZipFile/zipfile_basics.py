import zipfile

# --- create zip file ---
with zipfile.ZipFile("sample.zip", "w") as zipf:

    zipf.write("example.txt")

print("ZIP file created successfully")

# --- read zip file ---
with zipfile.ZipFile("sample.zip", "r") as zipf:

    print("\nFiles inside ZIP:")

    print(zipf.namelist())

# --- extract zip file ---
with zipfile.ZipFile("sample.zip", "r") as zipf:

    zipf.extractall("extracted_files")

print("\nZIP extracted successfully")