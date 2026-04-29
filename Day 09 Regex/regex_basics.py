import re

text = "My email is chakri123@gmail.com and phone is 9876543210"

# --- find all numbers ---
numbers = re.findall(r'\d+', text)
print("Numbers:", numbers)

# --- find email ---
email = re.search(r'\S+@\S+', text)
print("Email:", email.group())

# --- match at beginning ---
match = re.match(r'My', text)
print("Starts with 'My'?", bool(match))

# --- replace text ---
new_text = re.sub(r'\d', '*', text)
print("Masked Text:", new_text)

# --- split text ---
words = re.split(r'\s+', text)
print("Words:", words)

# --- mini example: validate phone number ---
phone = "9876543210"

if re.fullmatch(r'\d{10}', phone):
    print("Valid Phone Number")
else:
    print("Invalid Phone Number")