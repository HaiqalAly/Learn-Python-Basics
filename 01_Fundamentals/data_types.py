# Variable Declaration and Data Types in Python
name = "Haiqal" # string
age = 20 # integer
gpa = 3.5 # float
smart = True # boolean

print("Hello, " + name + "!")
print(f"You are {age} years old.")
print('Your GPA is:', gpa, 'and that is considered smart:', smart, "\n")

# Typechecking
print("Data type of name:", type(name))
print("Data type of age:", type(age))
print("Data type of gpa:", type(gpa))
print("Data type of smart:", type(smart), "\n")

# Type Conversion
age_str = str(age) # converting integer to string
age_float = float(age) # converting integer to float
gpa_int = int(gpa) # converting float to integer (note: this will truncate the decimal part)
smart_str = str(smart) # converting boolean to string

print("Age as string:", age_str)
print("Age as float:", age_float)
print("GPA as integer:", gpa_int)
print("Smart as string:", smart_str)