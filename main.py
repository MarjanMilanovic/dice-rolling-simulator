import random

game_active = True


def response():
    dice_roll = random.randint(1, 6)
    print(f"You rolled a {dice_roll}")


while game_active == True:
    roll = input("Roll the dice? Y / N ")
    
    if roll == "Y" or "y":
        response()
    elif roll == "N" or "n":
        quit()
    else:
        print("Please enter the proper value.")
