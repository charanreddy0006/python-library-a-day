from PIL import Image, ImageFilter

# --- open image ---
image = Image.open("sample.jpg")

print("Image Size:", image.size)
print("Image Format:", image.format)

# --- resize image ---
resized = image.resize((300, 300))
resized.save("resized_image.jpg")

print("Resized image saved")

# --- rotate image ---
rotated = image.rotate(45)
rotated.save("rotated_image.jpg")

print("Rotated image saved")

# --- blur filter ---
blurred = image.filter(ImageFilter.BLUR)
blurred.save("blurred_image.jpg")

print("Blurred image saved")

# --- grayscale conversion ---
gray = image.convert("L")
gray.save("gray_image.jpg")

print("Grayscale image saved")