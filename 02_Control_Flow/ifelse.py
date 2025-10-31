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