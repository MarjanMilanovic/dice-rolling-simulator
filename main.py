import random

# Create a condition for the main loop
game_active = True


# Function that rolls the dice and prints out the output
def response():
    dice_roll = random.randint(1, 6)
    print(f"You rolled a {dice_roll}")


# Check if the game_active is True, and start the while loop with constant input being asked.
# Game currently goes on forever for some reason
while game_active == True:
    roll = input("Roll the dice? Y / N ")
    
    if roll == "Y" or "y":
        response()
    # This part is not working for some reason, I need to figure it out
    elif roll == "N" or "n":
        quit()
    else:
        print("Please enter the proper value.")
