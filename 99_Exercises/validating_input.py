# Validate user input exercise
# 1. Username is no longer than 15 characters
# 2. Username must not contain any spaces
# 3. Username must start with a letter

username = input("Enter a username: ")

if len(username) > 15:
    print("Error: Username must be no longer than 15 characters.")
elif ' ' in username:
    print("Error: Username must not contain spaces.")
elif not username[0].isalpha():
    print("Error: Username must start with a letter.")
else:
    print("Username is valid. Welcome,", username + "!")