# Day 28 - BeautifulSoup Library

# 📌 Overview

On Day 28, I explored Python’s powerful **BeautifulSoup library**, which is used for parsing HTML and extracting data from web pages.

BeautifulSoup makes web scraping simple and beginner-friendly.

It allows Python programs to:

* read HTML content
* navigate webpage structure
* extract text and links
* collect website data
* automate web information gathering

It is widely used in:

* web scraping
* data collection
* automation systems
* price tracking applications
* analytics tools

---

# 📦 Installing BeautifulSoup

Install using pip:

```bash id="bs281d"
pip install beautifulsoup4
```

---

# 🧠 Importing the Library

```python id="bs281e"
from bs4 import BeautifulSoup
```

---

# 🌐 What is HTML Parsing?

HTML parsing means:

* reading webpage structure
* identifying tags
* extracting useful information

Example HTML tags:

* `<title>`
* `<p>`
* `<a>`
* `<h1>`

---

# 📄 Creating a BeautifulSoup Object

Example:

```python id="bs281f"
soup = BeautifulSoup(html, "html.parser")
```

Explanation:

* `html` → webpage content
* `"html.parser"` → parser engine

---

# 🏷️ Extracting Title

Example:

```python id="bs281g"
soup.title.text
```

This extracts webpage title text.

---

# 🔍 Extracting Headings

Example:

```python id="bs281h"
soup.h1.text
```

This extracts heading text.

---

# 🔗 Extracting Links

Example:

```python id="bs281i"
soup.a["href"]
```

This extracts hyperlink URLs.

---

# 📜 Extracting All Text

Example:

```python id="bs281j"
soup.get_text()
```

Used for:

* content extraction
* article scraping
* text analysis

---

# 💻 Complete Example

```python id="bs281k"
from bs4 import BeautifulSoup

html = "<h1>Hello</h1>"

soup = BeautifulSoup(html, "html.parser")

print(soup.h1.text)
```

---

# 🚀 Real-World Uses

BeautifulSoup is used in:

* news aggregators
* price comparison websites
* stock monitoring systems
* data collection tools
* web automation projects

---

# ⚡ Why BeautifulSoup is Popular

BeautifulSoup is:

* simple
* beginner-friendly
* powerful for HTML parsing
* widely used in scraping projects

---

# ⚠️ Important Note

Always respect:

* website policies
* robots.txt rules
* ethical scraping practices

Some websites block scraping.

---

# 🎯 Learning Outcome

After completing this topic, I learned:

* how HTML parsing works
* how Python extracts webpage data
* basics of web scraping
* webpage navigation techniques

---

# 🚀 Conclusion

BeautifulSoup is one of the best Python libraries for web scraping and HTML parsing.

It helps developers:

* collect website data
* automate information extraction
* build scraping systems

Learning BeautifulSoup is useful for:

* automation
* data analysis
* web scraping
* backend systems
