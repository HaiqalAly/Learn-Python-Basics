# Shopping Cart Implementation

foods = []
prices = []
total = 0

while True:
    food = input("Enter the food item you want to add to the cart (or type 'done' to finish): ")
    if food.lower() == 'done':
        break
    else:
        price = float(input(f"Enter the price for {food}: "))
        foods.append(food)
        prices.append(price)

print("\nYour Shopping Cart:")

for food, price in zip(foods, prices):
    print(f"{food}: ${price:.2f}")
    total += price

print(f"\nTotal: ${total:.2f}")