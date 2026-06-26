import zipfile

# Create a ZIP file
with zipfile.ZipFile("archive.zip", "w") as zip_file:
    zip_file.write("sample.txt")

print("ZIP file created successfully!")

# Read ZIP contents
with zipfile.ZipFile("archive.zip", "r") as zip_file:
    print("\nFiles inside ZIP:")
    print(zip_file.namelist())

# Extract ZIP
with zipfile.ZipFile("archive.zip", "r") as zip_file:
    zip_file.extractall("Extracted_Files")

print("\nZIP file extracted successfully!")