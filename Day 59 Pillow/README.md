# Day 59 - Pillow Library

# 📌 Overview

On Day 59, I explored Python's powerful Pillow library.

Pillow is the modern version of the Python Imaging Library (PIL).

It provides tools for:

- Opening images
- Editing images
- Resizing images
- Cropping images
- Rotating images
- Applying filters

Pillow is widely used in:

- Photo Editing Applications
- Computer Vision Projects
- AI Applications
- Social Media Tools
- Automation Systems

---

# 📦 Installation

```bash
pip install pillow
```

---

# 🧠 Importing Pillow

```python
from PIL import Image
```

---

# 🖼️ Opening an Image

```python
image = Image.open("sample.jpg")
```

Loads an image into memory.

---

# 📏 Image Size

```python
print(image.size)
```

Example Output:

```text
(1920, 1080)
```

---

# 🔄 Resizing Images

```python
resized = image.resize((300, 300))
```

Creates a resized image.

---

# 💾 Saving Images

```python
resized.save("new_image.jpg")
```

Saves the modified image.

---

# 🔄 Rotating Images

```python
rotated = image.rotate(90)
```

Rotates the image.

---

# ✂️ Cropping Images

```python
cropped = image.crop(
    (100, 100, 500, 500)
)
```

Extracts a portion of the image.

---

# 🎨 Converting Image Formats

```python
image.save("photo.png")
```

Convert JPG to PNG.

---

# 💻 Complete Example

```python
from PIL import Image

img = Image.open("sample.jpg")

img = img.resize((400, 400))

img.save("output.jpg")
```

---

# 🚀 Real-World Uses

## Photo Editing Software

Resize and edit images.

---

## Social Media Tools

Create thumbnails.

---

## AI Applications

Prepare images for machine learning.

---

## Automation Projects

Batch process images.

---

## Computer Vision

Image preprocessing.

---

# ⚡ Advantages of Pillow

- Easy to use
- Lightweight
- Fast image processing
- Supports many formats
- Cross-platform

---

# 🎯 Learning Outcome

After completing this topic, I learned:

- How images are processed
- How resizing works
- How cropping works
- How image formats are handled
- Basics of image manipulation

---

# 🚀 Conclusion

Pillow is one of the most useful Python libraries for image processing.

It helps developers:

- Edit images
- Resize photos
- Build automation tools
- Prepare images for AI projects

Learning Pillow is useful for:

- Computer Vision
- AI Projects
- Automation
- Photo Editing
- Python Development