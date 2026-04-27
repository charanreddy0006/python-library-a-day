import string

text = "hello world"

# --- basic string operations ---
print("Upper:", text.upper())
print("Lower:", text.lower())
print("Title:", text.title())
print("Replace:", text.replace("world", "python"))

# --- checking ---
print("Is Alphabet:", text.isalpha())
print("Is Lower:", text.islower())

# --- splitting and joining ---
words = text.split()
print("Split:", words)

joined = "-".join(words)
print("Joined:", joined)

# --- remove spaces ---
text2 = "   python   "
print("Stripped:", text2.strip())

# --- string constants ---
print("\nAlphabets:", string.ascii_letters)
print("Digits:", string.digits)
print("Punctuation:", string.punctuation)

# --- mini example: password generator ---
import random

characters = string.ascii_letters + string.digits + string.punctuation
password = "".join(random.choice(characters) for _ in range(8))

print("\nGenerated Password:", password)