import bcrypt


def hash_password(password):
    """Generate a hashed password."""
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), salt)
    return hashed


def verify_password(password, hashed_password):
    """Verify a password against its hash."""
    return bcrypt.checkpw(password.encode(), hashed_password)


def main():
    print("=" * 45)
    print("      PASSWORD HASHING SYSTEM")
    print("=" * 45)

    password = input("\nCreate a password: ")

    hashed_password = hash_password(password)

    print("\nPassword stored securely!")
    print(f"\nHashed Password:\n{hashed_password.decode()}")

    print("\nVerify Your Password")
    entered_password = input("Enter password: ")

    if verify_password(entered_password, hashed_password):
        print("\nLogin Successful ✅")
    else:
        print("\nIncorrect Password ❌")


if __name__ == "__main__":
    main()