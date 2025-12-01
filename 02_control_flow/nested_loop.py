# Nested loop = A loop inside a loop

rows = int(input("How many rows?: "))
columns = int(input("How many columns?: "))
symbol = input("Enter a symbol to use: ")

for x in range(rows):

    if x == 0:
        pass  
    for y in range(columns):

        if y == 1:
            continue

        if y == 3:
            break

        print(symbol, end=" ")

    print()