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

rareitem = ["Playful Cloud", "Split Soul Katana", "Black Rope", "Inverted Spear of Heaven"]
item = ["Katana", "Spear", "Slaughter Demon"] * 3
cs = ["a Grade 4 CS", "a Grade 3 CS", "a Grade 2 CS", "a Grade 1 CS"] * 5
sgcs = ["Mahito", "Jogo", "Finger Bearer", "Hanami", "Dagon"]

eyes = ["1"] * 7
eyes2 = ["2"]

randit = random.choice(item + rareitem)
loc = random.choice(["a boat in the middle of the ocean"])
six = random.choice(eyes + eyes2)

rareoptions = ["Soul Manipulation", "Ten Shadows", "Shrine", "Limitless", "Heavenly Restriction"]
options = ["Blessed By the Sparks", "Gambling", "Blood Manipulation", "Inverse", "Boogie Woogie", "Construction", "CE Heavenly Restriction", "Ratio"] * 2




cur1 = random.choice(options)
options.remove(cur1)  
cur2 = random.choice(options)


chr = check_input(f"CHOOSE YOUR CT, {cur1} or {cur2} (1 or 2): \n", "1", "2")
cur = cur1 if chr == "1" else cur2
print(f"\n{cur} chosen\n")
if six == "2":
    print("you have been given the six eyes")
print(f"You wake up in {loc}")


act = check_input("What do you do now? 1 = look around, 2 = Explore: ", "1", "2")

if act == "1":
    print("You look around but see nothing of interest.")
elif act == "2":
    if loc == "a boat in the middle of the ocean":
        print(f"\nYou go swimming and find {randit}.")
        csr = random.choice(cs + sgcs)  
        print(f"Out of breath, you go back to the boat, but you find {csr}.")
        
        
        if csr in sgcs:
            print("Yup, you get eviscerated.")
            print("End of journey.")
        elif csr in cs:
            print("\nYou start fighting!\n")
            if csr == "a Grade 1 CS":
                print("You awaken your CT with major injuries and win!")
            elif randit in rareitem:
                print("Your rare item helped you defeat the CS with minimal injuries.")
            elif randit in item:
                print("You win but suffer major injuries.")

