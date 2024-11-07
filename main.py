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
rare_items = ["Playful Cloud", "Split Soul Katana", "Black Rope", "Inverted Spear of Heaven"]
common_items = ["Katana", "Spear", "Slaughter Demon"] * 3
curse_spirits = ["a Grade 4 CS", "a Grade 3 CS", "a Grade 2 CS", "a Grade 1 CS"] * 5
special_grade_cs = ["Mahito", "Jogo", "Finger Bearer", "Hanami", "Dagon"]
special_drop = random.choice(rare_items)
common_drop = random.choice(common_items)
eyes = ["1"] * 15 + ["2"]

rare_options = ["Soul Manipulation", "Ten Shadows", "Shrine", "Limitless", "Heavenly Restriction", "Gambling"] * 2
common_options = ["Blessed By the Sparks", "Blood Manipulation", "Inverse", "Boogie Woogie", "Construction", "CE Heavenly Restriction", "Ratio"] * 3

# Randomly assign items, location, and abilities
randit, randit2 = random.sample(common_items + rare_items, 2)
randit_rare = random.choice(rare_items)
location = random.choice(["a boat in the middle of the ocean"])
six_eyes = random.choice(eyes) == "2"
cur1 = random.choice(common_options + rare_options)
cur2 = random.choice(common_options + rare_options)

# Choose a curse technique (CT)
if cur1 == cur2:
    print(f"You are chosen to have {cur1}")
else:
    choice = check_input(f"CHOOSE YOUR CT, {cur1} or {cur2} (1 or 2): \n", "1", "2")
    cur = cur1 if choice == "1" else cur2
print(f"{cur} chosen\n")

if cur in rare_options:
    print("\nThis is a rare option that will help you in battle.")

if six_eyes:
    print("You have been given the Six Eyes.")
print(f"You wake up in {location}")
if cur == "Heavenly Restriction":
    print(f"You wake up next to {randit_rare}")

# Initialize the number of Sukuna Fingers collected
sukuna_fingers = 0

def fight(csr, item, has_six_eyes, rare_ct, sukuna_fingers):
    """
    Simulates a fight against a curse spirit with a given item.
    """
    print("\nA fight begins!\n")
    success_chance = 0.5  # Base chance to win

    # Adjust success chance based on Sukuna Fingers collected
    success_chance += sukuna_fingers * 0.1  # 10% extra success chance per finger
    if sukuna_fingers > 0:
        print(f"Sukuna Fingers collected: {sukuna_fingers}. Your power increases!")

    # Adjust success chance based on the curse spirit's strength
    success_chance += {
        "a Grade 4 CS": 0.4,
        "a Grade 3 CS": 0.3,
        "a Grade 2 CS": 0.2,
        "a Grade 1 CS": 0.1
    }.get(csr, -0.5 if csr in special_grade_cs else 0)

    if csr in special_grade_cs:
        print("It's an extremely powerful special-grade curse spirit!")
    else:
        print(f"It's a {csr}.")

    # Increase chance if player has a rare item
    if item in rare_items:
        success_chance += 0.2
        print("Your rare item boosts your power!")
    
    # Increase chance if player has Six Eyes
    if has_six_eyes:
        success_chance += 0.5
        print("The Six Eyes grant you enhanced vision and reflexes!")
        
    # Increase chance if player has a rare CT
    if rare_ct:
        success_chance += 0.2
        print("Your rare CT helps you control the fight more effectively!")
    
    # Determine fight outcome
    if random.random() < success_chance:
        print("You managed to defeat the curse spirit!")
        if csr in special_grade_cs:
            print(f"You find {special_drop} where you defeated it.")
        if csr in curse_spirits:
            print(f"You find {common_drop} where you defeated it.")
        if csr == "Finger Bearer":
            # Collect a Sukuna Finger if the curse spirit is a Finger Bearer
            sukuna_fingers += 1
            print("You found a Sukuna Finger! Your power has increased.")
        if success_chance < 0.5:
            print("However, you are severely injured from the battle.")
        else:
            print("You defeated the curse spirit with minor injuries.")
    else:
        print("The curse spirit overpowered you. End of journey.")
    
    return sukuna_fingers  # Return the updated Sukuna Fingers count

# Prompt the player to explore
action = check_input("What do you do now? 1 = look around, 2 = Explore: ", "1", "2")

if action == "1":
    print("You look around but see nothing of interest.")
elif action == "2":
    if location == "a boat in the middle of the ocean":
        print(f"\nYou go swimming and find {randit}.")
        csr = random.choice(curse_spirits + special_grade_cs)  
        print(f"Out of breath, you go back to the boat, but you find {csr}.")

        # Determine if there's a fight
        if csr in special_grade_cs or csr in curse_spirits:
            sukuna_fingers = fight(csr, randit, six_eyes, cur in rare_options, sukuna_fingers)
