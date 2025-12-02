# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

capitals = {
    "USA": "Washington, D.C.",
    "Indonesia": "Jakarta",
    "India": "New Delhi",
    "Germany": "Hannover",
    "France": "Paris"
}

# print(dir(capitals))

# print(help(capitals))

print(capitals["Indonesia"])  # Accessing value by key
print(capitals.get("India"))  # Accessing value by key using get() method

if capitals.get("Spain") is None:
    print("Spain is not found in the dictionary.")

capitals.update({"Germany": "Berlin"})  # Updating value
capitals["Italy"] = "Rome"  # Adding new key-value pair
# capitals.pop("USA")  # Removing key-value pair
# capitals.clear()  # Removing all key-value pairs
# capitals.keys()  # Getting all keys
# capitals.values()  # Getting all values

for country, city in capitals.items():
    print(f"The capital of {country} is {city}.")