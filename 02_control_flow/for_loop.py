# For loop = A statement that will execute a block of code a limited number of times

number = "1-2-3"

for x in reversed(range(1, 11)):
    print(x)

print("HAPPY NEW YEAR!")

for x in number:
    if x == "-":
        continue
    print(x)
