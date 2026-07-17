from slugify import slugify


def generate_slug(title):
    return slugify(title)


def main():
    print("=" * 45)
    print("       SEO URL GENERATOR")
    print("=" * 45)

    while True:
        title = input("\nEnter Blog/Product Title: ").strip()

        if not title:
            print("Title cannot be empty!")
            continue

        slug = generate_slug(title)

        print("\nGenerated Slug")
        print("-" * 30)
        print(slug)

        print("\nComplete URL")
        print(f"https://mysite.com/{slug}")

        choice = input("\nGenerate another URL? (y/n): ").lower()

        if choice != "y":
            print("\nThank you!")
            break


if __name__ == "__main__":
    main()