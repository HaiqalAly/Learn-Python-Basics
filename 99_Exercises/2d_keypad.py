# 2D Keypad using List of Lists

numeric_keypad = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"],
    ["*", "0", "#"]
]
for row in numeric_keypad:
    for key in row:
        print(key, end=" ")
    print()  # New line after each row