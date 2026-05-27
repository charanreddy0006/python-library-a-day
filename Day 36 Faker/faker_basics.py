from faker import Faker

# --- create faker object ---
fake = Faker()

# --- generate fake data ---
print("Name:", fake.name())

print("Email:", fake.email())

print("Address:", fake.address())

print("Phone Number:", fake.phone_number())

print("Company:", fake.company())

print("Job:", fake.job())

print("Date of Birth:", fake.date_of_birth())

# --- generate multiple users ---
print("\nFake User Data:\n")

for i in range(3):

    print({
        "name": fake.name(),
        "email": fake.email(),
        "city": fake.city()
    })