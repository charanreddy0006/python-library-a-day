import pycountry


def lookup_country(country_name):
    country = pycountry.countries.get(name=country_name)

    if country:
        print("\nCountry Information")
        print("-" * 30)
        print(f"Name         : {country.name}")
        print(f"Official Name: {getattr(country, 'official_name', 'N/A')}")
        print(f"Alpha-2 Code : {country.alpha_2}")
        print(f"Alpha-3 Code : {country.alpha_3}")
        print(f"Numeric Code : {country.numeric}")
    else:
        print("\nCountry not found.")


def main():
    print("=== Country Lookup Tool ===")

    while True:
        country = input("\nEnter country name: ").strip()

        lookup_country(country)

        choice = input("\nSearch another country? (y/n): ").lower()

        if choice != "y":
            print("\nThank you!")
            break


if __name__ == "__main__":
    main()