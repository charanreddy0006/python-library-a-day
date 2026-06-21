from PIL import Image

# Open image
image = Image.open("sample.jpg")

# Display image information
print("Format:", image.format)
print("Size:", image.size)
print("Mode:", image.mode)

# Resize image
resized = image.resize((300, 300))

# Save resized image
resized.save("resized_image.jpg")

print("Image resized successfully!")