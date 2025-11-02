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

# keep the order letters were guessed correctly
guessed_right = []

# keep the order letters were guessed incorrectly
guessed_wrong = []

# create set for letters only, skipping spaces and punctuation, removing duplicates
def letters_in_state(): 
    return {ch.lower() for ch in chosen_state if ch.isalpha()}

game_won = False
letters_complete = False  # once all unique letters are found

def is_a_letter():
    guess = input("Guess a letter in a state: ").lower().strip()

    if len(guess) != 1 or not guess.isalpha():      # validate guess is a single letter
        print("Try again. Enter only one letter between a and z.")
        return

    if guess in guessed_right or guess in guessed_wrong:     # player already guessed the letter
        print(f"You already tried '{guess}'.")
        # recap guessed letters and right or wrong
        if guessed_right:
            print(f"You already know the state name contains {', '.join(guessed_right)}")
        if guessed_wrong:
            print(f"You already know the state name does not contain {', '.join(guessed_wrong)}")
        return

    if guess in chosen_state.lower():     # check guess and respond
        print(f"The letter {guess} IS in the state name.")
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
        print(f"Congratulations!  {chosen_state} is the right answer!")   # (optional: keeps proper capitalization)
        game_won = True
    else:
        print("You lose!")

# Game Header
print("Guess the U.S. State!")

while True:
    # If all letters have been found, require a word guess (no more letter guesses)
    if not letters_complete and letters_in_state().issubset(set(guessed_right)):
        letters_complete = True
        print("\nNice! You now know all the letters in the state name.")
        # Retype the list of only correct guesses
        print("They are:", ", ".join(guessed_right))
        print("Now you must guess the full state name to win.")

    if game_won:
        break

    if letters_complete: # Only allow W or Q since there are no more letters to guess
        choice = input("\nType W to guess the word, or Q to quit: ").strip().lower()
        if choice == "q":
            print(f"Goodbye! The state was: {chosen_state}")
            break
        elif choice == "w":
            is_the_word()
        elif choice == "l":
            print("Letter guesses are no longer allowed. Choose W to guess the word or Q to quit.")
        else:
            print("Please type W or Q.")
    else:  #  allow L/W/Q
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
