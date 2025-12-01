print("Welcome brave soul.")
print("You have been summoned to vanquish the evil dragon terrorizing the kingdom.")

name = input("Before you embark, tell me, what is your name? :")
print(f"Ah, {name}, a name that will be remembered in legends!")

print("And so your journey begins...")

print("===============================")

print("You arrive at a fork in the road.")
print("To the left, the path leads to a dark forest.")
print("To the right, the path leads to a steep mountain.")
choice1 = input("Do you choose to go left into the forest or right up the mountain? (left/right): ").lower()
if choice1 == "left":
    print("You venture into the dark forest, the trees whispering secrets as you pass.")
    print("Suddenly, a wild goblin jumps out and blocks your path!")
    action = input("Do you choose to fight the goblin or run away? (fight/run): ").lower()
    if action == "fight":
        print("With courage and skill, you defeat the goblin and continue deeper into the forest.")
        print("After hours of wandering, you find a hidden cave where the dragon sleeps.")
        print("You quietly approach and prepare for battle...")
        print("With a mighty roar, you slay the dragon and save the kingdom!")
        print(f"Congratulations, {name}! You are a true hero!")
    elif action == "run":
        print("You decide that discretion is the better part of valor and flee back to the fork in the road.")
        print("Perhaps another day you will face your fears.")
    else:
        print("Indecision is costly in these parts. The goblin takes advantage and captures you!")
        print("Game Over.")

elif choice1 == "right":
    print("You begin your ascent up the steep mountain, the wind howling around you.")
    print("Halfway up, a fierce storm hits, and you are forced to seek shelter.")
    print("You find a small cave and wait out the storm.")
    print("When the storm clears, you see the dragon flying above, heading towards the kingdom!")
    action = input("Do you choose to chase after the dragon or return to the kingdom to warn them? (chase/return): ").lower()
    if action == "chase":
        print("You bravely chase after the dragon, climbing higher and higher.")
        print("With a final leap, you reach the dragon and engage in an epic battle.")
        print("After a fierce fight, you emerge victorious and save the kingdom!")
        print(f"Congratulations, {name}! You are a true hero!")
    elif action == "return":
        print("You decide to return to the kingdom to warn them of the impending danger.")
        print("Thanks to your warning, the kingdom prepares and successfully defends against the dragon's attack.")
        print(f"Well done, {name}! Your wisdom has saved many lives!")
    else:
        print("Caught in indecision, you lose your footing and fall down the mountain!")
        print("Game Over.")


