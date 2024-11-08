##################
## Initial Plan ##
##################

# Ask user for name

user = str(input("Hello, What is your name?\n"))

# Create list of characters

print("\nHello, " + user +  " Which character would you like to choose:\n")
characters = [
    ("Pheonix The Professor", "Always trying to learn new things to pass along."),
    ("Sage The Healer", "Always focused on the health of others."),
    ("Omen The Coder", "Always on his computer, probably making a new game.")
]

## Display the list of characters

for i in range(len(characters)):
    print(f"{i+1} - {characters[i][0]}: {characters[i][1]}")

### Ask the users choice

choice = input("\nEnter the number of the character you would like to choose - 1, 2, or 3: ")

#### Display the chosen character or tell user to restart if given an invalid number

choice = int(choice)
if 1 <= choice <= 3:
    name, description = characters[choice - 1]
    print(f"\nYou have chosen {name}!")
else:
    print("\nSorry, the number you entered is not valid. Restart the game and pick a valid number.")

# Ask user's are of intrest



# Give the user steps of starting

