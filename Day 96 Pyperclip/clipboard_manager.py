import pyperclip

while True:
    print("\n" + "=" * 45)
    print("         CLIPBOARD MANAGER")
    print("=" * 45)

    print("1. Copy Text")
    print("2. View Clipboard")
    print("3. Clear Clipboard")
    print("4. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        text = input("Enter text to copy: ")
        pyperclip.copy(text)
        print("✅ Text copied successfully!")

    elif choice == "2":
        text = pyperclip.paste()

        if text:
            print("\n📋 Clipboard Content")
            print("-" * 30)
            print(text)
        else:
            print("Clipboard is empty.")

    elif choice == "3":
        pyperclip.copy("")
        print("🗑️ Clipboard cleared.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("❌ Invalid Choice")