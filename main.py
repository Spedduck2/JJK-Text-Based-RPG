import random

def check_input(text, *args):
    """
    Prompt user for input until one of the options in *args is entered.
    
    Parameters
    ----------
    text : str
        The text to display to the user.
    *args
        The options to accept.
    
    Returns
    -------
    str
        The user's valid input.
    """
    
    while True:
      args = str(args)
      inp = input(text)
      if inp in args:
          return inp 
      else:
          print("Please enter a valid option.")



# Define locations and options
location = ["a Forest", "a Cave", "a boat in the middle of the ocean"]
loc = random.choice(location)
options = ["Soul Manipulation", "Ten Shadows", "Blessed By the Sparks", "Shrine", "Limitless", "Gambling", "Blood Manipulation", "Heavenly Restriction"]

# Select two random options
cur1 = random.choice(options)
cur2 = random.choice(options)

while cur1 == cur2:
    cur2 = random.choice(options)

chr = check_input(f"Options: 1 = {cur1}, 2 = {cur2}\n", "1", "2")
cur = cur1 if chr == "1" else cur2



print(f"\n{cur1} chosen\n")
print(f"You wake up in {loc}")
act = check_input("What do you do now? 1 = look around, 2 = Explore", "1", "2")

