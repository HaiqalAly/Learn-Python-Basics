# Basic Arithmetic operators

# First way to do arithmetic operations
a = 10
b = 3

addition = a + b
subtraction = a - b
multiplication = a * b
division = a / b
modulus = a % b

print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)
print("Modulus:", modulus)

# Second way to do arithmetic operations using augmented assignment operators
b = 3 

a = 10
a += b
print("Test += : a =", a)
a = 10
a -= b
print("Test -= : a =", a)
a = 10
a *= b
print("Test *= : a =", a)
a = 10
a /= b
print("Test /= : a =", a) 
a = 10
a %= b
print("Test %= : a =", a)


# Using built-in functions for arithmetic operations
x = 5
y = 4.5
z = -2

round = round(y)
absolute = abs(z)
power = pow(x, 2)
max = max(x, y, z)

print("Round:", round)
print("Absolute:", absolute)
print("Power:", power)
print("Max:", max)
