import phonenumbers
from phonenumbers import geocoder, carrier, timezone

print("=" * 45)
print(" INTERNATIONAL PHONE VALIDATOR ")
print("=" * 45)

number = input("\nEnter phone number (with country code): ")

try:
    parsed = phonenumbers.parse(number)

    print("\n📋 Phone Details")
    print("-" * 35)
    print("Valid Number :", phonenumbers.is_valid_number(parsed))
    print("Possible Number :", phonenumbers.is_possible_number(parsed))
    print("Country :", geocoder.description_for_number(parsed, "en"))
    print("Carrier :", carrier.name_for_number(parsed, "en"))
    print("Timezone :", ", ".join(timezone.time_zones_for_number(parsed)))
    print("International Format :", phonenumbers.format_number(
        parsed,
        phonenumbers.PhoneNumberFormat.INTERNATIONAL
    ))

except Exception as e:
    print("\n❌ Invalid phone number!")
    print(e)