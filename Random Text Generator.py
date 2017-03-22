import random
min = "Heads, it is."
max = "Its tails!"
foo=[min,max,'Nothing to show...:(']
roll_again = "yes"
print ("Flipping the coin...")

while roll_again == "yes" or roll_again == "y":
    secure_random = random.SystemRandom()
    print(secure_random.choice(foo))

    roll_again = input("Roll the dices again?")
