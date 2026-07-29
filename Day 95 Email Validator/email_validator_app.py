from email_validator import validate_email, EmailNotValidError

print("=" * 45)
print("      PROFESSIONAL EMAIL VALIDATOR")
print("=" * 45)

email = input("\nEnter Email Address: ")

try:
    result = validate_email(email)

    print("\n✅ Email is Valid!")
    print("-" * 35)
    print("Original Email :", email)
    print("Normalized Email :", result.normalized)
    print("Domain :", result.domain)

except EmailNotValidError as e:
    print("\n❌ Invalid Email Address")
    print(e)