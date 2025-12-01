name = input("Enter your full name: ")

# String Methods
find = name.find("a")          # Finds the first occurrence of "a"
reverse_find = name.rfind("a") # Finds the last occurrence of "a"
replace = name.replace("a", "o")  # Replaces all occurrences of "a" with "o"
is_digit = name.isdigit()      # Checks if the string contains only digits
is_alpha = name.isalpha()      # Checks if the string contains only alphabetic characters
count = name.count("a")        # Counts the occurrences of "a" in the string
capitalize = name.capitalize()  # Capitalizes the first letter of the string
upper = name.upper()          # Converts the string to uppercase
lower = name.lower()          # Converts the string to lowercase
title = name.title()          # Converts the first letter of each word to uppercase
strip = name.strip()          # Removes leading and trailing whitespace