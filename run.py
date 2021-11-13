import random
import string
from words import words

def game_starts():
    """The initial stage of the game where a user's name is requested and if he/she would like to commence with the game.
    """
    print(
        """
        ██   ██  █████  ███    ██  ██████  ███    ███  █████  ███    ██ 
        ██   ██ ██   ██ ████   ██ ██       ████  ████ ██   ██ ████   ██ 
        ███████ ███████ ██ ██  ██ ██   ███ ██ ████ ██ ███████ ██ ██  ██ 
        ██   ██ ██   ██ ██  ██ ██ ██    ██ ██  ██  ██ ██   ██ ██  ██ ██ 
        ██   ██ ██   ██ ██   ████  ██████  ██      ██ ██   ██ ██   ████ 
                                                                                                                                                                                                       
        """
    )

    name = input('What is your name?\n')
    print(f'Hello, {name}'".Welcome to The Game of Hangman!")
    if input('Would you like to play the Hangman game? (Y)').upper() == "Y":
        hangman()

    else:
        print('Try Again')
        game_starts()

# function to get a random word from the list
def get_random_word():
    """
    A random word is picked from the list of words for the player to guess
    """
    word = random.choice(words)
    return word.upper()

def hangman():
    """Playing the Game"""
    word = get_random_word()
    word_letters = set(word) 
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # letters the user has guessed

    lives = 7

    while len(word_letters) > 0 and lives > 0:
        print('You have', lives, 'lives remaining')
        print('Letters used: ', ' '.join(used_letters))

        # what the current word is (ie W - R D)
        word_list = [
            letter if letter in used_letters else '_' for letter in word]
        print(stages[lives])
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter:\n').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives = lives - 1  # takes away a life if wrong
                print('Letter is not in word.')

        elif user_letter in used_letters:
            print('You have already used that character. Please try again.')

        else:
            print('Invalid character. Please try again.')   