from deep_translator import GoogleTranslator

print("=" * 45)
print("      MULTI LANGUAGE TRANSLATOR")
print("=" * 45)

text = input("\nEnter text: ")

print("\nLanguages")
print("1. Hindi")
print("2. Telugu")
print("3. French")
print("4. German")
print("5. Spanish")

choice = input("\nChoose language (1-5): ")

languages = {
    "1": "hi",
    "2": "te",
    "3": "fr",
    "4": "de",
    "5": "es"
}

if choice in languages:
    translated = GoogleTranslator(
        source="auto",
        target=languages[choice]
    ).translate(text)

    print("\n✅ Translation")
    print(translated)

else:
    print("Invalid choice")