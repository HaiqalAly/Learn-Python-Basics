# Creating a simple quiz game

questions = ("What is 2 + 2?: ", "What is the capital of France?: ", "What is the largest planet in our solar system?: ", "What is the square root of 16?: ", "What is the chemical symbol for water?: ")

options = (("A. 3", "B. 4", "C. 5", "D. 6"),
           ("A. Berlin", "B. Madrid", "C. Paris", "D. Rome"),
           ("A. Earth", "B. Jupiter", "C. Saturn", "D. Mars"),
           ("A. 2", "B. 3", "C. 4", "D. 5"),
           ("A. H2O", "B. CO2", "C. O2", "D. NaCl"))

answers = ("B", "C", "B", "C", "A")

guesses = []

score = 0
question_num = 0

for question in questions:
    print("-------------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Enter (A, B, C, or D): ").upper()
    guesses.append(guess)

    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("WRONG!")
        print(f"The correct answer was: {answers[question_num]}")
    
    question_num += 1