# Paige Rosen
# CIS 256 Fall 2025
# 30 Oct 25
# Ex 4 - Github

import random

# create list of states
STATES =[
    "Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado",
    "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho",
    "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana",
    "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota",
    "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada",
    "New Hampshire", "New Jersey", "New Mexico", "New York",
    "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon",
    "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota",
    "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington",
    "West Virginia", "Wisconsin", "Wyoming"
    ]

# choose random state
chosen_state = random.choice(STATES)

#create empty set of letters that were guessed correctly
matching_letters = set()

guess = input("Guess a letter in a state: ").lower()

if len(guess) != 1 or not guess.isalpha():
    print("Try again. Just enter one letter between a and z.")
    
else:
    if guess in chosen_state.lower():
        print(f"The letter {guess} IS in the state name.)
        matching_letters.add(guess)
    else:
        print(f"The letter {guess} is NOT in the state name.")

if len(matching_letters) ==0:
    print("You have not guessed any letters correctly yet.")
else:
    print(f"You have guessed the letters {matching_letters} correctly")









