import smtplib
from email.message import EmailMessage

# --- email details ---
sender = "your_email@gmail.com"
receiver = "receiver_email@gmail.com"
password = "your_app_password"

# --- create email ---
msg = EmailMessage()

msg["Subject"] = "Python Email Test"
msg["From"] = sender
msg["To"] = receiver

msg.set_content("Hello! This email was sent using Python.")

# --- connect to Gmail SMTP server ---
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:

    smtp.login(sender, password)

    smtp.send_message(msg)

print("Email sent successfully")