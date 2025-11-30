# 2D Collection = List of Lists

# This is 1D collection (a simple list)
fruits = ["apple", "banana", "cherry"]
vegetables = ["carrot", "broccoli", "spinach"]
meat = ["chicken", "beef", "venison"]

# This is a 2D collection (a list of lists)
groceries = [fruits, vegetables, meat]

print(groceries)
print(groceries[0])        # Accessing the first list (fruits)
print(groceries[1][2])     # Accessing "spinach" from the vegetables list

for category in groceries:
    print("Category:")
    for item in category:
        print(f"- {item}")