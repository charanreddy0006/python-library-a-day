import fitz
import os

print("=" * 55)
print("         PDF ANALYZER")
print("=" * 55)

pdf_path = input("\nEnter PDF file path: ").strip()

if not os.path.exists(pdf_path):
    print("❌ File not found.")
    exit()

doc = fitz.open(pdf_path)

print("\n📄 PDF INFORMATION")
print("-" * 35)

print(f"Pages      : {doc.page_count}")
print(f"Title      : {doc.metadata.get('title', 'N/A')}")
print(f"Author     : {doc.metadata.get('author', 'N/A')}")
print(f"Producer   : {doc.metadata.get('producer', 'N/A')}")

text = ""

for page in doc:
    text += page.get_text()

with open("extracted_text.txt", "w", encoding="utf-8") as file:
    file.write(text)

print("\n✅ Text extracted successfully!")
print("📁 Saved as: extracted_text.txt")

doc.close()