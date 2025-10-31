# input() function usage examples

name = input("Enter your name: ")
age = int(input("Enter your age: ")) # converting input string to integer
gpa = input("Enter your GPA: ")
smart = input("Are you smart? (True/False): ")

# Note: input() returns data as string by default

print("\nHello, " + name + "!")
print(f"You are {age} years old.")
print('Your GPA is:', gpa, 'and that is considered smart:', smart)