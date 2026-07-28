import barcode
from barcode.writer import ImageWriter

print("=" * 45)
print("      PRODUCT BARCODE GENERATOR")
print("=" * 45)

product_id = input("\nEnter Product ID (numbers only): ").strip()

try:
    ean = barcode.get("code128", product_id, writer=ImageWriter())
    filename = ean.save("product_barcode")

    print("\n✅ Barcode generated successfully!")
    print(f"Saved as: {filename}")

except Exception as e:
    print(f"\n❌ Error: {e}")