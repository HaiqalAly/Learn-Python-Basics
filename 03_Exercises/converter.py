# Weight coverter 

weight = float(input("Enter your weight: "))
unit = input("Enter your unit (K for kg and L for lb): ").upper()

if unit == "K":
    converted = weight / 0.45
    print(f"You are {converted} pounds")
elif unit == "L":
    converted = weight * 0.45
    print(f"You are {round(converted, 1)} kilos")
else:
    print("Invalid unit")