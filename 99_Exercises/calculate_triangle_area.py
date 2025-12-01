#1 Calculate the area of a rectangle

lenght = input("Enter the length of the rectangle: ")
width = input("Enter the width of the rectangle: ")
area = float(lenght) * float(width)
print("The area of the rectangle is:", area, "cm²")

#2 Shopping cart program

item = input("What item would you like to purchase? : ")
quantity = int(input("How many would you like? : "))
price = float(input("What is the price of one item? : "))
total_cost = quantity * price

print(f"The total cost for {quantity} {item}(s) is: ${total_cost:.2f}")