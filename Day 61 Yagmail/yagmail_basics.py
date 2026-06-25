import yagmail

# Login to Gmail
yag = yagmail.SMTP(
    user="your_email@gmail.com",
    password="your_app_password"
)

# Send Email
yag.send(
    to="receiver@gmail.com",
    subject="Python Email Test",
    contents="Hello! This email was sent using Python and Yagmail."
)

print("Email sent successfully! ✅")