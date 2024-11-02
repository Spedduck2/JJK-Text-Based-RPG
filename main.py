import random

def check_input(text, *args):
    while True:
      str(args)
      inp = input(text)
      if inp in args:
          return inp  # Exit the loop and return the valid input
      else:
          print("Please enter a valid option.")



# Define locations and options
chnce = ["1" "1" "1" "1" "1" "1" "1" "1" "1" "2"]
item = ["Playful Cloud", "Soul Split Katana"]
location = ["a boat in the middle of the ocean"]
loc = random.choice(location)
options = ["Soul Manipulation", "Ten Shadows", "Blessed By the Sparks", "Shrine", "Limitless", "Gambling", "Blood Manipulation", "Heavenly Restriction"]

# Select two random options
cur1 = random.choice(options)
cur2 = random.choice(options)
six = random.choice(chnce)

# Initialize user choice variable
chr = ""
while chr != "1" and chr != "2":  # Corrected condition to use 'and'
    chr = input(f"CHOOSE YOUR CT, {cur1} or {cur2} (1 or 2): \n")
cur = cur1 if chr == "1" else cur2
# Check which choice the user made



print(f"\n{cur1} chosen\n")
if six == "2":
    print("\nYou were blessed by the six eyes, the eyes of gods\n")
print(f"You wake up in {loc}")
act = input("What do you do now? 1 = look around, 2 = Explore")
if act != "1" or "2":
  print("Enter a valid num")
if act == "1" and loc == "a boat in the middle of the ocean":
   print(f"\nYou go swimming, and find {}")