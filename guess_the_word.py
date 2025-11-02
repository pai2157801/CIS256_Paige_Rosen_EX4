# Paige Rosen
# CIS 256 Fall 2025
# 30 Oct 25
# Ex 4 - Github
import random

# create list of states
STATES =[
    "Alabama", "Alaska", "Arkansas", "California", "Colorado",
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

# keep the order letters were guessed correctly
guessed_right = []

# keep the order letters were guessed incorrectly
guessed_wrong = []

# ---- helpers (no word layout reveal) ----
def letters_in_state(): # create set for letters only, skipping spaces and punctuation, removing duplicates
    return {ch.lower() for ch in chosen_state if ch.isalpha()}

game_won = False

def is_a_letter():
    guess = input("Guess a letter in a state: ").lower().strip()

    if len(guess) != 1 or not guess.isalpha():      # validate guess is a single letter
        print("Try again. Enter only one letter between a and z.")
        return

    if guess in guessed_right or guess in guessed_wrong:     # player already guessed the letter
        print(f"You already tried '{guess}'.")
        # reprint what was already guessed
        if guessed_right:
            print(f"You know the word contains {', '.join(guessed_right)}")
        if guessed_wrong:
            print(f"You know the word does not contain {', '.join(guessed_wrong)}")
        return

    if guess in chosen_state.lower():     # check guess and respond
        print(f"The letter {guess} IS in the state name.")
        matching_letters.add(guess)
        guessed_right.append(guess)
    else:
        print(f"The letter {guess} is NOT in the state name.")
        guessed_wrong.append(guess)

    # recap guessed letters and right or wrong
    if guessed_right:
        print(f"You already know the state name contains {', '.join(guessed_right)}")
    else:
        print("You have not guessed any letters correctly yet.")
    if guessed_wrong:
        print(f"You already know the state name does not contain {', '.join(guessed_wrong)}")

def is_the_word():
    global game_won
    word = input("What state do you think it is? ").lower().strip()
    if word == chosen_state.lower():
        print(f"Congratulations!  {word} is the right answer!")
        game_won = True
    else:
        print("You lose!")

# Game Header
print("Guess the U.S. State!")

while True:
    if letters_in_state().issubset(matching_letters):      # Win by finding all letters or by guessing the word
        print(f"\nYou guessed all the letters! The state is '{chosen_state}'.")
        break
    if game_won:
        break

    choice = input("\nType L to guess a letter, W to guess the word, or Q to quit: ").strip().lower()
    if choice == "q":
        print(f"Goodbye! The state was: {chosen_state}")
        break
    elif choice == "l":
        is_a_letter()
    elif choice == "w":
        is_the_word()
    else:
        print("Please type L, W, or Q.")
