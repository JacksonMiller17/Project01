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

choice = input("\nEnter the number of the character you would like to choose: 1, 2, or 3:\n")

#### Display the chosen character or tell user to restart if given an invalid number

choice = int(choice)
if 1 <= choice <= 3:
    name, description = characters[choice - 1]
    print(f"\n-----------------You have chosen {name}!-----------------\n *click enter to continue*")
    input()
else:
    print("\nSorry, the number you entered is not valid. Restart the game and pick a valid number.")

############# Ask user's are of intrest
print("\n\n\n\n\n\n\nWhat area are you interested in?\n")

interests = ["Computing and IT", "Science", "Engineering", "Health Sciences"]
        
for i in range(len(interests)):
    print(f"{i+1} - {interests[i]}") 

interest1 = int(input(str(f"\nEnter the number of the interest you would like to choose 1, 2, 3, or 4:\n")))

if 1 <= (interest1) <= 4:
    print(f"\n-----------------You have chosen: {interests[interest1 - 1]}!-----------------\n *click enter to continue*")
    input()
else:
    print(str("\nSorry, the number you entered is not valid. Restart the game and pick a valid number"))
    exit()


########### Give the user steps of starting

print("\n\n\n\n\n\n\nGetting Started...\n")
gettingstarted = ["Explore Our Educational Pathways", "Apply for Admissions Online", "Find Ways to Pay for College", "Complete Orientation", "Establish placement for Classes"]

getstarted1 = [
    ("Explore Our Educational Pathways", "Here's a link to some of the pathways that we offer: https://www.everettcc.edu/programs/pathways "),
    ("Apply for Admissions Online", "Here's a link to apply at EVCC: https://www.everettcc.edu/enrollment/registration/how-apply"),
    ("Find Ways to Pay for College", "Here's a link of methods of paying for college: https://www.everettcc.edu/students/financial/financial-aid/ways-pay-college"),
    ("Complete Orientation", "Here's a link to Complete the orientation: https://www.everettcc.edu/enrollment/future-students/orientation/"),
    ("Establish placement for Classes", "Here's a link to establish placment for classes: https://www.everettcc.edu/enrollment/placement")
]
       
for i in range(len(getstarted1)):
    print(f"{i+1} - {getstarted1[i][0]}")


startchoice = int(input(str(f"\nEnter the step you would like to choose 1, 2, 3, 4, or 5: ")))

if 1 <= (interest1) <= 5:
    print(f"\n-----------------You have chosen: {gettingstarted[startchoice - 1]}!-----------------\n")
    print(getstarted1[startchoice - 1][1])
    print("\n*click enter to continue*")
    input()
else:
    print(str("\nSorry, the number you entered is not valid. Restart the game and pick a valid number"))

###########last bullet point
print("\n\n\n\n\n\n\n\nBased on your chosen area of interest, here are some courses you will want to enroll in:\n\n ")
if startchoice == 1:

    print("\nSTEM101, STEM103, ENGL101 - Computing and IT\n")
elif startchoice == 2:

    print("\nSTEM101, STEM102, MATH101 - Science\n")
elif startchoice == 3:

    print("\nSTEM101, ENGR111, MATH101 - Engineering\n")
elif startchoice == 4:

    print("\nSTEM101, STEM102, ENGL101 - Health Sciences\n")
elif startchoice == 5:

    print("\nSTEM101, STEM102, ENGL101 - Health Sciences\n")
else:

    print("\nSorry, the number you entered is not valid. Restart the game and pick a valid number")




