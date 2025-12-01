# Python compound interest calculator

principal = 0
rate = 0
time = 0

while True:
    principal = float(input("Enter the principal amount (equal or greater than 0): "))
    if principal < 0:
        print("Principal amount can't be less than 0. Please try again.")
    else:
        break

while rate <= 0:
    rate = float(input("Enter the interest rate (greater than 0): "))
    if rate <= 0:
        print("Interest rate must be greater than 0. Please try again.")

while time <= 0:
    time = int(input("Enter the time amount in year (greater than 0): "))
    if time <= 0:
        print("Time must be greater than 0. Please try again.")

total_amount = principal * (1 + rate / 100) ** time
print(f"The total amount after {time} years is: {total_amount:.2f}")