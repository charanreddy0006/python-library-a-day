from babel.dates import format_date
from babel.numbers import format_currency
from datetime import date

today = date.today()

print("US Date:")
print(format_date(today, locale="en_US"))

print("\nIndian Date:")
print(format_date(today, locale="en_IN"))

print("\nFrench Date:")
print(format_date(today, locale="fr_FR"))

print("\nIndian Currency:")
print(format_currency(150000, "INR", locale="en_IN"))

print("\nUS Currency:")
print(format_currency(150000, "USD", locale="en_US"))