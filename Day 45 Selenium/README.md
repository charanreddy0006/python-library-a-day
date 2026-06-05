# Day 45 - Selenium Library

# 📌 Overview

On Day 45, I explored Python's powerful **Selenium library**, which is used for browser automation and web testing.

Selenium allows Python programs to control web browsers automatically just like a human user.

It can:

- Open websites
- Click buttons
- Fill forms
- Search content
- Navigate pages
- Download files

Selenium is widely used in:

- Web Testing
- Automation Scripts
- Data Collection
- Form Automation
- Browser-Based Tasks

---

# 🌐 What is Selenium?

Selenium is an open-source browser automation framework.

It allows developers to interact with websites programmatically.

Instead of manually opening a browser and clicking buttons, Selenium performs those actions automatically.

---

# 📦 Installation

Install Selenium using pip:

```bash
pip install selenium
```

---

# 🧠 Importing Selenium

```python
from selenium import webdriver
```

This provides browser automation capabilities.

---

# 🚀 Launching a Browser

Example:

```python
driver = webdriver.Chrome()
```

This opens a Chrome browser window.

---

# 🌍 Opening a Website

Example:

```python
driver.get("https://www.google.com")
```

This loads a webpage.

---

# 🔍 Finding Elements

Example:

```python
driver.find_element(By.NAME, "q")
```

This finds the Google search box.

Selenium can find elements using:

- ID
- Name
- Class Name
- XPath
- CSS Selector

---

# ⌨️ Sending Keyboard Input

Example:

```python
search_box.send_keys("Python")
```

This types text into an input field.

---

# ↩️ Pressing Enter

Example:

```python
search_box.send_keys(Keys.RETURN)
```

Simulates pressing the Enter key.

---

# ❌ Closing Browser

Example:

```python
driver.quit()
```

Closes all browser windows.

---

# 💻 Complete Example

```python
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://python.org")

driver.quit()
```

---

# 🚀 Real-World Uses

## Automated Testing

Test websites automatically.

---

## Form Filling

Fill repetitive forms.

---

## Web Scraping

Collect dynamic website data.

---

## Social Media Automation

Automate repetitive actions.

---

## Monitoring Websites

Track changes on websites.

---

# ⚡ Advantages of Selenium

- Browser automation
- Cross-platform
- Supports multiple browsers
- Powerful testing capabilities
- Easy integration with Python

---

# 🎯 Learning Outcome

After completing this topic, I learned:

- How browser automation works
- How Selenium controls browsers
- How to interact with webpages
- How automated testing works
- Basic web automation techniques

---

# 🚀 Conclusion

The Selenium library is one of the most powerful Python tools for browser automation.

It helps developers:

- Automate repetitive web tasks
- Test websites efficiently
- Collect web data
- Build automation systems

Learning Selenium is useful for:

- Web Development
- QA Testing
- Automation
- Data Collection
- Browser-Based Applications

It is one of the most practical libraries for real-world automation projects.