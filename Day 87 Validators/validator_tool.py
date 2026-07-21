import validators


def validate_input():
    print("\n===== Validation Tool =====")
    print("1. Validate URL")
    print("2. Validate Email")
    print("3. Validate IP Address")
    print("4. Exit")

    while True:
        choice = input("\nEnter your choice: ")

        if choice == "1":
            url = input("Enter URL: ")
            if validators.url(url):
                print("✅ Valid URL")
            else:
                print("❌ Invalid URL")

        elif choice == "2":
            email = input("Enter Email: ")
            if validators.email(email):
                print("✅ Valid Email")
            else:
                print("❌ Invalid Email")

        elif choice == "3":
            ip = input("Enter IP Address: ")
            if validators.ip_address.ipv4(ip):
                print("✅ Valid IPv4 Address")
            else:
                print("❌ Invalid IPv4 Address")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    validate_input()