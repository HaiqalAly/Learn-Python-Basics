# Format specifiers in Python are used to format strings in a specific way.
# {value:flags} where value is the variable, and flags define how to format it.

# Flag examples:
# .2f - Format a floating-point number to 2 decimal places
# , - Include commas as thousand separators
# 0 - Pad with leading zeros
# > - Right align
# < - Left align
# ^ - Center align

price1 = 49.99
price2 = 19.99
price3 = 5.49

# Using f-strings (Python 3.6+)
print(f"Price 1: ${price1:.2f}")  # Price 1: $49.99
print(f"Price 2: ${price2:.2f}")  # Price 2: $19.99
print(f"Price 3: ${price3:.2f}")  # Price 3: $5.49