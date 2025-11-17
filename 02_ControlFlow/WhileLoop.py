# While loop = A statement that will execute a block of code WHILE a condition is true

# name = input("Enter your name: ")
food = input("Enter your favorite food: ")

# while name == "":
#     print("You did not enter a name.")
#     name = input("Enter your name: ")

while not food == "quit":
    print("you like " + food)
    food = input("Enter another food (type quit to end the program): ")

print("Program ended.")