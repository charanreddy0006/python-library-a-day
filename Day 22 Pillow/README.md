# Day 22 - Pillow Library

# 📌 Overview

On Day 22, I explored Python’s powerful **Pillow library**, which is used for image processing and image manipulation.

Pillow is the modern version of PIL (Python Imaging Library).

It allows Python programs to:

* open images
* edit photos
* resize images
* rotate pictures
* apply filters
* convert image formats

It is widely used in:

* image editing applications
* AI and computer vision
* social media applications
* web development
* automation systems

---

# 📦 Installing Pillow

Install using pip:

```bash id="jlwm94"
pip install pillow
```

---

# 🧠 Importing the Library

```python id="jlwm95"
from PIL import Image
```

---

# 🖼️ Opening an Image

Example:

```python id="jlwm96"
image = Image.open("sample.jpg")
```

This loads an image into Python.

---

# 📏 Getting Image Information

Example:

```python id="jlwm97"
print(image.size)
print(image.format)
```

This shows:

* image dimensions
* image format

---

# 🔄 Resizing Images

Example:

```python id="jlwm98"
resized = image.resize((300, 300))
```

Used for:

* thumbnails
* social media posts
* optimization

---

# 🔁 Rotating Images

Example:

```python id="jlwm99"
rotated = image.rotate(45)
```

This rotates the image by 45 degrees.

---

# 🎨 Applying Filters

Example:

```python id="jlwm11"
image.filter(ImageFilter.BLUR)
```

Filters include:

* blur
* sharpen
* smooth
* edge enhancement

---

# ⚫ Converting to Grayscale

Example:

```python id="jlwm12"
gray = image.convert("L")
```

Used in:

* AI projects
* image analysis
* computer vision

---

# 💾 Saving Images

Example:

```python id="jlwm13"
image.save("output.jpg")
```

This saves the edited image.

---

# 💻 Complete Example

```python id="jlwm14"
from PIL import Image

image = Image.open("sample.jpg")

gray = image.convert("L")

gray.save("gray.jpg")
```

---

# 🚀 Real-World Uses

Pillow is widely used in:

* photo editing software
* AI image processing
* machine learning datasets
* social media apps
* thumbnail generation

---

# ⚡ Why Pillow is Popular

Pillow is:

* simple
* powerful
* beginner-friendly
* fast for image processing

---

# 🎯 Learning Outcome

After completing this topic, I learned:

* how Python processes images
* how to edit and manipulate images
* basics of image automation
* image transformation techniques

---

# 🚀 Conclusion

The Pillow library is one of the most useful Python libraries for image processing.

It helps developers:

* automate image tasks
* edit photos programmatically
* build image-based applications

Learning Pillow is useful for:

* AI projects
* computer vision
* web development
* automation systems
