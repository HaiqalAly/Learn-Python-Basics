# Collection = Used to store multiple items in a single variable

# List = A collection which is ordered and changeable. Allows duplicate members.
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits)
print(fruits[2])  # Accessing an item by index | note: index starts at 0

# Tuple = A collection which is ordered and unchangeable. Allows duplicate members.
vegetables = ("carrot", "potato", "cucumber", "tomato", "onion")
print(vegetables)
print(vegetables[:3])  # Slicing a tuple
print(vegetables[::3])  # Slicing with step

# Set = A collection which is unordered and unindexed. No duplicate members.
colors = {"red", "green", "blue", "yellow", "purple"}
print(colors)
print("green" in colors)  # Checking membership

print(dir(fruits))  # List methods
#print(help(vegetables)) 

fruits.append("pear")  # Adding an item to the set
fruits.remove("banana")  # Removing an item from the set
fruits.sort()  # Sorting the list
print(fruits)