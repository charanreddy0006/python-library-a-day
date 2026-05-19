from bs4 import BeautifulSoup

# --- sample HTML ---
html = """
<html>
<head>
    <title>Python Learning</title>
</head>

<body>

    <h1>Welcome to BeautifulSoup</h1>

    <p class="info">
        Learn web scraping with Python
    </p>

    <a href="https://python.org">
        Visit Python
    </a>

</body>
</html>
"""

# --- parse HTML ---
soup = BeautifulSoup(html, "html.parser")

# --- title ---
print("Title:", soup.title.text)

# --- heading ---
print("\nHeading:", soup.h1.text)

# --- paragraph ---
print("\nParagraph:", soup.p.text)

# --- link ---
print("\nLink:", soup.a["href"])

# --- all text ---
print("\nAll Text:\n")
print(soup.get_text())