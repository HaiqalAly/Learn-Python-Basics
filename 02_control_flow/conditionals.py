# if = do something only if a condition is true
# elif = do something else if the previous condition was false and this condition is true
# else = do something if all previous conditions were false

age = int(input("Enter your age: "))
if age >= 18:
    print("You are an adult.")
elif age >= 13:
    print("You are a teenager.")
else:
    print("You are either a child or a senior citizen.")

# Conditional expressions = One line conditional statements (ternary operator)

num = 10
grade = 100

print("Positive" if num > 0 else "Negative or Zero")
print("Even" if num % 2 == 0 else "Odd")
print("Pass" if grade >= 50 else "Fail")

# < = less than
# > = greater than
# <= = less than or equal to
# >= = greater than or equal to
# == = equal to
# != = not equal to