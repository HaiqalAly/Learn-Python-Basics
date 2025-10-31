# Logical operators = evaluate conditions (AND, OR, NOT)
#                           OR  - True if at least one condition is true
#                           AND - True if all conditions are true
#                           NOT - True if condition is false


weather = 25
is_sunny = True

# Example 1 - OR
if weather > 30 or weather < 0 or not is_sunny:
    print("The weather is bad")
else:
    print("The weather is good")

# Example 2 - AND
if weather > 0 and weather < 30 and is_sunny:
    print("The weather is good")
else:
    print("The weather is bad")

# Example 3 - NOT
if not is_sunny:
    print("The weather is bad")
else:
    print("The weather is good")

