from better_profanity import profanity

# Load default profanity words
profanity.load_censor_words()


def check_message(message):
    if profanity.contains_profanity(message):
        print("\n❌ Inappropriate message detected!")
        print("Censored Message:")
        print(profanity.censor(message))
    else:
        print("\n✅ Clean Message")
        print(message)


def main():
    print("=" * 40)
    print("      PROFANITY CHECKER")
    print("=" * 40)

    while True:
        text = input("\nEnter your message: ")

        check_message(text)

        choice = input("\nCheck another message? (y/n): ").lower()

        if choice != "y":
            print("\nGoodbye!")
            break


if __name__ == "__main__":
    main()