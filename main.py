import random

def check_input(text, *args):
    """
    Check if user input is valid.
    """
    while True:
        inp = input(text)
        if inp in args:
            return inp  
        else:
            print("Please enter a valid option.")

# Define items, curse spirits, and other options
rareitem = ["Playful Cloud", "Split Soul Katana", "Black Rope", "Inverted Spear of Heaven"]
item = ["Katana", "Spear", "Slaughter Demon"] * 3
cs = ["a Grade 4 CS", "a Grade 3 CS", "a Grade 2 CS", "a Grade 1 CS"] * 5
sgcs = ["Mahito", "Jogo", "Finger Bearer", "Hanami", "Dagon"]

eyes = ["1"] * 15
eyes2 = ["2"]

rareoptions = ["Soul Manipulation", "Ten Shadows", "Shrine", "Limitless", "Heavenly Restriction", "Gambling"] * 2
options = ["Blessed By the Sparks", "Blood Manipulation", "Inverse", "Boogie Woogie", "Construction", "CE Heavenly Restriction", "Ratio"] * 3

# Randomly assign items, location, and abilities
randit, randit2 = random.sample(item + rareitem, 2)
loc = random.choice(["a boat in the middle of the ocean"])
six = random.choice(eyes + eyes2)
cur1 = random.choice(options + rareoptions)
options.remove(cur1)
cur2 = random.choice(options + rareoptions)

# Choose a CT
if cur1 == cur2:
    print(f"I guess you are chosen to have {cur1}")
chr = check_input(f"CHOOSE YOUR CT, {cur1} or {cur2} (1 or 2): \n", "1", "2")
cur = cur1 if chr == "1" else cur2
if cur in rareoptions:
    print("\nThis is a rare option that will help you in battle.")
print(f"{cur} chosen\n")
if six == "2":
    print("You have been given the six eyes")
print(f"You wake up in {loc}")

# Initialize the number of Sukuna Fingers collected
sukuna_fingers = 0

# Define the fight function
def fight(csr, item, has_six_eyes, rare_ct, sukuna_fingers):
    """
    Simulates a fight against a curse spirit (csr) with a given item.
    """
    print("\nA fight begins!\n")
    success_chance = 0.5  # Base chance to win

    # Adjust success chance based on Sukuna Fingers collected
    success_chance += sukuna_fingers * 0.1  # 10% extra success chance per finger
    if sukuna_fingers > 0:
        print(f"Sukuna Fingers collected: {sukuna_fingers}. Your power increases!")

    # Adjust success chance based on the curse spirit's strength
    if csr == "a Grade 4 CS":
        success_chance += 0.4  # Easiest opponent
        print("It's a weak Grade 4 curse spirit.")
    elif csr == "a Grade 3 CS":
        success_chance += 0.3
        print("It's a moderate Grade 3 curse spirit.")
    elif csr == "a Grade 2 CS":
        success_chance += 0.2
        print("It's a tough Grade 2 curse spirit.")
    elif csr == "a Grade 1 CS":
        success_chance += 0.1
        print("It's a powerful Grade 1 curse spirit!")
    elif csr in sgcs:
        success_chance -= 0.5  # Strongest opponent
        print("It's an extremely powerful special-grade curse spirit!")

    # Increase chance if player has a rare item
    if item in rareitem:
        success_chance += 0.2
        print("Your rare item boosts your power!")
    
    # Increase chance if player has six eyes
    if has_six_eyes:
        success_chance += 0.5
        print("The six eyes grant you enhanced vision and reflexes!")
        
    # Increase chance if player has a rare CT
    if rare_ct:
        success_chance += 0.2
        print("Your rare CT helps you control the fight more effectively!")
    
    # Determine fight outcome
    if random.random() < success_chance:
        print("You managed to defeat the curse spirit!")
        if csr == "Finger Bearer":
            # Collect a Sukuna Finger if the curse spirit is a Finger Bearer
            sukuna_fingers += 1
            print("You found a Sukuna Finger! Your power has increased.")
            success_chance += 0.2
        if success_chance < 0.5:
            print("However, you are severely injured from the battle.")
        else:
            print("You defeated the curse spirit with minor injuries.")
    else:
        print("The curse spirit overpowered you.")
        print("End of journey.")
    
    return sukuna_fingers  # Return the updated Sukuna Fingers count

# Prompt the player to explore
act = check_input("What do you do now? 1 = look around, 2 = Explore: ", "1", "2")

if act == "1":
    print("You look around but see nothing of interest.")
elif act == "2":
    if loc == "a boat in the middle of the ocean":
        print(f"\nYou go swimming and find {randit}.")
        csr = random.choice(cs + sgcs)  
        print(f"Out of breath, you go back to the boat, but you find {csr}.")

        # Determine if there's a fight
        if csr in sgcs or csr in cs:
            sukuna_fingers = fight(csr, randit, six == "2", cur in rareoptions, sukuna_fingers)
