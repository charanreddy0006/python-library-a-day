import emoji

while True:
    print("\n" + "=" * 50)
    print("          EMOJI TEXT CONVERTER")
    print("=" * 50)

    print("1. Convert Alias ➜ Emoji")
    print("2. Convert Emoji ➜ Alias")
    print("3. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        text = input("\nEnter text with emoji aliases:\n")

        converted = emoji.emojize(text, language="alias")

        print("\n✅ Converted Text")
        print("-" * 30)
        print(converted)

    elif choice == "2":
        text = input("\nEnter text with emojis:\n")

        converted = emoji.demojize(text)

        print("\n✅ Converted Text")
        print("-" * 30)
        print(converted)

    elif choice == "3":
        print("\nThank you for using Emoji Converter!")
        break

    else:
        print("❌ Invalid choice.")