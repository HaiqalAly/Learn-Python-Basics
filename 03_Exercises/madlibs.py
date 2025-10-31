# Creating a simple Mad Libs game in Python
# Mad Libs is a phrasal template word game where one player prompts others for a list of words to substitute for blanks in a story.

print("Welcome to my Mad Libs game!")
print("Please provide the following words:\n")
# Collecting user inputs for the Mad Libs story
adjective1 = input("Adjective: ")
adjective2 = input("Another adjective: ")
noun1 = input("Noun: ")
noun2 = input("Another noun: ")
verb1 = input("Verb (base form): ")
verb2 = input("Another verb (base form): ")
place = input("A place: ")
number = input("A number: ")
animal = input("An animal: ")
color = input("A color: ")
food = input("A type of food: ")
celebrity = input("A celebrity: ")
emotion = input("An emotion: ")
adverb = input("An adverb: ")
time_of_day = input("A time of day (e.g., morning, evening): ")
weather = input("A type of weather (e.g., sunny, rainy): ")
# Constructing the Mad Libs story using the provided words

story = f"""
Once upon a time in a {adjective1} land, there lived a {adjective2} {noun1}. Every day, it would {verb1} happily in the {place}. One day, it met a {noun2} who loved to {verb2}. They became friends and went on many adventures together.
One day, they decided to visit a magical forest where they saw a {color} {animal}. The {animal} was eating some {food} and invited them to join. They all felt very {emotion} and danced {adverb} until the {time_of_day}.
As the {weather} weather set in, they knew it was time to head back home. They promised to meet again in {number} days for another adventure.
And so, the {adjective1} {noun1} and the {adjective2} {noun2} lived happily ever after, always cherishing their friendship and the memories they made together.
"""

# Displaying the completed Mad Libs story
print("\nHere is your Mad Libs story:\n")
print(story)
print("Thank you for playing my Mad Libs game!")
