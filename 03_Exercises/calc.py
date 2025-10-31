def add (x, y):
    return x + y

def subtract (x, y):
    return x - y

def multi (x, y):
    return x * y

def division (x, y):
    return x / y

print("Welcome to my cslculator app")
print("Which operation would you like to do today?")

print("==============================================================")

operation = float(input("1.ADDITION\n2.SUBTRACTION\n3.MULTIPLICATION \n4.DIVISION : "))

if operation == 1:
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print("The sum is: ", add(float(num1), float(num2)))

elif operation == 2:
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print("The difference is: ", subtract(float(num1), float(num2)))

elif operation == 3:
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print("The product is: ", multi(float(num1), float(num2)))

elif operation == 4:
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print("The quotient is: ", division(float(num1), float(num2)))