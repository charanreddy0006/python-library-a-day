from PyPDF2 import PdfReader, PdfWriter

# --- read PDF ---
reader = PdfReader("sample.pdf")

print("Total Pages:", len(reader.pages))

# --- extract text from first page ---
page = reader.pages[0]

text = page.extract_text()

print("\nExtracted Text:\n")
print(text)

# --- create PDF writer ---
writer = PdfWriter()

# --- add first page ---
writer.add_page(page)

# --- save new PDF ---
with open("output.pdf", "wb") as file:
    writer.write(file)

print("\nNew PDF created successfully")