import humanize
from datetime import datetime, timedelta

# Number Formatting
print("Comma Format:")
print(humanize.intcomma(123456789))

# File Size Formatting
print("\nFile Size:")
print(humanize.naturalsize(1536000))

# Relative Time
past = datetime.now() - timedelta(days=2, hours=5)

print("\nNatural Time:")
print(humanize.naturaltime(past))

# Ordinal Numbers
print("\nOrdinal:")
print(humanize.ordinal(21))

# Scientific Numbers
print("\nFractional Number:")
print(humanize.intword(2500000))